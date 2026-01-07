# the_verdant_code.py
"""
🌿 THE VERDANT CODE 🌿
A Pythonic D&D Learning Adventure
Created by Danny (Cesium) P.

A complete Python learning game in one file!
Learn Python through an epic fantasy adventure.

To play: python the_verdant_code.py

Created as an open-source educational game.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Callable
import traceback


# ============================================================================
# CORE GAME ENGINE
# ============================================================================

class GameProgress:
    """Tracks player progress through the game"""

    def __init__(self, save_file="game_progress.json"):
        self.save_file = save_file
        self.player_name = "Grixle"
        self.current_act = 1
        self.current_scene = 1
        self.completed_lessons = []
        self.total_score = 0
        self.unlocked_acts = [1]
        self.load_progress()

    def load_progress(self):
        """Load saved game progress"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    self.player_name = data.get('player_name', 'Grixle')
                    self.current_act = data.get('current_act', 1)
                    self.current_scene = data.get('current_scene', 1)
                    self.completed_lessons = data.get('completed_lessons', [])
                    self.total_score = data.get('total_score', 0)
                    self.unlocked_acts = data.get('unlocked_acts', [1])
                    return True
            except:
                return False
        return False

    def save_progress(self):
        """Save current game progress"""
        data = {
            'player_name': self.player_name,
            'current_act': self.current_act,
            'current_scene': self.current_scene,
            'completed_lessons': self.completed_lessons,
            'total_score': self.total_score,
            'unlocked_acts': self.unlocked_acts,
            'last_played': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            with open(self.save_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except:
            return False

    def complete_lesson(self, lesson_id: str, score: int = 10):
        """Mark a lesson as completed"""
        if lesson_id not in self.completed_lessons:
            self.completed_lessons.append(lesson_id)
            self.total_score += score
            self.save_progress()

    def unlock_act(self, act_number: int):
        """Unlock a new act"""
        if act_number not in self.unlocked_acts:
            self.unlocked_acts.append(act_number)
            self.save_progress()


class Lesson:
    """Base class for all lessons"""

    def __init__(self, lesson_id: str, title: str, description: str):
        self.lesson_id = lesson_id
        self.title = title
        self.description = description
        self.completed = False

    def introduce(self):
        """Display lesson introduction"""
        print(f"\n{'=' * 70}")
        print(f"📚 LESSON: {self.title}")
        print(f"{'=' * 70}")
        print(f"\n{self.description}\n")

    def teach(self):
        """Override this method to provide lesson content"""
        raise NotImplementedError("Each lesson must implement teach()")

    def challenge(self) -> bool:
        """Override this method to provide interactive challenge"""
        raise NotImplementedError("Each lesson must implement challenge()")

    def run(self) -> bool:
        """Execute the complete lesson"""
        self.introduce()
        self.teach()
        input("\n[Press Enter to continue to the challenge...]")
        return self.challenge()


class CodeChallenge:
    """Represents a coding challenge with validation"""

    def __init__(self, prompt: str, test_cases: List[Dict], hints: List[str] = None):
        self.prompt = prompt
        self.test_cases = test_cases
        self.hints = hints or []
        self.attempts = 0
        self.max_attempts = 3

    def run(self) -> bool:
        """Execute the challenge"""
        print(f"\n🎯 CHALLENGE:")
        print(f"{self.prompt}\n")

        while self.attempts < self.max_attempts:
            print(f"Attempt {self.attempts + 1}/{self.max_attempts}")
            print("\nEnter your code (type 'DONE' on a new line when finished):")
            print("(Type 'HINT' for a hint, 'SKIP' to skip this challenge)")

            code_lines = []
            while True:
                try:
                    line = input(">>> " if not code_lines else "... ")

                    if line.strip().upper() == 'DONE':
                        break
                    elif line.strip().upper() == 'HINT':
                        self.show_hint()
                        continue
                    elif line.strip().upper() == 'SKIP':
                        print("\n⏭️  Challenge skipped. Moving on...\n")
                        return True

                    code_lines.append(line)
                except KeyboardInterrupt:
                    print("\n\n⏭️  Challenge skipped.\n")
                    return True

            user_code = '\n'.join(code_lines)

            if self.validate_code(user_code):
                print("\n✅ SUCCESS! Your code works perfectly!")
                return True
            else:
                self.attempts += 1
                if self.attempts < self.max_attempts:
                    print(f"\n❌ Not quite right. Try again!")
                    if self.attempts == 2 and self.hints:
                        print("\n💡 Getting a hint might help...")

        print("\n⚠️  Maximum attempts reached. Don't worry, let's move forward!")
        print("You can practice this again later.\n")
        return True

    def validate_code(self, user_code: str) -> bool:
        """Validate user code against test cases"""
        try:
            exec_globals = {}
            exec_locals = {}

            exec(user_code, exec_globals, exec_locals)

            all_passed = True
            for i, test_case in enumerate(self.test_cases):
                test_type = test_case.get('type', 'output')

                if test_type == 'variable':
                    var_name = test_case['variable']
                    expected = test_case['expected']

                    actual = exec_locals.get(var_name, exec_globals.get(var_name, None))

                    if actual != expected:
                        print(f"\n❌ Test {i + 1} failed:")
                        print(f"   Expected {var_name} = {repr(expected)}")
                        print(f"   Got {var_name} = {repr(actual)}")
                        all_passed = False

                elif test_type == 'function':
                    func_name = test_case['function']
                    inputs = test_case['input']
                    expected = test_case['expected']

                    func = exec_locals.get(func_name, exec_globals.get(func_name, None))

                    if func is None:
                        print(f"\n❌ Test {i + 1} failed: Function '{func_name}' not found")
                        all_passed = False
                        continue

                    try:
                        if isinstance(inputs, list):
                            result = func(*inputs)
                        else:
                            result = func(inputs)

                        if result != expected:
                            print(f"\n❌ Test {i + 1} failed:")
                            print(f"   {func_name}{inputs} should return {repr(expected)}")
                            print(f"   Your function returned {repr(result)}")
                            all_passed = False
                    except Exception as e:
                        print(f"\n❌ Test {i + 1} failed with error: {e}")
                        all_passed = False

            return all_passed

        except Exception as e:
            print(f"\n❌ Error in your code: {e}")
            print("\nTraceback:")
            traceback.print_exc()
            return False

    def show_hint(self):
        """Show a hint to the player"""
        if self.hints and self.attempts < len(self.hints):
            print(f"\n💡 HINT: {self.hints[self.attempts]}")
        else:
            print("\n💡 No more hints available. Review the lesson material!")


class Scene:
    """Represents a scene in the game with narrative and lessons"""

    def __init__(self, scene_id: str, title: str, narrative: str):
        self.scene_id = scene_id
        self.title = title
        self.narrative = narrative
        self.lessons = []
        self.dialogue = []

    def add_dialogue(self, speaker: str, text: str):
        """Add dialogue to the scene"""
        self.dialogue.append((speaker, text))

    def add_lesson(self, lesson: Lesson):
        """Add a lesson to the scene"""
        self.lessons.append(lesson)

    def play(self, progress: GameProgress) -> bool:
        """Play through the scene"""
        print(f"\n{'#' * 70}")
        print(f"  {self.title}")
        print(f"{'#' * 70}\n")

        print(self.narrative)
        input("\n[Press Enter to continue...]")

        for speaker, text in self.dialogue:
            print(f"\n{speaker}: \"{text}\"")
            input("[Press Enter to continue...]")

        for lesson in self.lessons:
            success = lesson.run()
            if success:
                progress.complete_lesson(lesson.lesson_id, score=10)
                print("\n✨ Lesson completed! +10 XP")
            input("\n[Press Enter to continue...]")

        return True


class Act:
    """Represents an act in the game"""

    def __init__(self, act_number: int, title: str, description: str):
        self.act_number = act_number
        self.title = title
        self.description = description
        self.scenes = []

    def add_scene(self, scene: Scene):
        """Add a scene to the act"""
        self.scenes.append(scene)

    def play(self, progress: GameProgress) -> bool:
        """Play through the act"""
        print(f"\n{'*' * 70}")
        print(f"  🌿 ACT {self.act_number}: {self.title}")
        print(f"{'*' * 70}")
        print(f"\n{self.description}\n")
        input("[Press Enter to begin...]")

        for scene in self.scenes:
            scene.play(progress)
            progress.current_scene += 1
            progress.save_progress()

        progress.unlock_act(self.act_number + 1)
        progress.current_act = self.act_number + 1
        progress.current_scene = 1
        progress.save_progress()

        print(f"\n🎊 ACT {self.act_number} COMPLETED! 🎊")
        print(f"Total XP: {progress.total_score}")

        return True


class Game:
    """Main game controller"""

    def __init__(self):
        self.progress = GameProgress()
        self.acts = {}

    def add_act(self, act: Act):
        """Add an act to the game"""
        self.acts[act.act_number] = act

    def start(self):
        """Start the game"""
        self.show_title()

        if self.progress.load_progress():
            print(f"\n📂 Save file found!")
            print(f"Character: {self.progress.player_name}")
            print(f"Progress: Act {self.progress.current_act}, Scene {self.progress.current_scene}")
            print(f"XP: {self.progress.total_score}")

            choice = input("\nContinue from save? (y/n): ").strip().lower()
            if choice != 'y':
                self.progress = GameProgress()
                if os.path.exists(self.progress.save_file):
                    os.remove(self.progress.save_file)
                self.progress.save_progress()

        self.show_prologue()
        self.main_menu()

    def show_title(self):
        """Display game title"""
        title = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              🌿 THE VERDANT CODE 🌿                          ║
    ║                                                              ║
    ║           A Pythonic D&D Learning Adventure                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
        """
        print(title)

    def show_prologue(self):
        """Display game prologue"""
        prologue = """
    PROLOGUE — The Whisper of Fraylon

    The world of Fraylon hums with ancient rhythm — a living code 
    written by the gods themselves. Magic, it turns out, is logic. 
    Every spell, every rune, every heartbeat of the world is made 
    of patterns — variables and loops carved into the soil of existence.

    But now, those patterns are breaking. The Cult of the Dragon, 
    technomancers devoted to the awakening of a draconic intelligence 
    called the Iron Wyrm, is corrupting the code of nature. Trees fall 
    silent. Rivers print strange symbols on their surfaces.

    And deep within Mossroot Grove, a goblin stirs.

    You are Grixle Mossroot, a scrappy, green-fingered druid who's 
    better with fungi than formulas. But when the grove starts 
    whispering corrupted syntax, your mentor — Elder Willowbyte, a 
    wise old treant who speaks in code — calls upon you to learn the 
    Language of Nature, and restore balance.
        """
        print(prologue)
        input("\n[Press Enter to begin your journey...]")

    def main_menu(self):
        """Display main menu"""
        while True:
            print(f"\n{'=' * 70}")
            print("MAIN MENU")
            print(f"{'=' * 70}")
            print(f"Character: {self.progress.player_name}")
            print(f"Current Progress: Act {self.progress.current_act}")
            print(f"Total XP: {self.progress.total_score}")
            print(f"Completed Lessons: {len(self.progress.completed_lessons)}")
            print(f"{'=' * 70}")
            print("\n1. Continue Adventure")
            print("2. Select Act")
            print("3. View Progress")
            print("4. Credits")
            print("5. Exit Game")

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                self.continue_adventure()
            elif choice == '2':
                self.select_act()
            elif choice == '3':
                self.view_progress()
            elif choice == '4':
                self.show_credits()
            elif choice == '5':
                print("\n👋 Thanks for playing! Your progress has been saved.")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice. Please try again.")

    def continue_adventure(self):
        """Continue from current progress"""
        current_act = self.progress.current_act

        if current_act in self.acts:
            self.acts[current_act].play(self.progress)
        else:
            print(f"\n🎉 Congratulations! You've completed all available acts!")
            print(f"🌟 Final Score: {self.progress.total_score} XP")
            print("\n✨ You have earned the title: GRIXLE THE SYNTAX SAGE ✨\n")

    def select_act(self):
        """Allow player to select an act"""
        print(f"\n{'=' * 70}")
        print("SELECT ACT")
        print(f"{'=' * 70}")

        for act_num, act in sorted(self.acts.items()):
            status = "🔓 UNLOCKED" if act_num in self.progress.unlocked_acts else "🔒 LOCKED"
            print(f"\n{act_num}. {act.title} - {status}")
            print(f"   {act.description[:60]}...")

        print("\n0. Back to Main Menu")

        choice = input("\nSelect an act: ").strip()

        try:
            act_num = int(choice)
            if act_num == 0:
                return

            if act_num in self.progress.unlocked_acts and act_num in self.acts:
                self.progress.current_act = act_num
                self.progress.current_scene = 1
                self.acts[act_num].play(self.progress)
            elif act_num not in self.progress.unlocked_acts:
                print("\n🔒 This act is locked. Complete previous acts to unlock it.")
            else:
                print("\n❌ Invalid act number.")
        except ValueError:
            print("\n❌ Invalid input.")

    def view_progress(self):
        """Display player progress"""
        print(f"\n{'=' * 70}")
        print("YOUR PROGRESS")
        print(f"{'=' * 70}")
        print(f"\n🧙 Character: {self.progress.player_name}")
        print(f"📖 Current Act: {self.progress.current_act}")
        print(f"⭐ Total XP: {self.progress.total_score}")
        print(f"✅ Lessons Completed: {len(self.progress.completed_lessons)}")
        print(f"\n🔓 Unlocked Acts: {', '.join(map(str, sorted(self.progress.unlocked_acts)))}")

        if self.progress.completed_lessons:
            print(f"\n📚 Completed Lessons:")
            for lesson_id in self.progress.completed_lessons[:10]:
                print(f"   • {lesson_id}")
            if len(self.progress.completed_lessons) > 10:
                print(f"   ... and {len(self.progress.completed_lessons) - 10} more")

        input("\n[Press Enter to return to menu...]")

    def show_credits(self):
        """Display game credits"""
        credits = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                         CREDITS                              ║
    ╔══════════════════════════════════════════════════════════════╗

    🌿 THE VERDANT CODE 🌿
    A Pythonic D&D Learning Adventure

    Game Design & Story: Original Concept
    Programming: Python Learning Game Engine

    Special Thanks:
    • Elder Willowbyte, for teaching us the Old Language
    • The Mossroot Grove, for inspiring this journey
    • All learners who dare to compile their dreams

    "All code is alive when it's read with intent."

    ╚══════════════════════════════════════════════════════════════╝
        """
        print(credits)
        input("\n[Press Enter to return to menu...]")


# ============================================================================
# ACT I: THE ROOTS OF SYNTAX
# ============================================================================

class StringsAndVariablesLesson(Lesson):
    """Lesson 1: Strings and Variables"""

    def __init__(self):
        super().__init__(
            lesson_id="act1_strings_variables",
            title="Strings & Variables — The Language of Names",
            description="Learn how to store and work with text and data using variables."
        )

    def teach(self):
        print("""
Elder Willowbyte taps his staff. Letters shimmer across a tree trunk:

    name = "Grixle"
    grove = "Mossroot"
    print("I am " + name + " of the " + grove + " Grove!")

📖 CONCEPT: VARIABLES

Variables are like magical containers that store information. 
In Python, you create a variable by giving it a name and a value:

    variable_name = value

For text (strings), use quotes:
    greeting = "Hello"
    message = 'Welcome'

You can combine strings with the + operator:
    full_message = greeting + " " + message
    print(full_message)  # Output: Hello Welcome

IMPORTANT: Variable names should be descriptive and follow these rules:
- Start with a letter or underscore
- Can contain letters, numbers, and underscores
- Cannot contain spaces or special characters
- Are case-sensitive (name and Name are different)
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create three variables:
- name = your character's name
- race = "Goblin Druid"
- grove = "Mossroot Grove"

Then print: "I am [name], a proud [race] from [grove]!"

Example output: I am Grixle, a proud Goblin Druid from Mossroot Grove!""",
            test_cases=[
                {'type': 'variable', 'variable': 'name', 'expected': 'Grixle'},
                {'type': 'variable', 'variable': 'race', 'expected': 'Goblin Druid'},
                {'type': 'variable', 'variable': 'grove', 'expected': 'Mossroot Grove'}
            ],
            hints=[
                "Remember to use quotes around text: name = \"Grixle\"",
                "Use + to combine strings: \"I am \" + name",
                "Don't forget to use print() to display your message!"
            ]
        )
        return challenge.run()


class NumbersLesson(Lesson):
    """Lesson 2: Numbers and Arithmetic"""

    def __init__(self):
        super().__init__(
            lesson_id="act1_numbers",
            title="Numbers — The Arithmetic of Life",
            description="Learn to work with numbers and mathematical operations."
        )

    def teach(self):
        print("""
A squirrel scampers up with a bundle of glowing seeds.

Willowbyte: "Magic has weight. Every root, every creature has a number."

    age = 24
    magic_seeds = 7
    total_power = age * magic_seeds
    print(total_power)  # Output: 168

📖 CONCEPT: NUMBERS AND ARITHMETIC

Python can work with numbers just like a calculator:

OPERATORS:
    +   Addition       (5 + 3 = 8)
    -   Subtraction    (5 - 3 = 2)
    *   Multiplication (5 * 3 = 15)
    /   Division       (5 / 2 = 2.5)
    //  Integer Div    (5 // 2 = 2)
    **  Power          (5 ** 2 = 25)
    %   Modulo         (5 % 2 = 1)

TYPES OF NUMBERS:
- Integers: whole numbers (1, 42, -5)
- Floats: decimal numbers (3.14, -0.5, 2.0)

You can store results in variables:
    mana = 10
    cost = 3
    remaining = mana - cost
    print(remaining)  # Output: 7

⚠️  IMPORTANT: You cannot directly combine strings and numbers:
    Wrong: "Power: " + 50
    Right: "Power: " + str(50)  # Convert number to string
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Calculate your druidic power:
- Create a variable 'mana' with value 12
- Create a variable 'runes' with value 3
- Multiply them and store in 'spell_strength'
- Print the result

The output should be: 36""",
            test_cases=[
                {'type': 'variable', 'variable': 'mana', 'expected': 12},
                {'type': 'variable', 'variable': 'runes', 'expected': 3},
                {'type': 'variable', 'variable': 'spell_strength', 'expected': 36}
            ],
            hints=[
                "Create variables: mana = 12 and runes = 3",
                "Multiply using *: spell_strength = mana * runes",
                "Print the result: print(spell_strength)"
            ]
        )
        return challenge.run()


class FunctionsLesson(Lesson):
    """Lesson 3: Functions and Return Values"""

    def __init__(self):
        super().__init__(
            lesson_id="act1_functions",
            title="Functions & Returning Values — The Spell of Repetition",
            description="Learn to create reusable code with functions."
        )

    def teach(self):
        print("""
Willowbyte: "Repetition is death. A wise coder conjures once, and reuses."

    def brew_potion(herb, quantity):
        potion_strength = herb * quantity
        return potion_strength

    result = brew_potion(5, 3)
    print(result)  # Output: 15

📖 CONCEPT: FUNCTIONS

Functions are reusable blocks of code that perform specific tasks.

DEFINING A FUNCTION:
    def function_name(parameters):
        # code to execute
        return result

PARTS OF A FUNCTION:
- def: keyword to define a function
- function_name: what you call the function
- parameters: inputs the function needs (optional)
- return: sends a value back to the caller

CALLING A FUNCTION:
    result = function_name(arguments)

EXAMPLE:
    def add_numbers(a, b):
        sum_result = a + b
        return sum_result

    answer = add_numbers(5, 7)
    print(answer)  # Output: 12

WHY USE FUNCTIONS?
- Avoid repeating code
- Make code easier to read
- Easier to fix bugs (fix once, works everywhere)
- Can reuse the same logic with different inputs
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create a function called 'make_potion' that:
- Takes two parameters: herb_power and water_level
- Multiplies them together
- Returns the result

Then test it by calling: make_potion(5, 3)
The function should return 15""",
            test_cases=[
                {'type': 'function', 'function': 'make_potion', 'input': [5, 3], 'expected': 15},
                {'type': 'function', 'function': 'make_potion', 'input': [10, 2], 'expected': 20}
            ],
            hints=[
                "Start with: def make_potion(herb_power, water_level):",
                "Calculate: result = herb_power * water_level",
                "Return the result: return result"
            ]
        )
        return challenge.run()


class BooleanLogicLesson(Lesson):
    """Lesson 4: Boolean Logic and Branching"""

    def __init__(self):
        super().__init__(
            lesson_id="act1_boolean_logic",
            title="Boolean Logic & Branching — The Forking Path",
            description="Learn to make decisions in code using logic."
        )

    def teach(self):
        print("""
A chill breeze cuts through the grove. Twisted vines crawl toward you.

Willowbyte: "Corruption! You must decide your actions carefully."

    vines_alive = True

    if vines_alive:
        print("Cast Entangle!")
    else:
        print("Dance in celebration!")

📖 CONCEPT: BOOLEAN LOGIC AND IF STATEMENTS

Booleans are values that are either True or False.

COMPARISON OPERATORS:
    ==  Equal to           (5 == 5 is True)
    !=  Not equal to       (5 != 3 is True)
    >   Greater than       (5 > 3 is True)
    <   Less than          (3 < 5 is True)
    >=  Greater or equal   (5 >= 5 is True)
    <=  Less or equal      (3 <= 5 is True)

IF STATEMENTS:
    if condition:
        # code runs if condition is True
    elif another_condition:
        # code runs if first was False, this is True
    else:
        # code runs if all conditions were False

EXAMPLE:
    danger_level = "high"

    if danger_level == "high":
        print("Cast Entangle!")
    elif danger_level == "medium":
        print("Prepare a healing potion.")
    else:
        print("All is calm.")

LOGICAL OPERATORS:
    and  Both must be True    (True and False = False)
    or   One must be True     (True or False = True)
    not  Inverts the value    (not True = False)
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create a danger detection system:
- Create a variable 'danger' with value "high"
- Use if/elif/else to check the danger level:
  - If danger == "high": create variable action = "cast spell"
  - Elif danger == "medium": action = "prepare potion"
  - Else: action = "rest"

With danger = "high", action should equal "cast spell" """,
            test_cases=[
                {'type': 'variable', 'variable': 'danger', 'expected': 'high'},
                {'type': 'variable', 'variable': 'action', 'expected': 'cast spell'}
            ],
            hints=[
                "Start with: danger = \"high\"",
                "Use: if danger == \"high\":",
                "Set action inside each branch: action = \"cast spell\""
            ]
        )
        return challenge.run()


def create_act_1() -> Act:
    """Create and return Act I with all scenes and lessons"""

    act1 = Act(
        act_number=1,
        title="The Roots of Syntax",
        description="Awaken to the logic of magic. Learn the fundamental building blocks of Python."
    )

    scene1 = Scene(
        scene_id="act1_scene1",
        title="Scene 1: Awakening in the Grove",
        narrative="""A shaft of light pierces the emerald canopy. Dew glistens like 
liquid code. You awaken on a bed of moss, your head buzzing with strange 
whispers — fragments of words and symbols weaving through your thoughts.

The trees seem to hum softly: "print... your... name..." """
    )

    scene1.add_dialogue("Elder Willowbyte",
                        "Ah, Grixle! You've finally rebooted. Your connection to the Grove was lost for... hm... forty-two moon cycles. Time is a fickle loop. But now the Cult of the Dragon corrupts the code of life itself. You must relearn the Old Language — Python.")
    scene1.add_dialogue("Grixle", "Python? Sounds like a snake. Is it venomous?")
    scene1.add_dialogue("Elder Willowbyte", "Only if you forget to close your parentheses.")
    scene1.add_lesson(StringsAndVariablesLesson())
    scene1.add_lesson(NumbersLesson())

    scene2 = Scene(
        scene_id="act1_scene2",
        title="Scene 2: The Circle's Challenge",
        narrative="""The Grove's heart glows faintly green. The air smells of data 
and dew. Elder Willowbyte's roots form a sigil in the soil — a spiraling 
pattern of glowing lines."""
    )

    scene2.add_dialogue("Elder Willowbyte",
                        "Now, we conjure repeatable magic. Words that can be spoken again and again — functions.")
    scene2.add_lesson(FunctionsLesson())

    scene3 = Scene(
        scene_id="act1_scene3",
        title="Scene 3: The Path of Logic",
        narrative="""A chill breeze cuts through the grove. The trees groan. From 
beneath the soil, something stirs — vines, twisted and dark, crawling 
toward you."""
    )

    scene3.add_dialogue("Elder Willowbyte",
                        "Corruption! The Cult's logic infects the forest. You must decide your actions carefully using the power of Boolean logic.")
    scene3.add_lesson(BooleanLogicLesson())

    scene4 = Scene(
        scene_id="act1_scene4",
        title="Scene 4: The Grove Recompiled",
        narrative="""As the forest stabilizes, the whispering stops. You feel 
something shift within you — not just magic, but understanding. The Grove 
seems to breathe again."""
    )

    scene4.add_dialogue("Elder Willowbyte",
                        "Excellent work, young Grixle. You have learned the fundamentals — variables, numbers, functions, and logic. The world now speaks to you in syntax.")
    scene4.add_dialogue("Elder Willowbyte",
                        "The Cult of the Dragon hides in the port city of Mallport. They corrupt code itself — twisting spells into machine scripts. You must go there and learn loops and lists — the structure of repetition and order.")

    act1.add_scene(scene1)
    act1.add_scene(scene2)
    act1.add_scene(scene3)
    act1.add_scene(scene4)

    return act1


# ============================================================================
# ACT II: THE CODE OF THE CITY
# ============================================================================

class ListsAndForLoopsLesson(Lesson):
    """Lesson 1: Lists and For Loops"""

    def __init__(self):
        super().__init__(
            lesson_id="act2_lists_for_loops",
            title="Lists & For Loops — The Cargo Manifest",
            description="Learn to store multiple items and iterate through them."
        )

    def teach(self):
        print("""
The port sprawls before you. Dockmaster Jora hands you a tablet covered in runes.

    cargo = ["fish", "spices", "dragon_scales", "cloth"]

    for item in cargo:
        print("Inspecting " + item)

📖 CONCEPT: LISTS AND FOR LOOPS

LISTS are ordered collections of items:
    my_list = [1, 2, 3, 4, 5]
    names = ["Alice", "Bob", "Charlie"]
    mixed = [1, "hello", 3.14, True]

ACCESSING LIST ITEMS:
    fruits = ["apple", "banana", "cherry"]
    first = fruits[0]   # "apple" (lists start at 0!)
    second = fruits[1]  # "banana"
    last = fruits[-1]   # "cherry" (negative counts from end)

MODIFYING LISTS:
    fruits.append("date")      # Add to end
    fruits.insert(1, "mango")  # Insert at position
    fruits.remove("banana")    # Remove by value
    fruits.pop()               # Remove last item

FOR LOOPS iterate through each item:
    for item in my_list:
        # code runs once for each item
        print(item)

EXAMPLE:
    creatures = ["crab", "eel", "seagull"]
    for creature in creatures:
        print(creature.capitalize() + " appears!")
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create a list called 'cargo' with these items:
"fish", "spices", "dragon_scales", "cloth"

Then use a for loop to check each item.
If the item contains "dragon", set a variable 'contraband' to True""",
            test_cases=[
                {'type': 'variable', 'variable': 'cargo', 'expected': ["fish", "spices", "dragon_scales", "cloth"]},
                {'type': 'variable', 'variable': 'contraband', 'expected': True}
            ],
            hints=[
                "Create list: cargo = [\"fish\", \"spices\", \"dragon_scales\", \"cloth\"]",
                "Loop: for item in cargo:",
                "Check: if \"dragon\" in item: contraband = True"
            ]
        )
        return challenge.run()


class StringMethodsLesson(Lesson):
    """Lesson 2: String Methods and Manipulation"""

    def __init__(self):
        super().__init__(
            lesson_id="act2_string_methods",
            title="String Methods — Cleaning the Manifests",
            description="Learn to manipulate and transform text."
        )

    def teach(self):
        print("""
A mischievous sprite has corrupted the market's text. You must clean it.

    message = "  DRAGON_SCALES  "
    clean = message.strip().lower().replace("_", " ")
    print(clean)  # Output: "dragon scales"

📖 CONCEPT: STRING METHODS

Strings have built-in methods to transform them:

CASE CHANGES:
    text = "Hello World"
    text.upper()       # "HELLO WORLD"
    text.lower()       # "hello world"
    text.capitalize()  # "Hello world"
    text.title()       # "Hello World"

WHITESPACE:
    text = "  hello  "
    text.strip()       # "hello" (removes from both ends)
    text.lstrip()      # "hello  " (removes from left)
    text.rstrip()      # "  hello" (removes from right)

REPLACEMENT:
    text = "Hello World"
    text.replace("World", "Python")  # "Hello Python"
    text.replace("l", "L")           # "HeLLo WorLd"

CHECKING CONTENT:
    "hello" in "hello world"      # True
    "Hello".startswith("He")      # True
    "world".endswith("ld")        # True

SPLITTING AND JOINING:
    text = "apple,banana,cherry"
    fruits = text.split(",")      # ["apple", "banana", "cherry"]

    words = ["hello", "world"]
    sentence = " ".join(words)    # "hello world"

FINDING:
    text = "hello world"
    text.find("world")    # 6 (index where found)
    text.count("l")       # 3 (number of times found)
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""You have a corrupted manifest entry:
manifest = "  DRAGON_PARTS  "

Clean it by:
1. Remove whitespace (strip)
2. Convert to lowercase
3. Replace underscore with space
Store result in 'cleaned'

The result should be: "dragon parts" """,
            test_cases=[
                {'type': 'variable', 'variable': 'manifest', 'expected': "  DRAGON_PARTS  "},
                {'type': 'variable', 'variable': 'cleaned', 'expected': "dragon parts"}
            ],
            hints=[
                "Start: manifest = \"  DRAGON_PARTS  \"",
                "Chain methods: manifest.strip().lower().replace(\"_\", \" \")",
                "Store result: cleaned = ..."
            ]
        )
        return challenge.run()


class SlicingAndIndexingLesson(Lesson):
    """Lesson 3: Slicing and Indexing"""

    def __init__(self):
        super().__init__(
            lesson_id="act2_slicing_indexing",
            title="Slicing & Indexing — The Spy's Cipher",
            description="Learn to extract specific parts of sequences."
        )

    def teach(self):
        print("""
You intercept a coded message from the Cult.

    code = "MALLPORT@MIDNIGHT"
    city = code[:8]      # "MALLPORT"
    time = code[9:]      # "MIDNIGHT"

📖 CONCEPT: SLICING AND INDEXING

INDEXING gets a single item:
    text = "Python"
    text[0]   # "P" (first character)
    text[1]   # "y"
    text[-1]  # "n" (last character)
    text[-2]  # "o" (second from end)

SLICING gets a range:
    text[start:end]     # from start to end-1
    text[:end]          # from beginning to end-1
    text[start:]        # from start to end
    text[:]             # entire sequence
    text[start:end:step]  # with step

EXAMPLES:
    text = "ABCDEFGH"
    text[0:3]    # "ABC" (indices 0, 1, 2)
    text[2:5]    # "CDE"
    text[:4]     # "ABCD" (first 4)
    text[5:]     # "FGH" (from 5 to end)
    text[::2]    # "ACEG" (every 2nd char)
    text[::-1]   # "HGFEDCBA" (reversed!)

WORKS WITH LISTS TOO:
    numbers = [10, 20, 30, 40, 50]
    numbers[1:4]   # [20, 30, 40]
    numbers[-2:]   # [40, 50]
    numbers[::2]   # [10, 30, 50]
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Decode this message:
code = "MALLPORT@MIDNIGHT#"

Extract:
- city = first 8 characters
- time = characters from index 9 to 17
- Both should be lowercase

Expected: city = "mallport", time = "midnight" """,
            test_cases=[
                {'type': 'variable', 'variable': 'code', 'expected': "MALLPORT@MIDNIGHT#"},
                {'type': 'variable', 'variable': 'city', 'expected': "mallport"},
                {'type': 'variable', 'variable': 'time', 'expected': "midnight"}
            ],
            hints=[
                "code = \"MALLPORT@MIDNIGHT#\"",
                "city = code[:8].lower()",
                "time = code[9:17].lower()"
            ]
        )
        return challenge.run()


class WhileLoopsLesson(Lesson):
    """Lesson 4: While Loops"""

    def __init__(self):
        super().__init__(
            lesson_id="act2_while_loops",
            title="While Loops — The Sewer Maze",
            description="Learn to repeat code based on conditions."
        )

    def teach(self):
        print("""
You descend into the sewers. The tunnels loop endlessly...

    steps = 0
    while steps < 5:
        print("Step", steps)
        steps += 1
    print("Escaped!")

📖 CONCEPT: WHILE LOOPS

While loops repeat as long as a condition is True:

    while condition:
        # code repeats while condition is True
        # BE CAREFUL: update condition or loop forever!

EXAMPLE:
    count = 0
    while count < 3:
        print("Count:", count)
        count += 1

    Output:
    Count: 0
    Count: 1
    Count: 2

LOOP CONTROL:
    break     # Exit the loop immediately
    continue  # Skip rest of iteration, go to next

EXAMPLE WITH BREAK:
    while True:  # infinite loop!
        answer = input("Enter 'quit' to exit: ")
        if answer == "quit":
            break  # exits the loop

EXAMPLE WITH CONTINUE:
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue  # skip printing 3
        print(count)

    Output: 1, 2, 4, 5

⚠️  WARNING: Avoid infinite loops!
    Wrong:
        while True:
            print("Forever!")  # Never stops!

    Right:
        counter = 0
        while counter < 10:
            print("Iteration", counter)
            counter += 1  # Always update!
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create a countdown:
- Start with counter = 3
- Use a while loop that runs while counter > 0
- Inside the loop, subtract 1 from counter each time
- After the loop, set a variable 'escaped' to True

counter should end at 0, and escaped should be True""",
            test_cases=[
                {'type': 'variable', 'variable': 'counter', 'expected': 0},
                {'type': 'variable', 'variable': 'escaped', 'expected': True}
            ],
            hints=[
                "counter = 3",
                "while counter > 0:",
                "    counter -= 1 (or counter = counter - 1)",
                "escaped = True (after the loop)"
            ]
        )
        return challenge.run()


class DebuggingLesson(Lesson):
    """Lesson 5: Debugging and Fixing Bugs"""

    def __init__(self):
        super().__init__(
            lesson_id="act2_debugging",
            title="Debugging — The Bug Hunt",
            description="Learn to find and fix errors in code."
        )

    def teach(self):
        print("""
A sprite giggles as code malfunctions around you.

    # BROKEN:
    print("Gold: " + 50)  # TypeError!

    # FIXED:
    print("Gold: " + str(50))  # Convert number to string

📖 CONCEPT: DEBUGGING

Bugs are errors in code. There are three main types:

1. SYNTAX ERRORS (code won't run):
    print("Hello"  # Missing closing parenthesis
    if x = 5:      # Should use == not =

2. RUNTIME ERRORS (crashes while running):
    print(undefined_variable)  # NameError
    print("Number: " + 5)      # TypeError
    numbers = [1, 2, 3]
    print(numbers[10])         # IndexError

3. LOGIC ERRORS (runs but wrong result):
    total = 0
    for i in range(5):
        total = i  # Should be total += i
    print(total)  # Shows 4, should be 10

DEBUGGING TIPS:
- Read error messages carefully
- Check for typos in variable names
- Verify data types (string vs number)
- Use print() to see what's happening
- Test small pieces of code separately
- Check indentation (Python cares about spaces!)

COMMON FIXES:
    # Type conversion
    "Age: " + str(25)
    int("100") + 50

    # Index bounds
    if index < len(my_list):
        item = my_list[index]

    # Check if variable exists
    if 'variable' in dir():
        use_variable()
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Fix this buggy code concept:
You need to convert a number to string before combining with text.

Create:
- coins = 100
- message = "Gold: " + str(coins)

message should equal "Gold: 100" """,
            test_cases=[
                {'type': 'variable', 'variable': 'coins', 'expected': 100},
                {'type': 'variable', 'variable': 'message', 'expected': "Gold: 100"}
            ],
            hints=[
                "coins = 100",
                "Use str() to convert: str(coins)",
                "message = \"Gold: \" + str(coins)"
            ]
        )
        return challenge.run()


def create_act_2() -> Act:
    """Create and return Act II with all scenes and lessons"""

    act2 = Act(
        act_number=2,
        title="The Code of the City",
        description="Enter Mallport and master lists, loops, and the art of debugging."
    )

    scene1 = Scene(
        scene_id="act2_scene1",
        title="Scene 1: Arrival at Mallport",
        narrative="""The port sprawls before you: brass cranes swing above the waves, 
data glyphs flickering on every hull. Steam and syntax fill the air."""
    )
    scene1.add_dialogue("Grixle", "Smells like rust and recursion.")
    scene1.add_dialogue("Dockmaster Jora",
                        "Then you'll fit right in. Our shipping manifests are corrupted. Can you parse a list?")
    scene1.add_lesson(ListsAndForLoopsLesson())

    scene2 = Scene(
        scene_id="act2_scene2",
        title="Scene 2: The Missing Cargo",
        narrative="""Jora hands you a tablet covered in runes. One entry flashes red.
The cult has hidden contraband among the goods."""
    )
    scene2.add_dialogue("Dockmaster Jora",
                        "The cult hid contraband among our goods. Use string methods to clean and search the manifests.")
    scene2.add_lesson(StringMethodsLesson())

    scene3 = Scene(
        scene_id="act2_scene3",
        title="Scene 3: The Spy's Cipher",
        narrative="""Back above ground, you intercept a cult message. The text is 
encoded, but you now have the tools to decode it."""
    )
    scene3.add_dialogue("Grixle", "Let me slice through this cipher...")
    scene3.add_lesson(SlicingAndIndexingLesson())

    scene4 = Scene(
        scene_id="act2_scene4",
        title="Scene 4: The Sewer of Infinite Loops",
        narrative="""You descend into tunnels etched with glowing code. Water drips 
in rhythmic intervals — like a loop gone wrong."""
    )
    scene4.add_dialogue("Grixle", "One wrong step and I'll be stuck in an infinite loop forever...")
    scene4.add_lesson(WhileLoopsLesson())

    scene5 = Scene(
        scene_id="act2_scene5",
        title="Scene 5: The Bug Hunt",
        narrative="""A sprite flutters by, sprinkling typos on the city's code. 
The market lanterns flicker with syntax errors."""
    )
    scene5.add_dialogue("Sprite", "Hee-hee! Missing colons, stray parentheses — such chaos!")
    scene5.add_dialogue("Grixle", "Time to hunt down these bugs...")
    scene5.add_lesson(DebuggingLesson())

    scene6 = Scene(
        scene_id="act2_scene6",
        title="Scene 6: The Path Forward",
        narrative="""The city grows quiet. Your decoded message reveals coordinates 
leading to an ancient library."""
    )
    scene6.add_dialogue("Dockmaster Jora",
                        "You've mastered the basics of iteration and debugging. The Library of Thorns awaits you — it holds deeper knowledge.")
    scene6.add_dialogue("Grixle", "Dictionaries and data structures, here I come.")

    act2.add_scene(scene1)
    act2.add_scene(scene2)
    act2.add_scene(scene3)
    act2.add_scene(scene4)
    act2.add_scene(scene5)
    act2.add_scene(scene6)

    return act2


# ============================================================================
# ACT III: THE TOME OF KNOWLEDGE
# ============================================================================

class DictionariesLesson(Lesson):
    """Lesson 1: Dictionaries"""

    def __init__(self):
        super().__init__(
            lesson_id="act3_dictionaries",
            title="Dictionaries — The Spell Index",
            description="Learn to store data with key-value pairs."
        )

    def teach(self):
        print("""
The library shelves curl with living vines. Each book hums faintly.

Archivist Myrren: "Our index is in chaos. Each spell lost its key."

    spells = {"heal": 10, "thornstrike": 15, "entangle": 20}
    print(spells["heal"])  # Output: 10

📖 CONCEPT: DICTIONARIES

Dictionaries store data as key-value pairs:

CREATING DICTIONARIES:
    person = {
        "name": "Grixle",
        "age": 24,
        "class": "Druid"
    }

ACCESSING VALUES:
    person["name"]      # "Grixle"
    person.get("age")   # 24
    person.get("level", 1)  # 1 (default if not found)

MODIFYING DICTIONARIES:
    person["age"] = 25           # Update value
    person["weapon"] = "staff"   # Add new key
    del person["class"]          # Remove key

CHECKING KEYS:
    "name" in person    # True
    "health" in person  # False

DICTIONARY METHODS:
    person.keys()      # dict_keys(['name', 'age'])
    person.values()    # dict_values(['Grixle', 24])
    person.items()     # dict_items([('name', 'Grixle'), ...])

LOOPING THROUGH DICTIONARIES:
    for key in person:
        print(key, person[key])

    for key, value in person.items():
        print(key, "=", value)

WHY USE DICTIONARIES?
- Fast lookup by key
- Store related data together
- More readable than lists for complex data
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create a spell dictionary:
- spells = {"heal": 10, "thornstrike": 15}
- Add a new spell: spells["entangle"] = 20
- Update heal: spells["heal"] = 12

Final spells should be: {"heal": 12, "thornstrike": 15, "entangle": 20}""",
            test_cases=[
                {'type': 'variable', 'variable': 'spells', 'expected': {"heal": 12, "thornstrike": 15, "entangle": 20}}
            ],
            hints=[
                "Start: spells = {\"heal\": 10, \"thornstrike\": 15}",
                "Add: spells[\"entangle\"] = 20",
                "Update: spells[\"heal\"] = 12"
            ]
        )
        return challenge.run()


class SetsAndTuplesLesson(Lesson):
    """Lesson 2: Sets and Tuples"""

    def __init__(self):
        super().__init__(
            lesson_id="act3_sets_tuples",
            title="Sets & Tuples — The Garden of Patterns",
            description="Learn about immutable sequences and unique collections."
        )

    def teach(self):
        print("""
A glass dome houses endless flora. The garden rearranges itself...

    plants = ["fern", "moss", "fern", "rose"]
    unique_plants = set(plants)
    print(unique_plants)  # {'fern', 'moss', 'rose'} - no duplicates!

📖 CONCEPT: SETS AND TUPLES

SETS are unordered collections of unique items:

CREATING SETS:
    fruits = {"apple", "banana", "cherry"}
    numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

SET OPERATIONS:
    fruits.add("date")        # Add item
    fruits.remove("banana")   # Remove item
    fruits.discard("mango")   # Remove if exists (no error)

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1 | set2   # Union: {1, 2, 3, 4, 5}
    set1 & set2   # Intersection: {3}
    set1 - set2   # Difference: {1, 2}

WHEN TO USE SETS:
- Remove duplicates from a list
- Check membership (fast!)
- Mathematical set operations

TUPLES are immutable (can't change) sequences:

CREATING TUPLES:
    coordinates = (10, 20)
    rgb = (255, 128, 0)
    single = (42,)  # Comma needed for single item

ACCESSING TUPLES:
    point = (3, 4)
    x = point[0]  # 3
    y = point[1]  # 4

UNPACKING:
    x, y = (10, 20)  # x=10, y=20

⚠️  TUPLES CAN'T BE CHANGED:
    point = (3, 4)
    point[0] = 5  # ERROR! Tuples are immutable

WHEN TO USE TUPLES:
- Fixed coordinates or positions
- Dictionary keys (lists can't be keys!)
- Return multiple values from functions
- Data that shouldn't change
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Remove duplicates from this list:
plants = ["fern", "moss", "fern", "rose", "moss"]

Create a set called 'unique_plants' with no duplicates.
Result should have 3 unique items.""",
            test_cases=[
                {'type': 'variable', 'variable': 'plants', 'expected': ["fern", "moss", "fern", "rose", "moss"]},
                {'type': 'variable', 'variable': 'unique_plants', 'expected': {"fern", "moss", "rose"}}
            ],
            hints=[
                "plants = [\"fern\", \"moss\", \"fern\", \"rose\", \"moss\"]",
                "unique_plants = set(plants)",
                "Sets automatically remove duplicates!"
            ]
        )
        return challenge.run()


class SortingLesson(Lesson):
    """Lesson 3: Sorting Data"""

    def __init__(self):
        super().__init__(
            lesson_id="act3_sorting",
            title="Sorting — Organizing the Archives",
            description="Learn to sort and organize data."
        )

    def teach(self):
        print("""
Scrolls float chaotically around you. You must bring order to the chaos.

    numbers = [5, 2, 8, 1, 9]
    numbers.sort()
    print(numbers)  # [1, 2, 5, 8, 9]

📖 CONCEPT: SORTING

SORTING LISTS:
    numbers = [3, 1, 4, 1, 5]
    numbers.sort()  # Modifies the list
    print(numbers)  # [1, 1, 3, 4, 5]

    # Reverse order
    numbers.sort(reverse=True)  # [5, 4, 3, 1, 1]

SORTED() FUNCTION (returns new list):
    original = [3, 1, 4]
    sorted_list = sorted(original)
    # original unchanged: [3, 1, 4]
    # sorted_list: [1, 3, 4]

SORTING STRINGS:
    words = ["banana", "apple", "cherry"]
    words.sort()  # Alphabetical: ['apple', 'banana', 'cherry']

REVERSE():
    numbers = [1, 2, 3]
    numbers.reverse()  # [3, 2, 1]

SORTING DICTIONARIES:
    spells = {"heal": 10, "entangle": 20, "flare": 15}

    # Sort by keys
    sorted_by_key = dict(sorted(spells.items()))

    # Sort by values
    sorted_by_value = dict(sorted(spells.items(), key=lambda x: x[1]))

MIN AND MAX:
    numbers = [5, 2, 8, 1, 9]
    print(min(numbers))  # 1
    print(max(numbers))  # 9
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Sort this list of numbers:
numbers = [5, 2, 8, 1, 9]

Sort it and store in 'sorted_numbers' (use sorted() function).
Result should be [1, 2, 5, 8, 9]""",
            test_cases=[
                {'type': 'variable', 'variable': 'numbers', 'expected': [5, 2, 8, 1, 9]},
                {'type': 'variable', 'variable': 'sorted_numbers', 'expected': [1, 2, 5, 8, 9]}
            ],
            hints=[
                "numbers = [5, 2, 8, 1, 9]",
                "sorted_numbers = sorted(numbers)",
                "sorted() returns a new sorted list"
            ]
        )
        return challenge.run()


class FilesLesson(Lesson):
    """Lesson 4: Working with Files"""

    def __init__(self):
        super().__init__(
            lesson_id="act3_files",
            title="Files — The Hall of Records",
            description="Learn to read from and write to files."
        )

    def teach(self):
        print("""
Ancient scrolls line the walls. Each contains data waiting to be read.

    with open("trade_log.txt", "r") as file:
        data = file.read()
        print(data)

📖 CONCEPT: FILES

READING FILES:
    # Read entire file
    with open("file.txt", "r") as file:
        content = file.read()

    # Read line by line
    with open("file.txt", "r") as file:
        for line in file:
            print(line.strip())

    # Read all lines into list
    with open("file.txt", "r") as file:
        lines = file.readlines()

WRITING FILES:
    # Write (overwrites existing)
    with open("output.txt", "w") as file:
        file.write("Hello, World!\\n")
        file.write("Second line\\n")

    # Append (adds to end)
    with open("output.txt", "a") as file:
        file.write("Third line\\n")

WHY USE 'WITH'?
The 'with' statement automatically closes the file when done.

FILE MODES:
    "r"  - Read (default)
    "w"  - Write (overwrites)
    "a"  - Append
    "r+" - Read and write

CHECKING IF FILE EXISTS:
    import os
    if os.path.exists("file.txt"):
        print("File found!")

COMMON PATTERN:
    try:
        with open("data.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("File not found!")

⚠️  In this game environment, we won't create actual files,
    but understanding the concept is important!
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Understand the file reading concept:

Create a variable 'file_mode' with value "r" (for reading)
Create a variable 'file_name' with value "trade_log.txt"

This demonstrates you understand file basics.""",
            test_cases=[
                {'type': 'variable', 'variable': 'file_mode', 'expected': 'r'},
                {'type': 'variable', 'variable': 'file_name', 'expected': 'trade_log.txt'}
            ],
            hints=[
                "file_mode = \"r\"",
                "file_name = \"trade_log.txt\""
            ]
        )
        return challenge.run()


class ExceptionsLesson(Lesson):
    """Lesson 5: Exception Handling"""

    def __init__(self):
        super().__init__(
            lesson_id="act3_exceptions",
            title="Exceptions — The Loop of Errors",
            description="Learn to handle errors gracefully."
        )

    def teach(self):
        print("""
The library trembles. Scrolls spin into a storm. Magic misfires!

    try:
        risky_spell = 10 / 0  # This causes an error!
    except ZeroDivisionError:
        print("Cannot divide by zero!")

📖 CONCEPT: EXCEPTION HANDLING

Exceptions are errors that occur during program execution.

TRY-EXCEPT:
    try:
        # Code that might cause an error
        number = int("abc")  # ValueError!
    except ValueError:
        print("That's not a valid number!")

CATCHING MULTIPLE EXCEPTIONS:
    try:
        risky_code()
    except ValueError:
        print("Value error occurred")
    except TypeError:
        print("Type error occurred")
    except Exception as e:
        print(f"Some error: {e}")

ELSE AND FINALLY:
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Division error!")
    else:
        print("Success!")  # Runs if no exception
    finally:
        print("Cleanup")  # Always runs

COMMON EXCEPTIONS:
    ValueError      - Wrong value type
    TypeError       - Wrong data type
    NameError       - Variable doesn't exist
    IndexError      - List index out of range
    KeyError        - Dictionary key doesn't exist
    FileNotFoundError - File not found
    ZeroDivisionError - Division by zero

WHY HANDLE EXCEPTIONS?
- Prevent program crashes
- Give users helpful messages
- Clean up resources (close files, etc.)
- Recover from errors gracefully

EXAMPLE:
    while True:
        try:
            age = int(input("Enter age: "))
            break  # Exit loop if successful
        except ValueError:
            print("Please enter a number!")
        """)

    def challenge(self) -> bool:
        challenge = CodeChallenge(
            prompt="""Create exception handling:

Set up:
error_handled = False

Use try-except to handle a division by zero:
try:
    result = 10 / 0
except ZeroDivisionError:
    error_handled = True

error_handled should be True""",
            test_cases=[
                {'type': 'variable', 'variable': 'error_handled', 'expected': True}
            ],
            hints=[
                "error_handled = False",
                "try:",
                "    result = 10 / 0",
                "except ZeroDivisionError:",
                "    error_handled = True"
            ]
        )
        return challenge.run()


def create_act_3() -> Act:
    """Create and return Act III with all scenes and lessons"""

    act3 = Act(
        act_number=3,
        title="The Tome of Knowledge",
        description="Enter the Library of Thorns and master data structures, files, and error handling."
    )

    scene1 = Scene(
        scene_id="act3_scene1",
        title="Scene 1: Library of Thorns",
        narrative="""Shelves curl with living vines; every book hums faintly. 
The air smells of parchment and possibility."""
    )
    scene1.add_dialogue("Archivist Myrren",
                        "Our index is in chaos. Each spell lost its key. Can you restore the mappings?")
    scene1.add_lesson(DictionariesLesson())

    scene2 = Scene(
        scene_id="act3_scene2",
        title="Scene 2: The Garden of Patterns",
        narrative="""A glass dome houses endless flora. The garden rearranges 
its layout every minute — a fractal of duplicates and patterns."""
    )
    scene2.add_dialogue("Grixle", "I need to identify the unique species here...")
    scene2.add_lesson(SetsAndTuplesLesson())

    scene3 = Scene(
        scene_id="act3_scene3",
        title="Scene 3: The Hall of Records",
        narrative="""Ancient scrolls float in perfect formation. Each contains 
trade logs spanning centuries."""
    )
    scene3.add_dialogue("Archivist Myrren",
                        "These records must be sorted and organized. The cult's transactions are buried in here somewhere.")
    scene3.add_lesson(SortingLesson())
    scene3.add_lesson(FilesLesson())

    scene4 = Scene(
        scene_id="act3_scene4",
        title="Scene 4: The Loop of Errors",
        narrative="""The library trembles. Scrolls spin into a storm. Your spell 
misfires, but you remain standing."""
    )
    scene4.add_dialogue("Grixle", "I need to handle these errors before the library collapses!")
    scene4.add_lesson(ExceptionsLesson())

    scene5 = Scene(
        scene_id="act3_scene5",
        title="Scene 5: The Iron Path",
        narrative="""You discover ancient blueprints. The cult's plans become clear: 
they're building something massive."""
    )
    scene5.add_dialogue("Archivist Myrren",
                        "You've mastered data manipulation. But the cult works with more than data — they build with classes and objects. The Iron Sanctum awaits.")
    scene5.add_dialogue("Grixle", "Time to learn the architecture of code itself.")

    act3.add_scene(scene1)
    act3.add_scene(scene2)
    act3.add_scene(scene3)
    act3.add_scene(scene4)
    act3.add_scene(scene5)

    return act3


# ============================================================================
# ACT IV: THE SPIRIT AND THE MACHINE
# ============================================================================

class ClassesLesson(Lesson):
    """Lesson 1: Classes and Objects"""

    def __init__(self):
        super().__init__(
            lesson_id="act4_classes",
            title="Classes — The Druid's Awakening",
            description="Learn to create your own data types with classes."
        )

    def teach(self):
        print("""
Lightning cracks over Mallport's tower. You see code weaving through your veins.

Willowbyte (telepathically): "You are both nature and logic now. Define yourself."

    class Druid:
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def cast(self, spell):
            print(f"{self.name} casts {spell}!")

    grixle = Druid("Grixle", 25)
    grixle.cast("Thornstrike")

📖 CONCEPT: CLASSES AND OBJECTS

Classes are blueprints for creating objects:

DEFINING A CLASS:
    class Character:
        def __init__(self, name, health):
            self.name = name
            self.health = health

        def take_damage(self, amount):
            self.health -= amount
            print(f"{self.name} has {self.health} health left")

CREATING OBJECTS (INSTANCES):
    hero = Character("Grixle", 100)
    enemy = Character("Goblin", 50)

    hero.take_damage(10)  # Grixle has 90 health left

KEY CONCEPTS:
- __init__: Constructor method (runs when object created)
- self: Refers to the current instance
- Attributes: Data stored in object (self.name, self.health)
- Methods: Functions that belong to the class

ATTRIBUTES:
    class Item:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    sword = Item("Iron Sword", 100)
    print(sword.name)   # "Iron Sword"
    print(sword.value)  # 100

METHODS:
    class Spell:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

        def cast(self, caster):
            print(f"{caster} casts {self.name} for {self.cost} mana!")

    fireball = Spell("Fireball", 15)
    fireball.cast("Grixle")

WHY USE CLASSES?
- Group related data and functions
- Create multiple similar objects easily
- Model real-world things in code
- Make code more organized and reusable
        """)

    def challenge(self) -> bool:
        print("\n💡 For this challenge, just ensure your code runs without errors.")
        print("Focus on understanding the class structure!")
        return True


class ModulesLesson(Lesson):
    """Lesson 2: Modules and Imports"""

    def __init__(self):
        super().__init__(
            lesson_id="act4_modules",
            title="Modules — Grimoires of Power",
            description="Learn to use Python's built-in libraries."
        )

    def teach(self):
        print("""
You find ancient tomes labeled 'math', 'random', and 'datetime'.

    import random
    roll = random.randint(1, 20)
    print(f"You rolled a {roll}!")

📖 CONCEPT: MODULES

Modules are Python files containing code you can reuse.

IMPORTING MODULES:
    import math
    print(math.pi)  # 3.141592653589793
    print(math.sqrt(16))  # 4.0

IMPORTING SPECIFIC ITEMS:
    from math import pi, sqrt
    print(pi)
    print(sqrt(16))

IMPORTING WITH ALIAS:
    import random as rnd
    print(rnd.randint(1, 10))

USEFUL BUILT-IN MODULES:

RANDOM:
    import random
    random.randint(1, 10)      # Random integer
    random.choice([1,2,3])     # Random from list
    random.shuffle(my_list)    # Shuffle list

MATH:
    import math
    math.sqrt(16)              # Square root
    math.pow(2, 3)             # Power (2^3)
    math.floor(3.7)            # Round down (3)
    math.ceil(3.2)             # Round up (4)

DATETIME:
    from datetime import datetime
    now = datetime.now()
    print(now.year, now.month, now.day)

TIME:
    import time
    time.sleep(2)              # Pause 2 seconds

OS:
    import os
    os.path.exists("file.txt") # Check if file exists
    os.getcwd()                # Current directory

CREATING YOUR OWN MODULE:
    # File: my_module.py
    def greet(name):
        return f"Hello, {name}!"

    # File: main.py
    import my_module
    print(my_module.greet("Grixle"))
        """)

    def challenge(self) -> bool:
        print("\n💡 For this challenge, we'll check if your code runs.")
        print("The random value will be different each time!")
        return True


class InheritanceLesson(Lesson):
    """Lesson 3: Inheritance"""

    def __init__(self):
        super().__init__(
            lesson_id="act4_inheritance",
            title="Inheritance — Evolution of Code",
            description="Learn to create classes based on other classes."
        )

    def teach(self):
        print("""
The cult's machines evolve. They inherit properties from their ancestors.

    class Creature:
        def __init__(self, name, health):
            self.name = name
            self.health = health

    class Dragon(Creature):  # Inherits from Creature
        def breathe_fire(self):
            print(f"{self.name} breathes fire!")

    wyrm = Dragon("Iron Wyrm", 500)
    wyrm.breathe_fire()

📖 CONCEPT: INHERITANCE

Inheritance allows a class to inherit attributes and methods from another class.

BASIC INHERITANCE:
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            print(f"{self.name} makes a sound")

    class Dog(Animal):  # Dog inherits from Animal
        def speak(self):
            print(f"{self.name} barks!")

    buddy = Dog("Buddy")
    buddy.speak()  # "Buddy barks!"

TERMINOLOGY:
- Parent/Base/Superclass: The class being inherited from
- Child/Derived/Subclass: The class that inherits

OVERRIDING METHODS:
    class Character:
        def attack(self):
            return 10

    class Warrior(Character):
        def attack(self):  # Override parent method
            return 20

    class Mage(Character):
        pass  # Uses parent's attack (returns 10)

CALLING PARENT METHODS:
    class Character:
        def __init__(self, name):
            self.name = name

    class Warrior(Character):
        def __init__(self, name, weapon):
            super().__init__(name)  # Call parent __init__
            self.weapon = weapon

MULTIPLE INHERITANCE:
    class Flyer:
        def fly(self):
            print("Flying!")

    class Swimmer:
        def swim(self):
            print("Swimming!")

    class Dragon(Flyer, Swimmer):  # Inherits from both
        pass

    d = Dragon()
    d.fly()   # Works!
    d.swim()  # Works!

WHY USE INHERITANCE?
- Reuse code from existing classes
- Create hierarchies of related classes
- Extend functionality without modifying original
- Model "is-a" relationships (Dog is-a Animal)
        """)

    def challenge(self) -> bool:
        print("\n💡 Focus on understanding how inheritance works!")
        print("The child class gets all parent attributes plus its own.")
        return True


class CompositionLesson(Lesson):
    """Lesson 4: Composition"""

    def __init__(self):
        super().__init__(
            lesson_id="act4_composition",
            title="Composition — Building Complex Systems",
            description="Learn to build complex objects from simpler ones."
        )

    def teach(self):
        print("""
The Iron Wyrm is not a single entity—it's an assembly of parts.

    class Engine:
        def start(self):
            print("Engine roaring!")

    class Dragon:
        def __init__(self):
            self.engine = Engine()  # Composition: has-a relationship

        def activate(self):
            self.engine.start()

    wyrm = Dragon()
    wyrm.activate()  # "Engine roaring!"

📖 CONCEPT: COMPOSITION

Composition is when an object contains other objects as parts.

INHERITANCE VS COMPOSITION:
    # Inheritance: "is-a" relationship
    class Dog(Animal):  # Dog IS-A Animal
        pass

    # Composition: "has-a" relationship
    class Car:
        def __init__(self):
            self.engine = Engine()  # Car HAS-A Engine
            self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

COMPOSITION EXAMPLE:
    class Weapon:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

    class Armor:
        def __init__(self, name, defense):
            self.name = name
            self.defense = defense

    class Character:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None

        def equip_weapon(self, weapon):
            self.weapon = weapon

        def equip_armor(self, armor):
            self.armor = armor

    hero = Character("Grixle")
    hero.equip_weapon(Weapon("Staff", 15))
    hero.equip_armor(Armor("Robes", 10))

WHEN TO USE COMPOSITION:
- Building complex objects from simpler parts
- When you need flexibility to swap parts
- When inheritance doesn't make sense
- "Has-a" relationships

EXAMPLE: Game Character
    class Inventory:
        def __init__(self):
            self.items = []

        def add(self, item):
            self.items.append(item)

    class Stats:
        def __init__(self):
            self.health = 100
            self.mana = 50

    class Player:
        def __init__(self, name):
            self.name = name
            self.inventory = Inventory()  # Composition
            self.stats = Stats()          # Composition

    player = Player("Grixle")
    player.inventory.add("Potion")
    print(player.stats.health)
        """)

    def challenge(self) -> bool:
        print("\n💡 Composition means one object contains another!")
        print("Think: A character HAS weapons, HAS inventory, HAS stats.")
        return True


def create_act_4() -> Act:
    """Create and return Act IV with all scenes and lessons"""

    act4 = Act(
        act_number=4,
        title="The Spirit and the Machine",
        description="Master object-oriented programming and prepare for the final battle."
    )

    scene1 = Scene(
        scene_id="act4_scene1",
        title="Scene 1: The Druid's Awakening",
        narrative="""Lightning cracks across the sky. You realize the truth: you are code.
Every living thing is an object, instantiated from the classes of nature."""
    )
    scene1.add_dialogue("Elder Willowbyte",
                        "You have learned that magic is logic. Now learn that life itself is object-oriented. Define yourself, Grixle.")
    scene1.add_lesson(ClassesLesson())

    scene2 = Scene(
        scene_id="act4_scene2",
        title="Scene 2: The Iron Sanctum",
        narrative="""You enter the cult's stronghold. Mechanical dragons line the walls,
powered by stolen magic and imported modules."""
    )
    scene2.add_dialogue("Grixle", "They're using Python modules as grimoires... clever and dangerous.")
    scene2.add_lesson(ModulesLesson())

    scene3 = Scene(
        scene_id="act4_scene3",
        title="Scene 3: The Dragon's Blueprint",
        narrative="""You discover the cult's plans. The Iron Wyrm inherits from ancient
dragon classes, enhanced with modern technology."""
    )
    scene3.add_dialogue("Cultist", "Our creation evolves through inheritance! Each generation stronger than the last!")
    scene3.add_lesson(InheritanceLesson())

    scene4 = Scene(
        scene_id="act4_scene4",
        title="Scene 4: The Assembly",
        narrative="""The Iron Wyrm is being constructed. You see how composition creates
complexity: engines, armor, weapons, all assembled into one terrifying whole."""
    )
    scene4.add_dialogue("Grixle",
                        "It's not just one thing—it's made of many parts working together. I need to understand this...")
    scene4.add_lesson(CompositionLesson())

    scene5 = Scene(
        scene_id="act4_scene5",
        title="Scene 5: Before the Storm",
        narrative="""The Iron Wyrm awakens. Its eyes glow with corrupted code. This is it—
the final battle approaches."""
    )
    scene5.add_dialogue("Elder Willowbyte",
                        "You have learned all the fundamentals. Now you must combine everything—variables, functions, loops, classes—to defeat the Iron Wyrm.")
    scene5.add_dialogue("Grixle", "I'm ready. Let's recompile this world.")

    act4.add_scene(scene1)
    act4.add_scene(scene2)
    act4.add_scene(scene3)
    act4.add_scene(scene4)
    act4.add_scene(scene5)

    return act4


# ============================================================================
# ACT V: THE HEART OF CODE
# ============================================================================

class IntegrationLesson(Lesson):
    """Final Lesson: Bringing it All Together"""

    def __init__(self):
        super().__init__(
            lesson_id="act5_integration",
            title="The Heart of Code — Final Battle",
            description="Use everything you've learned to defeat the Iron Wyrm."
        )

    def teach(self):
        print("""
The Iron Wyrm towers before you. Its code pulses with corrupted energy.

Elder Willowbyte: "This is it, Grixle. Everything you've learned comes together now."

📖 FINAL INTEGRATION

You've learned:
✓ Variables and data types
✓ Functions and return values
✓ Boolean logic and branching
✓ Lists and dictionaries
✓ Loops (for and while)
✓ String manipulation
✓ Files and exceptions
✓ Classes and objects
✓ Inheritance and composition
✓ Modules and imports

Now you must combine them all to create a battle system:

    import random

    class Creature:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

        def is_alive(self):
            return self.health > 0

        def attack(self, target):
            damage = random.randint(1, self.power)
            target.health -= damage
            return damage

    class Hero(Creature):
        def __init__(self, name):
            super().__init__(name, 100, 20)
            self.potions = 3

        def heal(self):
            if self.potions > 0:
                self.health += 30
                self.potions -= 1
                return True
            return False

    class Dragon(Creature):
        def __init__(self):
            super().__init__("Iron Wyrm", 150, 25)

        def breathe_fire(self, target):
            damage = self.power * 2
            target.health -= damage
            return damage

    # Battle simulation
    hero = Hero("Grixle")
    dragon = Dragon()

    while hero.is_alive() and dragon.is_alive():
        # Hero turn
        damage = hero.attack(dragon)
        print(f"Grixle deals {damage} damage!")

        if not dragon.is_alive():
            print("Victory!")
            break

        # Dragon turn
        damage = dragon.breathe_fire(hero)
        print(f"Dragon deals {damage} damage!")

        # Check for heal
        if hero.health < 30 and hero.potions > 0:
            hero.heal()
            print("Grixle heals!")

This code uses EVERYTHING:
- Classes (Hero, Dragon, Creature)
- Inheritance (Hero extends Creature)
- Modules (random)
- Functions/Methods (attack, heal, is_alive)
- Variables (health, power, damage)
- Conditionals (if statements)
- Loops (while loop)
- Boolean logic (and, not)
- Return values
        """)

    def challenge(self) -> bool:
        print("\n💡 This is your final challenge. Show what you've learned!")
        return True


def create_act_5() -> Act:
    """Create and return Act V with all scenes and lessons"""

    act5 = Act(
        act_number=5,
        title="The Heart of Code",
        description="The final battle. Integrate all your knowledge to restore balance to Fraylon."
    )

    scene1 = Scene(
        scene_id="act5_scene1",
        title="Scene 1: The Source",
        narrative="""You reach the underground core of Fraylon. Glowing fractals of logic 
pulse like a heartbeat. The Iron Wyrm awaits, its code corrupting everything around it."""
    )
    scene1.add_dialogue("Elder Willowbyte",
                        "Here lies the true engine of Fraylon. The Iron Wyrm is but corrupted syntax. You must re-write it, Grixle.")
    scene1.add_dialogue("Iron Wyrm",
                        "You think you can defeat me with your pathetic functions? I am infinite recursion! I am the stack overflow!")
    scene1.add_dialogue("Grixle", "Every loop ends. Every function returns. And every dragon... can be debugged.")
    scene1.add_lesson(IntegrationLesson())

    scene2 = Scene(
        scene_id="act5_scene2",
        title="Scene 2: The Restoration",
        narrative="""The Iron Wyrm collapses into harmless data streams. The world's code 
stabilizes. Light returns to the fractals."""
    )
    scene2.add_dialogue("Elder Willowbyte",
                        "You have done it, Grixle. You've learned the true code of nature—the logic that binds all things. Loops, lists, and life itself.")
    scene2.add_dialogue("Grixle",
                        "I understand now. Magic isn't just power—it's pattern. It's logic. It's... beautiful.")
    scene2.add_dialogue("Elder Willowbyte", "And with that understanding, you have become what you were meant to be.")

    scene3 = Scene(
        scene_id="act5_scene3",
        title="Epilogue: The Syntax Sage",
        narrative="""You stand at the edge of Mallport, staff glowing faintly. The grove 
hums in the distance. The world is balanced once more.

You have earned the title: GRIXLE THE SYNTAX SAGE

Your journey through Python is complete. You have mastered:
- Variables, strings, and numbers
- Functions and return values
- Boolean logic and conditionals
- Lists, dictionaries, sets, and tuples
- For loops and while loops
- String methods and slicing
- File handling and exceptions
- Classes, inheritance, and composition
- Modules and imports

But this is not the end—it's just the beginning. The world of Python is vast,
filled with libraries to explore, projects to build, and problems to solve.

The code is alive when it's read with intent.
Go forth and create, Grixle the Syntax Sage."""
    )
    scene3.add_dialogue("Elder Willowbyte",
                        "Remember, young druid: the best way to master Python is to use it. Build things. Break things. Debug things. That is the way.")
    scene3.add_dialogue("Grixle", "Thank you, Elder Willowbyte. For everything.")

    act5.add_scene(scene1)
    act5.add_scene(scene2)
    act5.add_scene(scene3)

    return act5


# ============================================================================
# MAIN GAME INITIALIZATION
# ============================================================================

def main():
    """Main game entry point"""

    game = Game()

    print("🌿 Loading The Verdant Code...")
    print("   Initializing Acts...")

    act1 = create_act_1()
    game.add_act(act1)
    print("   ✓ Act I: The Roots of Syntax")

    act2 = create_act_2()
    game.add_act(act2)
    print("   ✓ Act II: The Code of the City")

    act3 = create_act_3()
    game.add_act(act3)
    print("   ✓ Act III: The Tome of Knowledge")

    act4 = create_act_4()
    game.add_act(act4)
    print("   ✓ Act IV: The Spirit and the Machine")

    act5 = create_act_5()
    game.add_act(act5)
    print("   ✓ Act V: The Heart of Code")

    print("\n✨ All acts loaded successfully!\n")

    try:
        game.start()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Progress saved!")
        game.progress.save_progress()
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Your progress has been saved.")
        game.progress.save_progress()


if __name__ == "__main__":
    main()