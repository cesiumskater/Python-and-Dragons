# LESSON TEMPLATE AND STANDARDS - The Verdant Code v1.2.2

**Purpose:** Define the exact structure and quality standards for every lesson

---

## LESSON STRUCTURE TEMPLATE

Every lesson must follow this exact structure:

```python
class LessonNameLesson(Lesson):
    """Lesson X.Y: Brief Description - FULLY IMPLEMENTED"""

    def __init__(self):
        super().__init__(
            lesson_id="unique_lesson_id",
            title="Engaging Title with Storyline Hook",
            description="Brief storyline description that hooks the player"
        )

        # REQUIRED: 3-5 key concepts
        self.key_concepts = [
            "Concept 1 - clear, concise statement",
            "Concept 2 - clear, concise statement",
            "Concept 3 - clear, concise statement",
            "Concept 4 - clear, concise statement (optional)",
            "Concept 5 - clear, concise statement (optional)"
        ]

        # REQUIRED: 3-5 common pitfalls
        self.common_pitfalls = [
            "Pitfall 1 - specific mistake beginners make",
            "Pitfall 2 - specific mistake beginners make",
            "Pitfall 3 - specific mistake beginners make",
            "Pitfall 4 - specific mistake beginners make (optional)",
            "Pitfall 5 - specific mistake beginners make (optional)"
        ]

        # REQUIRED: 3-5 best practices
        self.best_practices = [
            "Practice 1 - specific recommendation",
            "Practice 2 - specific recommendation",
            "Practice 3 - specific recommendation",
            "Practice 4 - specific recommendation (optional)",
            "Practice 5 - specific recommendation (optional)"
        ]

        # REQUIRED: 3-5 real-world applications
        self.real_world_apps = [
            "Application 1 - real company/use case",
            "Application 2 - real company/use case",
            "Application 3 - real company/use case",
            "Application 4 - real company/use case (optional)",
            "Application 5 - real company/use case (optional)"
        ]

    def teach(self):
        print("""
═══════════════════════════════════════════════════════════════════════════
                        [NARRATIVE TITLE/SECTION]
═══════════════════════════════════════════════════════════════════════════

[STORYLINE INTEGRATION - 2-4 paragraphs]
- Set the scene (where are we?)
- Introduce the mentor/NPC
- Connect to overall narrative
- Create engagement hook

[TOPIC OVERVIEW AND IMPORTANCE]
═══════════════════════════════════════════════════════════════════════════

[2-3 paragraphs explaining WHAT this topic is and WHY it matters]

[CORE CONCEPT 1]
═══════════════════════════════════════════════════════════════════════════

[Explanation with examples]

    # Code example 1
    example_code_here

[Explanation of code]

[CORE CONCEPT 2]
═══════════════════════════════════════════════════════════════════════════

[Explanation with examples]

    # Code example 2
    more_example_code

[Continue for all major concepts...]

[PRACTICAL EXAMPLES]
═══════════════════════════════════════════════════════════════════════════

Example 1: [Real-world scenario]
    # Code

Example 2: [Another scenario]
    # Code

[3-5 practical examples total]

[REAL-WORLD APPLICATIONS]
═══════════════════════════════════════════════════════════════════════════
""")
        # Display real-world apps
        for i, app in enumerate(self.real_world_apps, 1):
            print(f"  {i}. {app}")

        print("""
[KEY CONCEPTS SUMMARY]
═══════════════════════════════════════════════════════════════════════════
""")
        # Display key concepts
        for i, concept in enumerate(self.key_concepts, 1):
            print(f"  {i}. {concept}")

        print("""
═══════════════════════════════════════════════════════════════════════════

[CLOSING NARRATIVE - 1-2 paragraphs]
- Mentor's concluding wisdom
- Connection to next lesson
- Motivation boost
        """)

    def challenge(self) -> bool:
        print("""
═══════════════════════════════════════════════════════════════════════════
                          [CHALLENGE TITLE]
═══════════════════════════════════════════════════════════════════════════

[Challenge description - what must they do?]

[Specific requirements:]
  1. Requirement 1
  2. Requirement 2
  3. Requirement 3

[Example output or goal]
        """)

        # Interactive challenge code here
        # Could be:
        # - Code validation
        # - Multiple choice
        # - Text response
        # - Practical exercise

        input("\n[Press Enter to continue...]")
        return True
```

---

