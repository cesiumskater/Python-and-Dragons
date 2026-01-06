# Maintenance Guide - The Verdant Code v1.3.0

## Overview

This guide provides technical details for maintaining and improving The Verdant Code game.

## Current Status

### ✅ Completed
- All 181 lessons fully implemented with complete content
- Act IX registered in game registry
- Duplicate classes removed
- Version information updated
- File structure optimized

### ⚠️ Known Technical Issues

#### 1. Quote Delimiter Inconsistencies

**Issue**: Some lesson `teach()` methods have nested triple-quote strings causing syntax errors.

**Root Cause**:
```python
def teach(self):
    print('''
    ... lesson content ...

    Example:
        '''
        This is a docstring example
        '''

    ''')  # Python sees the inner ''' as closing the outer string
```

**Affected Pattern**:
- Outer: `print('''...''')`
- Inner: Contains `'''` for docstring examples
- Result: Syntax error (unterminated string)

**Solution**:
Change outer delimiters when inner content contains matching quotes:
```python
def teach(self):
    print("""  # Use double quotes for outer
    ... lesson content with ''' inside ...
    """)
```

**Locations**: Scattered throughout lessons, particularly in:
- Comments and Documentation lessons
- Docstrings lesson
- Advanced Python lessons with code examples

#### 2. Unicode Characters Outside Strings

**Issue**: Checkmark (✓) and box-drawing characters appearing outside string literals

**Root Cause**: Unclosed print statements from quote delimiter mismatches

