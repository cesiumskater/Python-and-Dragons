# Enterprise Skills Roadmap
## From Zero Knowledge to Job-Ready Python Developer

**Document Purpose**: Clear progression path showing what beginners need at each stage
**Target**: Someone who's never coded → Can work on professional development teams

---

## Table of Contents

1. [The Journey Overview](#the-journey-overview)
2. [Stage 0: Pre-Python (Week 0)](#stage-0-pre-python)
3. [Stage 1: Python Basics (Weeks 1-2)](#stage-1-python-basics)
4. [Stage 2: Data Structures (Weeks 3-4)](#stage-2-data-structures)
5. [Stage 3: Control Flow (Weeks 5-6)](#stage-3-control-flow)
6. [Stage 4: Functions (Week 7)](#stage-4-functions)
7. [Stage 5: Files & Modules (Week 8)](#stage-5-files--modules)
8. [Stage 6: OOP (Weeks 9-10)](#stage-6-oop)
9. [Stage 7: Enterprise Tools (Weeks 11-14)](#stage-7-enterprise-tools)
10. [Stage 8: Portfolio & Job Hunt (Weeks 15-16)](#stage-8-portfolio--job-hunt)
11. [Skill Assessment Checklists](#skill-assessment-checklists)
12. [D&D Themed Learning Metaphors](#dnd-themed-learning-metaphors)

---

## The Journey Overview

### Timeline: 16 Weeks (4 Months) to Job-Ready

```
Week 0:  Act 0 - Setup and basics
Weeks 1-10: Acts I-VII - Python fundamentals to advanced
Weeks 11-14: Act VIII - Enterprise professional skills
Weeks 15-16: Portfolio projects and job applications

TOTAL: ~200-300 hours of learning
```

### What "Job-Ready" Means

By the end, you'll be qualified for:
- Junior Python Developer
- Python Automation Engineer
- Junior DevOps Engineer (Python-focused)
- Entry-Level Data Analyst (with Python)
- Junior Backend Developer
- QA Automation Engineer

**Salary Range**: $50,000 - $85,000 (entry-level, varies by location)

---

## Stage 0: Pre-Python
### "What is Programming?" → "I ran my first Python program!"

**Duration**: 1-2 days (Act 0 in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] What Python is and what it's used for
- [ ] How to install Python on your operating system
- [ ] How to open and use a terminal/command prompt
- [ ] Basic terminal navigation (cd, ls/dir, pwd)
- [ ] What a text editor/IDE is
- [ ] How to create a .py file
- [ ] How to run a Python file from terminal
- [ ] How to read error messages

#### D&D Theme: "The Awakening"
*"Before you can wield the Language of Nature, you must first learn it exists."*

### Concrete Milestones

**You're ready for Stage 1 when you can:**
1. Install Python without external help
2. Open terminal and navigate to a folder
3. Create a file named `test.py`
4. Write `print("Hello, World!")` in it
5. Run it with `python test.py` and see output
6. Understand what `NameError: name 'x' is not defined` means

### Real Syntax at This Stage

```python
# You should be able to write and run this:
print("Hello, World!")
print("My name is Grixle")
print(2 + 2)
```

### Common Struggles & Solutions

**Struggle**: "Python is not recognized as a command"
**Solution**: PATH wasn't set during installation → Reinstall and check PATH box

**Struggle**: "I don't know what a 'directory' is"
**Solution**: Think of it as a folder; practice `cd` and `ls` commands

**Struggle**: "Where do I type code?"
**Solution**: In a text editor (VS Code), save as .py, then run from terminal

### Tools You'll Use
- Python 3.8+ (installed)
- Terminal/Command Prompt
- VS Code or PyCharm (recommended) or IDLE (basic)

---

## Stage 1: Python Basics
### "I can run code" → "I can do calculations and store values"

**Duration**: 1-2 weeks (Act I in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] Variables and assignment (`x = 5`)
- [ ] Data types: int, float, str, bool
- [ ] Basic operators: `+, -, *, /, //, %, **`
- [ ] String concatenation
- [ ] `print()` function
- [ ] `input()` function
- [ ] Type conversion: `int()`, `str()`, `float()`
- [ ] Comments (`#` and `'''`)
- [ ] Basic math with `math` module
- [ ] Understanding indentation importance

#### D&D Theme: "The Ancient Glyphs"
*"Learn to speak the fundamental words of the Language of Nature."*

### Concrete Milestones

**You're ready for Stage 2 when you can:**
1. Create variables and change their values
2. Get user input and convert it to numbers
3. Perform calculations with user input
4. Use f-strings to format output
5. Import and use the math module
6. Understand why indentation matters

### Real Syntax at This Stage

```python
# Calculator program you can build:
name = input("What's your name? ")
age = int(input("How old are you? "))
years_to_100 = 100 - age

print(f"Hello, {name}!")
print(f"You have {years_to_100} years until you're 100.")

# Math module usage:
import math
radius = float(input("Circle radius: "))
area = math.pi * radius ** 2
print(f"Area: {area:.2f}")
```

### Projects You Can Build
1. **Simple Calculator** - Add, subtract, multiply, divide two numbers
2. **Temperature Converter** - Celsius to Fahrenheit
3. **Age Calculator** - Calculate age in days/hours/minutes
4. **Tip Calculator** - Calculate tip and total bill

### Enterprise Connection
**Why This Matters for Jobs**: Every program uses variables, calculations, and user interaction. This is the foundation.

**Real-World Use Cases**:
- Configuration values in applications
- User input processing
- Data transformation
- Mathematical operations in data analysis

### Tools You'll Use
- Python REPL (for quick testing)
- Text editor (for writing scripts)
- Terminal (for running scripts)

---

## Stage 2: Data Structures
### "I can work with single values" → "I can manage collections of data"

**Duration**: 2 weeks (Act II in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] Lists: creation, indexing, slicing, methods
- [ ] Tuples: immutable sequences
- [ ] Sets: unique values, set operations
- [ ] Dictionaries: key-value pairs
- [ ] String methods (split, join, strip, replace, etc.)
- [ ] String formatting (f-strings, .format(), %)
- [ ] List comprehensions
- [ ] Dictionary comprehensions
- [ ] Nested data structures

#### D&D Theme: "The Tome of Collections"
*"The world is not just single values—it is LISTS of creatures, DICTIONARIES of spells, SETS of unique treasures."*

### Concrete Milestones

**You're ready for Stage 3 when you can:**
1. Create and manipulate lists (append, remove, sort)
2. Access list/string elements by index and slice
3. Use dictionaries to store structured data
4. Iterate over collections with for loops
5. Choose the right data structure for a task
6. Work with nested lists and dictionaries

### Real Syntax at This Stage

```python
# To-do list program you can build:
tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})

def complete_task(index):
    tasks[index]["completed"] = True

def show_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "○"
        print(f"{i}. [{status}] {task['name']}")

# Using it:
add_task("Learn Python")
add_task("Build a project")
show_tasks()
complete_task(0)
show_tasks()
```

### Projects You Can Build
1. **To-Do List Manager** - Add, view, complete tasks
2. **Contact Book** - Store names, phones, emails
3. **Inventory System** - Track items with quantities
4. **Word Counter** - Analyze text file, count word frequency
5. **Student Grade Tracker** - Store grades, calculate averages

### Enterprise Connection
**Why This Matters for Jobs**: Real applications work with COLLECTIONS of data—user lists, product catalogs, transaction records, log files.

**Real-World Use Cases**:
- User databases (list of dictionaries)
- API responses (JSON → dictionaries)
- Data processing pipelines
- Configuration management
- Log parsing and analysis

**Enterprise Patterns You Learn**:
```python
# Pattern: List of dictionaries (database rows)
users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"}
]

# Pattern: Nested dictionaries (configuration)
config = {
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "cache": {
        "enabled": True,
        "ttl": 300
    }
}

# Pattern: Dictionary for fast lookups
user_by_id = {user["id"]: user for user in users}
```

### Tools You'll Use
- Python REPL (experimenting with data structures)
- Text editor
- JSON files (for data storage)

---

## Stage 3: Control Flow
### "My code runs line by line" → "My code makes decisions and repeats actions"

**Duration**: 2 weeks (Act III in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] if/elif/else statements
- [ ] Comparison operators: `==, !=, <, >, <=, >=`
- [ ] Logical operators: `and, or, not`
- [ ] Membership: `in, not in`
- [ ] Identity: `is, is not`
- [ ] for loops (iterate over sequences)
- [ ] while loops (condition-based repetition)
- [ ] range() function
- [ ] break and continue
- [ ] Nested loops
- [ ] Conditional expressions (ternary operator)

#### D&D Theme: "The Branching Paths"
*"The world is not linear. You must choose your path and repeat your trials."*

### Concrete Milestones

**You're ready for Stage 4 when you can:**
1. Write if/elif/else to make decisions
2. Combine conditions with and/or
3. Use for loops to process lists
4. Use while loops for unknown iterations
5. Break out of loops when conditions are met
6. Handle nested loops for 2D data
7. Validate user input with loops

### Real Syntax at This Stage

```python
# Number guessing game you can build:
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("I'm thinking of a number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You won in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game over! The number was {secret}.")


# Password validator:
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)

    if not (has_digit and has_upper and has_lower):
        return False, "Password must have digit, uppercase, and lowercase"

    return True, "Password is valid"
```

### Projects You Can Build
1. **Number Guessing Game** - With limited attempts
2. **Rock Paper Scissors** - Best of 5 rounds
3. **Login System** - Username/password validation
4. **Quiz Game** - Multiple choice, score tracking
5. **Text Adventure** - Choose-your-own-adventure game

### Enterprise Connection
**Why This Matters for Jobs**: Business logic is ALL about conditions and loops—user permissions, data validation, batch processing.

**Real-World Use Cases**:
- Input validation (password strength, email format)
- Authentication and authorization
- Data filtering and searching
- Batch processing (process all files in directory)
- Retry logic (keep trying until success)

**Enterprise Patterns You Learn**:
```python
# Pattern: Input validation with retry
while True:
    email = input("Enter email: ")
    if "@" in email and "." in email:
        break
    print("Invalid email format. Try again.")

# Pattern: Permission checking
if user.role == "admin" or user.is_owner:
    allow_delete()
else:
    raise PermissionError("Insufficient privileges")

# Pattern: Batch processing
for file in os.listdir(directory):
    if file.endswith(".log"):
        process_log_file(file)
```

### Tools You'll Use
- Python REPL (testing conditions)
- Text editor
- Debugger (for understanding loop flow)

---

## Stage 4: Functions
### "My code is a long script" → "My code is organized, reusable, and modular"

**Duration**: 1 week (Act IV in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] Defining functions with `def`
- [ ] Parameters and arguments
- [ ] Return values
- [ ] Default parameter values
- [ ] Keyword arguments
- [ ] *args and **kwargs
- [ ] Docstrings
- [ ] Scope (local vs global)
- [ ] Lambda functions
- [ ] Functions as first-class objects
- [ ] Recursion basics

#### D&D Theme: "The Art of Incantations"
*"Spells (functions) can be invoked by name, passed ingredients (parameters), and produce magical effects (return values)."*

### Concrete Milestones

**You're ready for Stage 5 when you can:**
1. Write functions that take parameters and return values
2. Use default parameters appropriately
3. Write clear docstrings
4. Understand variable scope
5. Pass functions as arguments
6. Break large programs into functions
7. Write recursive functions for simple problems

### Real Syntax at This Stage

```python
# Well-structured calculator with functions:

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def get_number(prompt):
    """Get a valid number from user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def calculate(operation, a, b):
    """
    Perform calculation based on operation.

    Args:
        operation: String ('+', '-', '*', '/')
        a: First number
        b: Second number

    Returns:
        Result of calculation or None if invalid operation
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None
    }

    func = operations.get(operation)
    return func(a, b) if func else None

# Main program
def main():
    """Main calculator program."""
    print("Simple Calculator")

    num1 = get_number("First number: ")
    op = input("Operation (+, -, *, /): ")
    num2 = get_number("Second number: ")

    result = calculate(op, num1, num2)

    if result is not None:
        print(f"{num1} {op} {num2} = {result}")
    else:
        print("Invalid operation or division by zero")

if __name__ == "__main__":
    main()
```

### Projects You Can Build
1. **Calculator with History** - Functions for each operation
2. **Password Generator** - Configurable length, characters
3. **Text Analyzer** - Functions for different metrics
4. **Hangman Game** - Well-organized with functions
5. **Unit Converter** - Functions for each conversion

### Enterprise Connection
**Why This Matters for Jobs**: Professional code is 90% functions. Functions enable code reuse, testing, and team collaboration.

**Real-World Use Cases**:
- API endpoints (each endpoint is a function)
- Data transformation pipelines
- Business logic encapsulation
- Code reusability across projects
- Unit testing (test functions independently)

**Enterprise Patterns You Learn**:
```python
# Pattern: Single Responsibility Principle
def validate_email(email):
    """Only validates email format."""
    return "@" in email and "." in email

def send_email(to, subject, body):
    """Only handles sending."""
    if not validate_email(to):
        raise ValueError("Invalid email")
    # Send logic...

# Pattern: Factory functions
def create_user(username, email, role="user"):
    """Create user dictionary with defaults."""
    return {
        "username": username,
        "email": email,
        "role": role,
        "created_at": datetime.now()
    }

# Pattern: Higher-order functions
def apply_discount(percentage):
    """Return a function that applies a specific discount."""
    def discount_func(price):
        return price * (1 - percentage / 100)
    return discount_func

ten_percent_off = apply_discount(10)
final_price = ten_percent_off(100)  # $90
```

### Tools You'll Use
- Python REPL (testing functions)
- Text editor with function folding
- pdb debugger (step through function calls)

---

## Stage 5: Files & Modules
### "My code only works with data I type" → "My code works with files, databases, and external libraries"

**Duration**: 1 week (Act V in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] Reading files (`open()`, `read()`, `readline()`, `readlines()`)
- [ ] Writing files (text and binary)
- [ ] Context managers (`with` statement)
- [ ] CSV files (`csv` module)
- [ ] JSON files (`json` module)
- [ ] Exception handling (`try/except/finally`)
- [ ] Raising exceptions
- [ ] Creating modules
- [ ] Importing modules (`import`, `from...import`)
- [ ] `if __name__ == "__main__":`
- [ ] sys.argv (command-line arguments)

#### D&D Theme: "The Scrolls and Grimoires"
*"Knowledge must be preserved in scrolls (files) and organized in grimoires (modules)."*

### Concrete Milestones

**You're ready for Stage 6 when you can:**
1. Read and write text files with context managers
2. Parse CSV files into data structures
3. Save/load data as JSON
4. Handle file-related exceptions
5. Create your own importable modules
6. Accept command-line arguments
7. Organize code across multiple files

### Real Syntax at This Stage

```python
# File-based to-do list application:

import json
import sys
from datetime import datetime

class TodoList:
    """Persistent to-do list stored in JSON file."""

    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = self.load()

    def load(self):
        """Load tasks from JSON file."""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Warning: {self.filename} is corrupted. Starting fresh.")
            return []

    def save(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")

    def add(self, task):
        """Add a task."""
        self.tasks.append({
            "task": task,
            "created": datetime.now().isoformat(),
            "completed": False
        })
        self.save()

    def complete(self, index):
        """Mark task as complete."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save()
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks!")
            return

        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            print(f"{i}. [{status}] {task['task']}")

# Command-line interface
def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|complete] ...")
        return

    todo = TodoList()
    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        task = " ".join(sys.argv[2:])
        todo.add(task)
        print(f"Added: {task}")

    elif command == "list":
        todo.list_tasks()

    elif command == "complete" and len(sys.argv) > 2:
        try:
            index = int(sys.argv[2])
            todo.complete(index)
            print(f"Completed task {index}")
        except ValueError:
            print("Invalid task number")
        except IndexError as e:
            print(e)

    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

# Usage:
# python todo.py add "Learn Python"
# python todo.py add "Build a project"
# python todo.py list
# python todo.py complete 0
```

### Projects You Can Build
1. **Persistent To-Do List** - Save/load from JSON
2. **Log File Analyzer** - Parse and report on logs
3. **CSV Data Reporter** - Read CSV, generate reports
4. **Contact Manager** - Save contacts to file
5. **Configuration File Parser** - Read app settings

### Enterprise Connection
**Why This Matters for Jobs**: Real applications ALWAYS work with external data—files, databases, APIs, configuration.

**Real-World Use Cases**:
- Reading configuration files (JSON, YAML, .env)
- Processing data files (CSV, Excel, logs)
- Saving application state
- Data import/export
- Log generation
- Report generation

**Enterprise Patterns You Learn**:
```python
# Pattern: Configuration management
def load_config(config_file="config.json"):
    """Load application configuration."""
    try:
        with open(config_file) as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return get_default_config()

# Pattern: Robust file operations
def safe_write(filename, data):
    """Write data to file with backup."""
    backup = f"{filename}.bak"

    # Create backup if file exists
    if os.path.exists(filename):
        shutil.copy(filename, backup)

    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        # Restore backup on failure
        if os.path.exists(backup):
            shutil.copy(backup, filename)
        raise e

# Pattern: CSV processing
def process_csv_report(input_file, output_file):
    """Process CSV and generate report."""
    with open(input_file) as infile, \
         open(output_file, 'w') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=['summary'])

        for row in reader:
            # Process each row...
            pass
```

### Tools You'll Use
- Text editor with file explorer
- Terminal (for command-line programs)
- JSON viewer (browser or extension)
- CSV editor (Excel, LibreOffice)

---

## Stage 6: OOP
### "My code uses functions" → "My code models real-world objects and relationships"

**Duration**: 2 weeks (Act VI in The Verdant Code)

### What You Learn

#### Technical Skills
- [ ] Classes and objects
- [ ] `__init__` constructor
- [ ] Instance variables and methods
- [ ] Class variables and methods
- [ ] Inheritance
- [ ] Method overriding
- [ ] super()
- [ ] Special methods (`__str__`, `__repr__`, etc.)
- [ ] Properties (`@property`)
- [ ] Composition vs inheritance
- [ ] Abstract base classes

#### D&D Theme: "The Living Constructs"
*"Objects are not just data—they are living constructs with behaviors, relationships, and identities."*

### Concrete Milestones

**You're ready for Stage 7 when you can:**
1. Create classes with attributes and methods
2. Use inheritance to model relationships
3. Understand when to use composition vs inheritance
4. Implement special methods for custom behavior
5. Use properties for controlled attribute access
6. Design class hierarchies
7. Write object-oriented programs

### Real Syntax at This Stage

```python
# RPG Character system with OOP:

class Character:
    """Base class for all game characters."""

    # Class variable (shared by all instances)
    character_count = 0

    def __init__(self, name, health=100):
        """Initialize character."""
        self.name = name
        self.health = health
        self.max_health = health
        Character.character_count += 1

    def take_damage(self, amount):
        """Reduce health by amount."""
        self.health = max(0, self.health - amount)
        if self.health == 0:
            print(f"{self.name} has fallen!")

    def heal(self, amount):
        """Restore health up to max."""
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self):
        """Check if character is alive."""
        return self.health > 0

    def __str__(self):
        """String representation for players."""
        return f"{self.name} ({self.health}/{self.max_health} HP)"

    def __repr__(self):
        """String representation for developers."""
        return f"Character(name='{self.name}', health={self.health})"


class Player(Character):
    """Player character with inventory."""

    def __init__(self, name, health=100, player_class="Warrior"):
        super().__init__(name, health)
        self.player_class = player_class
        self.inventory = []
        self.level = 1
        self.xp = 0

    def add_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"{self.name} acquired {item}!")

    def gain_xp(self, amount):
        """Gain experience and possibly level up."""
        self.xp += amount
        xp_needed = self.level * 100

        if self.xp >= xp_needed:
            self.level_up()

    def level_up(self):
        """Increase level and stats."""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        print(f"{self.name} reached level {self.level}!")

    def __str__(self):
        return f"{self.name} (Lv{self.level} {self.player_class}) - {self.health}/{self.max_health} HP"


class Enemy(Character):
    """Enemy character with reward."""

    def __init__(self, name, health, xp_reward):
        super().__init__(name, health)
        self.xp_reward = xp_reward

    def drop_loot(self):
        """Return loot when defeated."""
        import random
        loot = ["Potion", "Gold Coin", "Dragon Scale", "Ancient Scroll"]
        return random.choice(loot)


# Using the classes:
def battle(player, enemy):
    """Simple battle system."""
    print(f"\n{player} encounters {enemy}!")

    while player.is_alive() and enemy.is_alive():
        # Player attacks
        damage = 20
        enemy.take_damage(damage)
        print(f"{player.name} deals {damage} damage!")

        if not enemy.is_alive():
            print(f"{enemy.name} defeated!")
            player.gain_xp(enemy.xp_reward)
            loot = enemy.drop_loot()
            player.add_item(loot)
            break

        # Enemy attacks
        damage = 15
        player.take_damage(damage)
        print(f"{enemy.name} deals {damage} damage!")

        print(f"{player} | {enemy}\n")
        input("Press Enter to continue...")

    if not player.is_alive():
        print("Game Over!")


# Game
player = Player("Grixle", health=150, player_class="Druid")
enemy = Enemy("Iron Wyrm", health=100, xp_reward=50)

battle(player, enemy)
```

### Projects You Can Build
1. **RPG Character System** - Classes for different character types
2. **Bank Account Simulator** - Account, SavingsAccount, CheckingAccount
3. **Library Management** - Book, Member, Library classes
4. **Task Management** - Task, Project, Team classes
5. **Pet Simulator** - Different pet types with behaviors

### Enterprise Connection
**Why This Matters for Jobs**: Enterprise software is BUILT on OOP—APIs, frameworks, databases, everything uses objects.

**Real-World Use Cases**:
- Web frameworks (Django models, Flask-SQLAlchemy)
- API clients (requests library uses OOP)
- Database ORMs (object-relational mapping)
- GUI applications (Tkinter, PyQt)
- Game development

**Enterprise Patterns You Learn**:
```python
# Pattern: Model-View-Controller (simplified)
class User:
    """Model: Represents user data."""
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        """Save to database."""
        db.execute("INSERT INTO users ...")

class UserView:
    """View: Handles display."""
    @staticmethod
    def show_user(user):
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")

class UserController:
    """Controller: Handles logic."""
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_email(self, new_email):
        self.model.email = new_email
        self.model.save()
        self.view.show_user(self.model)


# Pattern: Repository pattern
class UserRepository:
    """Handles user data access."""
    def __init__(self, database):
        self.db = database

    def get_by_id(self, user_id):
        """Retrieve user by ID."""
        data = self.db.query("SELECT * FROM users WHERE id=?", user_id)
        return User(**data) if data else None

    def save(self, user):
        """Persist user."""
        self.db.execute("UPDATE users SET ...", user)


# Pattern: Factory pattern
class CharacterFactory:
    """Create different character types."""
    @staticmethod
    def create(char_type, name):
        if char_type == "warrior":
            return Warrior(name, health=150, strength=20)
        elif char_type == "mage":
            return Mage(name, health=80, mana=100)
        elif char_type == "rogue":
            return Rogue(name, health=100, agility=25)
        else:
            raise ValueError(f"Unknown character type: {char_type}")
```

### Tools You'll Use
- Text editor with class/method navigation
- UML diagram tools (understanding class relationships)
- pdb debugger (inspecting object state)

---

## Stage 7: Enterprise Tools
### "I can write Python" → "I can work on professional development teams"

**Duration**: 4 weeks (Act VIII in The Verdant Code)

This is WHERE THE GAME CURRENTLY FALLS SHORT. These skills are MANDATORY for jobs but not taught.

### What You Learn

#### Week 11: Version Control & Environment Management
- [ ] **Git Basics**
  - Initializing repositories
  - Staging and committing
  - Viewing history
  - .gitignore files
  - Basic workflow

- [ ] **Git Branching & Collaboration**
  - Creating and merging branches
  - Resolving conflicts
  - Pull requests
  - GitHub workflow

- [ ] **Virtual Environments**
  - Creating venv
  - Activating/deactivating
  - Why isolation matters
  - Best practices

- [ ] **Package Management**
  - pip install
  - requirements.txt
  - Finding packages on PyPI
  - Dependency management

#### Week 12: Testing & Debugging
- [ ] **Unit Testing with pytest**
  - Writing test functions
  - Assertions
  - Test organization
  - Running test suites
  - Test coverage

- [ ] **Test-Driven Development (TDD)**
  - Write test first
  - Implement code
  - Refactor
  - Red-Green-Refactor cycle

- [ ] **Debugging with pdb**
  - Setting breakpoints
  - Stepping through code
  - Inspecting variables
  - Post-mortem debugging

- [ ] **IDE Debugging**
  - VS Code debugger
  - PyCharm debugger
  - Watch expressions

#### Week 13: Code Quality & Documentation
- [ ] **PEP 8 Style Guide**
  - Naming conventions
  - Indentation and spacing
  - Line length
  - Import organization

- [ ] **Code Formatting**
  - Black auto-formatter
  - Linters (pylint, flake8)
  - Pre-commit hooks

- [ ] **Documentation**
  - Writing docstrings
  - Google/NumPy style
  - Type hints
  - README files
  - API documentation

- [ ] **Logging**
  - logging module
  - Log levels
  - Log formatting
  - Log rotation

#### Week 14: Project Structure & Professional Practices
- [ ] **Project Organization**
  - Package structure
  - `__init__.py` files
  - setup.py / pyproject.toml
  - Installable packages

- [ ] **Configuration Management**
  - Environment variables
  - .env files
  - python-dotenv
  - Config files (JSON, YAML)

- [ ] **Command-Line Tools**
  - argparse module
  - Creating CLI apps
  - Help messages
  - Subcommands

- [ ] **CI/CD Basics**
  - GitHub Actions
  - Automated testing
  - Deployment basics
  - Pre-commit hooks

### D&D Theme: "The Forge of Mastery"
*"Learn the ways of the professional craftsdwarves—the tools and practices that separate apprentices from masters."*

### Concrete Milestones

**You're enterprise-ready when you can:**

1. **Version Control** ✓
   - [ ] Create Git repository for new project
   - [ ] Make meaningful commits with good messages
   - [ ] Create and merge branches
   - [ ] Resolve merge conflicts
   - [ ] Use GitHub for collaboration
   - [ ] Have GitHub profile with projects

2. **Environment Management** ✓
   - [ ] Create virtual environment for each project
   - [ ] Generate requirements.txt
   - [ ] Install dependencies from requirements.txt
   - [ ] Explain why virtual environments matter

3. **Testing** ✓
   - [ ] Write unit tests for functions
   - [ ] Achieve 70%+ code coverage
   - [ ] Practice TDD (write test first)
   - [ ] Run test suites automatically

4. **Debugging** ✓
   - [ ] Use pdb to find bugs
   - [ ] Set breakpoints and inspect variables
   - [ ] Debug in IDE
   - [ ] Read stack traces efficiently

5. **Code Quality** ✓
   - [ ] Follow PEP 8 style guide
   - [ ] Use Black to format code
   - [ ] Pass linter checks (pylint/flake8)
   - [ ] Write clear docstrings

6. **Project Structure** ✓
   - [ ] Organize code into packages
   - [ ] Create installable packages
   - [ ] Write comprehensive README
   - [ ] Proper .gitignore

7. **Professional Practices** ✓
   - [ ] Use logging instead of print()
   - [ ] Manage secrets with .env
   - [ ] Create CLI tools with argparse
   - [ ] Set up basic CI/CD

### Real Syntax at This Stage

```bash
# Week 11: Git & Environment Setup
# =================================

# Create project
mkdir my_awesome_project
cd my_awesome_project

# Initialize Git
git init
git config user.name "Your Name"
git config user.email "you@example.com"

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install packages
pip install requests pytest black

# Save dependencies
pip freeze > requirements.txt

# Create .gitignore
echo "__pycache__/
*.pyc
venv/
.env" > .gitignore

# First commit
git add .
git commit -m "Initial project setup with venv and dependencies"

# Create GitHub repo (on GitHub.com)
# Link and push
git remote add origin https://github.com/yourusername/my_awesome_project.git
git push -u origin main


# Week 12: Testing
# =================================

# project structure:
# my_project/
#   calculator.py
#   test_calculator.py

# calculator.py
def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Run tests
pytest test_calculator.py -v

# With coverage
pytest --cov=calculator test_calculator.py


# Week 13: Code Quality
# =================================

# Format with Black
black calculator.py

# Check style
pylint calculator.py
flake8 calculator.py

# Add docstrings with type hints
def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b

# Use logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.error("An error occurred")


# Week 14: Professional Structure
# =================================

# Project structure:
my_package/
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── tests/
│   ├── test_core.py
│   └── test_utils.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── .github/
    └── workflows/
        └── tests.yml

# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
)

# Install in development mode
pip install -e .

# Now can import anywhere:
from my_package import core

# CLI tool with argparse
import argparse

def main():
    parser = argparse.ArgumentParser(description='My awesome tool')
    parser.add_argument('command', choices=['run', 'test', 'build'])
    parser.add_argument('--verbose', '-v', action='store_true')

    args = parser.parse_args()

    if args.command == 'run':
        run_app(verbose=args.verbose)

if __name__ == "__main__":
    main()


# GitHub Actions (.github/workflows/tests.yml)
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.11
      - run: pip install -r requirements.txt
      - run: pytest --cov=my_package
      - run: black --check .
      - run: pylint my_package
```

### Projects You Can Build
1. **Tested Python Package** - Installable package with full test suite
2. **CLI Tool** - Command-line utility with argparse
3. **Automated Testing Pipeline** - GitHub Actions setup
4. **Professional Project** - Demonstrates all enterprise practices

### Enterprise Connection
**THIS IS THE BRIDGE TO EMPLOYMENT**

Without these skills, you CANNOT:
- Work on any development team (Git required)
- Collaborate on code (Git, testing required)
- Deploy professional applications (CI/CD required)
- Pass technical interviews (testing, debugging required)
- Build portfolio that impresses employers

With these skills:
- ✓ Can join any Python team immediately
- ✓ Can contribute to open source
- ✓ Have impressive GitHub portfolio
- ✓ Pass technical interviews confidently
- ✓ Command higher salary

**Real Interview Questions**:
- "Show me your GitHub profile" → Need Git skills
- "How do you test your code?" → Need pytest skills
- "Walk me through your development workflow" → Need Git, venv, testing
- "How do you ensure code quality?" → Need linting, formatting, testing
- "Describe a time you debugged a complex issue" → Need debugging skills

### Tools You'll Use
- Git and GitHub
- VS Code or PyCharm
- pytest
- Black, pylint, flake8
- GitHub Actions
- pdb debugger

---

## Stage 8: Portfolio & Job Hunt
### "I can write professional code" → "I have job offers"

**Duration**: 2 weeks

### What You Do

#### Week 15: Build Portfolio
- [ ] **GitHub Profile Setup**
  - Professional README.md
  - Pin best projects
  - Contribution graph (green squares!)
  - Bio and links

- [ ] **Portfolio Projects (3-5 projects)**
  - Web scraper with API
  - CLI tool
  - Data analysis script
  - Automation tool
  - Game or creative project

- [ ] **Project Documentation**
  - README for each project
  - Clear installation instructions
  - Usage examples
  - Screenshots/GIFs
  - What you learned

- [ ] **Blog Posts (Optional but Valuable)**
  - Write about learning journey
  - Technical tutorials
  - Project breakdowns
  - Share on dev.to, Medium

#### Week 16: Job Applications
- [ ] **Resume Update**
  - Add Python skills section
  - Add projects section (link to GitHub)
  - Add relevant coursework/certifications
  - Quantify achievements

- [ ] **LinkedIn Profile**
  - Update headline ("Python Developer")
  - Add skills (Python, Git, pytest, etc.)
  - Add projects with links
  - Connect with Python developers

- [ ] **Job Search**
  - Entry-level Python roles
  - Junior Backend Developer
  - Python Automation Engineer
  - DevOps Engineer (Python)
  - Data Analyst (Python)

- [ ] **Interview Prep**
  - Practice coding challenges (LeetCode Easy/Medium)
  - Prepare to explain your projects
  - Practice technical questions
  - Behavioral interview prep

### Concrete Milestones

**You're ready to apply when you have:**
1. GitHub profile with 5+ projects
2. At least 2 projects with tests
3. Resume showcasing Python skills
4. LinkedIn profile
5. Can explain your projects confidently
6. Can solve basic coding challenges

### Example Portfolio Projects

**Project 1: Web Scraper**
```
GitHub: username/news-scraper
• Scrapes news articles from multiple sites
• Stores in SQLite database
• CLI interface
• Scheduled execution
• 80% test coverage
Technologies: requests, BeautifulSoup, sqlite3, pytest
```

**Project 2: CLI Task Manager**
```
GitHub: username/taskmaster-cli
• Command-line task management tool
• JSON persistence
• Categories and priorities
• Colored output
• Installable package
Technologies: argparse, colorama, pytest
```

**Project 3: Data Analysis**
```
GitHub: username/covid-data-analysis
• Analyzes COVID data from public API
• Generates visualizations
• Exports reports to CSV
• Jupyter notebook included
Technologies: pandas, matplotlib, requests
```

**Project 4: Automation Script**
```
GitHub: username/backup-automation
• Automated backup system
• Configurable via .env
• Logging and error handling
• Email notifications
• GitHub Actions for scheduling
Technologies: shutil, smtplib, schedule
```

**Project 5: Game or Creative**
```
GitHub: username/python-roguelike
• Terminal-based roguelike game
• Object-oriented design
• Save/load system
• ASCII graphics
Technologies: Python standard library
```

### Example Resume Section

```
SKILLS
======
Languages: Python, SQL
Tools: Git, GitHub, VS Code, pytest
Frameworks: Flask (basic), SQLAlchemy
Other: Linux, Docker (basic), CI/CD

PROJECTS
========
News Scraper (Python)
• Automated web scraping tool collecting articles from 5+ news sources
• Implemented with requests and BeautifulSoup, storing data in SQLite
• Achieved 80% test coverage using pytest
• GitHub: github.com/username/news-scraper

CLI Task Manager (Python)
• Command-line productivity tool with JSON persistence
• Published as installable package on PyPI (500+ downloads)
• Implemented argparse for intuitive CLI interface
• GitHub: github.com/username/taskmaster-cli

COVID Data Analyzer (Python)
• Data analysis tool processing public health data
• Generated visualizations using matplotlib and pandas
• Automated daily reports with GitHub Actions
• GitHub: github.com/username/covid-data-analysis
```

### Example LinkedIn Headline

Before:
```
"Student at University"
```

After:
```
"Python Developer | Building automation tools and web scrapers |
Open source contributor | Passionate about clean code"
```

### Job Application Strategy

**Where to Apply**:
- Indeed (filter: "Entry Level Python")
- LinkedIn Jobs
- AngelList (startups)
- We Work Remotely (remote jobs)
- Python.org job board
- Company career pages directly

**Application Formula**:
1. Tailor resume to job description (match keywords)
2. Write cover letter mentioning specific projects
3. Apply to 10-20 jobs per week
4. Follow up after 1 week
5. Track applications in spreadsheet

**Interview Prep**:
- LeetCode Easy problems (arrays, strings, hashmaps)
- Explain projects in detail
- Practice: "Walk me through your code"
- Behavioral questions (STAR method)
- System design basics (for some interviews)

---

## Skill Assessment Checklists

### Beginner Assessment (After Stage 1-2)
```
□ Can install and run Python
□ Can use terminal to navigate and run scripts
□ Understands variables, types, and operators
□ Can use lists and dictionaries
□ Can write for and while loops
□ Can use if/elif/else statements
□ Can debug simple errors by reading tracebacks

VERDICT: Can build simple scripts
```

### Intermediate Assessment (After Stage 3-4)
```
□ Can write functions with parameters and return values
□ Understands variable scope
□ Can work with files (read/write)
□ Can parse CSV and JSON
□ Can handle exceptions properly
□ Can create and import modules
□ Can accept command-line arguments

VERDICT: Can build complete programs
```

### Advanced Assessment (After Stage 5-6)
```
□ Can design classes with proper encapsulation
□ Understands inheritance and composition
□ Can implement special methods (__str__, etc.)
□ Can organize code into packages
□ Comfortable with Python's standard library
□ Can read and understand others' code
□ Can refactor code for clarity

VERDICT: Can build professional applications
```

### Job-Ready Assessment (After Stage 7-8)
```
□ Uses Git for version control on every project
□ Creates virtual environments automatically
□ Writes tests (70%+ coverage) for all code
□ Follows PEP 8 style consistently
□ Uses logging instead of print()
□ Documents code with docstrings and type hints
□ Has GitHub profile with quality projects
□ Can debug efficiently with pdb or IDE
□ Understands CI/CD basics
□ Can build CLI tools with argparse
□ Manages configuration properly (.env)
□ Has deployed at least one project

VERDICT: Ready for junior developer roles
```

---

## D&D Themed Learning Metaphors

### Why D&D Themes Work for Programming

Programming concepts map beautifully to D&D:

| Programming Concept | D&D Metaphor | Why It Works |
|---------------------|--------------|--------------|
| Variables | Spell components | Both store values/ingredients |
| Functions | Spells/abilities | Both perform actions when invoked |
| Classes | Character classes | Both define types with behaviors |
| Objects | Characters/creatures | Both are instances with state |
| Inheritance | Class archetypes | Both inherit traits from parents |
| Modules | Spell schools | Both organize related functionality |
| Git commits | Save points | Both preserve state in time |
| Branches | Parallel timelines | Both allow experimentation |
| Testing | Trials/validation | Both prove something works |
| Debugging | Divination | Both reveal hidden truth |
| Virtual envs | Pocket dimensions | Both provide isolation |
| Packages | Spell libraries | Both provide reusable functionality |

### Complete Metaphor System

**ACT 0: THE AWAKENING**
- "Summoning Ritual" = Installing Python
- "Command Portal" = Terminal
- "Scribe's Tools" = Text editor/IDE
- "Oracle's Warnings" = Error messages

**ACT I-VII: THE LANGUAGE OF NATURE**
- "Ancient Glyphs" = Basic syntax
- "Tome of Collections" = Data structures
- "Branching Paths" = Control flow
- "Art of Incantations" = Functions
- "Scrolls and Grimoires" = Files and modules
- "Living Constructs" = Objects
- "Grand Algorithm" = Algorithms

**ACT VIII: THE FORGE OF MASTERY**
- "Repository of Time" = Git version control
- "Parallel Timelines" = Git branches
- "Isolated Spell Chambers" = Virtual environments
- "Great Library" = PyPI and pip
- "Trials of Validation" = Unit testing
- "Divination Chamber" = Debugging (pdb)
- "Scroll of Style" = PEP 8
- "Codex of Clarity" = Documentation
- "Sanctum of Organization" = Project structure
- "Chronicle Stone" = Logging
- "Hidden Vault" = Environment variables
- "Continuous Ritual" = CI/CD

### Example Narrative Integration

Instead of:
```
"Learn to use Git for version control."
```

Say:
```
"Welcome to the Repository of Time, young apprentice. Here, every
moment of your code's history is preserved. You can travel back to
any previous state, create parallel timelines to experiment safely,
and merge realities when your experiments succeed. This is time
magic—the power to never lose work, to collaborate with others
across space and time, and to show your journey to future employers."
```

This makes it MEMORABLE and MEANINGFUL.

---

## Success Metrics

### How to Know You're on Track

**Week 2**: Should be able to write calculator script
**Week 4**: Should be able to build to-do list
**Week 6**: Should be comfortable with functions
**Week 8**: Should be able to read/write files
**Week 10**: Should be comfortable with classes
**Week 12**: Should have Git repo with tests
**Week 14**: Should have clean, documented code
**Week 16**: Should have portfolio and be applying

### Red Flags (You Need to Slow Down)

- Can't explain what you wrote yesterday
- Copy-pasting without understanding
- Skipping challenges/projects
- Not practicing between lessons
- Still using print() debugging in Week 12
- No Git commits

### Green Flags (You're Crushing It)

- Building projects beyond assignments
- Reading documentation comfortably
- Helping others in communities
- Refactoring old code for practice
- Contributing to open source
- Excited about new concepts

---

## Conclusion: The Complete Path

**This roadmap transforms**:
- "What is Python?" (Day 0)
- → "I can build scripts" (Week 4)
- → "I can build applications" (Week 10)
- → "I can work on professional teams" (Week 14)
- → "I have job interviews scheduled" (Week 16)

**The key difference from typical courses**:
We don't stop at "I can write Python." We continue to "I can work professionally with Python."

**The D&D theme keeps you engaged** through concepts that would otherwise be dry (Git, testing, PEP 8).

**Real syntax at every stage** ensures transferability to actual jobs.

**Projects build your portfolio** as you learn.

**By Week 16, you're not just educated—you're EMPLOYABLE.**

---

**End of Enterprise Skills Roadmap**

*Next: See BEGINNER_ONBOARDING.md for detailed first-day setup guide*
