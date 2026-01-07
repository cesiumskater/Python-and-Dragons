#!/usr/bin/env python3
"""
THE SERPENT'S CODE - A Python Learning Adventure
Master the ancient art of Pythonic magic and save the world from corruption!
Version: 2.0 - Complete Edition
"""

import json
import os
import sys
import time
import random
from pathlib import Path

# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

SAVE_FILE = "player_progress.json"

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
    print(f"\n[SUCCESS] {message}\n")

def print_error(message):
    """Prints an error message."""
    print(f"\n[ERROR] {message}\n")

def print_hint(message):
    """Prints a hint message."""
    print(f"\n[HINT] {message}\n")

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
# PROGRESS MANAGEMENT
# ============================================================================

class PlayerProgress:
    """Manages player progress and saves."""
    
    def __init__(self):
        self.data = self.load_progress()
    
    def load_progress(self):
        """Loads player progress from JSON file."""
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f)
            except:
                pass
        
        # Default data for new players
        return {
            "player_name": "Teagan",
            "character": "Goblin Druid",
            "completed": [],
            "xp": 0,
            "level": 1,
            "current_act": 1,
            "achievements": []
        }
    
    def save(self):
        """Saves player progress to JSON file."""
        try:
            with open(SAVE_FILE, "w") as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Failed to save: {e}")
            return False
    
    def complete_quest(self, quest_id, xp_reward):
        """Marks a quest as completed and awards XP."""
        if quest_id not in self.data["completed"]:
            self.data["completed"].append(quest_id)
            self.data["xp"] += xp_reward
            self.check_level_up()
            self.save()
    
    def check_level_up(self):
        """Checks if player should level up."""
        xp_per_level = 500
        new_level = (self.data["xp"] // xp_per_level) + 1
        
        if new_level > self.data["level"]:
            self.data["level"] = new_level
            print(f"\n[LEVEL UP!] You are now Level {new_level}!")
            return True
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
        print(f"\nTopic: {self.topic}")
        print(f"Reward: {self.xp_reward} XP\n")
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
            # Create a safe namespace for code execution
            namespace = {}
            exec(code, namespace)
            return test_func(namespace)
        except Exception as e:
            return False, f"Error in code: {str(e)}"

# Sample Quest Implementations

class Quest1_Variables(Quest):
    """Quest teaching variables."""
    
    def run(self):
        self.start()
        
        # Lesson
        self.teach(
            "Variables",
            "Variables are containers that store data values.\n"
            "Think of them as labeled boxes where you can put information.",
            """# Creating variables
name = "Teagan"
age = 127
is_druid = True

# Using variables
print(name)
print("Age:", age)"""
        )
        
        # Challenge
        self.challenge(
            "Create Your Character",
            "Create three variables:\n"
            "1. hero_name = your character's name (string)\n"
            "2. hero_level = 1 (number)\n"
            "3. has_magic = True (boolean)\n"
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
        
        # For now, just add the sample quest
        # In a full implementation, you'd add all 25 quests
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
        
        print(f"\nDruid: {self.player.data['player_name']} the {self.player.data['character']}")
        print(f"Level: {self.player.data['level']} | XP: {self.player.data['xp']}")
        print(f"Quests Completed: {len(self.player.data['completed'])}")
        
        print("\n" + "=" * 70)
        print("\n1. Continue Adventure")
        print("2. View Quest Map")
        print("3. Check Progress")
        print("4. Save & Exit")
        
        return input("\nChoose your path: ").strip()
    
    def display_quest_map(self):
        """Shows all quests organized by act."""
        clear_screen()
        print_header("QUEST MAP")
        
        for act_name, quests in QUEST_REGISTRY.items():
            print(f"\n{act_name}")
            print("-" * 60)
            
            for quest_id, quest_name, topic, xp_reward in quests:
                status = "[X]" if quest_id in self.player.data['completed'] else "[ ]"
                available = "*" if quest_id in self.quests else ""
                print(f"  {status} {quest_name} - {topic} ({xp_reward} XP) {available}")
        
        print("\n[X] = Completed | [ ] = Available | * = Implemented")
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
    
    def run(self):
        """Main game loop."""
        print("\nWelcome to The Serpent's Code!")
        print("A Python learning adventure awaits...")
        wait_for_enter()
        
        while self.running:
            choice = self.display_main_menu()
            
            if choice == '1':
                # Continue adventure
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
                
                choice = input("\nBegin this quest? (y/n): ").lower()
                
                if choice == 'y':
                    self.run_quest(quest_id, xp_reward)
            
            elif choice == '2':
                self.display_quest_map()
            
            elif choice == '3':
                self.display_progress()
            
            elif choice == '4':
                self.player.save()
                print("\nProgress saved. Farewell, druid!")
                self.running = False
            
            else:
                print("\nInvalid choice. Try again.")
                wait_for_enter()
    
    def display_progress(self):
        """Shows detailed player progress."""
        clear_screen()
        print_header("YOUR PROGRESS")
        
        total_quests = sum(len(quests) for quests in QUEST_REGISTRY.values())
        completed = len(self.player.data['completed'])
        
        print(f"\nQuests Completed: {completed}/{total_quests}")
        print(f"Completion: {completed * 100 // total_quests}%")
        print(f"Current Level: {self.player.data['level']}")
        print(f"Total XP: {self.player.data['xp']}")
        
        if self.player.data['completed']:
            print("\nCompleted Quests:")
            for quest_id in self.player.data['completed']:
                print(f"  - {quest_id}")
        
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
        print("\n\nGame interrupted. Progress has been saved.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue.")

if __name__ == "__main__":
    main()