**Resolution**: Fix quote delimiters first (see #1 above)

## File Structure

### Main Components

```
the_verdant_code_1.3.0.py
├── Imports and Setup (lines 1-100)
├── Version Information (lines 60-68)
├── PreFlightCheck System (lines 70-200)
├── Base Classes
│   ├── Lesson (base class)
│   ├── GameProgress
│   └── SkillAssessment
├── Act Lessons (grouped by Act)
│   ├── Act 0: Lines ~600-3000
│   ├── Act I: Lines ~3000-9000
│   ├── Act II: Lines ~9000-22000
│   ├── Act III: Lines ~22000-35000
│   ├── Act IV: Lines ~35000-48000
│   ├── Act V: Lines ~48000-64000
│   ├── Act VI: Lines ~64000-81000
│   ├── Act VII: Lines ~81000-90000
│   ├── Act VIII: Lines ~90000-113000
│   └── Act IX: Lines ~113000-123000
├── Lesson Registry (lines ~122800-123030)
└── Game Modes and Main Loop (lines ~123030-end)
```

### Key Functions

| Function | Purpose | Location |
|----------|---------|----------|
| `get_lesson_registry()` | Returns dict mapping Acts to lessons | ~122850 |
| `get_lessons_for_act()` | Get lessons for specific Act | ~123034 |
| `get_next_lesson()` | Determine next lesson for player | ~123039 |
| `main_menu()` | Main game loop | ~123325 |
| `main()` | Entry point | ~123425 |

## Maintenance Tasks

### Task 1: Fix Quote Delimiters

**Priority**: High
**Estimated Time**: 2-3 hours

**Process**:
1. Identify all `print('''` statements containing internal `'''`
2. Change outer delimiter to `print("""`
3. Change closing `''')` to `""")`
4. Test each modified lesson

**Script Template**:
```python
def fix_quote_delimiters(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        if "print('''" in lines[i]:
            # Find closing
            j = i + 1
            has_internal_triple = False

            while j < len(lines):
                if "'''" in lines[j] and j != i:
                    has_internal_triple = True
                if "''')" in lines[j]:
                    if has_internal_triple:
                        lines[i] = lines[i].replace("print('''", 'print("""')
                        lines[j] = lines[j].replace("''')", '""")')
                    break
                j += 1
            i = j
        i += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
```

### Task 2: PEP 8 Compliance

**Priority**: Medium
**Tools**: `black`, `flake8`, `pylint`

**Common Issues**:
- Line length > 79 characters (content-heavy lessons)
- Whitespace around operators
- Blank line usage
- Import organization

**Approach**:
```bash
# Auto-format (be careful with multi-line strings!)
black the_verdant_code_1.3.0.py --line-length 88

# Check for issues
flake8 the_verdant_code_1.3.0.py --max-line-length 88 --ignore E501,W503

# Detailed analysis
pylint the_verdant_code_1.3.0.py
```

**Note**: Educational content may need longer lines for readability.

### Task 3: PEP 20 (Zen of Python) Review

**Priority**: Low
**Principles to Focus On**:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

**Areas for Improvement**:
1. **DRY Violations**: Some repetitive code in lesson structure
2. **Long Methods**: Some `teach()` methods exceed 500 lines
3. **Magic Numbers**: XP values, timeouts could be constants

**Refactoring Ideas**:
```python
# Constants at top of file
DEFAULT_LESSON_XP = 15
MAX_TIMEOUT = 60000
ACT_COMPLETION_BONUS = 50

# Lesson template helper
def create_standard_lesson_header(title, act, mentor):
    return f"""
═══════════════════════════════════════════════════════════════════
    {title}
═══════════════════════════════════════════════════════════════════

{mentor} greets you warmly...
"""
```

## Testing

### Manual Testing Checklist

- [ ] Game starts without errors
- [ ] Skill assessment runs
- [ ] New game creation works
- [ ] Lesson progression (test each Act)
- [ ] Save/load functionality
- [ ] Act transitions
- [ ] Challenge completion
- [ ] XP and reputation tracking
- [ ] All menu options
- [ ] Game exit and cleanup

### Automated Testing (Future)

```python
# Example test structure
import pytest
from the_verdant_code_1_3_0 import *

def test_lesson_registry():
    registry = get_lesson_registry()
    assert 9 in registry
    assert len(registry[9]) == 20

def test_game_progress():
    progress = GameProgress()
    progress.complete_lesson("variables", 15)
    assert "variables" in progress.completed_lessons
    assert progress.total_score >= 15

def test_lesson_structure():
    lesson = VariablesLesson()
    assert hasattr(lesson, 'teach')
    assert hasattr(lesson, 'challenge')
    assert hasattr(lesson, 'key_concepts')
```

## Performance Optimization

### Current Performance

- **Load Time**: ~2-3 seconds (acceptable for educational game)
- **Memory Usage**: ~50-100MB (lesson content in memory)
- **Startup**: Minimal checks, fast initialization

### Potential Optimizations

1. **Lazy Loading**: Load lessons on-demand instead of all at startup
2. **Caching**: Cache compiled lesson content
3. **Compression**: Compress lesson text (minor benefit)

**Not Recommended**: The current approach prioritizes simplicity and maintainability over marginal performance gains.

## Adding New Lessons

### Process

1. **Create Lesson Class**:
```python
class NewTopicLesson(Lesson):
    def __init__(self):
        super().__init__(
            lesson_id="unique_id",
            title="Engaging Title",
            description="Brief description"
        )
        self.key_concepts = [...]
        self.common_pitfalls = [...]
        self.best_practices = [...]
        self.real_world_apps = [...]

    def teach(self):
        print("""
        ... lesson content ...
        """)

    def challenge(self) -> bool:
        # Interactive challenge
        return True
```

2. **Register in Act**:
```python
def get_lesson_registry():
    return {
        # ... existing acts ...
        5: [
            # ... existing lessons ...
            NewTopicLesson(),  # Add here
        ],
    }
```

3. **Update Counts**:
```python
TOPICS_COUNT = 182  # Increment
TOTAL_XP_AVAILABLE = 2730  # Add XP (usually +15)
```

4. **Test**:
- Start game
- Navigate to Act
- Complete new lesson
- Verify progression

## Troubleshooting

### Issue: Game Won't Start

**Check**:
1. Python version (need 3.8+)
2. File encoding (should be UTF-8)
3. Syntax errors (`python -m py_compile filename.py`)

### Issue: Lessons Not Appearing

**Check**:
1. Lesson class defined?
2. Registered in `get_lesson_registry()`?
3. Correct Act number?
4. Unique lesson_id?

### Issue: Save File Corrupted

**Location**: `verdant_code_save.json`

**Fix**:
```bash
# Backup
cp verdant_code_save.json verdant_code_save.json.bak

# Delete to reset
rm verdant_code_save.json

# Or manually edit JSON
```

## Version Control Best Practices

### Branching Strategy

- `main`: Stable releases only
- `develop`: Integration branch
- `feature/*`: New features/lessons
- `fix/*`: Bug fixes

### Commit Messages

```
feat: Add Lesson 9.21 - Advanced Decorators
fix: Correct quote delimiters in StringsLesson
docs: Update maintenance guide
refactor: Extract lesson header template
test: Add tests for lesson progression
```

## Contact and Support

For issues, questions, or contributions:
- Review this guide
- Check CHANGELOG.md for recent changes
- See README.md for user-facing documentation

## Appendix: Complete Lesson List

See README.md for the full breakdown of all 181 lessons across Acts 0-IX.

---

**Last Updated**: January 1, 2026
**Version**: 1.3.0
**Maintainer**: Danny (Cesium) P.
