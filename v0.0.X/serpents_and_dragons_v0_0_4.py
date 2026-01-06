#!/usr/bin/env python3
"""
THE SERPENT'S CODE - A Python Learning Adventure
A game by Danny P. AKA CesiumSkater
Learn Python by saving the world of Fraylon!
"""

import json
import os
import sys
import time
import random
from datetime import datetime
from pathlib import Path
import traceback
import io
from contextlib import redirect_stdout, redirect_stderr

# ============================================================================
# CONFIGURATION
# ============================================================================

SAVE_FILE = "serpents_code_save.json"
VERSION = "2.0"

# Complete quest registry covering all Python concepts
QUEST_REGISTRY = {
    "Act 1: Roots of Code": [
        ("quest1_variables", "The Mossy Burrow", "Variables & Print", 50),
        ("quest2_numbers", "Numbers in Nature", "Numbers & Math", 75),
        ("quest3_strings", "String Spells", "Strings & Methods", 75),
        ("quest4_booleans", "Boolean Logic Gates", "Boolean Logic", 100),
        ("quest5_conditionals", "The Corrupted Creek", "Branching (if/elif/else)", 100),
    ],
    "Act 2: Structures of Power": [
        ("quest6_input", "The Talking Toad", "User Input", 125),
        ("quest7_lists", "The Arcane Archive", "Lists & Indexing", 150),
        ("quest8_for_loops", "The Clockwork Market", "For Loops", 150),
        ("quest9_list_operations", "List Magic", "Working with Lists", 175),
        ("quest10_while_loops", "Endless Patrols", "While Loops", 175),
    ],
    "Act 3: Advanced Magics": [
        ("quest11_functions", "Ritual of Balance", "Functions", 200),
        ("quest12_return_values", "Return of Power", "Returning Values", 200),
        ("quest13_dictionaries", "The Cult's Codex", "Dictionaries", 225),
        ("quest14_dict_operations", "Dictionary Mastery", "Working with Dictionaries", 225),
        ("quest15_sets_tuples", "Sacred Collections", "Sets & Tuples", 250),
    ],
    "Act 4: Master Techniques": [
        ("quest16_string_advanced", "String Alchemy", "Advanced String Methods", 275),
        ("quest17_data_processing", "Processing Ancient Texts", "Processing Text", 275),
        ("quest18_sorting", "Order from Chaos", "Sorting", 300),
        ("quest19_files", "The Rusted Catacombs", "Files", 300),
        ("quest20_exceptions", "Debugging Reality", "Exceptions & Bug Fixing", 325),
    ],
    "Act 5: Arcane Mastery": [
        ("quest21_classes", "The Iron Serpent", "Classes", 400),
        ("quest22_modules", "Council of Libraries", "Modules & Libraries", 400),
        ("quest23_inheritance", "Elemental Guardians", "Inheritance", 450),
        ("quest24_composition", "The Living Forest", "Composition", 450),
        ("quest25_integration", "The Verdant Crown", "Final Integration", 500),
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
    width = max(max_len + 4, len(title) + 4, 50)
    
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
    """Manages save game functionality."""
    
    def __init__(self):
        self.save_file = SAVE_FILE
    
    def create_new_game(self):
        """Creates a new game save."""
        return {
            "version": VERSION,
            "player_name": "Teagan",
            "character": "Goblin Druid",
            "completed": [],
            "xp": 0,
            "level": 1,
            "nature_tokens": 0,
            "achievements": [],
            "total_playtime": 0,
            "created_at": datetime.now().isoformat(),
            "last_saved": datetime.now().isoformat()
        }
    
    def save_game(self, data):
        """Saves game data to file."""
        try:
            data["last_saved"] = datetime.now().isoformat()
            with open(self.save_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save: {e}")
            return False
    
    def load_game(self):
        """Loads game data from file."""
        try:
            if os.path.exists(self.save_file):
                with open(self.save_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Failed to load save: {e}")
        return None
    
    def delete_save(self):
        """Deletes the save file."""
        try:
            if os.path.exists(self.save_file):
                os.remove(self.save_file)
            return True
        except Exception as e:
            print(f"Failed to delete save: {e}")
            return False

# ============================================================================
# CODE VALIDATOR
# ============================================================================

class CodeValidator:
    """Validates player code submissions safely."""
    
    def run_code(self, code, test_input=None):
        """Safely executes player code and captures output."""
        namespace = {
            '__builtins__': __builtins__,
            '__name__': '__main__'
        }
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        old_stdin = sys.stdin
        
        try:
            if test_input is not None:
                sys.stdin = io.StringIO(test_input)
            
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                exec(code, namespace)
            
            output = stdout_capture.getvalue()
            error = stderr_capture.getvalue()
            
            return True, output, error, namespace
            
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            return False, stdout_capture.getvalue(), error_msg, namespace
        finally:
            sys.stdin = old_stdin
    
    def check_output(self, code, expected_output, test_input=None):
        """Checks if code produces expected output."""
        success, output, error, _ = self.run_code(code, test_input)
        
        if not success:
            return False, f"Code error: {error}"
        
        output_clean = output.strip()
        expected_clean = expected_output.strip()
        
        if output_clean == expected_clean:
            return True, "Perfect! Output matches."
        else:
            return False, f"Output mismatch.\nExpected: {expected_clean}\nGot: {output_clean}"
    
    def check_contains(self, code, required):
        """Checks if code contains required elements."""
        missing = [r for r in required if r not in code]
        if missing:
            return False, f"Missing required: {', '.join(missing)}"
        return True, "All required elements present"
    
    def check_variable(self, code, var_name, expected_value=None):
        """Checks if a variable exists with optional value check."""
        success, _, _, namespace = self.run_code(code)
        
        if not success:
            return False, "Code has errors"
        
        if var_name not in namespace:
            return False, f"Variable '{var_name}' not found"
        
        if expected_value is not None and namespace[var_name] != expected_value:
            return False, f"Variable '{var_name}' has wrong value"
        
        return True, f"Variable '{var_name}' is correct"
    
    def check_function(self, code, func_name, test_args=None, expected_return=None):
        """Checks if a function exists and works correctly."""
        success, _, _, namespace = self.run_code(code)
        
        if not success:
            return False, "Code has errors"
        
        if func_name not in namespace:
            return False, f"Function '{func_name}' not found"
        
        if not callable(namespace[func_name]):
            return False, f"'{func_name}' is not a function"
        
        if test_args is not None and expected_return is not None:
            try:
                result = namespace[func_name](*test_args) if isinstance(test_args, tuple) else namespace[func_name](test_args)
                if result != expected_return:
                    return False, f"Function returned {result}, expected {expected_return}"
            except Exception as e:
                return False, f"Function error: {str(e)}"
        
        return True, f"Function '{func_name}' works correctly"

# ============================================================================
# QUEST IMPLEMENTATIONS
# ============================================================================

class Quest:
    """Base class for all quests."""
    
    def __init__(self, validator):
        self.validator = validator
        self.max_attempts = 3
    
    def get_code_input(self):
        """Gets multi-line code input from user."""
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("-" * 60)
        
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == 'DONE':
                    break
                lines.append(line)
            except EOFError:
                break
        
        return '\n'.join(lines)
    
    def run_challenge(self, title, task, validator_func, hints=None):
        """Runs a coding challenge with attempts."""
        clear_screen()
        print_header(f"CHALLENGE: {title}")
        print(f"\n{task}\n")
        
        if hints:
            print_hint(hints[0])
        
        for attempt in range(self.max_attempts):
            code = self.get_code_input()
            success, message = validator_func(code)
            
            if success:
                print_success(message)
                return True
            else:
                print_error(message)
                if attempt < self.max_attempts - 1:
                    remaining = self.max_attempts - attempt - 1
                    print(f"Attempts remaining: {remaining}")
                    if hints and len(hints) > attempt + 1:
                        print_hint(hints[attempt + 1])
        
        return False

# Quest 1: Variables
class Quest1_Variables(Quest):
    """Teaching variables and print statements."""
    
    def run(self):
        clear_screen()
        print_header("THE MOSSY BURROW")
        print("\nA raven drops a scroll at your feet.")
        print("'The forest is corrupted! Learn the ancient code to save us!'")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Variables")
        print("\nVariables are containers that store data.")
        print_code_box("""
message = "Hello, Fraylon!"
hero_level = 1
has_magic = True

print(message)
print("Level:", hero_level)
""", "Variable Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, msg = self.validator.check_variable(code, 'forest_name')
            if not success:
                return False, msg
            
            success, msg = self.validator.check_variable(code, 'tree_count')
            if not success:
                return False, msg
            
            success, output, _, _ = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'forest_name' not in code or 'tree_count' not in code:
                return False, "Use the variables forest_name and tree_count"
            
            return True, "Perfect! You've mastered variables!"
        
        return self.run_challenge(
            "Create Forest Variables",
            "1. Create a variable 'forest_name' with any forest name\n"
            "2. Create a variable 'tree_count' with any number\n"
            "3. Print both variables",
            validate,
            ["Variables store data. Use = to assign values."]
        )

# Quest 2: Numbers
class Quest2_Numbers(Quest):
    """Teaching numbers and math operations."""
    
    def run(self):
        clear_screen()
        print_header("NUMBERS IN NATURE")
        print("\nThe forest spirits speak in mathematical patterns.")
        print("Master numbers to understand their wisdom!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Numbers & Math")
        print_code_box("""
# Integer (whole numbers)
trees = 42
animals = 17

# Float (decimal numbers)
temperature = 23.5
rainfall = 12.7

# Math operations
total = trees + animals
difference = trees - animals
product = trees * 2
quotient = trees / 2
remainder = trees % 5
power = 2 ** 3  # 2 to the power of 3

print("Total creatures:", total)
""", "Number Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'mana_cost' in namespace and 'spell_power' in namespace:
                if 'total_power' in namespace:
                    expected = namespace['mana_cost'] + namespace['spell_power']
                    if namespace['total_power'] == expected:
                        return True, "Excellent math magic!"
            
            return False, "Calculate total_power as mana_cost + spell_power"
        
        return self.run_challenge(
            "Calculate Spell Power",
            "1. Create variable 'mana_cost' = 25\n"
            "2. Create variable 'spell_power' = 40\n"
            "3. Create 'total_power' = mana_cost + spell_power\n"
            "4. Print total_power",
            validate,
            ["Use + to add numbers", "Remember to print the result"]
        )

# Quest 3: Strings
class Quest3_Strings(Quest):
    """Teaching strings and string methods."""
    
    def run(self):
        clear_screen()
        print_header("STRING SPELLS")
        print("\nWords have power in Fraylon.")
        print("Learn to manipulate text to cast verbal spells!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Strings")
        print_code_box("""
# Creating strings
spell = "Lightning Bolt"
chant = 'Ancient wisdom'

# String methods
loud_spell = spell.upper()  # LIGHTNING BOLT
quiet_spell = spell.lower()  # lightning bolt
word_count = len(spell)     # 14

# Combining strings
full_chant = spell + " of " + chant

# String formatting
power = 100
message = f"Cast {spell} with {power} power!"

print(message)
""", "String Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'spell_name' not in namespace:
                return False, "Create a variable called 'spell_name'"
            
            if '.upper()' in code and namespace['spell_name'].upper() in output:
                return True, "String magic mastered!"
            
            return False, "Use .upper() to make the spell name uppercase"
        
        return self.run_challenge(
            "Create a Power Word",
            "1. Create variable 'spell_name' with any spell name\n"
            "2. Print the spell name in UPPERCASE using .upper()\n"
            "3. Print the length of the spell name using len()",
            validate,
            ["Strings have methods like .upper() and .lower()", "len() gives you the length"]
        )

# Quest 4: Booleans
class Quest4_Booleans(Quest):
    """Teaching boolean logic."""
    
    def run(self):
        clear_screen()
        print_header("BOOLEAN LOGIC GATES")
        print("\nThe ancient gates respond only to truth and falsehood.")
        print("Master boolean logic to pass!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Boolean Logic")
        print_code_box("""
# Boolean values
is_magical = True
is_corrupted = False

# Comparisons create booleans
health = 100
is_alive = health > 0  # True
is_hurt = health < 50  # False

# Boolean operators
has_key = True
door_unlocked = False
can_enter = has_key or door_unlocked  # True

is_day = True
is_safe = True
can_travel = is_day and is_safe  # True

is_trap = False
is_safe = not is_trap  # True

print("Can enter:", can_enter)
""", "Boolean Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'has_spell' in namespace and 'has_mana' in namespace:
                if 'can_cast' in namespace:
                    expected = namespace['has_spell'] and namespace['has_mana']
                    if namespace['can_cast'] == expected:
                        return True, "Boolean mastery achieved!"
            
            return False, "Set can_cast = has_spell and has_mana"
        
        return self.run_challenge(
            "Logic Gate Challenge",
            "1. Create 'has_spell' = True\n"
            "2. Create 'has_mana' = True\n"
            "3. Create 'can_cast' = has_spell and has_mana\n"
            "4. Print can_cast",
            validate,
            ["Use 'and' to check if both conditions are true"]
        )

# Quest 5: Conditionals
class Quest5_Conditionals(Quest):
    """Teaching if/elif/else statements."""
    
    def run(self):
        clear_screen()
        print_header("THE CORRUPTED CREEK")
        print("\nThe creek flows with dark magic.")
        print("Use conditional logic to purify it!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Conditionals")
        print_code_box("""
health = 75

if health > 80:
    print("Healthy")
elif health > 50:
    print("Wounded")
else:
    print("Critical")

# Multiple conditions
mana = 100
spell_cost = 30

if mana >= spell_cost:
    print("Cast spell!")
    mana = mana - spell_cost
else:
    print("Not enough mana!")
""", "If/Elif/Else")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, _ = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'if' not in code or 'else' not in code:
                return False, "Use if and else statements"
            
            if 'ph' not in code:
                return False, "Create a variable called 'ph'"
            
            # Check logic
            test_code = code.replace('ph = ', 'ph = 5 #')
            success, output, _, _ = self.validator.run_code(test_code)
            if success and 'acidic' in output.lower():
                return True, "Conditional logic mastered!"
            
            return False, "Check if ph < 7 for acidic water"
        
        return self.run_challenge(
            "Water Purification",
            "1. Create variable 'ph' with value 5\n"
            "2. If ph < 7, print 'Water is acidic'\n"
            "3. Else, print 'Water is alkaline'",
            validate,
            ["Remember indentation after if:", "Use < to check less than"]
        )

# Quest 6: Input
class Quest6_Input(Quest):
    """Teaching user input."""
    
    def run(self):
        clear_screen()
        print_header("THE TALKING TOAD")
        print("\nToadbert guards the gate.")
        print("'Answer my riddles to pass!'")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: User Input")
        print_code_box("""
# Getting input from user
name = input("What is your name? ")
print("Hello,", name)

# Input is always a string
age_text = input("Your age: ")
age = int(age_text)  # Convert to number

# Comparing input
password = input("Password: ")
if password.lower() == "ribbit":
    print("Gate opens!")
""", "Input Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            test_input = "Teagan\n"
            success, output, _, _ = self.validator.run_code(code, test_input)
            if not success:
                return False, "Code has errors"
            
            if 'input' not in code:
                return False, "Use input() to get user input"
            
            if 'Teagan' in output and 'Hello' in output:
                return True, "Input mastery achieved!"
            
            return False, "Get name with input() and print a greeting"
        
        return self.run_challenge(
            "Greet the Player",
            "1. Use input() to ask 'Enter your name: '\n"
            "2. Store it in variable 'player_name'\n"
            "3. Print 'Hello, ' followed by the name",
            validate,
            ["input() returns what the user types", "Store input in a variable"]
        )

# Quest 7: Lists
class Quest7_Lists(Quest):
    """Teaching lists and indexing."""
    
    def run(self):
        clear_screen()
        print_header("THE ARCANE ARCHIVE")
        print("\nThe magical library stores spells in ordered lists.")
        print("Learn to organize and access them!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Lists")
        print_code_box("""
# Creating lists
spells = ["fireball", "heal", "shield"]
numbers = [10, 20, 30, 40]
mixed = ["magic", 42, True]

# Accessing items (index starts at 0)
first_spell = spells[0]   # "fireball"
last_spell = spells[-1]   # "shield"

# List operations
spells.append("teleport")  # Add to end
spells.insert(0, "light")  # Add at position
spells.remove("heal")      # Remove item

# List info
spell_count = len(spells)
has_fireball = "fireball" in spells

print("Spells:", spells)
""", "List Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'inventory' not in namespace:
                return False, "Create a list called 'inventory'"
            
            if not isinstance(namespace['inventory'], list):
                return False, "inventory should be a list"
            
            if len(namespace['inventory']) >= 3:
                if 'inventory[0]' in code or 'inventory[1]' in code:
                    return True, "List mastery achieved!"
            
            return False, "Create a list with 3 items and access one by index"
        
        return self.run_challenge(
            "Create Inventory",
            "1. Create list 'inventory' with 3 items\n"
            "2. Print the entire list\n"
            "3. Print the first item using inventory[0]",
            validate,
            ["Lists use square brackets []", "Index starts at 0"]
        )

# Quest 8: For Loops
class Quest8_ForLoops(Quest):
    """Teaching for loops."""
    
    def run(self):
        clear_screen()
        print_header("THE CLOCKWORK MARKET")
        print("\nThe market automata repeat their tasks endlessly.")
        print("Master loops to control them!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: For Loops")
        print_code_box("""
# Loop through a list
spells = ["fire", "ice", "lightning"]
for spell in spells:
    print("Casting:", spell)

# Loop with range
for i in range(5):
    print("Count:", i)  # 0, 1, 2, 3, 4

# Loop with range start/stop
for level in range(1, 6):
    print("Level", level)  # 1, 2, 3, 4, 5

# Loop through string
word = "MAGIC"
for letter in word:
    print(letter)  # M A G I C
""", "For Loop Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, _ = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'for' not in code:
                return False, "Use a for loop"
            
            if 'range(3)' in code or 'range(1, 4)' in code:
                count = output.lower().count('hello')
                if count >= 3:
                    return True, "Loop mastery achieved!"
            
            return False, "Use for loop with range(3) to print 3 times"
        
        return self.run_challenge(
            "Repeat the Chant",
            "1. Use a for loop with range(3)\n"
            "2. Print 'Hello Fraylon!' three times",
            validate,
            ["for i in range(3):", "Remember to indent the print"]
        )

# Quest 9: List Operations
class Quest9_ListOperations(Quest):
    """Teaching advanced list operations."""
    
    def run(self):
        clear_screen()
        print_header("LIST MAGIC")
        print("\nManipulate magical lists with advanced techniques!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Working with Lists")
        print_code_box("""
# Slicing lists
items = ["a", "b", "c", "d", "e"]
first_two = items[0:2]    # ["a", "b"]
middle = items[1:4]       # ["b", "c", "d"]
last_two = items[-2:]     # ["d", "e"]

# List methods
numbers = [3, 1, 4, 1, 5]
numbers.sort()            # [1, 1, 3, 4, 5]
numbers.reverse()         # [5, 4, 3, 1, 1]
numbers.count(1)          # 2 (count of 1s)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Combining lists
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4]
""", "Advanced List Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'numbers' in namespace:
                if '.append(' in code and '.sort(' in code:
                    return True, "List operations mastered!"
            
            return False, "Create numbers list, append items, and sort"
        
        return self.run_challenge(
            "Organize the Arsenal",
            "1. Create list 'numbers' = [3, 1, 4]\n"
            "2. Append the number 2\n"
            "3. Sort the list with .sort()\n"
            "4. Print the sorted list",
            validate,
            ["Use .append() to add items", "Use .sort() to sort"]
        )

# Quest 10: While Loops
class Quest10_WhileLoops(Quest):
    """Teaching while loops."""
    
    def run(self):
        clear_screen()
        print_header("ENDLESS PATROLS")
        print("\nThe guards patrol until conditions change.")
        print("Control their eternal march!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: While Loops")
        print_code_box("""
# Basic while loop
count = 0
while count < 5:
    print("Count:", count)
    count = count + 1

# While with condition
health = 100
while health > 0:
    print("Still alive!")
    health = health - 20

# Break and continue
while True:
    command = input("Enter command: ")
    if command == "quit":
        break  # Exit loop
    if command == "skip":
        continue  # Skip to next iteration
    print("Processing:", command)
""", "While Loop Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, _ = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'while' not in code:
                return False, "Use a while loop"
            
            countdown_found = all(str(i) in output for i in range(5, 0, -1))
            if countdown_found:
                return True, "While loop mastered!"
            
            return False, "Count down from 5 to 1"
        
        return self.run_challenge(
            "Countdown Timer",
            "1. Create variable 'timer' = 5\n"
            "2. While timer > 0:\n"
            "3. Print timer value\n"
            "4. Decrease timer by 1",
            validate,
            ["while timer > 0:", "timer = timer - 1"]
        )

# Additional quests follow the same pattern...
# I'll add a few more key ones:

# Quest 11: Functions
class Quest11_Functions(Quest):
    """Teaching functions."""
    
    def run(self):
        clear_screen()
        print_header("RITUAL OF BALANCE")
        print("\nCreate reusable magical rituals with functions!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Functions")
        print_code_box("""
# Define a function
def greet():
    print("Hello, adventurer!")

# Call the function
greet()

# Function with parameters
def cast_spell(spell_name, power):
    print(f"Casting {spell_name} with {power} power!")

cast_spell("Fireball", 100)

# Function with return value
def add(a, b):
    result = a + b
    return result

total = add(5, 3)
print("Total:", total)
""", "Function Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, msg = self.validator.check_function(
                code, 'calculate', (10, 5), 15
            )
            if success:
                return True, "Function mastery achieved!"
            return False, msg
        
        return self.run_challenge(
            "Create a Calculator",
            "1. Define function 'calculate' with parameters a, b\n"
            "2. Return a + b\n"
            "3. Call calculate(10, 5) and print result",
            validate,
            ["def calculate(a, b):", "return a + b"]
        )

# Quest 13: Dictionaries
class Quest13_Dictionaries(Quest):
    """Teaching dictionaries."""
    
    def run(self):
        clear_screen()
        print_header("THE CULT'S CODEX")
        print("\nThe cult stores their secrets in key-value pairs.")
        print("Master dictionaries to decode them!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Dictionaries")
        print_code_box("""
# Creating dictionaries
player = {
    "name": "Teagan",
    "level": 5,
    "health": 100,
    "mana": 50
}

# Accessing values
name = player["name"]
level = player.get("level", 1)  # With default

# Modifying dictionaries
player["health"] = 75  # Update
player["gold"] = 100   # Add new
del player["mana"]     # Remove

# Dictionary methods
keys = player.keys()     # All keys
values = player.values() # All values
items = player.items()   # Key-value pairs

# Check if key exists
if "health" in player:
    print("Health:", player["health"])
""", "Dictionary Operations")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'character' in namespace:
                if isinstance(namespace['character'], dict):
                    if 'name' in namespace['character'] and 'class' in namespace['character']:
                        return True, "Dictionary mastery achieved!"
            
            return False, "Create dictionary with 'name' and 'class' keys"
        
        return self.run_challenge(
            "Character Sheet",
            "1. Create dictionary 'character' with:\n"
            "   - 'name': any name\n"
            "   - 'class': any class\n"
            "   - 'level': 1\n"
            "2. Print the character's name",
            validate,
            ["Use curly braces {}", "key: value pairs"]
        )

# Quest 21: Classes
class Quest21_Classes(Quest):
    """Teaching classes and objects."""
    
    def run(self):
        clear_screen()
        print_header("THE IRON SERPENT")
        print("\nThe Iron Serpent awakens! Create elemental guardians!")
        wait_for_enter()
        
        # Lesson
        clear_screen()
        print_header("LESSON: Classes")
        print_code_box("""
# Define a class
class Spell:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def cast(self):
        print(f"{self.name} deals {self.damage} damage!")

# Create objects
fireball = Spell("Fireball", 50)
lightning = Spell("Lightning", 40)

# Use objects
fireball.cast()
print(fireball.damage)

# Class with methods
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount}")
""", "Class Examples")
        wait_for_enter()
        
        # Challenge
        def validate(code):
            success, output, _, namespace = self.validator.run_code(code)
            if not success:
                return False, "Code has errors"
            
            if 'Dragon' in namespace:
                if 'class' in str(type(namespace['Dragon'])):
                    if '__init__' in code and 'self' in code:
                        return True, "Class mastery achieved!"
            
            return False, "Define Dragon class with __init__ method"
        
        return self.run_challenge(
            "Create the Dragon",
            "1. Define class 'Dragon'\n"
            "2. Add __init__ method with self, name\n"
            "3. Store self.name = name\n"
            "4. Create a Dragon object",
            validate,
            ["class Dragon:", "def __init__(self, name):"]
        )

# ============================================================================
# GAME ENGINE
# ============================================================================

class GameEngine:
    """Main game engine."""
    
    def __init__(self):
        self.save_manager = SaveManager()
        self.validator = CodeValidator()
        self.player_data = None
        self.running = True
        
        # Quest implementations
        self.quests = {
            "quest1_variables": Quest1_Variables(self.validator),
            "quest2_numbers": Quest2_Numbers(self.validator),
            "quest3_strings": Quest3_Strings(self.validator),
            "quest4_booleans": Quest4_Booleans(self.validator),
            "quest5_conditionals": Quest5_Conditionals(self.validator),
            "quest6_input": Quest6_Input(self.validator),
            "quest7_lists": Quest7_Lists(self.validator),
            "quest8_for_loops": Quest8_ForLoops(self.validator),
            "quest9_list_operations": Quest9_ListOperations(self.validator),
            "quest10_while_loops": Quest10_WhileLoops(self.validator),
            "quest11_functions": Quest11_Functions(self.validator),
            "quest13_dictionaries": Quest13_Dictionaries(self.validator),
            "quest21_classes": Quest21_Classes(self.validator),
        }
    
    def show_title(self):
        """Display title screen."""
        clear_screen()
        print("=" * 70)
        print()
        print("         THE SERPENT'S CODE".center(70))
        print("     A Python Learning Adventure".center(70))
        print()
        print("        Learn Python, Save Fraylon!".center(70))
        print()
        print("=" * 70)
        print()
        input("           Press Enter to begin...")
    
    def main_menu(self):
        """Display main menu."""
        clear_screen()
        print_header("MAIN MENU")
        
        if self.player_data:
            print(f"\nWelcome back, {self.player_data['player_name']}!")
            print(f"Level {self.player_data['level']} {self.player_data['character']}")
            print(f"XP: {self.player_data['xp']}")
            print(f"Completed: {len(self.player_data['completed'])} quests")
        
        print("\n1. New Game")
        print("2. Continue")
        print("3. Quest Map")
        print("4. Save Game")
        print("5. Exit")
        
        return input("\nChoice: ").strip()
    
    def quest_map(self):
        """Display available quests."""
        clear_screen()
        print_header("QUEST MAP")
        
        for act_name, quests in QUEST_REGISTRY.items():
            print(f"\n{act_name}")
            print("-" * 50)
            for quest_id, name, topic, xp in quests:
                status = "[DONE]" if quest_id in self.player_data.get('completed', []) else "[    ]"
                available = "*" if quest_id in self.quests else " "
                print(f"{status} {name} - {topic} ({xp} XP) {available}")
        
        print("\n* = Available now")
        wait_for_enter()
    
    def get_next_quest(self):
        """Find next available quest."""
        for act_name, quests in QUEST_REGISTRY.items():
            for quest_id, name, topic, xp in quests:
                if quest_id not in self.player_data['completed'] and quest_id in self.quests:
                    return quest_id, name, topic, xp
        return None
    
    def run_quest(self, quest_id, name, topic, xp):
        """Run a specific quest."""
        clear_screen()
        print_header(f"STARTING: {name}")
        print(f"\nTopic: {topic}")
        print(f"Reward: {xp} XP")
        wait_for_enter()
        
        if quest_id in self.quests:
            success = self.quests[quest_id].run()
            
            if success:
                print_success(f"Quest Complete! +{xp} XP")
                self.player_data['completed'].append(quest_id)
                self.player_data['xp'] += xp
                
                # Level up check
                new_level = (self.player_data['xp'] // 250) + 1
                if new_level > self.player_data['level']:
                    self.player_data['level'] = new_level
                    print(f"\n[LEVEL UP!] You are now level {new_level}!")
                
                self.save_manager.save_game(self.player_data)
                wait_for_enter()
                return True
            else:
                print_error("Quest failed. Try again!")
                wait_for_enter()
                return False
        else:
            print_error("Quest not yet implemented")
            wait_for_enter()
            return False
    
    def run(self):
        """Main game loop."""
        self.show_title()
        
        # Try to load save
        save_data = self.save_manager.load_game()
        if save_data:
            self.player_data = save_data
        
        while self.running:
            choice = self.main_menu()
            
            if choice == '1':  # New Game
                self.player_data = self.save_manager.create_new_game()
                print("\nStarting new adventure...")
                self.save_manager.save_game(self.player_data)
                wait_for_enter()
                
            elif choice == '2':  # Continue
                if not self.player_data:
                    print("No save game found. Starting new game...")
                    self.player_data = self.save_manager.create_new_game()
                    wait_for_enter()
                
                next_quest = self.get_next_quest()
                if next_quest:
                    quest_id, name, topic, xp = next_quest
                    self.run_quest(quest_id, name, topic, xp)
                else:
                    print("\nAll available quests completed!")
                    print("More content coming soon...")
                    wait_for_enter()
                
            elif choice == '3':  # Quest Map
                if self.player_data:
                    self.quest_map()
                else:
                    print("Start a game first!")
                    wait_for_enter()
                
            elif choice == '4':  # Save
                if self.player_data:
                    if self.save_manager.save_game(self.player_data):
                        print("Game saved!")
                    else:
                        print("Save failed!")
                    wait_for_enter()
                else:
                    print("No game to save!")
                    wait_for_enter()
                
            elif choice == '5':  # Exit
                if self.player_data:
                    self.save_manager.save_game(self.player_data)
                print("\nFarewell, brave coder!")
                self.running = False
                
            else:
                print("Invalid choice!")
                wait_for_enter()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Run the game."""
    try:
        game = GameEngine()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Progress saved.")
    except Exception as e:
        print(f"\nError: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
