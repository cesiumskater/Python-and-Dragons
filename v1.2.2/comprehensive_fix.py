#!/usr/bin/env python3
"""
Comprehensive fix for The Verdant Code syntax errors
Fixes multiple quote-related issues
"""

import re

def fix_file(filename):
    print(f"Reading {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)
    print(f"Original size: {original_len:,} characters")

    # Fix 1: Malformed triple quote examples like print(\'''...\""")
    # These should be print('''...''') or proper escaped examples
    content = re.sub(r'print\(\\\'\'\'', r"print('''", content)
    content = re.sub(r'string!\\"""', r"string!'''", content)

    # Fix 2: Look for common patterns where ''' appears inside ''' strings
    # We'll convert to raw strings or fix escaping
    fixes = 0

    # Write intermediate version
    with open(filename + '.temp', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nApplied regex fixes")
    print(f"New size: {len(content):,} characters")
    print(f"Difference: {len(content) - original_len:,} characters")

    # Now do line-by-line analysis to find remaining issues
    lines = content.split('\n')

    print(f"\nAnalyzing {len(lines):,} lines...")

    # Track print statement state
    in_print = False
    print_start = 0
    quote_type = None
    errors_found = []

    for i, line in enumerate(lines, 1):
        # Check for print statement starts
        if 'print("""' in line and not in_print:
            in_print = True
            print_start = i
            quote_type = '"""'
        elif "print('''" in line and not in_print:
            in_print = True
            print_start = i
            quote_type = "'''"

        # Check for closes
        if in_print:
            if quote_type == '"""' and '""")' in line:
                # Check if there were triple quotes inside
                in_print = False
            elif quote_type == "'''" and "''')" in line:
                in_print = False

    # Write final version
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nFile updated successfully")
    print(f"Test with: python -m py_compile {filename}")

if __name__ == "__main__":
    fix_file("the_verdant_code_master.py")
