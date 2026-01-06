# Story Mode Demo - How It Works

## Starting Story Mode

When you select "Story Mode" from the main menu, here's what happens:

### Act 1: The Awakening
```
======================================================================
 Act I: The Awakening
======================================================================

The Mossroot Grove thrums with unnatural energy. Trees whisper in broken
syntax. Elder Willowbyte, a wise treant, calls upon you to learn the
Language of Nature - Python itself.

'Young Grixle,' the elder's bark creaks, 'the world's code is breaking.
You must learn to read it, and restore balance.'

[Press Enter to begin...]
```

### Story Mode Menu
```
======================================================================
 Act I: The Awakening - Scene 1
======================================================================
Progress: 0/13 lessons completed
XP: 0
======================================================================

1. Continue Story (Next Lesson)
2. Save Game
3. Skip to Next Act
4. Return to Main Menu
```

## Lesson Progression

### When you select "Continue Story":

1. **Lesson Starts**: Next incomplete lesson in the act
   ```
   [STORY] Now learning: Basic Input and Output

   ======================================================================
   [LESSON] LESSON: Basic Input and Output
   ======================================================================

   Learn how to get input from users and display output.

   [Lesson content displays...]
   ```

2. **Challenge Completes**: Interactive coding challenge or review

3. **Auto-Save Triggers**:
   ```
   [SAVE] Progress auto-saved! (XP: +10, Total: 10)
   ```

4. **Scene Advances**: Returns to story menu with updated progress
   ```
   Progress: 1/13 lessons completed
   XP: 10
   ```

## Act Completion

When all lessons in an act are complete:

```
======================================================================
 ACT 1 COMPLETE!
======================================================================

You have mastered all lessons in this act.
XP Earned: 130

[Press Enter to advance to the next act...]
```

## Manual Save

At any time in Story Mode, select option 2:

```
[SAVE] Game saved successfully!
       Act 1, Scene 5
       XP: 40, Lessons: 4
```

## Progress Through All Acts

### Act Structure:
- **Act 1: The Awakening** (13 topics) - Fundamentals
- **Act 2: Strings and Collections** (22 topics) - Data structures
- **Act 3: The Path Diverges** (19 topics) - Control flow and loops
- **Act 4: Functions of Power** (15 topics) - Functions
- **Act 5: The Archive** (21 topics) - Files and modules
- **Act 6: Objects of Power** (8 topics) - OOP
- **Act 7: The Iron Wyrm** (6 topics) - Algorithms

Total: **104 Python topics**

## Completing the Game

After finishing Act 7:

```
======================================================================
                    THE IRON WYRM FALLS
======================================================================

Through your mastery of Python, you have debugged the world itself.
The Iron Wyrm, that terrible algorithm of chaos, has been refactored
into elegant, efficient code.

The trees sing once more. Rivers flow with clean data. And Fraylon
is restored to balance.

Elder Willowbyte nods with satisfaction: 'You have learned well,
Grixle Mossroot. You are now a true Druid of the Verdant Code.'

Final Stats:
- Total XP: 1040
- Lessons Completed: 104
- Acts Conquered: 7

The Verdant Code thanks you for playing!
======================================================================
```

## Key Features

### Auto-Save System
- Saves after EVERY lesson completion
- Saves when advancing scenes
- Saves when advancing acts
- Progress never lost

### Manual Save
- Available anytime in story menu
- Shows current position
- Confirms save success

### Skip Option
- Can skip acts if stuck
- Requires confirmation
- Won't earn XP for skipped lessons

### Resume Anytime
- Progress saved to `game_progress_enhanced.json`
- Load from main menu
- Continue exactly where you left off

## Comparison: Story Mode vs Reference Mode

### Story Mode
- Linear progression through acts
- XP and progress tracking
- Auto-save after lessons
- Manual save option
- Narrative experience
- Must complete lessons in order

### Reference Mode
- Browse any topic instantly
- NO progress tracking
- NO saves
- NO XP
- Quick lookup only
- No order required

## Example Play Session

```
1. Start game
2. Select "Story Mode"
3. Begin Act 1
4. Complete "Basic Input and Output" -> Auto-save, +10 XP
5. Complete "How Errors Work" -> Auto-save, +10 XP
6. Select "Save Game" -> Manual save
7. Complete "Why Whitespace Matters" -> Auto-save, +10 XP
8. Return to Main Menu
9. Exit game -> Save prompt appears
10. Next session: Load save, continue from Scene 4
```

The story mode is fully playable from start to finish!
