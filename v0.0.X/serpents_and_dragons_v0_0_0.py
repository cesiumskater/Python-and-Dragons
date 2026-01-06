#!/usr/bin/env python3
"""
🐍 THE SERPENT'S CODE 🐍
A Python Learning Adventure in the World of Fraylon

Master the ancient art of Pythonic magic and save the world from corruption!

Created by: Danny & Claude (Anthropic)
Version: 1.0
Python: 3.7+

Run this file to start your adventure:
    python serpents_code.py
"""

import json
import time
import random
import os
import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path


# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

SAVE_FILE = "player_data.json"

QUEST_REGISTRY = {
    "Act 1: Roots of Code": [
        ("quest1_mossy_burrow", "The Mossy Burrow", "Variables & Print", 50),
        ("quest2_corrupted_creek", "The Corrupted Creek", "Conditionals", 75),
        ("quest3_talking_toad", "The Talking Toad", "Input & Logic", 100),
        ("quest4_numbers_nature", "Numbers in Nature", "Numbers & Math", 100),
        ("quest5_string_spells", "String Spells", "String Methods", 125),
    ],
    "Act 2: City of Iron": [
        ("quest6_clockwork_market", "The Clockwork Market", "For Loops", 150),
        ("quest7_arcane_archive", "The Arcane Archive", "Lists & Indexing", 150),
        ("quest8_list_magic", "List Magic", "List Operations", 175),
        ("quest9_ritual_balance", "The Ritual of Balance", "Functions", 200),
        ("quest10_while_loops", "Endless Patrols", "While Loops", 200),
    ],
    "Act 3: Draconic Algorithm": [
        ("quest11_cult_network", "The Cult's Network", "Dictionaries", 225),
        ("quest12_sets_tuples", "Sacred Collections", "Sets & Tuples", 225),
        ("quest13_rusted_catacombs", "The Rusted Catacombs", "File I/O", 250),
        ("quest14_debugging", "Debugging the Corruption", "Exceptions", 250),
        ("quest15_iron_serpent", "The Iron Serpent", "Classes", 300),
    ],
    "Act 4: Verdant Rebirth": [
        ("quest16_modules", "The Council of Syntax", "Modules", 300),
        ("quest17_inheritance", "Elemental Guardians", "Inheritance", 350),
        ("quest18_composition", "The Living Forest", "Composition", 350),
        ("quest19_verdant_crown", "The Verdant Crown", "Integration", 500),
    ]
}


# ============================================================================
# UTILITY FUNCTIONS - DIALOGUE & UI
# ============================================================================

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    """Prints a fancy header."""
    width = 60
    print("\n" + "=" * width)
    print(text.center(width))
    print("=" * width)


def speak(text, delay=0.03, add_pause=True):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
    if add_pause:
        time.sleep(0.3)


def speak_fast(text):
    """Prints text quickly without character delay."""
    print(text)


def wait_for_enter():
    """Waits for user to press Enter."""
    input("\n[Press Enter to continue]")


def print_code_box(code, title="Code"):
    """Prints code in a nice box."""
    lines = code.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    width = max(max_len + 4, len(title) + 4)
    
    print("\n" + "┌─" + title + "─" + "─" * (width - len(title) - 2) + "┐")
    for line in lines:
        print("│ " + line.ljust(width - 2) + " │")
    print("└" + "─" * width + "┘\n")


def print_success(message):
    """Prints a success message."""
    print(f"\n✨ {message} ✨\n")


def print_error(message):
    """Prints an error message."""
    print(f"\n❌ {message}\n")


def print_hint(message):
    """Prints a hint message."""
    print(f"\n💡 Hint: {message}\n")


# ============================================================================
# PROGRESS MANAGEMENT
# ============================================================================

def load_progress():
    """Loads player progress from JSON file."""
    if not os.path.exists(SAVE_FILE):
        default_data = {
            "player_name": "Teagan",
            "character": "Goblin Druid",
            "completed": [],
            "xp": 0,
            "level": 1,
            "nature_tokens": 0,
            "current_act": 1,
            "achievements": [],
            "hints_used": 0,
            "total_attempts": 0,
            "perfect_quests": 0
        }
        save_progress(default_data)
        return default_data
    
    with open(SAVE_FILE, "r") as f:
        return json.load(f)


def save_progress(data):
    """Saves player progress to JSON file."""
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def award_xp(player, amount):
    """Awards XP to the player."""
    player['xp'] += amount
    return amount


def check_level_up(player):
    """Checks if player should level up."""
    xp_needed = 250 * player['level'] + 100 * (player['level'] - 1) * player['level'] // 2
    
    if player['xp'] >= xp_needed:
        player['level'] += 1
        return True
    return False


# ============================================================================
# CODE VALIDATOR
# ============================================================================

class CodeValidator:
    """Validates player code submissions."""
    
    def __init__(self):
        self.test_results = []
    
    def run_code(self, code, test_input=None):
        """
        Executes player code safely and captures output.
        Returns: (success: bool, output: str, error: str)
        """
        namespace = {
            '__builtins__': __builtins__,
            '__name__': '__main__'
        }
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            if test_input is not None:
                old_stdin = sys.stdin
                sys.stdin = io.StringIO(test_input)
            
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                exec(code, namespace)
            
            if test_input is not None:
                sys.stdin = old_stdin
            
            output = stdout_capture.getvalue()
            error = stderr_capture.getvalue()
            
            return True, output, error
            
        except Exception as e:
            if test_input is not None:
                sys.stdin = old_stdin
            
            error_msg = f"{type(e).__name__}: {str(e)}\n"
            error_msg += traceback.format_exc()
            return False, stdout_capture.getvalue(), error_msg
    
    def check_output(self, code, expected_output, test_input=None):
        """Checks if code produces expected output."""
        success, output, error = self.run_code(code, test_input)
        
        if not success:
            return False, f"Error in code:\n{error}"
        
        output_clean = output.strip()
        expected_clean = expected_output.strip()
        
        if output_clean == expected_clean:
            return True, "Perfect! Output matches expected result."
        else:
            return False, f"Output doesn't match.\nExpected:\n{expected_clean}\n\nGot:\n{output_clean}"
    
    def check_contains(self, code, required_keywords):
        """Checks if code contains required keywords/patterns."""
        missing = []
        for keyword in required_keywords:
            if keyword not in code:
                missing.append(keyword)
        
        if missing:
            return False, f"Code must contain: {', '.join(missing)}"
        return True, "All required elements present!"
    
    def check_variable_exists(self, code, var_name, expected_value=None):
        """Checks if a variable is defined with optional value check."""
        namespace = {}
        try:
            exec(code, namespace)
            
            if var_name not in namespace:
                return False, f"Variable '{var_name}' not found."
            
            if expected_value is not None and namespace[var_name] != expected_value:
                return False, f"Variable '{var_name}' has wrong value.\nExpected: {expected_value}\nGot: {namespace[var_name]}"
            
            return True, f"Variable '{var_name}' correctly defined!"
            
        except Exception as e:
            return False, f"Error executing code: {str(e)}"
    
    def check_function_exists(self, code, func_name, test_args=None, expected_return=None):
        """Checks if a function is defined and works correctly."""
        namespace = {}
        try:
            exec(code, namespace)
            
            if func_name not in namespace:
                return False, f"Function '{func_name}' not found."
            
            func = namespace[func_name]
            
            if not callable(func):
                return False, f"'{func_name}' is not a function."
            
            if test_args is not None and expected_return is not None:
                result = func(*test_args) if isinstance(test_args, tuple) else func(test_args)
                if result != expected_return:
                    return False, f"Function returned wrong value.\nExpected: {expected_return}\nGot: {result}"
            
            return True, f"Function '{func_name}' works correctly!"
            
        except Exception as e:
            return False, f"Error testing function: {str(e)}"


