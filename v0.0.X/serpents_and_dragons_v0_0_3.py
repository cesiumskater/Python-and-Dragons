#!/usr/bin/env python3
"""
THE SERPENT'S CODE - Enhanced Edition
Master Python and save the world from corruption!
Version: 2.1 - Complete with Multi-Slot Save System
"""

import json
import os
import sys
import time
import shutil
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

# Complete quest registry with all Python concepts
QUEST_REGISTRY = {
    "Act 1: Foundation of Code": [
        ("quest1_variables", "The Ancient Scrolls", "Variables", 50),
        ("quest2_numbers", "Numbers in Nature", "Numbers & Math", 75),
        ("quest3_strings", "String Spells", "Strings", 75),
        ("quest4_booleans", "Boolean Logic Gates", "Boolean Logic", 100),
        ("quest5_conditionals", "Branching Paths", "Branching (if/elif/else)", 100),
    ],
    "Act 2: Structures of Power": [
        ("quest6_lists", "The Arcane Archive", "Lists", 125),
        ("quest7_for_loops", "For Loop Rituals", "For Loops", 150),
        ("quest8_list_operations", "Working with Lists", "List Operations", 150),
        ("quest9_slicing", "Slicing Reality", "Slicing & Indexing", 175),
        ("quest10_list_shortcuts", "List Mastery", "List Shortcuts", 175),
    ],
    "Act 3: Advanced Magics": [
        ("quest11_string_methods", "String Alchemy", "String Methods", 200),
        ("quest12_while_loops", "Endless Patrols", "While Loops", 200),
        ("quest13_dictionaries", "The Cult's Codex", "Dictionaries", 225),
        ("quest14_dict_operations", "Dictionary Magic", "Working with Dictionaries", 225),
        ("quest15_sets_tuples", "Sacred Collections", "Sets & Tuples", 250),
    ],
    "Act 4: Master Techniques": [
        ("quest16_functions", "Ritual of Balance", "Functions", 275),
        ("quest17_return_values", "Return of Power", "Returning Values", 275),
        ("quest18_data_transformation", "Changing Data", "Data Transformation", 300),
        ("quest19_text_processing", "Processing Ancient Texts", "Processing Text", 300),
        ("quest20_sorting", "Order from Chaos", "Sorting", 325),
    ],
    "Act 5: Professional Powers": [
        ("quest21_files", "The Rusted Catacombs", "Files", 350),
        ("quest22_exceptions", "Debugging Reality", "Exceptions & Bug Fixing", 350),
        ("quest23_classes", "The Iron Serpent", "Classes", 400),
        ("quest24_modules", "Council of Libraries", "Modules & Libraries", 400),
        ("quest25_inheritance", "Elemental Guardians", "Inheritance & Composition", 500),
    ]
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Prints a fancy header."""
    width = 70
    print("\n" + "=" * width)
    print(text.center(width))
    print("=" * width)

def print_success(message):
    """Prints a success message."""
    print(f"\n✓ [SUCCESS] {message}\n")

def print_error(message):
    """Prints an error message."""
    print(f"\n✗ [ERROR] {message}\n")

def print_hint(message):
    """Prints a hint message."""
    print(f"\n💡 [HINT] {message}\n")

def wait_for_enter():
    """Waits for user to press Enter."""
    input("\n[Press Enter to continue]")

def print_code_box(code, title="Code Example"):
    """Prints code in a nice box."""
    lines = code.strip().split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    width = max(max_len + 4, len(title) + 4)
    
    print("\n" + "+" + "-" * (width - 2) + "+")
    print("|" + title.center(width - 2) + "|")
    print("+" + "-" * (width - 2) + "+")
    for line in lines:
        print("| " + line.ljust(width - 4) + " |")
    print("+" + "-" * (width - 2) + "+\n")

# ============================================================================
# SAVE SYSTEM
# ============================================================================

class SaveManager:
    """Manages all save game operations with multiple slots and backups."""
    
    def __init__(self, game_name="SerpentsCode"):
        self.game_name = game_name
        self.save_dir = self._get_save_directory()
        self.ensure_save_directory()
        
    def _get_save_directory(self):
        """Gets the appropriate save directory for the OS."""
        if sys.platform == "win32":
            base = os.environ.get('APPDATA', os.path.expanduser('~'))
            save_path = Path(base) / self.game_name / "saves"
        elif sys.platform == "darwin":
            base = os.path.expanduser('~/Library/Application Support')
            save_path = Path(base) / self.game_name / "saves"
        else:
            base = os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))
            save_path = Path(base) / self.game_name / "saves"
        
        try:
            save_path.mkdir(parents=True, exist_ok=True)
            test_file = save_path / ".test"
            test_file.touch()
            test_file.unlink()
            return save_path
        except:
            return Path.cwd() / "game_saves"
    
    def ensure_save_directory(self):
        """Creates save directory if it doesn't exist."""
        try:
            self.save_dir.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"Warning: Could not create save directory: {e}")
            self.save_dir = Path.cwd()
            return False
    
    def get_save_slots(self):
        """Returns a list of available save slots."""
        slots = []
        for i in range(1, 4):
            slot_file = self.save_dir / f"slot_{i}.json"
            if slot_file.exists():
                try:
                    with open(slot_file, 'r') as f:
                        data = json.load(f)
                        slots.append({
                            'slot': i,
                            'exists': True,
                            'player_name': data.get('player_name', 'Unknown'),
                            'level': data.get('level', 1),
                            'xp': data.get('xp', 0),
                            'last_saved': data.get('last_saved', 'Unknown'),
                            'completed_quests': len(data.get('completed', []))
                        })
                except:
                    slots.append({'slot': i, 'exists': False})
            else:
                slots.append({'slot': i, 'exists': False})
        return slots
    
    def save_game(self, slot_number, player_data):
        """Saves the game to a specific slot with backup."""
        if not 1 <= slot_number <= 3:
            return False, "Invalid slot number (use 1-3)"
        
        save_file = self.save_dir / f"slot_{slot_number}.json"
        backup_file = self.save_dir / f"slot_{slot_number}.backup.json"
        
        player_data['last_saved'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            if save_file.exists():
                shutil.copy2(save_file, backup_file)
            
            temp_file = save_file.with_suffix('.tmp')
            with open(temp_file, 'w') as f:
                json.dump(player_data, f, indent=4)
            
            temp_file.replace(save_file)
            return True, f"Game saved to slot {slot_number}"
            
        except Exception as e:
            if backup_file.exists():
                try:
                    shutil.copy2(backup_file, save_file)
                except:
                    pass
            return False, f"Failed to save: {str(e)}"
    
    def load_game(self, slot_number):
        """Loads the game from a specific slot."""
        if not 1 <= slot_number <= 3:
            return None, "Invalid slot number (use 1-3)"
        
        save_file = self.save_dir / f"slot_{slot_number}.json"
        backup_file = self.save_dir / f"slot_{slot_number}.backup.json"
        
        if save_file.exists():
            try:
                with open(save_file, 'r') as f:
                    data = json.load(f)
                return data, "Game loaded successfully"
            except Exception as e:
                if backup_file.exists():
                    try:
                        with open(backup_file, 'r') as f:
                            data = json.load(f)
                        return data, "Game loaded from backup"
                    except:
                        return None, "Both saves are corrupted"
        
        return None, f"No save found in slot {slot_number}"
    
    def delete_save(self, slot_number):
        """Deletes a save slot."""
        if not 1 <= slot_number <= 3:
            return False, "Invalid slot number"
        
        save_file = self.save_dir / f"slot_{slot_number}.json"
        backup_file = self.save_dir / f"slot_{slot_number}.backup.json"
        
        try:
            if save_file.exists():
                save_file.unlink()
            if backup_file.exists():
                backup_file.unlink()
            return True, f"Slot {slot_number} deleted"
        except Exception as e:
            return False, f"Failed to delete: {str(e)}"

# ============================================================================
# PROGRESS MANAGEMENT
# ============================================================================

class PlayerProgress:
    """Enhanced player progress manager with multi-slot save support."""
    
    def __init__(self):
        self.save_manager = SaveManager()
        self.current_slot = None
        self.data = self.create_new_game()
    
    def create_new_game(self):
        """Creates a new game data structure."""
        return {
            "player_name": "Teagan",
            "character": "Goblin Druid",
            "completed": [],
            "xp": 0,
            "level": 1,
            "current_act": 1,
            "achievements": [],
            "total_playtime": 0,
            "session_start": time.time()
        }
    
    def complete_quest(self, quest_id, xp_reward):
        """Marks a quest as completed and awards XP."""
        if quest_id not in self.data["completed"]:
            self.data["completed"].append(quest_id)
            self.data["xp"] += xp_reward
            self.check_level_up()
            self.autosave()
    
    def check_level_up(self):
        """Checks if player should level up."""
        xp_per_level = 500
        new_level = (self.data["xp"] // xp_per_level) + 1
        
        if new_level > self.data["level"]:
            self.data["level"] = new_level
            print(f"\n🎉 [LEVEL UP!] You are now Level {new_level}!")
            return True
        return False
    
    def save_menu(self):
        """Interactive save menu."""
        clear_screen()
        print_header("SAVE GAME")
        
        slots = self.save_manager.get_save_slots()
        for slot in slots:
            if slot['exists']:
                print(f"\n📁 Slot {slot['slot']}: {slot['player_name']} (Level {slot['level']})")
                print(f"   XP: {slot['xp']} | Quests: {slot['completed_quests']}")
                print(f"   Last saved: {slot['last_saved']}")
            else:
                print(f"\n📁 Slot {slot['slot']}: [Empty]")
        
        print("\n" + "-" * 70)
        print("1-3: Save to slot | D: Delete slot | C: Cancel")
        
        choice = input("\nChoice: ").strip().upper()
        
        if choice in ['1', '2', '3']:
            slot_num = int(choice)
            
            if slots[slot_num-1]['exists']:
                confirm = input(f"Overwrite save in slot {slot_num}? (y/n): ").lower()
                if confirm != 'y':
                    print("Save cancelled.")
                    wait_for_enter()
                    return False
            
            self.data['total_playtime'] += time.time() - self.data['session_start']
            self.data['session_start'] = time.time()
            
            success, message = self.save_manager.save_game(slot_num, self.data)
            print(f"\n{message}")
            
            if success:
                self.current_slot = slot_num
            
            wait_for_enter()
            return success
            
        elif choice == 'D':
            slot_num = input("Delete which slot (1-3)? ").strip()
            if slot_num in ['1', '2', '3']:
                confirm = input(f"Are you sure? This cannot be undone! (y/n): ").lower()
                if confirm == 'y':
                    success, message = self.save_manager.delete_save(int(slot_num))
                    print(f"\n{message}")
            wait_for_enter()
            return False
        else:
            return False
    
    def load_menu(self):
        """Interactive load menu."""
        clear_screen()
        print_header("LOAD GAME")
        
        slots = self.save_manager.get_save_slots()
        has_saves = False
        
        for slot in slots:
            if slot['exists']:
                has_saves = True
                print(f"\n📁 Slot {slot['slot']}: {slot['player_name']} (Level {slot['level']})")
                print(f"   XP: {slot['xp']} | Quests: {slot['completed_quests']}")
                print(f"   Last saved: {slot['last_saved']}")
            else:
                print(f"\n📁 Slot {slot['slot']}: [Empty]")
        
        if not has_saves:
            print("\nNo saved games found.")
            wait_for_enter()
            return False
        
        print("\n" + "-" * 70)
        print("1-3: Load slot | C: Cancel")
        
        choice = input("\nChoice: ").strip().upper()
        
        if choice in ['1', '2', '3']:
            slot_num = int(choice)
            data, message = self.save_manager.load_game(slot_num)
            print(f"\n{message}")
            
            if data:
                self.data = data
                self.current_slot = slot_num
                self.data['session_start'] = time.time()
                wait_for_enter()
                return True
            wait_for_enter()
            return False
        
        return False
    
    def quick_save(self):
        """Quick save to current slot or slot 1."""
        if self.current_slot is None:
            self.current_slot = 1
        
        self.data['total_playtime'] += time.time() - self.data['session_start']
        self.data['session_start'] = time.time()
        
        success, message = self.save_manager.save_game(self.current_slot, self.data)
        print(f"\n{message}")
        return success
    
    def autosave(self):
        """Autosave to dedicated autosave slot."""
        autosave_file = self.save_manager.save_dir / "autosave.json"
        try:
            self.data['total_playtime'] += time.time() - self.data['session_start']
            self.data['session_start'] = time.time()
            self.data['last_saved'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(autosave_file, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True
        except:
            return False

# ============================================================================
# QUEST IMPLEMENTATIONS
# ============================================================================

class Quest:
    """Base class for all quests."""
    
    def __init__(self, quest_id, title, topic, xp_reward):
        self.quest_id = quest_id
        self.title = title
        self.topic = topic
        self.xp_reward = xp_reward
    
    def start(self):
        """Starts the quest."""
        clear_screen()
        print_header(self.title)
        print(f"\n📚 Topic: {self.topic}")
        print(f"⭐ Reward: {self.xp_reward} XP\n")
        wait_for_enter()
    
    def teach(self, lesson_title, content, example_code=None):
        """Teaches a concept."""
        clear_screen()
        print_header(f"LESSON: {lesson_title}")
        print(f"\n{content}\n")
        
        if example_code:
            print_code_box(example_code, "Example")
        
        wait_for_enter()
    
    def challenge(self, challenge_title, task_description):
        """Presents a challenge."""
        clear_screen()
        print_header(f"CHALLENGE: {challenge_title}")
        print(f"\n{task_description}\n")
    
    def get_code_input(self):
        """Gets multi-line code input from user."""
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("-" * 60)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        return '\n'.join(lines)
    
    def validate_code(self, code, test_func):
        """Validates user code using a test function."""
        try:
            namespace = {}
            exec(code, namespace)
            return test_func(namespace)
        except Exception as e:
            return False, f"Error in code: {str(e)}"

class Quest1_Variables(Quest):
    """Quest teaching variables."""
    
    def run(self):
        self.start()
        
        self.teach(
            "Variables",
            "Variables are containers that store data values.\n"
            "Think of them as labeled boxes where you can put information.\n"
            "In Python, you create a variable by giving it a name and assigning a value.",
            """# Creating variables
name = "Teagan"
age = 127
is_druid = True

# Using variables
print(name)
print("Age:", age)"""
        )
        
        self.challenge(
            "Create Your Character",
            "Create three variables:\n"
            "1. hero_name = your character's name (string)\n"
            "2. hero_level = 1 (number)\n"
            "3. has_magic = True (boolean)\n\n"
            "Then print all three variables."
        )
        
        max_attempts = 3
        for attempt in range(max_attempts):
            code = self.get_code_input()
            
            def test(ns):
                if 'hero_name' not in ns:
                    return False, "Variable 'hero_name' not found"
                if 'hero_level' not in ns:
                    return False, "Variable 'hero_level' not found"
                if 'has_magic' not in ns:
                    return False, "Variable 'has_magic' not found"
                if ns['hero_level'] != 1:
                    return False, "hero_level should be 1"
                if ns['has_magic'] != True:
                    return False, "has_magic should be True"
                return True, "Perfect! Variables created successfully!"
            
            success, message = self.validate_code(code, test)
            
            if success:
                print_success(message)
                return True
            else:
                print_error(message)
                if attempt < max_attempts - 1:
                    print_hint(f"Attempts remaining: {max_attempts - attempt - 1}")
        
        return False

# ============================================================================
# GAME ENGINE
# ============================================================================

class GameEngine:
    """Main game engine managing quest flow and player state."""
    
    def __init__(self):
        self.player = PlayerProgress()
        self.quests = self.initialize_quests()
        self.running = True
    
    def initialize_quests(self):
        """Initializes all quest objects."""
        quests = {}
        quests["quest1_variables"] = Quest1_Variables(
            "quest1_variables",
            "The Ancient Scrolls",
            "Variables",
            50
        )
        return quests
    
    def display_main_menu(self):
        """Displays the main game menu."""
        clear_screen()
        print_header("THE SERPENT'S CODE")
        
        print(f"\n🧙 Druid: {self.player.data['player_name']} the {self.player.data['character']}")
        print(f"⚡ Level: {self.player.data['level']} | XP: {self.player.data['xp']}")
        print(f"✓ Quests Completed: {len(self.player.data['completed'])}")
        if self.player.current_slot:
            print(f"💾 Save Slot: {self.player.current_slot}")
        
        print("\n" + "=" * 70)
        print("\n1. Continue Adventure")
        print("2. View Quest Map")
        print("3. Check Progress")
        print("4. Save Game")
        print("5. Load Game")
        print("6. Quick Save (F5)")
        print("7. Exit")
        
        return input("\nChoose your path: ").strip()
    
    def display_quest_map(self):
        """Shows all quests organized by act."""
        clear_screen()
        print_header("QUEST MAP")
        
        for act_name, quests in QUEST_REGISTRY.items():
            print(f"\n{act_name}")
            print("-" * 60)
            
            for quest_id, quest_name, topic, xp_reward in quests:
                status = "✓" if quest_id in self.player.data['completed'] else "○"
                available = "*" if quest_id in self.quests else ""
                print(f"  {status} {quest_name} - {topic} ({xp_reward} XP) {available}")
        
        print("\n✓ = Completed | ○ = Available | * = Implemented")
        wait_for_enter()
    
    def get_next_quest(self):
        """Determines the next available quest for the player."""
        for act_name, quests in QUEST_REGISTRY.items():
            for quest_id, quest_name, topic, xp_reward in quests:
                if quest_id not in self.player.data['completed'] and quest_id in self.quests:
                    return quest_id, quest_name, topic, xp_reward
        return None
    
    def run_quest(self, quest_id, xp_reward):
        """Runs a specific quest."""
        if quest_id not in self.quests:
            print_error(f"Quest '{quest_id}' is not yet implemented!")
            wait_for_enter()
            return False
        
        quest = self.quests[quest_id]
        success = quest.run()
        
        if success:
            self.player.complete_quest(quest_id, xp_reward)
            print_success("Quest Complete!")
            wait_for_enter()
            return True
        else:
            print_error("Quest not completed. Try again!")
            wait_for_enter()
            return False
    
    def display_progress(self):
        """Shows detailed player progress."""
        clear_screen()
        print_header("YOUR PROGRESS")
        
        total_quests = sum(len(quests) for quests in QUEST_REGISTRY.values())
        completed = len(self.player.data['completed'])
        
        print(f"\n📊 Quests Completed: {completed}/{total_quests}")
        print(f"📈 Completion: {completed * 100 // total_quests}%")
        print(f"⚡ Current Level: {self.player.data['level']}")
        print(f"⭐ Total XP: {self.player.data['xp']}")
        
        playtime_hours = self.player.data.get('total_playtime', 0) / 3600
        print(f"⏱️  Playtime: {playtime_hours:.1f} hours")
        
        if self.player.data['completed']:
            print("\nCompleted Quests:")
            for quest_id in self.player.data['completed']:
                print(f"  ✓ {quest_id}")
        
        wait_for_enter()
    
    def run(self):
        """Main game loop."""
        print("\nWelcome to The Serpent's Code!")
        print("A Python learning adventure awaits...")
        print(f"Save directory: {self.player.save_manager.save_dir}")
        wait_for_enter()
        
        while self.running:
            choice = self.display_main_menu()
            
            if choice == '1':
                next_quest = self.get_next_quest()
                
                if next_quest is None:
                    print("\nAll implemented quests completed!")
                    print("More quests are being developed...")
                    wait_for_enter()
                    continue
                
                quest_id, quest_name, topic, xp_reward = next_quest
                
                clear_screen()
                print(f"\nNext Quest: {quest_name}")
                print(f"Topic: {topic}")
                print(f"Reward: {xp_reward} XP")
                
                confirm = input("\nBegin this quest? (y/n): ").lower()
                
                if confirm == 'y':
                    self.run_quest(quest_id, xp_reward)
            
            elif choice == '2':
                self.display_quest_map()
            
            elif choice == '3':
                self.display_progress()
            
            elif choice == '4':
                self.player.save_menu()
            
            elif choice == '5':
                self.player.load_menu()
            
            elif choice == '6':
                self.player.quick_save()
                wait_for_enter()
            
            elif choice == '7':
                if self.player.current_slot:
                    save_choice = input("Save before exiting? (y/n): ").lower()
                    if save_choice == 'y':
                        self.player.quick_save()
                print("\nProgress autosaved. Farewell, druid!")
                self.running = False
            
            else:
                print("\nInvalid choice. Try again.")
                wait_for_enter()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point for the game."""
    try:
        game = GameEngine()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Progress has been autosaved.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue.")

if __name__ == "__main__":
    main()