## REQUIRED COMPONENTS

### 1. Storyline Integration
**Required:** Yes
**Location:** Beginning of teach() method
**Length:** 2-4 paragraphs
**Purpose:** Connect lesson to main narrative

**Must Include:**
- Current location (Mossroot Grove, Mallport, Library, etc.)
- Current mentor/NPC (Elder Willowbyte, Dockmaster Jora, etc.)
- Narrative hook related to topic
- Connection to defeating the Iron Wyrm/saving Fraylon

**Example:**
```
Elder Willowbyte taps his gnarled staff against an ancient oak. Glowing
runes appear on the bark, shimmering with pythonic energy.

"Young Grixle, before you can wield the Language of Nature against the
Cult of the Dragon, you must understand VARIABLES - the containers that
hold power, store values, and preserve state across time."

The old treant gestures, and acorns begin floating in the air, each
labeled with a name: 'health', 'mana', 'level'. They pulse with light.

"These are variables. They store data. They can change. They are the
foundation upon which all code is built. Master them, and you master
the first law of programming."
```

### 2. Topic Overview and Importance
**Required:** Yes
**Location:** After storyline, beginning of technical content
**Length:** 2-3 paragraphs
**Purpose:** Explain WHAT this is and WHY it matters

**Must Include:**
- Clear definition of the topic
- Why beginners need to learn it
- How it fits into programming as a whole
- Real-world necessity

**Example:**
```
WHAT ARE VARIABLES?
═══════════════════════════════════════════════════════════════════════════

Variables are named containers that store data. Think of them as labeled
boxes where you can put values - numbers, text, lists, or any Python object.

WHY VARIABLES MATTER

Without variables, you couldn't:
- Remember user input
- Track game scores
- Store calculation results
- Build any program more complex than "Hello, World!"

Every program you'll ever write uses variables. They're as fundamental as
nouns in language - you can't communicate without them.
```

### 3. Practical Code Examples
**Required:** Yes (minimum 3, ideally 5)
**Location:** Throughout teach() method
**Length:** Each example 5-15 lines
**Purpose:** Show concept in action

**Must Include:**
- Code comments explaining each line
- Realistic scenarios (not just x=1, y=2)
- Progression from simple to complex
- Output shown or described

**Example Format:**
```python
Example 1: Character Stats in RPG
    # Storing player information
    player_name = "Grixle"      # String variable
    player_health = 100         # Integer variable
    player_level = 1            # Integer variable
    is_poisoned = False         # Boolean variable

    print(f"{player_name} has {player_health} HP")
    # Output: Grixle has 100 HP
```

### 4. Real-World Applications
**Required:** Yes (3-5 specific examples)
**Location:** Dedicated section + summary list
**Purpose:** Show how professionals use this topic

**Must Include:**
- Actual companies/projects
- Specific use cases
- How the topic solves real problems
- Salary-earning relevance

**Example:**
```
REAL-WORLD APPLICATIONS:
- Instagram: Stores user data in variables (username, post count, followers)
- Spotify: Variables track current song, play time, volume level
- NASA: Variables monitor rocket fuel levels, velocity, altitude
- Your future job: Every application you build will use variables
```

### 5. Key Concepts List
**Required:** Yes (3-5 bullets)
**Location:** self.key_concepts in __init__
**Display:** End of teach() method
**Purpose:** Reinforce main takeaways

**Format:**
- Clear, concise statements
- Can be copied to flashcards
- Cover the absolute essentials

**Example:**
```python
self.key_concepts = [
    "Variables store data using the = operator (assignment)",
    "Variable names must start with letter/underscore, can contain numbers",
    "Python variables are dynamically typed (type can change)",
    "Use descriptive names: player_health not ph",
    "Variables can be reassigned: x = 5; x = 10 is valid"
]
```

### 6. Common Pitfalls
**Required:** Yes (3-5 specific mistakes)
**Location:** self.common_pitfalls in __init__
**Display:** show_common_pitfalls() method
**Purpose:** Prevent student mistakes

**Format:**
- Specific mistake beginners actually make
- Why it happens
- How to avoid it

**Example:**
```python
self.common_pitfalls = [
    "Using = for comparison instead of == (assignment vs equality)",
    "Forgetting Python is case-sensitive: Name != name",
    "Using reserved words as variable names (def, class, if, etc.)",
    "Not initializing variables before use (NameError results)",
    "Using spaces in variable names: player health (use player_health)"
]
```

