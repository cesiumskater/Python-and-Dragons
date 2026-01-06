#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive quote-fixing script for the_verdant_code_1.2.2.py

This script systematically fixes mismatched quotes in teaching content
to ensure the file compiles without syntax errors.
"""

import re
import sys


def fix_quotes(filename):
    """Fix all quote mismatches in the file."""
    print(f"Reading {filename}...")

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixes_applied = []

    # Fix 1: Replace all remaining ''' in code examples (4+ spaces indent) with """
    pattern1 = r"(    +)'''"
    replacement1 = r'\1"""'
    content, count1 = re.subn(pattern1, replacement1, content)
    if count1 > 0:
        fixes_applied.append(f"Fixed {count1} indented ''' to triple-double-quotes")

    # Fix 2: Find and fix mismatched docstring delimiters like """...'
    # Pattern: """text''' or '''text"""
    pattern2 = r'"""([^"]*?)' + "'''"
    replacement2 = r'"""\1"""'
    content, count2 = re.subn(pattern2, replacement2, content)
    if count2 > 0:
        fixes_applied.append(f"Fixed {count2} mismatched triple-quote endings")

    pattern3 = "'''([^']*?)\"\"\" "
    replacement3 = r"'''\1'''"
    content, count3 = re.subn(pattern3, replacement3, content)
    if count3 > 0:
        fixes_applied.append(f"Fixed {count3} mismatched triple-quote beginnings")

    # Fix 3: Email template and similar cases - ensure EMAIL_TEMPLATE uses """
    # Find lines like: TEMPLATE = ''' and change to """
    pattern4 = r"(\s+\w+_TEMPLATE\s*=\s*)'''"
    replacement4 = r'\1"""'
    content, count4 = re.subn(pattern4, replacement4, content)
    if count4 > 0:
        fixes_applied.append(f"Fixed {count4} TEMPLATE assignments to use triple-double-quotes")

    # Fix 4: Ensure all def lines with docstrings use consistent quotes
    # Find: def name(): """docstring''' and fix
    pattern5 = r'(def\s+\w+\([^)]*\):\s*\n\s+)"""([^"]+)' + "'''"
    replacement5 = r'\1"""\2"""'
    content, count5 = re.subn(pattern5, replacement5, content, flags=re.MULTILINE)
    if count5 > 0:
        fixes_applied.append(f"Fixed {count5} function docstring mismatches")

    # Fix 5: Find and fix orphaned triple quotes that break balancing
    # Look for lines with odd """ counts (single """ not paired on same line)
    lines = content.split('\n')
    fixed_orphans = 0
    for i, line in enumerate(lines):
        triple_double_count = line.count('"""')
        triple_single_count = line.count("'''")

        # Skip lines that are clearly code examples (have = assignment)
        if '=' in line and ("story = '''" in line or "prophecy = '''" in line):
            continue

        # If line has exactly 1 """ and multiple ''', likely mismatch
        if triple_double_count == 1 and triple_single_count >= 1:
            # Replace ''' with """ on this line to balance
            lines[i] = line.replace("'''", '"""')
            fixed_orphans += 1

    if fixed_orphans > 0:
        content = '\n'.join(lines)
        fixes_applied.append(f"Fixed {fixed_orphans} lines with orphaned triple-quotes")

    # Fix 6: Ensure all class docstrings use """
    pattern6 = r"(class\s+\w+[^:]*:\s*\n\s*)'''([^']+)'''"
    replacement6 = r'\1"""\2"""'
    content, count6 = re.subn(pattern6, replacement6, content, flags=re.MULTILINE)
    if count6 > 0:
        fixes_applied.append(f"Fixed {count6} class docstring to use triple-double-quotes")

    # Write fixed content
    if content != original_content:
        backup_file = filename + '.before_fix'
        print(f"\nCreating backup: {backup_file}")
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_content)

        print(f"Writing fixed content to {filename}...")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\nFixes applied:")
        for fix in fixes_applied:
            print(f"  OK: {fix}")

        print(f"\nTotal characters changed: {len(content) - len(original_content)}")
        return True
    else:
        print("No fixes needed!")
        return False


def verify_syntax(filename):
    """Verify the file compiles without syntax errors."""
    print(f"\nVerifying syntax of {filename}...")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        compile(content, filename, 'exec')
        print("OK: Syntax verification PASSED!")
        return True

    except SyntaxError as e:
        print(f"ERROR: Syntax error at line {e.lineno}: {e.msg}")
        if e.text:
            print(f"  Text: {e.text.strip()}")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return False


def count_quotes(filename):
    """Count and report quote statistics."""
    print(f"\nAnalyzing quotes in {filename}...")

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    triple_double = content.count('"""')
    triple_single = content.count("'''")

    print(f"  Triple double-quotes (\"\"\"):  {triple_double} ({'EVEN' if triple_double % 2 == 0 else 'ODD WARNING'})")
    print(f"  Triple single-quotes ('''): {triple_single} ({'EVEN' if triple_single % 2 == 0 else 'ODD WARNING'})")

    if triple_double % 2 == 0 and triple_single % 2 == 0:
        print("\nOK: Quote counts are balanced!")
        return True
    else:
        print("\nWARNING: Quote counts are UNBALANCED - additional fixes may be needed")
        return False


if __name__ == '__main__':
    filename = 'the_verdant_code_1.2.2.py'

    print("=" * 70)
    print("  QUOTE FIXING SCRIPT FOR THE VERDANT CODE")
    print("=" * 70)

    # Step 1: Count quotes before fixing
    count_quotes(filename)

    # Step 2: Apply fixes
    print("\n" + "=" * 70)
    fix_quotes(filename)

    # Step 3: Count quotes after fixing
    print("\n" + "=" * 70)
    balanced = count_quotes(filename)

    # Step 4: Verify syntax
    print("\n" + "=" * 70)
    syntax_ok = verify_syntax(filename)

    # Final report
    print("\n" + "=" * 70)
    print("  FINAL REPORT")
    print("=" * 70)

    if balanced and syntax_ok:
        print("OK: All fixes successful! File is ready.")
        sys.exit(0)
    else:
        print("WARNING: Additional manual fixes may be required.")
        print("  Check the syntax error details above.")
        sys.exit(1)
