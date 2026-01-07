# The Verdant Code v1.1.6 - Proposed Lessons
## New Content Designs with D&D Themes Teaching Real Syntax

**Document Purpose**: Detailed lesson designs for Act 0 and Act VIII
**Target**: Complete beginners → Enterprise-ready developers

---

## Table of Contents

1. [Act 0: The Awakening](#act-0-the-awakening) (Pre-Python Setup)
2. [Act VIII: The Forge of Mastery](#act-viii-the-forge-of-mastery) (Enterprise Skills)
3. [Real-World Projects](#real-world-projects) (Practical Applications)
4. [Supplemental Lessons](#supplemental-lessons) (Enhancements)

---

# Act 0: The Awakening
## *"Before you can wield the Language of Nature, you must first wake to its existence."*

### Act 0 Introduction

```
═══════════════════════════════════════════════════════════════════════════
                          ACT 0: THE AWAKENING
                    The Journey Before the Journey
═══════════════════════════════════════════════════════════════════════════

You stand at the threshold of a great adventure. Before you can learn the
Language of Nature, before you can master the ancient glyphs, you must first
prepare yourself.

This is the path of preparation. You will:
  • Discover what Python is and why it matters
  • Summon Python to your realm (installation)
  • Learn to speak through the Command Portal (terminal)
  • Acquire the Scribe's Tools (text editor)
  • Cast your first spell (Hello, World!)
  • Learn to read the Oracle's warnings (error messages)

Think of this as your training before joining the druid's grove. Elder
Willowbyte cannot teach you the Language of Nature if you don't yet have
the basic tools to practice it.

Take your time. This foundation will support everything that follows.
```

---

## Lesson 0.1: The Call to Adventure - What is Python?

### Lesson ID: `act0_what_is_python`
### Duration: 10 minutes (reading)
### Type: Informational (no code challenge)

### Teaching Content

```python
class WhatIsPythonLesson(Lesson):
    """Introduction to Python and programming"""

    def teach(self):
        print("""
═══════════════════════════════════════════════════════════════════════════
                    LESSON: THE CALL TO ADVENTURE
                          What is Python?
═══════════════════════════════════════════════════════════════════════════

Elder Willowbyte appears before you, ancient and wise:

'Before we begin, you must understand: What IS the Language of Nature?
What mortals call "Python" is more than mere words on parchment. It is
a language that allows you to speak to machines, to command them, to
create worlds from pure thought.'


WHAT IS PROGRAMMING?
═══════════════════════════════════════════════════════════════════════════

Programming is giving instructions to a computer. Like teaching a very
literal apprentice:

  You: "Bring me the dragon scale from the chest."
  Computer: "Which chest? Where? How do I open it? What is a dragon scale?"

You must be PRECISE. But once trained, your computer apprentice never
forgets, never tires, and executes your commands instantly.


WHAT IS PYTHON?
═══════════════════════════════════════════════════════════════════════════

Python is a PROGRAMMING LANGUAGE - a way to write instructions that
computers understand. It was created in 1991 by Guido van Rossum.

Think of it like Common (the language adventurers speak):
  • English - for humans to communicate
  • Python - for humans to communicate with computers

Python is special because it's:
  ✓ READABLE - Looks almost like English
  ✓ BEGINNER-FRIENDLY - Forgiving and clear error messages
  ✓ POWERFUL - Can build anything from games to AI
  ✓ POPULAR - Millions of developers, huge community


WHAT CAN YOU BUILD WITH PYTHON?
═══════════════════════════════════════════════════════════════════════════

1. WEB APPLICATIONS
   • Instagram, Spotify, YouTube, Netflix (all use Python!)
   • Your own website or web app

2. DATA SCIENCE & AI
   • Analyze data like a wizard scrying patterns
   • Machine learning (teach computers to learn)
   • Scientific computing

3. AUTOMATION & SCRIPTING
   • Automate boring tasks (like a magical servant)
   • System administration
   • File processing

4. CYBERSECURITY
   • Penetration testing tools
   • Security automation
   • Network analysis

5. GAME DEVELOPMENT
   • 2D games (like this one!)
   • Game logic and AI
   • Modding tools

6. CAREER PATHS - Where can Python take you?
   • Software Developer ($70k-$120k+)
   • Data Scientist ($90k-$150k+)
   • DevOps Engineer ($80k-$130k+)
   • Security Analyst ($75k-$125k+)
   • Automation Engineer ($70k-$115k+)


PYTHON VS. OTHER LANGUAGES
═══════════════════════════════════════════════════════════════════════════

Like choosing your adventuring class:

PYTHON (Druid - Versatile, Nature-Friendly)
  • Easy to learn, reads like English
  • Great for beginners, data science, automation
  • Slightly slower execution
  • BEST FIRST LANGUAGE

JavaScript (Bard - Web-Focused)
  • Required for web browsers
  • Runs in browsers and servers (Node.js)
  • Essential for web development

Java (Paladin - Structured, Enterprise)
  • Very popular in corporate environments
  • More verbose, stricter rules
  • Android development

C++ (Barbarian - Fast, Powerful, Dangerous)
  • Very fast, complete control
  • Complex, easy to make critical errors
  • Game engines, systems programming

Why Python FIRST? It teaches programming concepts clearly, then you can
learn other languages faster (like learning Common before Elvish).


WHAT YOU'LL LEARN IN THIS GAME
═══════════════════════════════════════════════════════════════════════════

By the end of The Verdant Code, you'll be able to:

✓ Write Python programs from scratch
✓ Work with data (lists, dictionaries, files)
✓ Build web scrapers and automation tools
✓ Create databases and query them
✓ Write network programs
✓ Build object-oriented applications
✓ Use Git version control
✓ Write tests for your code
✓ Debug professional code
✓ Work on development teams

You'll go from "What is a terminal?" to "I can build that."


THE JOURNEY AHEAD
═══════════════════════════════════════════════════════════════════════════

Act 0: Learn to set up your tools
Acts I-VII: Master Python from basics to advanced
Act VIII: Learn professional development practices

Expected Timeline:
  • Casual pace: 3-6 months
  • Focused pace: 1-2 months
  • Intense pace: 2-4 weeks

This is a marathon, not a sprint. Every expert was once a beginner.


Elder Willowbyte concludes:

'The path is long, young one, but every master of the Language began where
you stand now. Python is not just a skill—it is a way of thinking, of
solving problems, of creating from nothing.

Are you ready to begin?'
        """)

    def challenge(self):
        """Simple comprehension check"""
        print("""
═══════════════════════════════════════════════════════════════════════════
                              REFLECTION
═══════════════════════════════════════════════════════════════════════════

Before we continue, let's reflect:

Question: What excites you most about learning Python?

(This is just for you - type anything, then press Enter)
        """)

        response = input("Your answer: ").strip()

        print(f"""
'{response}'

Excellent! Keep that excitement burning. It will fuel your journey through
the challenges ahead.

Remember: Every line of code you write is progress. Every error is a lesson.
Every program you build is proof of your growing power.

Let's continue...
        """)

        input("\n[Press Enter to continue to the next lesson...]")
        return True
```

---

## Lesson 0.2: The Installation Ritual - Installing Python

### Lesson ID: `act0_installing_python`
### Duration: 20-30 minutes (hands-on)
### Type: Guided tutorial with verification

### Teaching Content

```python
class InstallingPythonLesson(Lesson):
    """Guide students through Python installation"""

    def teach(self):
        import sys
        import platform

        current_os = platform.system()

        print("""
═══════════════════════════════════════════════════════════════════════════
                    LESSON: THE INSTALLATION RITUAL
                          Installing Python
═══════════════════════════════════════════════════════════════════════════

Elder Willowbyte gestures to an empty pedestal:

'Before you can wield the Language of Nature, you must first SUMMON it to
your realm. This is the Installation Ritual - binding Python to your
machine so you may call upon it whenever needed.'
        """)

        print(f"\nDetected Operating System: {current_os}")
        print(f"Current Python Version: {sys.version}")

        if current_os == "Windows":
            self.teach_windows()
        elif current_os == "Darwin":  # macOS
            self.teach_macos()
        elif current_os == "Linux":
            self.teach_linux()
        else:
            self.teach_generic()

        self.teach_verification()

    def teach_windows(self):
        print("""

INSTALLING PYTHON ON WINDOWS
═══════════════════════════════════════════════════════════════════════════

STEP 1: DOWNLOAD PYTHON
────────────────────────────────────────────────────────────────────────────
1. Open your web browser
2. Go to: https://www.python.org/downloads/
3. Click the big yellow button: "Download Python 3.12.x"
   (Version number may be different - that's fine!)
4. Save the file (python-3.12.x.exe or similar)


STEP 2: RUN THE INSTALLER
────────────────────────────────────────────────────────────────────────────
1. Find the downloaded file (usually in Downloads folder)
2. Double-click python-3.12.x.exe
3. **CRITICAL**: Check the box "Add Python to PATH"

   ┌────────────────────────────────────────┐
   │ [✓] Add Python to PATH                 │  ← CHECK THIS BOX!
   │                                        │
   │ [ Install Now ]  [ Customize ]        │
   └────────────────────────────────────────┘

   This checkbox is ESSENTIAL. If you forget it, Python won't work
   from the command line!

4. Click "Install Now"
5. Wait for installation (1-2 minutes)
6. Click "Close" when finished


STEP 3: VERIFY THE INSTALLATION
────────────────────────────────────────────────────────────────────────────
1. Press Windows Key + R
2. Type: cmd
3. Press Enter (opens Command Prompt - black window)
4. Type: python --version
5. Press Enter

You should see: Python 3.12.x (or whatever version you installed)


TROUBLESHOOTING WINDOWS
────────────────────────────────────────────────────────────────────────────

❌ ERROR: "python is not recognized as an internal or external command"

CAUSE: Python wasn't added to PATH (you forgot to check the box!)

SOLUTION:
  Option 1 (Easy): Uninstall Python and reinstall, checking the PATH box
  Option 2 (Advanced): Manually add Python to PATH
    1. Search for "Environment Variables" in Start Menu
    2. Click "Edit the system environment variables"
    3. Click "Environment Variables" button
    4. Under "System variables", find "Path", click "Edit"
    5. Click "New" and add: C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python312
    6. Click "New" and add: C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python312\\Scripts
    7. Click OK on all dialogs
    8. Close and reopen Command Prompt
    9. Try "python --version" again


❌ ERROR: Nothing happens when I type "python --version"

SOLUTION:
  • Make sure you pressed Enter
  • Try: python3 --version
  • Try: py --version
  • Restart your computer and try again


IF ALL ELSE FAILS:
  • Uninstall Python completely
  • Restart computer
  • Download fresh installer from python.org
  • Run as Administrator (right-click → Run as administrator)
  • CHECK THE PATH BOX
  • Install again
        """)

    def teach_macos(self):
        print("""

INSTALLING PYTHON ON macOS
═══════════════════════════════════════════════════════════════════════════

IMPORTANT: macOS comes with Python 2.7 pre-installed. This is OLD and
deprecated. You need Python 3.8+!


METHOD 1: PYTHON.ORG (Recommended for Beginners)
────────────────────────────────────────────────────────────────────────────
1. Open Safari or your preferred browser
2. Go to: https://www.python.org/downloads/
3. Click "Download Python 3.12.x"
4. Open the downloaded .pkg file
5. Follow the installer (click Continue, Agree, Install)
6. Enter your password when prompted
7. Click "Close" when finished


METHOD 2: HOMEBREW (For Advanced Users)
────────────────────────────────────────────────────────────────────────────
If you have Homebrew installed:

1. Open Terminal (Cmd + Space, type "Terminal")
2. Type: brew install python3
3. Wait for installation


STEP 3: VERIFY THE INSTALLATION
────────────────────────────────────────────────────────────────────────────
1. Open Terminal (Cmd + Space, type "Terminal", press Enter)
2. Type: python3 --version
3. Press Enter

You should see: Python 3.12.x


IMPORTANT: macOS Python Commands
────────────────────────────────────────────────────────────────────────────
• python  → Old Python 2.7 (DON'T USE)
• python3 → New Python 3.x (USE THIS)

When running Python files:
  ✓ CORRECT: python3 my_script.py
  ❌ WRONG:   python my_script.py  (might use Python 2)


TROUBLESHOOTING macOS
────────────────────────────────────────────────────────────────────────────

❌ ERROR: "command not found: python3"

SOLUTION:
  • Make sure installation completed successfully
  • Try closing and reopening Terminal
  • Try: /usr/local/bin/python3 --version
  • Reinstall from python.org


❌ ERROR: Shows Python 2.7.x when I type "python3 --version"

SOLUTION:
  • This shouldn't happen, but if it does:
  • Check what python3 points to: which python3
  • Reinstall Python 3 from python.org
  • Make sure you're typing python3, not python


SETTING UP AN ALIAS (OPTIONAL)
────────────────────────────────────────────────────────────────────────────
To use "python" instead of "python3":

1. Open Terminal
2. Type: nano ~/.zshrc (or ~/.bash_profile for older macOS)
3. Add this line: alias python=python3
4. Press Ctrl + O, Enter, Ctrl + X
5. Type: source ~/.zshrc
6. Now "python --version" will use Python 3
        """)

    def teach_linux(self):
        print("""

INSTALLING PYTHON ON LINUX
═══════════════════════════════════════════════════════════════════════════

Good news: Most Linux distributions come with Python 3 pre-installed!

Let's check first, then install if needed.


STEP 1: CHECK IF PYTHON 3 IS INSTALLED
────────────────────────────────────────────────────────────────────────────
1. Open Terminal (Ctrl + Alt + T)
2. Type: python3 --version
3. Press Enter

If you see "Python 3.8" or higher → YOU'RE DONE! Skip to verification.
If you see "command not found" → Continue to installation.


UBUNTU/DEBIAN INSTALLATION
────────────────────────────────────────────────────────────────────────────
sudo apt update
sudo apt install python3 python3-pip python3-venv


FEDORA/RHEL/CENTOS INSTALLATION
────────────────────────────────────────────────────────────────────────────
sudo dnf install python3 python3-pip


ARCH LINUX INSTALLATION
────────────────────────────────────────────────────────────────────────────
sudo pacman -S python python-pip


VERIFY INSTALLATION
────────────────────────────────────────────────────────────────────────────
python3 --version

Should show: Python 3.x.x


LINUX TIPS
────────────────────────────────────────────────────────────────────────────
• Use python3 and pip3 commands (not python/pip)
• Most distros have Python 2 as "python" for compatibility
• You may need sudo for system-wide installations
• Use virtual environments (we'll learn this in Act VIII)


TROUBLESHOOTING LINUX
────────────────────────────────────────────────────────────────────────────

❌ ERROR: "command not found: python3"

SOLUTION:
  • Check your distribution's package manager
  • Try: sudo apt install python-is-python3 (Ubuntu)
  • Or compile from source (advanced)


❌ ERROR: Permission denied

SOLUTION:
  • Use sudo for installation commands
  • Don't use sudo for running your own scripts
        """)

    def teach_verification(self):
        print("""

VERIFICATION CHECKLIST
═══════════════════════════════════════════════════════════════════════════

Before continuing, verify you can do ALL of these:

1. Open a terminal/command prompt
2. Type: python --version (or python3 --version on Mac/Linux)
3. See output like: Python 3.8.x or higher
4. Type: python (or python3)
5. See the Python prompt: >>>
6. Type: print("Hello, Fraylon!")
7. See output: Hello, Fraylon!
8. Type: exit() to leave Python

If ALL of these work → YOU'RE READY!


WHAT YOU JUST DID
═══════════════════════════════════════════════════════════════════════════

You've summoned the Python interpreter to your machine. It's now waiting
for your commands, like a magical servant bound to your will.

The >>> prompt means Python is listening. It's like standing in a spell
circle, ready to channel your incantations.


NEXT STEPS
═══════════════════════════════════════════════════════════════════════════

In the next lesson, you'll learn about the COMMAND PORTAL - the terminal
itself. You've already used it, but we'll explore its mysteries deeper.

Elder Willowbyte nods: 'The summoning is complete. Python awakens in your
realm. Now, let us learn to speak through the Command Portal...'
        """)

    def challenge(self):
        """Verification challenge"""
        print("""
═══════════════════════════════════════════════════════════════════════════
                            VERIFICATION
═══════════════════════════════════════════════════════════════════════════

Have you successfully installed Python and verified it works?

To verify:
  1. Open terminal/command prompt
  2. Type: python --version (or python3 --version)
  3. You should see Python 3.8 or higher

Did this work?
        """)

        response = input("(y/n): ").strip().lower()

        if response == 'y':
            print("""
✓ EXCELLENT! The Installation Ritual is complete!

Python is now bound to your realm. You can summon it whenever you need.

The ancient glyphs recognize you as a student of the Language of Nature.

        """)
            input("[Press Enter to continue...]")
            return True
        else:
            print("""
The ritual requires more preparation. Here's what to do:

1. Re-read the installation instructions for your operating system
2. Follow each step carefully
3. If you encounter errors, check the troubleshooting section
4. Ask for help in Python communities:
   • r/learnpython on Reddit
   • Python Discord servers
   • Stack Overflow

Don't give up! Installation is often the hardest part.
Once Python is installed, the real fun begins.

You can return to this lesson anytime.
        """)
            input("[Press Enter to continue anyway...]")
            return True
```

---

## Lesson 0.3: The Command Portal - Terminal Basics

### Lesson ID: `act0_terminal_basics`
### Duration: 15 minutes
### Type: Guided tutorial

### Teaching Content

```python
class TerminalBasicsLesson(Lesson):
    """Learn terminal/command prompt basics"""

    def teach(self):
        print("""
═══════════════════════════════════════════════════════════════════════════
                    LESSON: THE COMMAND PORTAL
                        Terminal Basics
═══════════════════════════════════════════════════════════════════════════

Elder Willowbyte summons a shimmering portal in the air. Text scrolls
across its surface.

'This,' the elder intones, 'is the COMMAND PORTAL. What the mundane call
a "terminal" or "command line." It is the most direct way to speak to
your computer - no graphics, no buttons. Just pure command.'


WHAT IS A TERMINAL?
═══════════════════════════════════════════════════════════════════════════

A terminal (also called: command line, command prompt, console, shell) is
a text-based interface to your computer.

Instead of clicking buttons:  [Save] [Open] [Close]
You type commands:            save file.txt

Why use it?
  ✓ FASTER - Type commands faster than clicking through menus
  ✓ POWERFUL - Access features GUIs don't expose
  ✓ AUTOMATION - Can script repetitive tasks
  ✓ REQUIRED - All professional development uses terminals
  ✓ UNIVERSAL - Works the same remotely (SSH) or locally


HOW TO OPEN A TERMINAL
═══════════════════════════════════════════════════════════════════════════

WINDOWS:
  Method 1: Press Windows Key + R → Type "cmd" → Enter
  Method 2: Press Windows Key → Type "command prompt" → Enter
  Method 3: Right-click Start → "Windows Terminal" or "Command Prompt"

macOS:
  Method 1: Cmd + Space → Type "terminal" → Enter
  Method 2: Applications → Utilities → Terminal
  Method 3: Spotlight search → "terminal"

LINUX:
  Method 1: Ctrl + Alt + T (most distributions)
  Method 2: Applications → Terminal
  Method 3: Right-click desktop → "Open Terminal Here"


UNDERSTANDING THE PROMPT
═══════════════════════════════════════════════════════════════════════════

When you open a terminal, you see something like:

Windows:
  C:\\Users\\YourName>

macOS/Linux:
  yourname@computer:~$

This is the PROMPT. It's waiting for your command.

Breaking it down:
  C:\\Users\\YourName  → Current directory (folder) you're in
  >                   → Prompt symbol (ready for command)

On Mac/Linux:
  yourname            → Your username
  @computer           → Computer name
  :~                  → Current directory (~ means home)
  $                   → Prompt symbol


BASIC NAVIGATION COMMANDS
═══════════════════════════════════════════════════════════════════════════

Think of your computer as a castle with many rooms (folders/directories).
You're always "standing in" one room. These commands help you move around:


1. WHERE AM I? (Print Working Directory)
────────────────────────────────────────────────────────────────────────────
Windows:  cd              (shows current directory)
Mac/Linux: pwd             (print working directory)

Example:
  $ pwd
  /Users/grixle/Documents


2. WHAT'S IN THIS ROOM? (List Files)
────────────────────────────────────────────────────────────────────────────
Windows:  dir              (directory listing)
Mac/Linux: ls               (list)

Example:
  $ ls
  file1.py  file2.txt  my_folder  notes.md


3. MOVE TO ANOTHER ROOM (Change Directory)
────────────────────────────────────────────────────────────────────────────
All systems: cd FOLDER_NAME

Example:
  $ cd Documents        (enter Documents folder)
  $ cd ..               (go up one level - to parent folder)
  $ cd                  (go to home directory)
  $ cd /                (go to root - top of file system)

Think of it like:
  cd Documents    → Walk through door labeled "Documents"
  cd ..           → Walk back out to the previous room
  cd              → Teleport home


4. CREATING ROOMS (Make Directory)
────────────────────────────────────────────────────────────────────────────
All systems: mkdir FOLDER_NAME

Example:
  $ mkdir my_python_projects
  $ ls
  my_python_projects  (now exists!)


FILE PATHS EXPLAINED
═══════════════════════════════════════════════════════════════════════════

A file path is like directions to a room in the castle:

ABSOLUTE PATH (Full directions from entrance):
  Windows:  C:\\Users\\Grixle\\Documents\\game.py
  Mac/Linux: /Users/grixle/Documents/game.py

RELATIVE PATH (Directions from where you are):
  If you're in /Users/grixle:
    Documents/game.py    → Go into Documents, find game.py
    ../OtherUser/file.py → Go up one level, into OtherUser, find file.py


SPECIAL SYMBOLS:
  .  → Current directory (here)
  .. → Parent directory (up one level)
  ~  → Home directory (your user folder)
  /  → Root directory (top of file system) OR path separator


RUNNING PYTHON FROM TERMINAL
═══════════════════════════════════════════════════════════════════════════

Now the power of the Command Portal becomes clear:

1. Navigate to where your Python file is:
   $ cd Documents/python_projects

2. Run your Python file:
   $ python game.py             (Windows)
   $ python3 game.py            (Mac/Linux)

3. Python executes your code and shows output


TERMINAL SHORTCUTS
═══════════════════════════════════════════════════════════════════════════

These will save you HOURS:

• UP ARROW - Recall previous command (no retyping!)
• DOWN ARROW - Go forward in command history
• TAB - Auto-complete file/folder names
  Type: cd Doc[TAB] → cd Documents

• CTRL + C - STOP running program (emergency exit!)
• CTRL + L - Clear screen (or type "clear"/"cls")
• CTRL + A - Jump to start of line
• CTRL + E - Jump to end of line


PRACTICE CHALLENGE
═══════════════════════════════════════════════════════════════════════════

Let's practice! Open your terminal and try these commands:

1. Find where you are:
   Windows: cd
   Mac/Linux: pwd

2. List what's in this folder:
   Windows: dir
   Mac/Linux: ls

3. Create a new folder:
   mkdir python_practice

4. Enter that folder:
   cd python_practice

5. Check you're inside it:
   Windows: cd
   Mac/Linux: pwd

6. Go back out:
   cd ..

7. Remove the test folder:
   Windows: rmdir python_practice
   Mac/Linux: rmdir python_practice


COMMON TERMINAL ERRORS
═══════════════════════════════════════════════════════════════════════════

❌ "No such file or directory"
   → You're trying to access something that doesn't exist
   → Use ls/dir to see what's actually there
   → Check your spelling (capitalization matters on Mac/Linux!)

❌ "command not found"
   → The program isn't installed or not in PATH
   → Check spelling of command
   → Make sure software is installed

❌ "Permission denied"
   → You don't have rights to access this
   → Try: sudo command_name (Mac/Linux) - but be careful!
   → Run as Administrator (Windows)


WHY THIS MATTERS
═══════════════════════════════════════════════════════════════════════════

Every professional developer lives in the terminal. You'll use it to:
  • Run Python scripts
  • Install packages (pip install)
  • Use Git version control
  • Deploy applications
  • Connect to remote servers
  • Automate tasks

Getting comfortable with the terminal NOW will make everything else easier.


Elder Willowbyte concludes:

'The Command Portal is your direct line to the machine's soul. Learn to
speak its language, and you command great power. Fear it not - with
practice, it becomes second nature.'
        """)

    def challenge(self):
        """Verification of terminal skills"""
        print("""
═══════════════════════════════════════════════════════════════════════════
                        CHALLENGE: PORTAL MASTERY
═══════════════════════════════════════════════════════════════════════════

Test your knowledge:

1. What command shows your current directory?
   Windows: cd    Mac/Linux: pwd

2. What command lists files in current directory?
   Windows: dir   Mac/Linux: ls

3. What command moves you into a folder called "projects"?
   Answer: cd projects

4. What does "cd .." do?
   Answer: Goes up one directory level

5. How do you stop a running Python program?
   Answer: Ctrl + C


Have you practiced these commands in your actual terminal?
        """)

        response = input("(y/n): ").strip().lower()

        if response == 'y':
            print("""
✓ EXCELLENT! You've mastered the Command Portal basics!

You can now:
  • Navigate your file system
  • Find and run Python files
  • Stop programs that are running
  • Use terminal shortcuts

This skill will serve you throughout your entire programming journey.

Elder Willowbyte grants you the title: PORTAL WALKER
            """)
        else:
            print("""
That's okay! Terminal skills take practice.

Try this:
  1. Open your terminal right now
  2. Try each command one by one
  3. Don't just read - actually type them!
  4. Make mistakes - they won't break your computer
  5. Get comfortable exploring

The Command Portal awaits your commands...
            """)

        input("\n[Press Enter to continue...]")
        return True
```

---

## Lesson 0.4: The Scribe's Tools - Text Editors and IDEs

### Lesson ID: `act0_text_editors`
### Duration: 20 minutes
### Type: Guided tutorial

*[This lesson would cover VS Code installation, PyCharm introduction, understanding syntax highlighting, creating/saving .py files, etc. - Similar detailed format as above]*

---

## Lesson 0.5: The First Incantation - Hello, World!

### Lesson ID: `act0_hello_world`
### Duration: 15 minutes
### Type: Hands-on coding

*[This lesson guides students through creating their FIRST Python file outside the game, running it from terminal, and seeing output. Major milestone!]*

---

## Lesson 0.6: The Oracle's Warnings - Understanding Errors

### Lesson ID: `act0_understanding_errors`
### Duration: 20 minutes
### Type: Tutorial with examples

*[This lesson teaches error message anatomy, common beginner errors, debugging with print(), and where to get help]*

---

# Act VIII: The Forge of Mastery
## *"You have learned the Language. Now learn the ways of those who wield it in the mortal realm."*

### Act VIII Introduction

```
═══════════════════════════════════════════════════════════════════════════
                      ACT VIII: THE FORGE OF MASTERY
                    The Path to Professional Mastery
═══════════════════════════════════════════════════════════════════════════

You stand before a massive forge, its flames casting dancing shadows on
ancient walls. This is not the mystical grove of Elder Willowbyte. This
is the FORGE OF MASTERY, where Python skills are tempered into professional
tools.

A weathered dwarf emerges from the smoke—Master Ironcode, legendary
craftsdwarf and keeper of the enterprise ways:

'Aye, so ye've learned the Language of Nature, have ye? That's a fine
start. But out there in the REAL WORLD—in the great corporations and
guilds—ye'll need more than just Python syntax.

Ye'll need to work with TEAMS. Track your CHANGES. TEST your CODE. DEBUG
when things break. Follow the STANDARDS. Organize your PROJECTS.

This is where apprentices become MASTERS. This is where hobby code becomes
PROFESSIONAL CRAFT. Welcome to the Forge!'


WHAT YOU'LL LEARN:
═══════════════════════════════════════════════════════════════════════════

1. The Repository of Time - Git Version Control
   Track every change, collaborate with teams, never lose work

2. Isolated Spell Chambers - Virtual Environments
   Keep project dependencies separate and clean

3. The Great Library - Package Management (pip)
   Install and manage thousands of Python packages

4. The Trials of Validation - Unit Testing
   Prove your code works, catch bugs before users do

5. The Divination Chamber - Debugging with pdb
   Hunt down bugs efficiently with professional tools

6. The Scroll of Style - PEP 8 and Code Quality
   Write code that other professionals respect

7. The Codex of Clarity - Documentation
   Make your code understandable to others (and future you)

8. The Sanctum of Organization - Project Structure
   Organize code like a professional project

9. The Chronicle Stone - Logging
   Track what your code does in production

10. The Hidden Vault - Configuration Management
    Manage secrets, settings, and environments

11. The Continuous Ritual - CI/CD Basics
    Automate testing and deployment

12. The Grand Portfolio - From Code to Career
    Build a GitHub portfolio that gets you hired


Master Ironcode raises his hammer:

'Each of these lessons will take you deeper into the professional craft.
By the end, ye'll not just write Python—ye'll write it like a MASTER.

Let's begin with the foundation of all professional development:
Version Control.'
```

---

## Lesson 8.1: The Repository of Time - Git Basics

### Lesson ID: `git_basics`
### Duration: 30 minutes
### Type: Hands-on tutorial

### Teaching Content

```python
class GitBasicsLesson(Lesson):
    """Introduction to Git version control"""

    def teach(self):
        print("""
═══════════════════════════════════════════════════════════════════════════
                  LESSON: THE REPOSITORY OF TIME
                        Git Version Control
═══════════════════════════════════════════════════════════════════════════

Master Ironcode leads you to a massive bronze clock with infinite gears:

'Behold—the REPOSITORY OF TIME! This is Git, the most important tool in
a professional developer's arsenal. More important than fancy IDEs, more
important than frameworks, more important than anything else.

Git tracks EVERY change you make to your code. It's like having infinite
save points in a game, plus the ability to:
  • Go back in time to any previous version
  • Work on multiple versions simultaneously (branches)
  • Collaborate with other developers without conflict
  • Never lose work again
  • Show employers your coding journey (GitHub portfolio)'


WHAT IS GIT?
═══════════════════════════════════════════════════════════════════════════

Git is a VERSION CONTROL SYSTEM. It tracks changes to files over time.

Think of it like this:

WITHOUT GIT:
  my_game.py
  my_game_v2.py
  my_game_v3.py
  my_game_FINAL.py
  my_game_FINAL_ACTUALLY.py
  my_game_FINAL_FOR_REAL_THIS_TIME.py

WITH GIT:
  my_game.py  ← One file, infinite history

Git remembers every version automatically. You can:
  • See who changed what and when
  • Go back to any previous version
  • Try new features without breaking working code
  • Merge multiple people's changes together


WHY GIT IS MANDATORY FOR JOBS
═══════════════════════════════════════════════════════════════════════════

EVERY professional development team uses Git. Not some. ALL.

When you apply for jobs, employers will ask:
  • "Share your GitHub profile" (Git hosting site)
  • "Have you used version control?" (Must say yes!)
  • "Can you resolve merge conflicts?" (Git skill)

If you can't use Git, you CANNOT work on a development team. Period.


GIT VS GITHUB
═══════════════════════════════════════════════════════════════════════════

GIT:
  • The tool on your computer
  • Tracks changes locally
  • Free, open-source software

GITHUB:
  • Website that hosts Git repositories
  • Share code with others
  • Portfolio for employers
  • Collaboration platform

Think: Git is email, GitHub is Gmail.


INSTALLING GIT
═══════════════════════════════════════════════════════════════════════════

WINDOWS:
  1. Download from: https://git-scm.com/download/win
  2. Run installer (accept defaults)
  3. Verify: Open terminal, type: git --version

macOS:
  Method 1: git --version (may auto-install)
  Method 2: brew install git

LINUX:
  Ubuntu/Debian: sudo apt install git
  Fedora: sudo dnf install git


FIRST-TIME SETUP
═══════════════════════════════════════════════════════════════════════════

Tell Git who you are (required once):

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

Use your real name and email (will appear in commits).


THE BASIC GIT WORKFLOW
═══════════════════════════════════════════════════════════════════════════

The fundamental Git cycle (you'll do this hundreds of times):


1. CREATE A REPOSITORY (ONCE PER PROJECT)
────────────────────────────────────────────────────────────────────────────
A repository (or "repo") is a project tracked by Git.

# Navigate to your project folder
cd my_python_project

# Initialize Git
git init

You now have a .git folder (hidden) tracking everything!


2. CHECK STATUS (ANYTIME)
────────────────────────────────────────────────────────────────────────────
See what's changed:

git status

Output shows:
  • Untracked files (Git doesn't know about them yet)
  • Modified files (Git knows about them, but changes not saved)
  • Staged files (ready to commit)


3. STAGE CHANGES (PREPARE TO SAVE)
────────────────────────────────────────────────────────────────────────────
Tell Git which changes to include in next save:

# Stage one file
git add my_game.py

# Stage all files
git add .

Think: You're gathering items to put in a save chest.


4. COMMIT (SAVE POINT!)
────────────────────────────────────────────────────────────────────────────
Create a save point with a message:

git commit -m "Add player health system"

The message should describe WHAT you did and WHY.

GOOD commit messages:
  ✓ "Add input validation to login form"
  ✓ "Fix crash when player health reaches zero"
  ✓ "Refactor database connection code for clarity"

BAD commit messages:
  ❌ "Update"
  ❌ "Fixed stuff"
  ❌ "asdfasdf"


5. REPEAT!
────────────────────────────────────────────────────────────────────────────
Work → Stage (git add) → Commit (git commit) → Work → Stage → Commit...


VIEWING HISTORY
═══════════════════════════════════════════════════════════════════════════

See all your commits:

git log

Output:
  commit 1a2b3c4d (HEAD -> main)
  Author: Grixle <grixle@fraylon.com>
  Date:   Mon Dec 22 10:30:00 2025

      Add player health system

  commit 5e6f7g8h
  Author: Grixle <grixle@fraylon.com>
  Date:   Mon Dec 22 09:15:00 2025

      Initial commit - basic game structure

Each commit has:
  • Unique ID (1a2b3c4d...)
  • Author
  • Date
  • Message


PRACTICAL EXAMPLE - FRAYLON QUEST TRACKER
═══════════════════════════════════════════════════════════════════════════

Let's track a real project with Git:

# Create project folder
mkdir fraylon_quests
cd fraylon_quests

# Initialize Git
git init
# Output: Initialized empty Git repository

# Create a Python file
echo "quest_list = []" > quests.py

# Check status
git status
# Output: Untracked files: quests.py

# Stage the file
git add quests.py

# Check status again
git status
# Output: Changes to be committed: new file: quests.py

# Commit
git commit -m "Initialize quest tracking system"
# Output: [main (root-commit) 1a2b3c4] Initialize quest tracking system

# Make changes
echo "quest_list.append('Defeat the Iron Wyrm')" >> quests.py

# Check what changed
git diff
# Shows line-by-line differences

# Stage and commit
git add quests.py
git commit -m "Add first quest to list"

# View history
git log
# Shows both commits!


GITIGNORE - EXCLUDING FILES
═══════════════════════════════════════════════════════════════════════════

Some files should NEVER be tracked by Git:
  • __pycache__/ (Python cache)
  • *.pyc (Compiled Python)
  • .env (Secret keys!)
  • venv/ (Virtual environment)
  • .DS_Store (Mac system files)

Create a .gitignore file:

# Create .gitignore
nano .gitignore

# Add these lines:
__pycache__/
*.pyc
.env
venv/
.DS_Store

# Save and commit
git add .gitignore
git commit -m "Add gitignore file"

Now Git ignores these files!


WHY THIS MATTERS IN THE REAL WORLD
═══════════════════════════════════════════════════════════════════════════

Example scenario:

You: "The new feature broke everything!"
Git: "No problem. What was the last working commit?"
You: "3 commits ago"
Git: "Restored. Want to see exactly what changed?"
You: "Yes!"
Git: "Here's every line you added since then."

Or:

Boss: "Who changed the authentication code last month?"
Git: "Bob did, on October 15th at 2:30 PM. Here's the exact change."

Or:

You: "I want to try a risky experiment but can't break the working code."
Git: "Create a branch! Experiment safely, merge when ready."


COMMON GIT COMMANDS - QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════

git init                  # Create new repository
git status                # Check what's changed
git add file.py           # Stage specific file
git add .                 # Stage all changes
git commit -m "message"   # Save changes with message
git log                   # View commit history
git diff                  # See unstaged changes
git diff --staged         # See staged changes


NEXT LESSON PREVIEW
═══════════════════════════════════════════════════════════════════════════

In the next lesson, we'll learn:
  • Branches (parallel timelines)
  • Merging (combining changes)
  • GitHub (sharing your code)
  • Collaboration (working with teams)

But first, master these basics!


Master Ironcode nods approvingly:

'The Repository of Time is yours to command. Every commit is a moment
preserved forever. Every change is recorded. Never again will ye lose
work to a crashed hard drive or accidental deletion.

This is the foundation. Build upon it well.'
        """)

    def challenge(self):
        """Hands-on Git challenge"""
        print("""
═══════════════════════════════════════════════════════════════════════════
                        CHALLENGE: FIRST REPOSITORY
═══════════════════════════════════════════════════════════════════════════

TIME TO CREATE YOUR FIRST GIT REPOSITORY!

Follow these steps in your terminal:

1. Create a new project folder:
   mkdir my_first_repo
   cd my_first_repo

2. Initialize Git:
   git init

3. Create a Python file:
   echo "print('Hello from Git!')" > hello.py

4. Check status:
   git status

5. Stage the file:
   git add hello.py

6. Commit:
   git commit -m "Add hello world script"

7. Make a change:
   echo "print('Git is awesome!')" >> hello.py

8. Check status:
   git status

9. Check differences:
   git diff

10. Stage and commit:
    git add hello.py
    git commit -m "Add second print statement"

11. View your history:
    git log


Have you completed these steps?
        """)

        response = input("(y/n): ").strip().lower()

        if response == 'y':
            print("""
═══════════════════════════════════════════════════════════════════════════
                    ✓ ACHIEVEMENT UNLOCKED: TIME WEAVER
═══════════════════════════════════════════════════════════════════════════

You've created your first Git repository and made commits!

You now understand:
  • What Git is and why it's essential
  • How to initialize a repository
  • The add/commit workflow
  • How to view history

NEXT STEPS:
  • Practice creating repositories for every project
  • Commit often (not just when "done")
  • Write clear commit messages
  • Never commit secrets or sensitive data

Master Ironcode grants you the bronze hammer token:
"Ye've taken your first step into version control. This is the way of
professionals. Guard this knowledge well."

+50 XP - Professional Skills Unlocked!
        """)
        else:
            print("""
The Repository of Time is patient. Take time to practice:

1. Don't just read—actually type the commands
2. Make mistakes—they won't break your computer
3. Experiment with different commits
4. Get comfortable with the workflow

Git takes practice, but it's worth every minute invested.

When you're ready, return and try again.
            """)

        input("\n[Press Enter to continue...]")
        return True
```

---

## Lesson 8.2: Parallel Timelines - Git Branching

### Lesson ID: `git_branching`
### Duration: 30 minutes

*[This lesson would cover creating branches, switching between them, merging, resolving conflicts, and GitHub integration. D&D theme: Parallel realities that can be merged.]*

---

## Lesson 8.3: Isolated Spell Chambers - Virtual Environments

### Lesson ID: `virtual_environments`
### Duration: 25 minutes

*[Teaching venv creation, activation/deactivation, why they matter, and best practices]*

---

## Lesson 8.4: The Great Library - Package Management (pip)

### Lesson ID: `package_management`
### Duration: 20 minutes

*[Teaching pip install, requirements.txt, PyPI, managing dependencies]*

---

## Lesson 8.5: The Trials of Validation - Unit Testing

### Lesson ID: `unit_testing`
### Duration: 40 minutes

### Teaching Content (Abbreviated)

```python
class UnitTestingLesson(Lesson):
    """Learn to write tests with pytest"""

    def teach(self):
        print("""
═══════════════════════════════════════════════════════════════════════════
                  LESSON: THE TRIALS OF VALIDATION
                          Unit Testing
═══════════════════════════════════════════════════════════════════════════

Master Ironcode leads you to a grand arena:

'Every spell must be TESTED before battle. Every weapon must be PROVEN
before the forge certifies it. Your code is no different.

This is the Arena of Trials—where your code proves its worth.'


WHAT IS UNIT TESTING?
═══════════════════════════════════════════════════════════════════════════

Unit testing means writing code that TESTS your code.

Example:

# Your code (in spells.py)
def fireball(power):
    return power * 10

# Your test (in test_spells.py)
def test_fireball():
    assert fireball(5) == 50
    assert fireball(0) == 0
    assert fireball(10) == 100

The test PROVES fireball() works correctly.


WHY TESTING IS MANDATORY IN REAL JOBS
═══════════════════════════════════════════════════════════════════════════

WITHOUT TESTS:
  • Change code → Hope it still works → Ship to users → Users find bugs
  • Afraid to change anything (might break something)
  • Spend days debugging
  • Boss doesn't trust your code

WITH TESTS:
  • Change code → Run tests → Know immediately if something broke
  • Confidently refactor
  • Catch bugs before users do
  • Boss trusts your code (tests prove it works)

PROFESSIONAL TEAMS REQUIRE TESTS. Many won't even review code without them.


PYTEST - THE TESTING FRAMEWORK
═══════════════════════════════════════════════════════════════════════════

Install pytest:
  pip install pytest


WRITING YOUR FIRST TEST
═══════════════════════════════════════════════════════════════════════════

# File: calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# File: test_calculator.py
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


Run tests:
  pytest test_calculator.py

Output:
  ======================== test session starts ========================
  collected 2 items

  test_calculator.py ..                                         [100%]

  ========================= 2 passed in 0.05s =========================

✓ ALL TESTS PASSED!


ANATOMY OF A TEST
═══════════════════════════════════════════════════════════════════════════

def test_function_name():
    # 1. ARRANGE - Set up test data
    power = 5

    # 2. ACT - Call the function
    damage = fireball(power)

    # 3. ASSERT - Check the result
    assert damage == 50

This is called AAA pattern (Arrange, Act, Assert).


ASSERTIONS - THE TRUTH SPELLS
═══════════════════════════════════════════════════════════════════════════

assert CONDITION, "Error message if false"

assert 2 + 2 == 4                    # Passes
assert 2 + 2 == 5                    # FAILS!

Common assertions:
  assert x == y                       # Equal
  assert x != y                       # Not equal
  assert x > y                        # Greater than
  assert x in [1, 2, 3]              # In list
  assert "dragon" in text            # Substring
  assert my_list                      # Not empty
  assert x is None                    # Is None


TESTING ERRORS (THEY SHOULD HAPPEN!)
═══════════════════════════════════════════════════════════════════════════

Sometimes functions SHOULD raise errors:

# Code
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

This test PASSES if ValueError is raised!


REAL-WORLD EXAMPLE - FRAYLON GAME
═══════════════════════════════════════════════════════════════════════════

# game.py
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


# test_game.py
from game import Player

def test_player_creation():
    player = Player("Grixle")
    assert player.name == "Grixle"
    assert player.health == 100

def test_take_damage():
    player = Player("Grixle", health=50)
    player.take_damage(20)
    assert player.health == 30

def test_health_cannot_go_negative():
    player = Player("Grixle", health=10)
    player.take_damage(50)
    assert player.health == 0  # Not -40!

def test_is_alive():
    player = Player("Grixle", health=10)
    assert player.is_alive() == True

    player.take_damage(10)
    assert player.is_alive() == False


Run: pytest test_game.py
All tests pass → Your Player class works correctly!


TEST-DRIVEN DEVELOPMENT (TDD)
═══════════════════════════════════════════════════════════════════════════

Professional technique: WRITE TESTS FIRST!

1. Write test (it fails - function doesn't exist)
2. Write minimal code to make test pass
3. Refactor code
4. Repeat

Example:

# test_inventory.py
def test_add_item():
    inventory = Inventory()
    inventory.add_item("sword")
    assert "sword" in inventory.items

# This test FAILS - Inventory doesn't exist yet

# inventory.py
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# Now test PASSES!


WHY THIS MATTERS
═══════════════════════════════════════════════════════════════════════════

Scenario: You're applying for a Python job

Interviewer: "How do you ensure code quality?"
You: "I write unit tests using pytest"

Interviewer: "Show me an example"
You: [Shows your GitHub with 80% test coverage]

Interviewer: "You're hired"

VS:

You: "I... test it manually?"
Interviewer: "Next candidate, please"


PYTEST COMMAND REFERENCE
═══════════════════════════════════════════════════════════════════════════

pytest                    # Run all tests
pytest test_file.py       # Run specific file
pytest -v                 # Verbose output
pytest -k "keyword"       # Run tests matching keyword
pytest --cov              # Show code coverage


Master Ironcode raises his hammer in salute:

'Ye've learned to prove your craft! Tests are not optional—they are
the mark of a TRUE professional. Write tests, young smith, and your
code will stand the test of time.'
        """)
```

---

*[Continue with lessons 8.6-8.12 covering debugging, PEP 8, documentation, project structure, logging, configuration, CI/CD, and portfolio building]*

---

# Real-World Projects
## Practical Applications to Build Portfolio

Each act should include 2-3 real-world projects that students can:
1. Build following guided steps
2. Add to their GitHub portfolio
3. Show to employers
4. Actually use in daily life

## Project Structure

```python
class RealWorldProject:
    """Template for practical projects"""

    def __init__(self, title, description, difficulty, skills):
        self.title = title
        self.description = description
        self.difficulty = difficulty  # Beginner, Intermediate, Advanced
        self.skills = skills  # List of skills practiced

    def introduction(self):
        """Explain what students will build"""
        pass

    def requirements(self):
        """List technical requirements"""
        pass

    def guided_build(self):
        """Step-by-step building instructions"""
        pass

    def challenges(self):
        """Extensions to make it their own"""
        pass

    def portfolio_tips(self):
        """How to present this on GitHub/portfolio"""
        pass
```

---

## Act I Projects (Fundamentals)

### Project 1.1: Interactive Calculator

**Skills**: Variables, input(), operators, type conversion, error handling

**What You'll Build**: A calculator that takes user input and performs operations

**Steps**:
1. Get two numbers from user
2. Ask which operation (+, -, *, /)
3. Calculate result
4. Handle division by zero
5. Loop to allow multiple calculations

**Portfolio Value**: Shows basic Python skills, user interaction, error handling

---

### Project 1.2: Number Guessing Game

**Skills**: random, while loops, conditionals, user feedback

**What You'll Build**: Computer picks random number, user guesses

**Extensions**:
- Difficulty levels (different ranges)
- Limited guesses
- High score tracking
- Hints (higher/lower)

---

### Project 1.3: Temperature Converter

**Skills**: Functions, input validation, formatting

**What You'll Build**: Convert between Celsius, Fahrenheit, Kelvin

**Professional Touch**:
- Function for each conversion
- Input validation
- Nice formatted output
- Support both ways (C→F and F→C)

---

## Act II Projects (Collections)

### Project 2.1: To-Do List Manager

**Skills**: Lists, file I/O, persistence, CRUD operations

**What You'll Build**: Add, view, complete, and delete tasks

**Features**:
- Save/load from file
- Mark tasks complete
- Filter by status
- Priority levels

**Portfolio Value**: Shows data management, file operations, user interface

---

### Project 2.2: Contact Book

**Skills**: Dictionaries, JSON, search, validation

**What You'll Build**: Store and search contacts with multiple fields

**Features**:
- Add/edit/delete contacts
- Search by name/phone/email
- Export to CSV
- Import from file

---

### Project 2.3: Word Frequency Analyzer

**Skills**: String methods, dictionaries, file reading, data analysis

**What You'll Build**: Analyze text files and show word frequencies

**Applications**:
- Analyze books from Project Gutenberg
- Compare writing styles
- Find most common words
- Generate word clouds (with library)

---

## Act V Projects (Files & I/O)

### Project 5.1: Log File Analyzer

**Skills**: File reading, regex, data aggregation, reporting

**What You'll Build**: Parse server logs and generate reports

**Real-World Application**: Actual IT/DevOps task

**Features**:
- Count errors by type
- Find most active IPs
- Time-based analysis
- Generate summary report

**Portfolio Value**: Shows cybersecurity/DevOps skills

---

### Project 5.2: CSV Data Reporter

**Skills**: CSV module, data processing, statistics

**What You'll Build**: Read CSV files and generate insights

**Examples**:
- Sales data analysis
- Student grade calculator
- Survey results processor

---

### Project 5.3: Automated Backup Script

**Skills**: os module, shutil, datetime, scheduling

**What You'll Build**: Automatically backup important files

**Features**:
- Copy files to backup location
- Date-stamped backups
- Configurable paths
- Log backup status

**Portfolio Value**: Shows automation skills (valuable for DevOps)

---

## Act VIII Projects (Enterprise)

### Project 8.1: GitHub Portfolio Setup

**Skills**: Git, GitHub, markdown, project documentation

**What You'll Build**: Professional GitHub profile

**Includes**:
- Profile README
- Pinned repositories
- Project documentation
- Clean commit history

**This IS the portfolio!**

---

### Project 8.2: Tested Python Package

**Skills**: Project structure, testing, packaging, documentation

**What You'll Build**: Installable Python package with tests

**Structure**:
```
my_package/
├── my_package/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_core.py
├── README.md
├── setup.py
└── requirements.txt
```

**Portfolio Value**: Shows professional development practices

---

### Project 8.3: CLI Tool with Argparse

**Skills**: argparse, project structure, error handling

**What You'll Build**: Command-line tool (like git, npm, etc.)

**Example Tools**:
- File organizer
- Batch file renamer
- Text processor
- Development utility

---

## Portfolio Presentation Guide

### How to Present Projects on GitHub

**README Template**:
```markdown
# Project Name

Brief description of what it does (1-2 sentences)

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --help
```

## Examples

```python
# Example code
```

## Technologies Used

- Python 3.11
- pytest for testing
- argparse for CLI

## What I Learned

What you learned building this project

## Future Improvements

- [ ] Feature to add
- [ ] Another feature

## License

MIT License
```

**Screenshots**: Add screenshots showing the tool in action

**Demo GIFs**: Use tools like ScreenToGif to record usage

**Live Demo**: Deploy web projects (Heroku, PythonAnywhere)

---

# Supplemental Lessons

## Common Pitfalls Section

Each lesson should include a "Common Pitfalls" section:

```python
def teach_common_pitfalls(self):
    print("""
═══════════════════════════════════════════════════════════════════════════
                 COMMON PITFALLS - WATCH OUT!
═══════════════════════════════════════════════════════════════════════════

These are mistakes EVERY beginner makes. Learn from them:

❌ PITFALL 1: Forgetting to convert input()

WRONG:
  age = input("Enter age: ")
  years_to_100 = 100 - age  # ERROR! age is string

CORRECT:
  age = int(input("Enter age: "))
  years_to_100 = 100 - age  # Works!


❌ PITFALL 2: Modifying list while iterating

WRONG:
  for item in my_list:
      my_list.remove(item)  # Skips items!

CORRECT:
  for item in my_list[:]:  # Copy of list
      my_list.remove(item)


❌ PITFALL 3: Mutable default arguments

WRONG:
  def add_item(item, items=[]):
      items.append(item)
      return items

  # Calling twice uses SAME list!
  add_item(1)  # [1]
  add_item(2)  # [1, 2] - not [2]!

CORRECT:
  def add_item(item, items=None):
      if items is None:
          items = []
      items.append(item)
      return items
    """)
```

---

## Try-It-Yourself Sandbox

After each lesson, provide interactive sandbox:

```python
def sandbox_mode(self):
    """Let students experiment with concepts"""

    print("""
═══════════════════════════════════════════════════════════════════════════
                    TRY-IT-YOURSELF SANDBOX
═══════════════════════════════════════════════════════════════════════════

Experiment with what you just learned!

Type Python code to test concepts. Type 'exit' to continue.

Try these:
  • Create variables
  • Do calculations
  • Make mistakes on purpose
  • Fix the mistakes

    """)

    while True:
        try:
            code = input("sandbox >>> ")

            if code.strip().lower() == 'exit':
                print("\nLeaving sandbox. Knowledge retained!")
                break

            try:
                # Try eval first (for expressions)
                result = eval(code)
                if result is not None:
                    print(result)
            except SyntaxError:
                # Fall back to exec (for statements)
                exec(code)

        except KeyboardInterrupt:
            print("\n\nExiting sandbox...")
            break
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            print("Try again! Errors are learning opportunities.")
```

---

## Video Tutorial References

Link to external resources:

```python
def show_resources(self):
    print("""
═══════════════════════════════════════════════════════════════════════════
                      ADDITIONAL RESOURCES
═══════════════════════════════════════════════════════════════════════════

📺 VIDEO TUTORIALS:
  • Git Basics: https://www.youtube.com/watch?v=HVsySz-h9r4
  • Python Virtual Environments: https://realpython.com/python-virtual-environments/
  • Pytest Tutorial: https://www.youtube.com/watch?v=bbp_849-RZ4

📚 DOCUMENTATION:
  • Official Python Docs: https://docs.python.org/3/
  • Git Documentation: https://git-scm.com/doc
  • PEP 8 Style Guide: https://pep8.org/

💬 COMMUNITIES:
  • r/learnpython: Reddit community for beginners
  • Python Discord: discord.gg/python
  • Stack Overflow: Tag your questions with [python]

🎓 PRACTICE PLATFORMS:
  • Exercism: https://exercism.org/tracks/python
  • HackerRank: https://www.hackerrank.com/domains/python
  • LeetCode: https://leetcode.com/

    """)
```

---

## Achievement System

Gamify enterprise skills:

```python
ACHIEVEMENTS = {
    'first_repo': {
        'name': 'Time Weaver',
        'description': 'Created your first Git repository',
        'icon': '⏰',
        'xp': 50
    },
    'first_commit': {
        'name': 'History Maker',
        'description': 'Made your first Git commit',
        'icon': '📝',
        'xp': 25
    },
    'first_test': {
        'name': 'Trial Master',
        'description': 'Wrote your first unit test',
        'icon': '✅',
        'xp': 50
    },
    'test_coverage_50': {
        'name': 'Guardian of Quality',
        'description': 'Achieved 50% test coverage',
        'icon': '🛡️',
        'xp': 100
    },
    'first_venv': {
        'name': 'Chamber Keeper',
        'description': 'Created your first virtual environment',
        'icon': '🏰',
        'xp': 50
    },
    'pep8_clean': {
        'name': 'Style Guardian',
        'description': 'Formatted code with PEP 8',
        'icon': '✨',
        'xp': 25
    },
    'github_profile': {
        'name': 'Portfolio Crafter',
        'description': 'Created professional GitHub profile',
        'icon': '🎖️',
        'xp': 100
    },
    'first_pr': {
        'name': 'Collaborator',
        'description': 'Made your first pull request',
        'icon': '🤝',
        'xp': 75
    },
    'debug_master': {
        'name': 'Oracle of Bugs',
        'description': 'Used pdb to find and fix a bug',
        'icon': '🔍',
        'xp': 50
    }
}

def unlock_achievement(achievement_id):
    achievement = ACHIEVEMENTS[achievement_id]
    print(f"""
═══════════════════════════════════════════════════════════════════════════
              ✨ ACHIEVEMENT UNLOCKED ✨
═══════════════════════════════════════════════════════════════════════════

{achievement['icon']} {achievement['name']}

{achievement['description']}

+{achievement['xp']} XP!
═══════════════════════════════════════════════════════════════════════════
    """)
```

---

## End of Proposed Lessons Document

**Summary**: This document provides:
1. Complete Act 0 (6 lessons for complete beginners)
2. Complete Act VIII (12 lessons for enterprise skills)
3. Real-world projects for portfolio building
4. Supplemental teaching enhancements
5. Achievement system for motivation

**Next**: See ENTERPRISE_SKILLS_ROADMAP.md for learning progression
**Next**: See BEGINNER_ONBOARDING.md for step-by-step setup guide