### 7. Best Practices
**Required:** Yes (3-5 recommendations)
**Location:** self.best_practices in __init__
**Display:** show_best_practices() method
**Purpose:** Teach professional habits

**Format:**
- Actionable recommendation
- Why professionals do it this way
- Impact on code quality

**Example:**
```python
self.best_practices = [
    "Use snake_case for variable names: user_count not userCount",
    "Make names descriptive: total_price not tp",
    "Constants in UPPER_CASE: MAX_HEALTH = 100",
    "Avoid single-letter names except in loops: i, j, k okay; x, y, z not ideal",
    "Initialize variables close to where they're used"
]
```

### 8. Interactive Challenge
**Required:** Yes
**Location:** challenge() method
**Length:** At least 5 lines of code required
**Purpose:** Apply knowledge immediately

**Must Include:**
- Clear instructions
- Specific requirements
- Success feedback
- Connection to storyline

**Types:**
- Code validation (write working code)
- Multiple choice (test understanding)
- Debugging (fix broken code)
- Practical application (solve real problem)

---

## QUALITY STANDARDS

### Writing Style
- **Tone:** Friendly, encouraging, epic
- **Voice:** Second person ("you"), present tense
- **Vocabulary:** Explain jargon, don't assume knowledge
- **Length:** Verbose is good - aim for 300-500 lines per lesson

### Code Style
- **All code must be valid Python 3.8+**
- **Include comments for every non-obvious line**
- **Use realistic variable names (not x, y, z)**
- **Show output as comments where helpful**
- **Follow PEP 8 style**

### Narrative Integration
- **Every lesson mentions current location**
- **Every lesson has NPC dialogue**
- **Connect to saving Fraylon / defeating Wyrm**
- **Build on previous lessons narratively**
- **Set up next lesson's hook**

### Technical Accuracy
- **All information must be factually correct**
- **Specify Python version for version-specific features**
- **Test all code examples**
- **Cite real companies/applications accurately**
- **Explain WHY, not just WHAT**

---

## PROGRESSION GUIDELINES

### Early Lessons (Acts 0-II)
- **Assume:** No prior programming knowledge
- **Explain:** Everything explicitly
- **Examples:** Very simple, one concept at a time
- **Challenges:** Basic, guided

### Middle Lessons (Acts III-V)
- **Assume:** Basic Python knowledge
- **Explain:** Build on foundations
- **Examples:** Moderate complexity
- **Challenges:** Require thinking, less guidance

### Advanced Lessons (Acts VI-VII)
- **Assume:** Solid fundamentals
- **Explain:** Focus on design and architecture
- **Examples:** Complex, multi-file
- **Challenges:** Open-ended problem solving

### Professional Lessons (Act VIII)
- **Assume:** Can write Python
- **Explain:** Professional practices
- **Examples:** Real-world scenarios
- **Challenges:** Industry-standard tasks

### Master Lessons (Act IX)
- **Assume:** Strong Python skills
- **Explain:** Advanced techniques
- **Examples:** Sophisticated patterns
- **Challenges:** Expert-level problems

---

## CHECKLIST FOR EACH LESSON

Before marking a lesson complete, verify:

- [ ] Lesson ID is unique and follows naming convention
- [ ] Title is engaging and includes storyline element
- [ ] Description hooks the player
- [ ] 3-5 key concepts defined
- [ ] 3-5 common pitfalls identified
- [ ] 3-5 best practices listed
- [ ] 3-5 real-world applications cited
- [ ] Storyline integration (2-4 paragraphs)
- [ ] Topic overview explains WHAT and WHY
- [ ] 3-5 practical code examples
- [ ] All code is valid and tested
- [ ] Real-world applications section
- [ ] Key concepts displayed
- [ ] Mentor dialogue included
- [ ] Location mentioned
- [ ] Connection to main narrative
- [ ] Interactive challenge implemented
- [ ] Challenge has clear requirements
- [ ] Total length 300-500+ lines
- [ ] No spelling/grammar errors
- [ ] Consistent tone and voice

---

## EXAMPLE FULL LESSON

See WhatIsPythonLesson and InstallingPythonLesson in the main file as reference
implementations that follow this template perfectly.

---

**Last Updated:** December 23, 2025
**Purpose:** Maintain consistent quality across all 185 lessons
**Status:** Standards defined, ready for implementation