# ============================================================================
# QUEST 1: THE MOSSY BURROW
# ============================================================================

def quest1_mossy_burrow(player, validator):
    """Quest 1: Teaching Variables, print(), and comments."""
    
    # INTRO
    clear_screen()
    print_header("🍃 THE MOSSY BURROW 🍃")
    
    speak("\nA raven with feathers dark as obsidian swoops into your burrow,")
    speak("dropping a scroll sealed with emerald wax.")
    speak("\nThe bird caws harshly: 'Message for the druid who listens to wind!'")
    speak("'And don't fry my feathers with your druidic nonsense!'\n")
    wait_for_enter()
    
    speak("You break the seal. Ancient script glows softly...")
    speak("But the words are encoded in... Python?\n")
    wait_for_enter()
    
    # LESSON: VARIABLES
    clear_screen()
    print_header("📚 LESSON: VARIABLES 📚")
    
    example = """# Creating variables (containers for data)
message = "The forest is in danger!"
sender = "Council of Mages"
urgency = "HIGH"

# Variables can be used and reused
print(message)
print(sender)"""
    
    print_code_box(example, "Example")
    
    speak("Notice:")
    speak("  • Variable names are on the LEFT of the =")
    speak("  • Values are on the RIGHT of the =")
    speak("  • Text (strings) must be in quotes: 'like this' or \"like this\"")
    speak("  • No quotes needed for numbers: age = 127\n")
    wait_for_enter()
    
    # LESSON: PRINT
    clear_screen()
    print_header("📚 LESSON: PRINT STATEMENTS 📚")
    
    speak("\nThe print() function displays output to the screen.")
    speak("It's how your program 'speaks' to the world.\n")
    
    example = """# Printing text
print("Hello, forest!")

# Printing variables
name = "Teagan"
print(name)

# Printing multiple things
print("Druid:", name)
print("Level:", 1)"""
    
    print_code_box(example, "Example")
    
    speak("The print() function:")
    speak("  • Can print text in quotes")
    speak("  • Can print variable values")
    speak("  • Can print multiple items separated by commas\n")
    wait_for_enter()
    
    # LESSON: COMMENTS
    clear_screen()
    print_header("📚 LESSON: COMMENTS 📚")
    
    speak("\nComments are notes for yourself (and other coders).")
    speak("Python ignores them - they're just for humans.\n")
    
    example = """# This is a comment - Python ignores this line
# Use comments to explain your code

message = "Help!"  # Comments can go after code too

# Comments are like a druid's journal notes
# They help you remember what spells do what"""
    
    print_code_box(example, "Example")
    
    speak("Comments start with the # symbol.")
    speak("Everything after # on that line is ignored by Python.\n")
    wait_for_enter()
    
    # CHALLENGE 1
    clear_screen()
    print_header("⚔️ CHALLENGE 1: DECODE THE MESSAGE ⚔️")
    
    speak("\nThe scroll contains an encoded message.")
    speak("Create variables to decode it!\n")
    
    speak("Your task:")
    speak("  1. Create a variable called 'message' with text: The forest is in danger!")
    speak("  2. Create a variable called 'sender' with text: Council of Mages")
    speak("  3. Print both variables\n")
    
    print_hint("Remember: text must be in quotes!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['message', 'sender', 'print'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, msg2 = validator.check_variable_exists(code, 'message', 'The forest is in danger!')
        if not success2:
            print_error(msg2)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success3, msg3 = validator.check_variable_exists(code, 'sender', 'Council of Mages')
        if not success3:
            print_error(msg3)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success4, output, error = validator.run_code(code)
        if not success4:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'The forest is in danger!' in output and 'Council of Mages' in output:
            print_success("The scroll glows brightly and reveals its message!")
            speak(f"\nYour code output:\n{output}")
            break
        else:
            print_error("The variables are defined, but they're not being printed!")
            if attempts < max_attempts:
                print_hint(f"Did you print() both variables? Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 2
    clear_screen()
    print_header("⚔️ CHALLENGE 2: GRIBBLE'S NOTES ⚔️")
    
    speak("\nYou must record your observations about the corrupted forest.")
    speak("Use comments to document what you see!\n")
    
    speak("Your task:")
    speak("  1. Create a variable 'observation' with text: The creek runs backward")
    speak("  2. Add a comment above it explaining what you noticed")
    speak("  3. Print the observation")
    speak("  4. Add another comment describing how you feel\n")
    
    print_hint("Comments start with #")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        if '#' not in code:
            print_error("No comments found! Remember to use # for comments.")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success1, msg1 = validator.check_variable_exists(code, 'observation', 'The creek runs backward')
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'The creek runs backward' in output:
            print_success("Excellent! Your druidic notes are clear and well-documented!")
            speak(f"\nYour code output:\n{output}")
            break
        else:
            print_error("Don't forget to print the observation!")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    # OUTRO
    clear_screen()
    speak("\n✨ The scroll's magic dissipates, its message now clear. ✨\n")
    speak("The raven tilts its head: 'Not bad for a mushroom-muncher.'")
    speak("'The Council will want to hear from you. Head to Mallport... if you dare.'\n")
    speak("With a final caw, the bird takes flight.\n")
    speak("You've learned the basics of variables and print statements—")
    speak("the foundation of all Pythonic magic.\n")
    wait_for_enter()
    
    return True


# ============================================================================
# QUEST 2: THE CORRUPTED CREEK
# ============================================================================

def quest2_corrupted_creek(player, validator):
    """Quest 2: Teaching Conditionals (if, elif, else)."""
    
    # INTRO
    clear_screen()
    print_header("🌊 THE CORRUPTED CREEK 🌊")
    
    speak("\nYou follow the creek that once ran crystal-clear through your grove.")
    speak("Now it flows thick and black, like corrupted code.")
    speak("\nA mushroom spirit materializes on a log:")
    speak("'Balance is like a well-written program, goblin.'")
    speak("'Too acidic, and everything breaks! You need conditional logic!'\n")
    wait_for_enter()
    
    # LESSON: CONDITIONALS
    clear_screen()
    print_header("📚 LESSON: CONDITIONALS 📚")
    
    speak("\nConditionals let your program make DECISIONS based on conditions.")
    speak("They're like choosing different paths in a forest.\n")
    
    example = """# Basic if statement
temperature = 75

if temperature > 80:
    print("It's hot!")

# if-else: two options
if temperature > 80:
    print("It's hot!")
else:
    print("It's not too hot")

# if-elif-else: multiple options
if temperature > 90:
    print("It's very hot!")
elif temperature > 70:
    print("It's warm")
else:
    print("It's cool")"""
    
    print_code_box(example, "Example")
    
    speak("Key points:")
    speak("  • 'if' checks a condition")
    speak("  • 'elif' checks another condition (else-if)")
    speak("  • 'else' handles everything else")
    speak("  • Code under each must be INDENTED (4 spaces or Tab)")
    speak("  • Conditions end with a colon :\n")
    wait_for_enter()
    
    # LESSON: COMPARISONS
    clear_screen()
    print_header("📚 LESSON: COMPARISON OPERATORS 📚")
    
    speak("\nComparison operators let you compare values.\n")
    
    example = """# Comparison operators
x = 10
y = 5

# Greater than
if x > y:
    print("x is greater")

# Less than
if y < x:
    print("y is smaller")

# Equal to (double equals!)
if x == 10:
    print("x equals 10")

# Not equal to
if x != y:
    print("x and y are different")"""
    
    print_code_box(example, "Example")
    
    speak("Common operators:")
    speak("  > greater than")
    speak("  < less than")
    speak("  == equal to (note: TWO equals signs!)")
    speak("  != not equal to")
    speak("  >= greater than or equal")
    speak("  <= less than or equal\n")
    
    print_hint("A single = assigns a value. Double == compares values!")
    wait_for_enter()
    
    # CHALLENGE 1
    clear_screen()
    print_header("⚔️ CHALLENGE 1: TEST THE WATER ⚔️")
    
    speak("\nThe mushroom spirit hands you a pH testing kit.")
    speak("'Test the water and decide which potion to use!'\n")
    
    speak("Your task:")
    speak("  1. Create a variable 'ph' and set it to 5 (very acidic)")
    speak("  2. If ph is less than 6, print: Use mossroot elixir")
    speak("  3. Otherwise, print: Water is not too acidic\n")
    
    print_hint("Use if and else, with proper indentation!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['if', 'ph'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Check your indentation and colons! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'Use mossroot elixir' in output or 'mossroot' in output.lower():
            print_success("Correct! The acidic water needs mossroot elixir!")
            speak(f"\nYour code output:\n{output}")
            break
        else:
            print_error("The output isn't quite right. Check your condition.")
            if attempts < max_attempts:
                print_hint(f"Since ph=5 and 5 < 6, what should print? Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 2
    clear_screen()
    print_header("⚔️ CHALLENGE 2: FULL POTION LOGIC ⚔️")
    
    speak("\nNow you must handle ALL possible pH levels!")
    speak("Different ranges need different potions.\n")
    
    speak("Your task:")
    speak("  1. Create a variable 'ph' and set it to 9 (very alkaline)")
    speak("  2. If ph < 6, print: Use mossroot elixir")
    speak("  3. Elif ph > 8, print: Use stonebloom powder")
    speak("  4. Else, print: Use waterleaf infusion\n")
    
    print_hint("Use if, elif, and else. Don't forget colons and indentation!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        required = ['if', 'elif', 'else', 'ph']
        success1, msg1 = validator.check_contains(code, required)
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"You need if, elif, and else! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Check your syntax! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'stonebloom' in output.lower():
            print_success("Perfect! Your conditional logic handles all cases!")
            speak(f"\nYour code output:\n{output}")
            break
        else:
            print_error("With pH=9, you should use stonebloom powder!")
            if attempts < max_attempts:
                print_hint(f"Check your elif condition. Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    # OUTRO
    clear_screen()
    speak("\n✨ You pour the correct potion into the creek. ✨\n")
    speak("The black water begins to clear, flowing pure once more.")
    speak("The mushroom spirit nods approvingly:")
    speak("'Balance restored through logic! You're learning, goblin.'\n")
    speak("'But darker corruption lies ahead. You'll need more than conditionals.'\n")
    wait_for_enter()
    
    return True


# ============================================================================
# QUEST 3: THE TALKING TOAD
# ============================================================================

def quest3_talking_toad(player, validator):
    """Quest 3: Teaching input() and string methods."""
    
    # INTRO
    clear_screen()
    print_header("🐸 THE TALKING TOAD 🐸")
    
    speak("\nThe path to Mallport is blocked by an enormous toad.")
    speak("It wears a tiny wizard hat and looks incredibly smug.")
    speak("\n'Toadbert the Gatekeeper, at your service,' it croaks.")
    speak("'You can't brute-force my gate, genius! Try some logic instead!'")
    speak("\n'Speak the secret word, and I'll let you pass.'")
    speak("'But you'll need to ASK for it first...'\n")
    wait_for_enter()
    
    # LESSON: INPUT
    clear_screen()
    print_header("📚 LESSON: USER INPUT 📚")
    
    speak("\nThe input() function lets you ASK the user for information.")
    speak("Your program can pause and wait for them to type something.\n")
    
    example = """# Getting input from the user
name = input("What is your name? ")
print("Hello,", name)

# Input is always stored as text (a string)
age = input("How old are you? ")
print("You are", age, "years old")"""
    
    print_code_box(example, "Example")
    
    speak("How input() works:")
    speak("  • Shows a prompt message to the user")
    speak("  • Waits for them to type and press Enter")
    speak("  • Returns what they typed as text (a string)")
    speak("  • You usually store it in a variable\n")
    
    print_hint("Input is ALWAYS text, even if someone types numbers!")
    wait_for_enter()
    
    # LESSON: STRING COMPARISON
    clear_screen()
    print_header("📚 LESSON: STRING COMPARISON 📚")
    
    speak("\nYou can compare text (strings) just like numbers.\n")
    
    example = """# Comparing strings
password = input("Enter password: ")

if password == "secret":
    print("Access granted!")
else:
    print("Wrong password!")

# Case matters!
word = "HELLO"
if word == "hello":  # This is False!
    print("Match")
else:
    print("No match - case is different!")"""
    
    print_code_box(example, "Example")
    
    speak("Important:")
    speak("  • Use == to compare strings (double equals!)")
    speak("  • Case matters: 'Hello' != 'hello'")
    speak("  • Spaces matter: 'hi' != 'hi '")
    speak("  • Always use quotes around text\n")
    wait_for_enter()
    
    # LESSON: LOWER
    clear_screen()
    print_header("📚 LESSON: THE .lower() METHOD 📚")
    
    speak("\nThe .lower() method converts text to all lowercase.")
    speak("This makes comparisons easier when case doesn't matter!\n")
    
    example = """# Making case-insensitive comparisons
answer = input("Do you agree? (yes/no) ")

# Convert to lowercase before comparing
if answer.lower() == "yes":
    print("Great!")
else:
    print("Maybe next time")

# Now "YES", "Yes", "yes", "YeS" all work!"""
    
    print_code_box(example, "Example")
    
    speak("String methods:")
    speak("  • .lower() → makes everything lowercase")
    speak("  • .upper() → makes everything UPPERCASE")
    speak("  • .strip() → removes spaces from start/end")
    speak("  • Call them with: text.lower()\n")
    wait_for_enter()
    
    # CHALLENGE 1
    clear_screen()
    print_header("⚔️ CHALLENGE 1: ASK FOR INPUT ⚔️")
    
    speak("\nToadbert grins: 'First, show me you can ASK a question!'\n")
    
    speak("Your task:")
    speak("  1. Use input() to ask: What is your name?")
    speak("  2. Store the answer in a variable called 'name'")
    speak("  3. Print: Hello, [name]!\n")
    
    print_hint("Use input() and store the result in a variable!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['input', 'name'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Use input() and a 'name' variable! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        test_input = "Teagan\n"
        success2, output, error = validator.run_code(code, test_input)
        
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'Hello' in output and 'Teagan' in output:
            print_success("Perfect! You've mastered asking for input!")
            speak(f"\nYour code output (with input 'Teagan'):\n{output}")
            break
        else:
            print_error("Your code should print a greeting with the name!")
            if attempts < max_attempts:
                print_hint(f"Try: print('Hello,', name, '!') Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 2
    clear_screen()
    print_header("⚔️ CHALLENGE 2: THE SECRET WORD ⚔️")
    
    speak("\nToadbert's eyes gleam: 'Now for the REAL test!'")
    speak("'The secret word is... ribbit.'")
    speak("'But I'll accept it in ANY case - RiBBit, RIBBIT, whatever.'\n")
    
    speak("Your task:")
    speak("  1. Ask the user: What's the secret word?")
    speak("  2. Store it in a variable called 'password'")
    speak("  3. Convert it to lowercase using .lower()")
    speak("  4. If it equals 'ribbit', print: Gate opens! You may pass.")
    speak("  5. Otherwise, print: Wrong word, slimy fingers!\n")
    
    print_hint("Use password.lower() == 'ribbit' for case-insensitive checking!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        required = ['input', 'password', 'lower', 'if']
        success1, msg1 = validator.check_contains(code, required)
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"You need: input(), .lower(), and if statement! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        test_cases = [
            ("ribbit\n", "Gate opens", True),
            ("RIBBIT\n", "Gate opens", True),
            ("croak\n", "Wrong", False)
        ]
        
        all_passed = True
        for test_input, expected_phrase, should_pass in test_cases:
            success, output, error = validator.run_code(code, test_input)
            
            if not success:
                print_error(f"Code error with input '{test_input.strip()}':\n{error}")
                all_passed = False
                break
            
            if should_pass and expected_phrase not in output:
                print_error(f"With input '{test_input.strip()}', expected '{expected_phrase}' in output")
                all_passed = False
                break
            elif not should_pass and "Wrong" not in output and "wrong" not in output:
                print_error(f"With wrong password, should print rejection message")
                all_passed = False
                break
        
        if all_passed:
            print_success("Excellent! Your password check works perfectly!")
            speak("\nTesting with 'ribbit':")
            success, output, _ = validator.run_code(code, "ribbit\n")
            speak(output)
            break
        else:
            if attempts < max_attempts:
                print_hint(f"Test your code logic carefully. Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    # OUTRO
    clear_screen()
    speak("\n✨ The gate shimmers and swings open! ✨\n")
    speak("Toadbert tips his wizard hat:")
    speak("'Not bad for a mushroom-muncher. You've got the basics of input and logic.'")
    speak("'But Mallport is full of REAL challenges. Loops, lists, functions...'")
    speak("'Hope you're ready, druid.'\n")
    speak("The path to Mallport lies open before you.\n")
    wait_for_enter()
    
    return True


# ============================================================================
# QUEST 7: THE ARCANE ARCHIVE
# ============================================================================

def quest7_arcane_archive(player, validator):
    """Quest 7: Teaching Lists, indexing, and list methods."""
    
    # INTRO
    clear_screen()
    print_header("📚 THE ARCANE ARCHIVE 📚")
    
    speak("\nYou enter the great Arcane Archive of Mallport.")
    speak("Floating books drift through the air, their pages glowing with code.")
    speak("\nAn ethereal archivist materializes before you:")
    speak("'Welcome, druid. The Lexicon of Fraylon has been... fragmented.'")
    speak("'Each spell is a line of code. Misplace a comma, summon a cactus instead of a shield.'")
    speak("\n'You must learn to work with LISTS - ordered collections of power.'\n")
    wait_for_enter()
    
    # LESSON: LISTS
    clear_screen()
    print_header("📚 LESSON: LISTS 📚")
    
    speak("\nLists are ordered collections that can hold multiple values.")
    speak("Think of them as a scroll with numbered items.\n")
    
    example = """# Creating lists
spells = ["rootcall", "stoneward", "leafburst"]
numbers = [1, 2, 3, 4, 5]
mixed = ["fire", 42, "water", 7]

# Printing lists
print(spells)  # Shows the whole list

# Empty list
ingredients = []"""
    
    print_code_box(example, "Example")
    
    speak("List basics:")
    speak("  • Created with square brackets []")
    speak("  • Items separated by commas")
    speak("  • Can hold any type of data")
    speak("  • Can mix different types")
    speak("  • Order matters!\n")
    wait_for_enter()
    
    # LESSON: INDEXING
    clear_screen()
    print_header("📚 LESSON: INDEXING 📚")
    
    speak("\nYou can access individual items in a list using their INDEX.")
    speak("Think of it as the item's position number.\n")
    
    example = """# Indexing starts at 0!
spells = ["rootcall", "stoneward", "leafburst"]

# Access by index
print(spells[0])  # "rootcall" - first item
print(spells[1])  # "stoneward" - second item
print(spells[2])  # "leafburst" - third item

# Negative indexing (from the end)
print(spells[-1])  # "leafburst" - last item
print(spells[-2])  # "stoneward" - second to last"""
    
    print_code_box(example, "Example")
    
    speak("Indexing rules:")
    speak("  • Index starts at 0, not 1!")
    speak("  • First item: list[0]")
    speak("  • Second item: list[1]")
    speak("  • Last item: list[-1]")
    speak("  • Out of range index = error!\n")
    
    print_hint("Python uses ZERO-BASED indexing. The first item is at position 0!")
    wait_for_enter()
    
    # LESSON: LIST METHODS
    clear_screen()
    print_header("📚 LESSON: LIST METHODS 📚")
    
    speak("\nLists have special methods to modify them.\n")
    
    example = """# Starting list
spells = ["rootcall", "stoneward"]

# .append() - add to end
spells.append("leafburst")
print(spells)  # ["rootcall", "stoneward", "leafburst"]

# .insert() - add at position
spells.insert(0, "firebolt")
print(spells)  # ["firebolt", "rootcall", "stoneward", "leafburst"]

# len() - get list length
print(len(spells))  # 4"""
    
    print_code_box(example, "Example")
    
    speak("Common list methods:")
    speak("  • .append(item) - adds to end")
    speak("  • .insert(index, item) - adds at position")
    speak("  • .remove(item) - removes first matching item")
    speak("  • .pop() - removes and returns last item")
    speak("  • len(list) - returns number of items\n")
    wait_for_enter()
    
    # CHALLENGE 1
    clear_screen()
    print_header("⚔️ CHALLENGE 1: CREATE THE LEXICON ⚔️")
    
    speak("\nThe archivist hands you three glowing spell fragments.")
    speak("'Store these in a list called spells!'\n")
    
    speak("Your task:")
    speak("  1. Create a list called 'spells' with these three strings:")
    speak("     'rootcall', 'stoneward', 'leafburst'")
    speak("  2. Print the entire list")
    speak("  3. Print the SECOND spell (index 1)\n")
    
    print_hint("Remember: lists use square brackets and indexing starts at 0!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['spells', '[', ']'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Create a list with square brackets! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Check your syntax! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'stoneward' in output:
            namespace = {}
            try:
                exec(code, namespace)
                if 'spells' in namespace:
                    spell_list = namespace['spells']
                    if (isinstance(spell_list, list) and 
                        len(spell_list) == 3 and 
                        spell_list[0] == 'rootcall' and
                        spell_list[1] == 'stoneward' and
                        spell_list[2] == 'leafburst'):
                        print_success("Perfect! The Lexicon is forming!")
                        speak(f"\nYour code output:\n{output}")
                        break
                    else:
                        print_error("The spells list doesn't have the correct items in order.")
                        if attempts < max_attempts:
                            print_hint(f"Check the order and spelling! Attempts remaining: {max_attempts - attempts}")
                        else:
                            return False
                else:
                    print_error("Variable 'spells' not found!")
                    if attempts < max_attempts:
                        print_hint(f"Attempts remaining: {max_attempts - attempts}")
                    else:
                        return False
            except:
                print_error("Couldn't verify your list structure.")
                if attempts < max_attempts:
                    print_hint(f"Attempts remaining: {max_attempts - attempts}")
                else:
                    return False
        else:
            print_error("You need to print the second spell!")
            if attempts < max_attempts:
                print_hint(f"Use spells[1] to get the second item! Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 2
    clear_screen()
    print_header("⚔️ CHALLENGE 2: MODIFY THE LEXICON ⚔️")
    
    speak("\nThe archivist continues: 'Now demonstrate mastery over the list!'")
    speak("'Add, remove, and access spells with precision.'\n")
    
    speak("Your task:")
    speak("  1. Start with this list: spells = ['fire', 'water', 'earth']")
    speak("  2. Append 'air' to the end")
    speak("  3. Insert 'lightning' at the beginning (index 0)")
    speak("  4. Print the list length using len()")
    speak("  5. Print the last item using negative indexing\n")
    
    print_hint("Use .append(), .insert(), len(), and negative indexing [-1]!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        required = ['append', 'insert', 'len']
        success1, msg1 = validator.check_contains(code, required)
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"You need .append(), .insert(), and len()! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Check your method calls! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        namespace = {}
        try:
            exec(code, namespace)
            if 'spells' in namespace:
                spell_list = namespace['spells']
                expected = ['lightning', 'fire', 'water', 'earth', 'air']
                
                if spell_list == expected:
                    if '5' in output and 'air' in output:
                        print_success("Masterful! You've controlled the list perfectly!")
                        speak(f"\nYour code output:\n{output}")
                        break
                    else:
                        print_error("Don't forget to print the length and last item!")
                        if attempts < max_attempts:
                            print_hint(f"Attempts remaining: {max_attempts - attempts}")
                        else:
                            return False
                else:
                    print_error(f"List order is wrong.\nExpected: {expected}\nGot: {spell_list}")
                    if attempts < max_attempts:
                        print_hint(f"Check your append and insert calls! Attempts remaining: {max_attempts - attempts}")
                    else:
                        return False
            else:
                print_error("Variable 'spells' not found!")
                if attempts < max_attempts:
                    print_hint(f"Attempts remaining: {max_attempts - attempts}")
                else:
                    return False
        except Exception as e:
            print_error(f"Error verifying code: {str(e)}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    # OUTRO
    clear_screen()
    speak("\n✨ The fragments coalesce into a complete grimoire! ✨\n")
    speak("The archivist bows deeply:")
    speak("'You understand the power of ordered collections, druid.'")
    speak("'Lists are fundamental to all complex magic.'")
    speak("'But beware - the Cult uses corrupted data structures...'")
    speak("'Dictionaries twisted into tangles, loops that never end.'\n")
    speak("The Archive's light dims as you prepare for deeper challenges.\n")
    wait_for_enter()
    
    return True


# ============================================================================
# QUEST 9: THE RITUAL OF BALANCE
# ============================================================================

def quest9_ritual_balance(player, validator):
    """Quest 9: Teaching Functions, parameters, and return values."""
    
    # INTRO
    clear_screen()
    print_header("🌒 THE RITUAL OF BALANCE 🌒")
    
    speak("\nThe city's energy grid pulses erratically, threatening to collapse.")
    speak("An old druid mentor appears in a shimmer of light:")
    speak("\n'Child of the green, you've learned variables, loops, and lists.'")
    speak("'But true power comes from REUSABLE magic - functions!'")
    speak("\n'Magic that repeats should be wrapped neatly, called upon at will.'")
    speak("'Create a ritual that can be invoked whenever balance is needed.'\n")
    wait_for_enter()
    
    # LESSON: FUNCTIONS
    clear_screen()
    print_header("📚 LESSON: FUNCTIONS 📚")
    
    speak("\nFunctions are reusable blocks of code with a name.")
    speak("Like spells in a grimoire - cast them whenever needed!\n")
    
    example = """# Defining a function
def greet():
    print("Hello, druid!")
    print("Welcome to the forest.")

# Calling (using) the function
greet()  # Runs the code inside
greet()  # Can call it multiple times!"""
    
    print_code_box(example, "Example")
    
    speak("Function basics:")
    speak("  • def keyword starts definition")
    speak("  • Name followed by parentheses ()")
    speak("  • Colon : at the end")
    speak("  • Code inside must be indented")
    speak("  • Call with: function_name()\n")
    wait_for_enter()
    
    # LESSON: PARAMETERS
    clear_screen()
    print_header("📚 LESSON: PARAMETERS 📚")
    
    speak("\nParameters let you pass information INTO a function.")
    speak("They make functions flexible and powerful!\n")
    
    example = """# Function with one parameter
def greet(name):
    print("Hello,", name)

greet("Teagan")   # Output: Hello, Teagan
greet("Toadbert") # Output: Hello, Toadbert

# Multiple parameters
def balance(sunlight, water, soil):
    print("Balancing with:")
    print("Sunlight:", sunlight)
    print("Water:", water)
    print("Soil:", soil)

balance("gentle rays", "pure dew", "rich earth")"""
    
    print_code_box(example, "Example")
    
    speak("Parameter rules:")
    speak("  • Define in parentheses: def func(param1, param2):")
    speak("  • Separate multiple params with commas")
    speak("  • Use them like variables inside the function")
    speak("  • Pass values when calling: func(value1, value2)\n")
    wait_for_enter()
    
    # LESSON: RETURN
    clear_screen()
    print_header("📚 LESSON: RETURN VALUES 📚")
    
    speak("\nFunctions can RETURN values back to the caller.")
    speak("This lets them calculate and give you results!\n")
    
    example = """# Function that returns a value
def add(a, b):
    result = a + b
    return result  # Sends the value back

# Capture the returned value
total = add(5, 3)
print(total)  # 8

# Use return value directly
print(add(10, 20))  # 30"""
    
    print_code_box(example, "Example")
    
    speak("Return statement:")
    speak("  • return keyword sends a value back")
    speak("  • Exits the function immediately")
    speak("  • Store result in a variable")
    speak("  • Or use return value directly\n")
    
    print_hint("return is how functions give you answers!")
    wait_for_enter()
    
    # CHALLENGE 1
    clear_screen()
    print_header("⚔️ CHALLENGE 1: CREATE A RITUAL ⚔️")
    
    speak("\nThe mentor nods: 'Create your first reusable ritual!'")
    speak("'A simple spell to restore a single element.'\n")
    
    speak("Your task:")
    speak("  1. Define a function called 'restore' (no parameters)")
    speak("  2. Inside it, print: Balance restored")
    speak("  3. Call the function twice to cast it twice\n")
    
    print_hint("def restore(): followed by indented code, then call restore()")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['def', 'restore'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Define a function called 'restore'! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, msg2 = validator.check_function_exists(code, 'restore')
        if not success2:
            print_error(msg2)
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success3, output, error = validator.run_code(code)
        if not success3:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        count = output.lower().count("balance restored")
        if count >= 2:
            print_success("Excellent! Your ritual can be cast repeatedly!")
            speak(f"\nYour code output:\n{output}")
            break
        elif count == 1:
            print_error("The ritual was only cast once! Call it twice.")
            if attempts < max_attempts:
                print_hint(f"Call restore() two times! Attempts remaining: {max_attempts - attempts}")
            else:
                return False
        else:
            print_error("The ritual didn't print the restoration message!")
            if attempts < max_attempts:
                print_hint(f"Make sure to print 'Balance restored' inside the function! Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 2
    clear_screen()
    print_header("⚔️ CHALLENGE 2: PARAMETERIZED RITUAL ⚔️")
    
    speak("\nThe mentor smiles: 'Good. Now make it adaptable!'")
    speak("'A ritual that can work with ANY element passed to it.'\n")
    
    speak("Your task:")
    speak("  1. Define a function called 'balance' with ONE parameter: 'element'")
    speak("  2. Inside it, print: Restoring [element]")
    speak("  3. Call it three times with: 'Earth', 'Water', 'Fire'\n")
    
    print_hint("def balance(element): and use the element parameter in your print!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        success1, msg1 = validator.check_contains(code, ['def', 'balance'])
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Define a function called 'balance'! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Check your function definition and calls! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if 'Earth' in output and 'Water' in output and 'Fire' in output:
            namespace = {}
            try:
                exec(code, namespace)
                if 'balance' in namespace:
                    test_output = []
                    import io
                    from contextlib import redirect_stdout
                    
                    f = io.StringIO()
                    with redirect_stdout(f):
                        namespace['balance']('Test')
                    test_result = f.getvalue()
                    
                    if 'Test' in test_result:
                        print_success("Perfect! Your parameterized ritual works!")
                        speak(f"\nYour code output:\n{output}")
                        break
                    else:
                        print_error("Your function doesn't use the parameter!")
                        if attempts < max_attempts:
                            print_hint(f"Print the 'element' parameter inside the function! Attempts remaining: {max_attempts - attempts}")
                        else:
                            return False
            except Exception as e:
                print_error(f"Error testing function: {str(e)}")
                if attempts < max_attempts:
                    print_hint(f"Attempts remaining: {max_attempts - attempts}")
                else:
                    return False
        else:
            print_error("You need to call balance() with 'Earth', 'Water', and 'Fire'!")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    
    wait_for_enter()
    
    # CHALLENGE 3
    clear_screen()
    print_header("⚔️ CHALLENGE 3: RETURN THE POWER ⚔️")
    
    speak("\nThe mentor's eyes glow: 'Now harness the true power - RETURN values!'")
    speak("'Create a ritual that calculates and returns energy levels.'\n")
    
    speak("Your task:")
    speak("  1. Define a function called 'calculate_energy' with two parameters:")
    speak("     'sunlight' and 'water'")
    speak("  2. Inside, add sunlight + water and RETURN the result")
    speak("  3. Call it with values 50 and 30, store result in 'total_energy'")
    speak("  4. Print: Total energy: [total_energy]\n")
    
    print_hint("Use return to send the value back!")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print("\nEnter your code (type 'DONE' on a new line when finished):")
        print("─" * 50)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        code = '\n'.join(lines)
        attempts += 1
        
        required = ['def', 'calculate_energy', 'return']
        success1, msg1 = validator.check_contains(code, required)
        if not success1:
            print_error(msg1)
            if attempts < max_attempts:
                print_hint(f"Define calculate_energy with a return statement! Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        # --- Start of the corrupted logic that was at the end of the file ---
        # This checks the function's return value and prints the output.
        
        success2, output, error = validator.run_code(code)
        if not success2:
            print_error(f"Your code has an error:\n{error}")
            if attempts < max_attempts:
                print_hint(f"Attempts remaining: {max_attempts - attempts}")
                continue
            else:
                return False
        
        if '80' in output:
            namespace = {}
            try:
                exec(code, namespace)
                if 'calculate_energy' in namespace:
                    result = namespace['calculate_energy'](50, 30)
                    if result == 80:
                        print_success("Magnificent! You've mastered return values!")
                        speak(f"\nYour code output:\n{output}")
                        break
                    else:
                        print_error(f"Function returned {result} instead of 80!")
                        if attempts < max_attempts:
                            print_hint(f"Return sunlight + water! Attempts remaining: {max_attempts - attempts}")
                        else:
                            return False
                else:
                    print_error("Function 'calculate_energy' not found!")
                    if attempts < max_attempts:
                        print_hint(f"Attempts remaining: {max_attempts - attempts}")
                    else:
                        return False
            except Exception as e:
                print_error(f"Error testing function: {str(e)}")
                if attempts < max_attempts:
                    print_hint(f"Attempts remaining: {max_attempts - attempts}")
                else:
                    return False
        else:
            print_error("Output should show the total energy (80)!")
            if attempts < max_attempts:
                print_hint(f"Store the returned value and print it! Attempts remaining: {max_attempts - attempts}")
            else:
                return False
    else:
        return False
    # --- End of corrected logic that was misplaced ---
    
    # OUTRO
    clear_screen()
    speak("\n✨ The energy grid stabilizes, humming with perfect harmony! ✨\n")
    speak("The old druid mentor places a hand on your shoulder:")
    speak("'You have learned the art of reusable magic - functions.'")
    speak("'Define once, invoke many times. This is the way of efficient code.'")
    speak("\n'But remember: with parameters, you gain flexibility.'")
    speak("'With return values, you gain power.'")
    speak("'Use both wisely in the battles ahead.'\n")
    speak("The mentor fades into mist, leaving you stronger and wiser.\n")
    wait_for_enter()
    
    return True


# ============================================================================
# GAME ENGINE
# ============================================================================

class GameEngine:
    """Main game engine managing quest flow and player state."""
    
    def __init__(self):
        self.player = load_progress()
        self.validator = CodeValidator()
        self.current_quest = None
        self.quest_functions = {
            "quest1_mossy_burrow": quest1_mossy_burrow,
            "quest2_corrupted_creek": quest2_corrupted_creek,
            "quest3_talking_toad": quest3_talking_toad,
            "quest7_arcane_archive": quest7_arcane_archive,
            "quest9_ritual_balance": quest9_ritual_balance,
        }
        
    def display_main_menu(self):
        """Displays the main game menu."""
        clear_screen()
        print_header("🐍 THE SERPENT'S CODE 🐍")
        
        print(f"\n🧙 Druid: {self.player['player_name']} the {self.player['character']}")
        print(f"⭐ Level: {self.player['level']} | XP: {self.player['xp']}")
        print(f"🌿 Nature Tokens: {self.player['nature_tokens']}")
        print(f"📖 Quests Completed: {len(self.player['completed'])}")
        
        print("\n" + "="*60)
        print("\n1. Continue Adventure")
        print("2. Review Completed Quests")
        print("3. Check Achievements")
        print("4. View Story So Far")
        print("5. Save & Exit")
        
        return input("\nChoose your path: ").strip()
    
    def display_act_progress(self):
        """Shows progress through each act."""
        clear_screen()
        print_header("📜 YOUR JOURNEY THROUGH FRAYLON 📜")
        
        for act_name, quests in QUEST_REGISTRY.items():
            print(f"\n{act_name}")
            print("-" * 50)
            
            for quest_id, quest_name, topic, xp_reward in quests:
                status = "✓" if quest_id in self.player['completed'] else "○"
                available = "✓" if quest_id in self.quest_functions else "⏳"
                print(f"  {status} {quest_name} - {topic} ({xp_reward} XP) {available}")
        
        print("\n✓ = Completed | ○ = Available | ⏳ = Coming Soon")
        wait_for_enter()
    
    def get_next_quest(self):
        """Determines the next available quest for the player."""
        for act_name, quests in QUEST_REGISTRY.items():
            for quest_id, quest_name, topic, xp_reward in quests:
                if quest_id not in self.player['completed'] and quest_id in self.quest_functions:
                    return {
                        'id': quest_id,
                        'name': quest_name,
                        'topic': topic,
                        'xp': xp_reward,
                        'act': act_name
                    }
        return None
    
    def run_quest(self, quest_info):
        """Dynamically loads and runs a quest."""
        quest_id = quest_info['id']
        
        if quest_id not in self.quest_functions:
            speak(f"\n❌ Quest '{quest_id}' is coming soon!")
            wait_for_enter()
            return False
        
        try:
            clear_screen()
            print_header(f"🌿 {quest_info['name']} 🌿")
            speak(f"\nTopic: {quest_info['topic']}")
            speak(f"Reward: {quest_info['xp']} XP\n")
            
            # Run the quest
            quest_func = self.quest_functions[quest_id]
            success = quest_func(self.player, self.validator)
            
            if success:
                self.complete_quest(quest_info)
                return True
            else:
                speak("\n⚠️ Quest not yet complete. Review the lessons and try again.")
                return False
                
        except Exception as e:
            speak(f"\n❌ An error occurred: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def complete_quest(self, quest_info):
        """Handles quest completion rewards and progression."""
        quest_id = quest_info['id']
        
        if quest_id not in self.player['completed']:
            self.player['completed'].append(quest_id)
            
            # Award XP and tokens
            xp_gained = award_xp(self.player, quest_info['xp'])
            self.player['nature_tokens'] += 1
            
            speak(f"\n✨ Quest Complete! ✨")
            speak(f"🌟 +{xp_gained} XP")
            speak(f"🌿 +1 Nature Token")
            
            # Check for level up
            leveled_up = check_level_up(self.player)
            if leveled_up:
                speak(f"\n🎉 LEVEL UP! You are now Level {self.player['level']}!")
                speak("New powers of code unlock within you...")
            
            # Save progress
            save_progress(self.player)
            
            wait_for_enter()
    
    def play(self):
        """Main game loop."""
        speak("🌿 Welcome to The Serpent's Code 🌿")
        speak(f"\nWelcome back, {self.player['player_name']}.")
        speak("The forest whispers of dark code corrupting the land...")
        
        wait_for_enter()
        
        while True:
            choice = self.display_main_menu()
            
            if choice == '1':
                # Continue adventure
                next_quest = self.get_next_quest()
                
                if next_quest is None:
                    speak("\n🎊 You've completed all available quests!")
                    speak("More adventures are being written...")
                    speak("Check back soon for new content!")
                    wait_for_enter()
                    continue
                
                clear_screen()
                speak(f"\n📖 Next Quest: {next_quest['name']}")
                speak(f"🎯 Focus: {next_quest['topic']}")
                speak(f"🏆 Reward: {next_quest['xp']} XP\n")
                
                choice = input("Begin this quest? (y/n): ").lower()
                
                if choice == 'y':
                    self.run_quest(next_quest)
                    
            elif choice == '2':
                self.display_act_progress()
                
            elif choice == '3':
                self.display_achievements()
                
            elif choice == '4':
                self.display_story()
                
            elif choice == '5':
                save_progress(self.player)
                speak("\n🌙 Progress saved. Rest well, druid.")
                break
            
            else:
                speak("\n⚠️ Invalid choice. Try again.")
                wait_for_enter()
    
    def display_achievements(self):
        """Shows player achievements."""
        clear_screen()
        print_header("🏆 ACHIEVEMENTS 🏆")
        
        # Auto-award achievements based on progress
        if len(self.player['completed']) >= 1 and "First Steps" not in self.player['achievements']:
            self.player['achievements'].append("First Steps - Completed your first quest")
        if len(self.player['completed']) >= 5 and "Apprentice Coder" not in self.player['achievements']:
            self.player['achievements'].append("Apprentice Coder - Completed 5 quests")
        if self.player['level'] >= 3 and "Rising Power" not in self.player['achievements']:
            self.player['achievements'].append("Rising Power - Reached Level 3")
        
        if not self.player['achievements']:
            speak("\nNo achievements yet. Complete quests to earn them!")
        else:
            for achievement in self.player['achievements']:
                print(f"  ✓ {achievement}")
        
        wait_for_enter()
    
    def display_story(self):
        """Shows the story recap."""
        clear_screen()
        print_header("📚 THE STORY SO FAR 📚")
        
        story = """
In the mystical world of Fraylon, the Goblin Druid Teagan lives peacefully
in a mossy burrow near the great city of Mallport. But darkness stirs...

The Cult of the Dragon has corrupted nature's code itself, causing reality
to glitch and break. Rivers flow backward in endless loops. Trees grow
upside-down. The very fabric of the world is unraveling.

To save Fraylon, Teagan must master the ancient art of Pythonic magic—
the language that writes reality itself. Each spell learned brings balance
closer, but the Iron Serpent awakens...

Only by mastering the complete syntax of creation can Teagan hope to
restore harmony to the land.
        """
        
        print(story)
        
        # Show current progress
        completed = len(self.player['completed'])
        total_available = len([q for q in self.quest_functions.keys()])
        
        print(f"\n📊 Your Progress: {completed}/{total_available} quests completed")
        print(f"⭐ Level {self.player['level']} Druid")
        print(f"🌿 {self.player['nature_tokens']} Nature Tokens collected")
        
        wait_for_enter()


# ============================================================================
# TITLE SCREEN & MAIN ENTRY POINT
# ============================================================================

def show_title_screen():
    """Displays the game title screen."""
    clear_screen()
    
    title = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              🐍  THE SERPENT'S CODE  🐍                      ║
    ║                                                              ║
    ║           A Python Learning Adventure                        ║
    ║                                                              ║
    ║        Master the ancient art of Pythonic magic             ║
    ║        Save the world of Fraylon from corruption            ║
    ║        Become the druid who debugs reality itself           ║
    ║                                                              ║
    ║                    Created by Danny & Claude                 ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    
    print(title)
    speak("\n              Press Enter to begin your journey...", delay=0.05, add_pause=False)
    input()


def main():
    """Main entry point for the game."""
    try:
        show_title_screen()
        
        game = GameEngine()
        game.play()
        
    except KeyboardInterrupt:
        clear_screen()
        speak("\n\n🌙 The forest calls you to rest. Farewell, druid. 🌙\n")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()


