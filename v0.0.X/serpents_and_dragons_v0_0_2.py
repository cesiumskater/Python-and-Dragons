#!/usr/bin/env python3
"""
Enhanced Save System for The Serpent's Code
Robust save/load functionality with multiple slots and backups
"""

import json
import os
import sys
import time
import shutil
from datetime import datetime
from pathlib import Path

class SaveManager:
    """Manages all save game operations with error handling and backups."""
    
    def __init__(self, game_name="SerpentsCode"):
        self.game_name = game_name
        self.save_dir = self._get_save_directory()
        self.ensure_save_directory()
        
    def _get_save_directory(self):
        """Gets the appropriate save directory for the OS."""
        # Try to use user's home directory for saves
        if sys.platform == "win32":
            # Windows
            base = os.environ.get('APPDATA', os.path.expanduser('~'))
            save_path = Path(base) / self.game_name / "saves"
        elif sys.platform == "darwin":
            # macOS
            base = os.path.expanduser('~/Library/Application Support')
            save_path = Path(base) / self.game_name / "saves"
        else:
            # Linux and others
            base = os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))
            save_path = Path(base) / self.game_name / "saves"
        
        # Fallback to current directory if home isn't accessible
        try:
            save_path.mkdir(parents=True, exist_ok=True)
            # Test if we can write to this directory
            test_file = save_path / ".test"
            test_file.touch()
            test_file.unlink()
            return save_path
        except:
            # Fall back to current directory
            return Path.cwd() / "game_saves"
    
    def ensure_save_directory(self):
        """Creates save directory if it doesn't exist."""
        try:
            self.save_dir.mkdir(parents=True, exist_ok=True)
            print(f"Save directory: {self.save_dir}")
            return True
        except Exception as e:
            print(f"Warning: Could not create save directory: {e}")
            print("Saves will be created in current directory.")
            self.save_dir = Path.cwd()
            return False
    
    def get_save_slots(self):
        """Returns a list of available save slots."""
        slots = []
        for i in range(1, 4):  # 3 save slots
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
        
        # Add timestamp to save data
        player_data['last_saved'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Create backup of existing save if it exists
            if save_file.exists():
                shutil.copy2(save_file, backup_file)
            
            # Write new save
            temp_file = save_file.with_suffix('.tmp')
            with open(temp_file, 'w') as f:
                json.dump(player_data, f, indent=4)
            
            # Atomic rename (safer than direct write)
            temp_file.replace(save_file)
            
            return True, f"Game saved to slot {slot_number}"
            
        except Exception as e:
            # Try to restore from backup if save failed
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
        
        # Try to load main save file
        if save_file.exists():
            try:
                with open(save_file, 'r') as f:
                    data = json.load(f)
                return data, "Game loaded successfully"
            except Exception as e:
                print(f"Main save corrupted: {e}")
                # Try backup
                if backup_file.exists():
                    try:
                        with open(backup_file, 'r') as f:
                            data = json.load(f)
                        print("Loaded from backup save")
                        return data, "Game loaded from backup"
                    except:
                        return None, "Both main and backup saves are corrupted"
        
        return None, f"No save found in slot {slot_number}"
    
    def delete_save(self, slot_number):
        """Deletes a save slot."""
        if not 1 <= slot_number <= 3:
            return False, "Invalid slot number (use 1-3)"
        
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
    
    def export_save(self, slot_number, export_path=None):
        """Exports a save to a portable file."""
        if not 1 <= slot_number <= 3:
            return False, "Invalid slot number"
        
        save_file = self.save_dir / f"slot_{slot_number}.json"
        if not save_file.exists():
            return False, "Save slot is empty"
        
        if export_path is None:
            export_path = Path.cwd() / f"serpents_code_save_slot{slot_number}.json"
        
        try:
            shutil.copy2(save_file, export_path)
            return True, f"Save exported to: {export_path}"
        except Exception as e:
            return False, f"Export failed: {str(e)}"
    
    def import_save(self, import_path, slot_number):
        """Imports a save from a portable file."""
        if not 1 <= slot_number <= 3:
            return False, "Invalid slot number"
        
        import_file = Path(import_path)
        if not import_file.exists():
            return False, "Import file not found"
        
        try:
            # Validate the save file
            with open(import_file, 'r') as f:
                data = json.load(f)
            
            # Import to specified slot
            return self.save_game(slot_number, data)
        except Exception as e:
            return False, f"Import failed: {str(e)}"


class PlayerProgress:
    """Enhanced player progress manager with save slot support."""
    
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
    
    def save_menu(self):
        """Interactive save menu."""
        print("\n" + "="*50)
        print("SAVE GAME")
        print("="*50)
        
        # Show available slots
        slots = self.save_manager.get_save_slots()
        for slot in slots:
            if slot['exists']:
                print(f"\nSlot {slot['slot']}: {slot['player_name']} (Level {slot['level']})")
                print(f"  XP: {slot['xp']} | Quests: {slot['completed_quests']}")
                print(f"  Last saved: {slot['last_saved']}")
            else:
                print(f"\nSlot {slot['slot']}: [Empty]")
        
        print("\nOptions:")
        print("1-3: Save to slot")
        print("E: Export current save")
        print("C: Cancel")
        
        choice = input("\nChoice: ").strip().upper()
        
        if choice in ['1', '2', '3']:
            slot_num = int(choice)
            
            # Check if slot has existing save
            if slots[slot_num-1]['exists']:
                confirm = input(f"Overwrite save in slot {slot_num}? (y/n): ").lower()
                if confirm != 'y':
                    print("Save cancelled.")
                    return False
            
            # Update playtime before saving
            self.data['total_playtime'] += time.time() - self.data['session_start']
            self.data['session_start'] = time.time()
            
            success, message = self.save_manager.save_game(slot_num, self.data)
            print(message)
            
            if success:
                self.current_slot = slot_num
            
            return success
            
        elif choice == 'E':
            if self.current_slot:
                success, message = self.save_manager.export_save(self.current_slot)
                print(message)
            else:
                print("No active save to export. Save your game first.")
            return False
            
        else:
            print("Save cancelled.")
            return False
    
    def load_menu(self):
        """Interactive load menu."""
        print("\n" + "="*50)
        print("LOAD GAME")
        print("="*50)
        
        # Show available slots
        slots = self.save_manager.get_save_slots()
        has_saves = False
        
        for slot in slots:
            if slot['exists']:
                has_saves = True
                print(f"\nSlot {slot['slot']}: {slot['player_name']} (Level {slot['level']})")
                print(f"  XP: {slot['xp']} | Quests: {slot['completed_quests']}")
                print(f"  Last saved: {slot['last_saved']}")
            else:
                print(f"\nSlot {slot['slot']}: [Empty]")
        
        if not has_saves:
            print("\nNo saved games found.")
            return False
        
        print("\nOptions:")
        print("1-3: Load slot")
        print("I: Import save file")
        print("N: New game")
        print("C: Cancel")
        
        choice = input("\nChoice: ").strip().upper()
        
        if choice in ['1', '2', '3']:
            slot_num = int(choice)
            data, message = self.save_manager.load_game(slot_num)
            print(message)
            
            if data:
                self.data = data
                self.current_slot = slot_num
                # Reset session timer
                self.data['session_start'] = time.time()
                return True
            return False
            
        elif choice == 'I':
            import_path = input("Enter path to save file: ").strip()
            slot_num = input("Import to which slot (1-3): ").strip()
            
            if slot_num in ['1', '2', '3']:
                success, message = self.save_manager.import_save(import_path, int(slot_num))
                print(message)
                return success
            return False
            
        elif choice == 'N':
            self.data = self.create_new_game()
            self.current_slot = None
            print("Starting new game...")
            return True
            
        else:
            print("Load cancelled.")
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
        # Use a hidden slot 0 for autosaves
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


# Example usage in main game
def demonstrate_save_system():
    """Demonstrates the save system functionality."""
    
    print("SERPENT'S CODE - Save System Demo")
    print("="*50)
    
    player = PlayerProgress()
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. New Game")
        print("2. Load Game")
        print("3. Save Game")
        print("4. Quick Save (F5)")
        print("5. Play (simulate progress)")
        print("6. View Current Data")
        print("7. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            player.data = player.create_new_game()
            player.current_slot = None
            print("New game started!")
            
        elif choice == '2':
            player.load_menu()
            
        elif choice == '3':
            player.save_menu()
            
        elif choice == '4':
            player.quick_save()
            
        elif choice == '5':
            # Simulate some progress
            player.data['xp'] += 100
            player.data['level'] = (player.data['xp'] // 500) + 1
            if 'quest1' not in player.data['completed']:
                player.data['completed'].append('quest1')
            print(f"Progress made! XP: {player.data['xp']}, Level: {player.data['level']}")
            
        elif choice == '6':
            print("\nCurrent Game Data:")
            print(f"Player: {player.data['player_name']}")
            print(f"Level: {player.data['level']}")
            print(f"XP: {player.data['xp']}")
            print(f"Completed Quests: {player.data['completed']}")
            print(f"Current Slot: {player.current_slot or 'Not saved'}")
            
        elif choice == '7':
            if player.current_slot:
                save_choice = input("Save before exiting? (y/n): ").lower()
                if save_choice == 'y':
                    player.quick_save()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    # Run the demo
    demonstrate_save_system()