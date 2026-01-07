# Beginner Onboarding Guide
## Complete Step-by-Step Instructions for Someone Who Has NEVER Coded

**Who This Is For**: Someone who doesn't know what Python is, what a terminal is, or how to run a program.

**Where You'll End Up**: Playing The Verdant Code game and learning Python!

**Time Required**: 30-60 minutes for setup

---

## Table of Contents

1. [What You Need](#what-you-need)
2. [Step 1: Install Python](#step-1-install-python)
3. [Step 2: Verify Python Works](#step-2-verify-python-works)
4. [Step 3: Install a Text Editor](#step-3-install-a-text-editor)
5. [Step 4: Download The Verdant Code](#step-4-download-the-verdant-code)
6. [Step 5: Run The Game](#step-5-run-the-game)
7. [Troubleshooting](#troubleshooting)
8. [What's Next](#whats-next)

---

## What You Need

Before you start, make sure you have:

- [ ] A computer (Windows, Mac, or Linux)
- [ ] Internet connection
- [ ] Administrator access (ability to install software)
- [ ] 30-60 minutes of time
- [ ] Patience (this is all new, but you CAN do it!)

**Don't have any programming experience?** PERFECT! This guide assumes you know NOTHING.

**Nervous about breaking your computer?** Don't be. You can't break your computer by following these steps. The worst that happens is you need to uninstall and try again.

---

## Step 1: Install Python

### What is Python?

Python is a **programming language**—a way to give instructions to your computer. Think of it like learning Spanish or French, except you're learning to speak to computers.

When you "install Python," you're installing a program called an **interpreter** that can read and execute Python code.

### Which Version?

**Get Python 3.8 or higher.** (As of December 2025, Python 3.12 is current)

**DO NOT** get Python 2. It's old and no longer supported.

---

### For Windows Users

#### Step 1.1: Download Python

1. Open your web browser (Chrome, Edge, Firefox, etc.)
2. Go to: **https://www.python.org/downloads/**
3. You'll see a big yellow button that says **"Download Python 3.X.X"**
   - The X's will be numbers like 3.12.1—that's fine!
4. Click the button
5. The file will download (probably to your Downloads folder)
   - It's named something like: `python-3.12.1-amd64.exe`

#### Step 1.2: Run the Installer

1. Open your **Downloads** folder
   - Press **Windows Key + E** to open File Explorer
   - Click "Downloads" on the left
2. Find the file you just downloaded (starts with `python-`)
3. **Double-click** the file to run it
4. **IMPORTANT**: A window appears. You'll see two checkboxes at the bottom:

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  [✓] Install launcher for all users (recommended) │
│  [✓] Add Python 3.12 to PATH                      │  ← MUST CHECK THIS!
│                                                    │
│  [ Install Now ]          [ Customize installation ]│
└────────────────────────────────────────────────────┘
```

5. **CHECK THE BOX** that says "Add Python to PATH"
   - This is CRITICAL. If you forget, Python won't work from the command line!
6. Click **"Install Now"**
7. Wait 1-2 minutes while it installs
   - You might see a User Account Control prompt—click "Yes"
8. When it says "Setup was successful," click **Close**

#### Step 1.3: Did it work?

Let's check!

1. Press **Windows Key + R** (this opens "Run")
2. Type: `cmd`
3. Press **Enter**
   - A black window opens—this is the **Command Prompt** (terminal)
4. Type: `python --version`
5. Press **Enter**

**What should happen**:
```
Python 3.12.1
```

**If you see this**: SUCCESS! Python is installed! ✓

**If you see "python is not recognized"**: The PATH wasn't set correctly. Jump to [Troubleshooting](#troubleshooting-windows).

---

### For Mac Users

#### Step 1.1: Check if Python 3 is Already Installed

Mac comes with Python 2.7 (old), but might have Python 3.

1. Press **Cmd + Space** (this opens Spotlight search)
2. Type: `terminal`
3. Press **Enter**
   - A white or black window opens—this is the **Terminal**
4. Type: `python3 --version`
5. Press **Enter**

**If you see**: `Python 3.8.X` or higher → You're done! Skip to Step 2!

**If you see**: `command not found` → You need to install Python 3

#### Step 1.2: Download and Install Python

1. Open your web browser (Safari, Chrome, etc.)
2. Go to: **https://www.python.org/downloads/**
3. Click the big yellow button: **"Download Python 3.X.X"**
4. The file downloads (probably to Downloads folder)
   - Named something like: `python-3.12.1-macos11.pkg`
5. Open **Finder** → **Downloads**
6. **Double-click** the .pkg file
7. Follow the installer:
   - Click **Continue**
   - Click **Continue** again
   - Click **Agree** (to license)
   - Click **Install**
   - Enter your Mac password when prompted
   - Click **Install Software**
8. Wait a minute or two
9. When it says "The installation was successful," click **Close**

#### Step 1.3: Verify it Worked

1. Open **Terminal** again (Cmd + Space → "terminal")
2. Type: `python3 --version`
3. Press **Enter**

**What should happen**:
```
Python 3.12.1
```

**If you see this**: SUCCESS! ✓

**Important Note for Mac Users**:
- Type `python3` (not just `python`) on Mac
- `python` might point to old Python 2.7

---

### For Linux Users

Most Linux distributions come with Python 3 pre-installed, but let's verify!

#### Step 1.1: Check Current Version

1. Open **Terminal**
   - Usually: **Ctrl + Alt + T**
   - Or search for "Terminal" in applications
2. Type: `python3 --version`
3. Press **Enter**

**If you see Python 3.8 or higher**: You're done! ✓

**If you see older version or "command not found"**: Install Python 3

#### Step 1.2: Install Python 3 (if needed)

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora**:
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux**:
```bash
sudo pacman -S python python-pip
```

Enter your password when prompted, then wait for installation.

#### Step 1.3: Verify

```bash
python3 --version
```

Should show Python 3.8 or higher.

---

## Step 2: Verify Python Works

Let's make sure Python is actually working by running it!

### For Windows:

1. Open Command Prompt (Windows Key + R → type `cmd` → Enter)
2. Type: `python`
3. Press **Enter**

You should see something like:
```
Python 3.12.1 (main, Dec 22 2025, 10:00:00)
[MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**The `>>>` means Python is waiting for your commands!**

4. Type: `print("Hello, World!")`
5. Press **Enter**

You should see:
```
Hello, World!
```

**IT WORKS!** You just ran your first Python code! 🎉

6. Type: `exit()`
7. Press **Enter** to leave Python

### For Mac/Linux:

Same steps, but use `python3` instead of `python`:

1. Open Terminal
2. Type: `python3`
3. Press **Enter**
4. You see `>>>`
5. Type: `print("Hello, World!")`
6. See: `Hello, World!`
7. Type: `exit()` to leave

---

## Step 3: Install a Text Editor

### What's a Text Editor?

A text editor is where you'll WRITE your Python code. It's like Microsoft Word, but for code instead of essays.

**DO NOT use Microsoft Word or Notepad!** They add invisible formatting that breaks code.

You need a **code editor**. Here are your options:

### Option 1: VS Code (Recommended for Beginners)

**Why VS Code?**
- Free
- Beginner-friendly
- Lots of helpful features
- Most popular among professionals

**Installation**:

1. Go to: **https://code.visualstudio.com/**
2. Click **"Download for [Your OS]"**
   - Windows: Downloads a .exe file
   - Mac: Downloads a .zip file
   - Linux: Choose your package manager

**Windows**:
3. Run the downloaded .exe file
4. Follow the installer (click Next, Next, Install)
5. Check "Add to PATH" if asked

**Mac**:
3. Open the downloaded .zip
4. Drag "Visual Studio Code" to Applications folder
5. Open Applications → Visual Studio Code

**Linux**:
3. Follow instructions for your distro on the VS Code site

**First Launch**:
1. Open VS Code
2. Click the **Extensions icon** (four squares) on the left sidebar
3. Search for: **Python**
4. Install the one by Microsoft (has millions of downloads)
5. Restart VS Code

**Test it**:
1. Click **File → New Text File**
2. Type: `print("VS Code works!")`
3. Click **File → Save**
4. Name it: `test.py`
5. Save it to your **Desktop** or **Documents**

Now you can write Python code!

### Option 2: PyCharm (More Advanced)

**Why PyCharm?**
- Powerful IDE (Integrated Development Environment)
- Lots of features
- Great for larger projects
- Also professional-grade

**Installation**:
1. Go to: **https://www.jetbrains.com/pycharm/download/**
2. Download **PyCharm Community Edition** (free!)
3. Run the installer
4. Follow the setup wizard

PyCharm is more complex, so beginners might prefer VS Code initially.

### Option 3: IDLE (Simplest)

**Why IDLE?**
- Comes with Python (already installed!)
- Very simple
- Good for absolute beginners
- Limited features

**How to Use**:

**Windows**: Search for "IDLE" in Start Menu
**Mac**: Applications → Python 3.X → IDLE
**Linux**: Type `idle3` in terminal

IDLE opens a window with `>>>` prompt. You can:
- Type code directly (like `print("hello")`)
- Create files: File → New File

**Limitation**: No advanced features, but fine for learning basics.

---

## Step 4: Download The Verdant Code

Now that Python and a text editor are installed, let's get the game!

### Option A: Download from GitHub (if available)

1. Go to the GitHub repository (link would be provided)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. The file downloads (probably to Downloads folder)
5. Open **Downloads** folder
6. **Right-click** the ZIP file → **Extract All** (Windows) or **double-click** (Mac)
7. Choose where to extract:
   - Recommended: Create a folder called `PythonProjects` in your Documents
   - Extract there
8. You now have a folder with the game file(s)

### Option B: Copy the Game File Directly

If you have the game file directly:

1. Create a folder for your Python projects:
   - Windows: `C:\Users\YourName\Documents\PythonProjects`
   - Mac: `/Users/YourName/Documents/PythonProjects`
   - Linux: `/home/yourname/PythonProjects`

2. Copy `the_verdant_code_1.1.5.py` (or whatever version) to this folder

3. Remember where you put it! You'll need to navigate there in the terminal.

---

## Step 5: Run The Game

This is the moment of truth! Let's run The Verdant Code!

### For Windows:

1. Open **Command Prompt** (Windows Key + R → `cmd` → Enter)

2. Navigate to where you put the game file:
   ```
   cd Documents\PythonProjects
   ```
   - `cd` means "change directory" (move to a folder)
   - Adjust the path if you put it somewhere else

3. Verify the file is there:
   ```
   dir
   ```
   - You should see `the_verdant_code_1.1.5.py` in the list

4. Run the game:
   ```
   python the_verdant_code_1.1.5.py
   ```

5. Press **Enter**

**The game should start!** 🎮

You'll see the title screen and prologue!

### For Mac/Linux:

1. Open **Terminal**

2. Navigate to the game folder:
   ```bash
   cd Documents/PythonProjects
   ```

3. Verify the file is there:
   ```bash
   ls
   ```
   - You should see `the_verdant_code_1.1.5.py`

4. Run the game:
   ```bash
   python3 the_verdant_code_1.1.5.py
   ```

5. Press **Enter**

**Game starts!** 🎮

### What You'll See

```
Loading The Verdant Code - Enhanced Edition...
   Topic Registry: 153 topics loaded
   Table of Contents: Ready
   Reference Mode: Active

All systems ready!

    ================================================================

              THE VERDANT CODE - ENHANCED EDITION

             A Complete Python Learning Adventure
              with Table of Contents Navigation

    ================================================================

    PROLOGUE — The Whisper of Fraylon

    The world of Fraylon hums with ancient rhythm...
```

**Welcome to the game!** Follow the on-screen prompts to begin your journey!

---

## Troubleshooting

### Problem: "python is not recognized" (Windows)

**What it means**: Python wasn't added to PATH during installation.

**Solution 1: Reinstall** (Easiest)
1. Go to Settings → Apps → Installed apps
2. Find "Python 3.X"
3. Click the three dots → Uninstall
4. Download Python again from python.org
5. **CHECK THE "Add Python to PATH" BOX!**
6. Install again

**Solution 2: Manually Add to PATH** (Advanced)
1. Search for "Environment Variables" in Start Menu
2. Click "Edit the system environment variables"
3. Click **Environment Variables** button
4. Under "System variables," find "Path" → Click **Edit**
5. Click **New**
6. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python312`
   - Replace "YourName" with your username
   - Replace "Python312" with your version
7. Click **New** again
8. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts`
9. Click OK on all dialogs
10. **Close and reopen Command Prompt**
11. Try `python --version` again

### Problem: "command not found: python3" (Mac/Linux)

**Solution**:
1. Make sure installation completed successfully
2. Try: `python --version` (without the 3)
3. Try: `/usr/local/bin/python3 --version`
4. Reinstall Python from python.org

### Problem: Can't Find the Game File

**Solution**:
1. Remember where you extracted/saved it
2. In terminal, use `cd` to navigate:
   - List folders: `dir` (Windows) or `ls` (Mac/Linux)
   - Enter folder: `cd FolderName`
   - Go up one level: `cd ..`
3. Use absolute path if needed:
   - Windows: `cd C:\Users\YourName\Documents\PythonProjects`
   - Mac/Linux: `cd /Users/yourname/Documents/PythonProjects`

### Problem: "No module named..." Error

**What it means**: The game needs a library that's not installed.

**Solution**:
```bash
# Windows
pip install [module_name]

# Mac/Linux
pip3 install [module_name]
```

Example: If it says "No module named requests":
```bash
pip install requests
```

### Problem: Terminal Shows Weird Characters or Colors

**What it means**: Your terminal might not support UTF-8 (the character encoding).

**Solution (Windows)**:
1. Right-click Command Prompt title bar
2. Properties → Options tab
3. Check "Use legacy console" is UNCHECKED
4. Or use Windows Terminal (search in Start menu)

**Solution (Mac/Linux)**:
- Usually works by default
- Make sure terminal is set to UTF-8 encoding

### Problem: Permission Denied

**What it means**: You don't have rights to access the file/folder.

**Solution**:
- Make sure file is in your Documents or Desktop (you own these)
- Don't put files in Program Files or System folders
- On Linux/Mac, don't use `sudo` to run the game

### Problem: Python Opens But Nothing Happens

**What it means**: You're in the Python REPL, not running the file.

**Correct**:
```bash
python the_verdant_code_1.1.5.py    ← Runs the file
```

**Incorrect**:
```bash
python                               ← Opens Python REPL
>>> the_verdant_code_1.1.5.py       ← This doesn't work!
```

If you see `>>>`, type `exit()` and try running the file properly.

### Still Stuck?

**Get Help**:
- r/learnpython on Reddit (friendly community!)
- Python Discord servers
- Stack Overflow (search your error message)
- Post your error message and include:
  - Your operating system
  - Python version (`python --version`)
  - Exact error message
  - What you were trying to do

**Don't give up!** Everyone struggles with installation. It gets easier after this first hurdle!

---

## What's Next

### You Successfully Ran The Game!

**Congratulations!** You've accomplished something many people never do:
- ✓ Installed a programming language
- ✓ Used a terminal/command line
- ✓ Navigated your file system
- ✓ Ran a Python program

**These are REAL skills!** You're now in the top 1% of computer users who can actually program.

### Playing The Game

**Two Modes**:

1. **Story Mode**: Follow the narrative from Act I → Act VII
   - Your progress is saved automatically
   - Earns XP and unlocks acts
   - Linear learning path

2. **Reference Mode**: Look up any topic anytime
   - No progress tracking
   - Great for reviewing
   - Quick lookups

**Recommendation**: Start with Story Mode. It's designed for beginners!

### Learning Tips

**Do**:
- ✓ Actually TYPE the code (don't just read)
- ✓ Experiment in the challenges
- ✓ Take breaks (your brain needs time to process)
- ✓ Make mistakes (errors are learning opportunities)
- ✓ Ask questions (there are no dumb questions)
- ✓ Practice daily (even 20 minutes helps)

**Don't**:
- ✗ Copy/paste without understanding
- ✗ Skip challenges (that's where learning happens)
- ✗ Compare yourself to others (everyone learns at their own pace)
- ✗ Give up after first error (debugging is part of programming)
- ✗ Try to memorize everything (understanding > memorization)

### Beyond The Game

**After completing The Verdant Code, you'll know**:
- Python fundamentals (variables, types, operators)
- Data structures (lists, dictionaries, sets)
- Control flow (if/else, loops)
- Functions
- File handling
- Object-oriented programming
- Algorithms
- Cybersecurity basics

**Next steps after the game**:
1. Build your own projects (not just tutorial following)
2. Learn Git version control
3. Learn testing (pytest)
4. Build a GitHub portfolio
5. Apply for junior Python developer jobs

**Career Paths with Python**:
- Software Developer ($70k-$120k)
- Data Scientist ($90k-$150k)
- DevOps Engineer ($80k-$130k)
- Security Analyst ($75k-$125k)
- Automation Engineer ($70k-$115k)

### Resources for After

**Practice**:
- Exercism.org (free coding exercises)
- HackerRank (coding challenges)
- LeetCode (interview prep)

**Learning**:
- Real Python (excellent tutorials)
- Official Python docs
- "Python Crash Course" book
- "Automate the Boring Stuff" book (free online)

**Community**:
- r/learnpython (Reddit)
- Python Discord
- Stack Overflow
- Local Python meetups

### Final Words of Encouragement

**You're at the beginning of an amazing journey.**

Programming is:
- A superpower (you can create anything you imagine)
- A career (companies desperately need Python developers)
- A tool (automate your life, analyze data, build apps)
- A way of thinking (problem-solving skills transfer everywhere)

**The hardest part is starting. You've already done that.**

Every expert was once a beginner. Every senior developer once struggled with installation, just like you might have. The difference between them and someone who gave up? They kept going.

**You can do this.**

Elder Willowbyte says: *"The path is long, young one, but every master of the Language began where you stand now. The grove awaits. Let us begin."*

---

## Quick Reference Card

### Terminal Commands

**Windows**:
```
cd folder_name          # Enter a folder
cd ..                   # Go up one level
dir                     # List files
python file.py          # Run Python file
```

**Mac/Linux**:
```
cd folder_name          # Enter a folder
cd ..                   # Go up one level
ls                      # List files
python3 file.py         # Run Python file
```

### Running The Verdant Code

**Windows**:
```cmd
cd Documents\PythonProjects
python the_verdant_code_1.1.5.py
```

**Mac/Linux**:
```bash
cd Documents/PythonProjects
python3 the_verdant_code_1.1.5.py
```

### If You Get Stuck

1. Read the error message carefully
2. Google the error (usually first result helps)
3. Check this troubleshooting section
4. Ask on r/learnpython
5. Take a break and try again

### Remember

- **Errors are normal** (even experts see them daily)
- **Google is your friend** (programmers Google constantly)
- **Asking for help is smart** (not weak)
- **Progress > Perfection** (done is better than perfect)

---

**Ready? Let's begin your journey into Python!**

Welcome to The Verdant Code, adventurer. The Language of Nature awaits. 🐉

---

## Appendix: Understanding Key Concepts

### What is a Terminal?

A **terminal** (also called command line, command prompt, console, or shell) is a text-based way to interact with your computer.

**Instead of**:
- Clicking folders to open them
- Clicking "New Folder" button
- Clicking "Run" button

**You type**:
- `cd folder_name` to open folder
- `mkdir new_folder` to create folder
- `python program.py` to run program

**Why use it?**
- Faster once you learn it
- More powerful (can do things GUI can't)
- Required for programming
- How servers and professional tools work

### What is a File Path?

A **file path** is the address of a file on your computer.

**Windows example**:
```
C:\Users\Alice\Documents\PythonProjects\game.py
```

Breaking it down:
- `C:\` = C drive (your main hard drive)
- `Users\` = Users folder
- `Alice\` = Your user folder
- `Documents\` = Documents folder
- `PythonProjects\` = Your project folder
- `game.py` = The file

**Mac/Linux example**:
```
/Users/alice/Documents/PythonProjects/game.py
```

Similar breakdown (but uses `/` instead of `\`).

### Absolute vs Relative Paths

**Absolute path** (full address from root):
- Windows: `C:\Users\Alice\Documents\game.py`
- Mac/Linux: `/Users/alice/Documents/game.py`

**Relative path** (from where you currently are):
- If you're in `Documents`: `PythonProjects\game.py`
- If you're in `PythonProjects`: `game.py`

### What is .py?

`.py` is the file extension for Python files. It tells your computer "this file contains Python code."

Just like:
- `.txt` = Text file
- `.jpg` = Image file
- `.mp3` = Music file
- `.py` = Python code file

### What Does "Run" Mean?

**"Running" a program** means executing it—making the computer actually DO what the code says.

**Creating a file** = Writing down instructions
**Running the file** = Following the instructions

In Python:
- You write code in a `.py` file
- You run it with `python filename.py`
- Python reads the file and executes each instruction

---

**End of Beginner Onboarding Guide**

You're ready to start your Python journey. May your code be ever elegant and bug-free! ✨
