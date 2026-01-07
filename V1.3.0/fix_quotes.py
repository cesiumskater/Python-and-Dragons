#!/usr/bin/env python3
"""
Quote Delimiter Fix Utility for The Verdant Code
Fixes nested triple-quote issues in lesson teach() methods

Usage:
    python fix_quotes.py the_verdant_code_1.3.0.py

This script:
1. Finds print(''' statements
2. Checks for internal ''' that would close the string early
3. Changes outer delimiter to """ when conflicts found
4. Creates backup before modifying
"""

import sys
import os
from datetime import datetime


def create_backup(filename):
    """Create timestamped backup of file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(backup_name, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Created backup: {backup_name}")
    return backup_name


def find_print_statements(lines):
    """Find all multi-line print statements and their ranges"""
    statements = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for print with triple quotes
        if 'print(' in line and ("'''" in line or '"""' in line):
            if "print('''" in line:
                opening = "'''"
                closing = "''')"
                quote_type = 'single'
            elif 'print("""' in line:
                opening = '"""'
                closing = '""")'
                quote_type = 'double'
            else:
                i += 1
                continue

            # Find the closing
            start = i
            j = i + 1
            found_close = False

            while j < len(lines) and j < i + 5000:  # Max 5000 lines per statement
                if closing in lines[j]:
                    found_close = True
                    end = j
                    break
                j += 1

            if found_close:
                statements.append({
                    'start': start,
                    'end': end,
                    'quote_type': quote_type,
                    'opening': opening,
                    'closing': closing
                })
                i = end

        i += 1

    return statements


def check_for_conflicts(lines, statement):
    """Check if a print statement has internal quote conflicts"""
    start = statement['start']
    end = statement['end']
    quote = statement['opening']

    # Check lines between start and end for the same quote type
    for i in range(start + 1, end):
        if quote in lines[i]:
            return True

    return False


def fix_statement(lines, statement):
    """Fix a conflicting print statement by changing quote type"""
    start = statement['start']
    end = statement['end']

    if statement['quote_type'] == 'single':
        # Change ''' to """
        lines[start] = lines[start].replace("print('''", 'print("""')
        lines[end] = lines[end].replace("''')", '""")')
        new_type = 'double'
    else:
        # Change """ to '''
        lines[start] = lines[start].replace('print("""', "print('''")
        lines[end] = lines[end].replace('""")', "''')")
        new_type = 'single'

    return new_type


def fix_file(filename):
    """Main fix function"""
    print(f"\n{'='*70}")
    print(f"  Quote Delimiter Fix Utility")
    print(f"{'='*70}\n")

    if not os.path.exists(filename):
        print(f"✗ Error: File not found: {filename}")
        return False

    # Create backup
    backup = create_backup(filename)

    # Read file
    print(f"Reading {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"  Total lines: {len(lines):,}")

    # Find all print statements
    print("\nScanning for multi-line print statements...")
    statements = find_print_statements(lines)
    print(f"  Found {len(statements)} print statements")

    # Check for conflicts
    print("\nChecking for quote conflicts...")
    conflicts = []
    for stmt in statements:
        if check_for_conflicts(lines, stmt):
            conflicts.append(stmt)

    print(f"  Found {len(conflicts)} statements with conflicts")

    if not conflicts:
        print("\n✓ No conflicts found! File is clean.")
        return True

    # Fix conflicts
    print("\nApplying fixes...")
    fixes_applied = 0
    for stmt in conflicts:
        new_type = fix_statement(lines, stmt)
        fixes_applied += 1
        start_line = stmt['start'] + 1
        end_line = stmt['end'] + 1
        old_type = stmt['quote_type']
        print(f"  Fixed lines {start_line:,} to {end_line:,} ({old_type} → {new_type})")

    # Write fixed file
    print(f"\nWriting fixed file...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"\n{'='*70}")
    print(f"  ✓ Complete!")
    print(f"{'='*70}")
    print(f"\n  Fixes applied: {fixes_applied}")
    print(f"  Backup saved: {backup}")
    print(f"\nNext steps:")
    print(f"  1. Test file: python -m py_compile {filename}")
    print(f"  2. Run game: python {filename}")
    print(f"  3. If issues occur, restore from: {backup}")

    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_quotes.py <filename>")
        print("Example: python fix_quotes.py the_verdant_code_1.3.0.py")
        sys.exit(1)

    filename = sys.argv[1]
    success = fix_file(filename)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
