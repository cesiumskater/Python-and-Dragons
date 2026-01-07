#!/usr/bin/env python3
"""
Simple Quote Fix for The Verdant Code
Fixes the most common quote delimiter issues
"""

import sys

def main():
    filename = "the_verdant_code_1.3.0_clean.py"

    print("Reading file...")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines):,}")

    fixes_made = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Find print statements with triple single quotes
        if "print('''" in line:
            # Find the closing
            j = i + 1
            has_internal_triple = False

            while j < len(lines) and j < i + 3000:
                # Check for internal triple quotes
                if "'''" in lines[j] and j != i:
                    has_internal_triple = True

                # Check for closing
                if "''')" in lines[j]:
                    if has_internal_triple:
                        # Fix it
                        lines[i] = lines[i].replace("print('''", 'print("""')
                        lines[j] = lines[j].replace("''')", '""")')
                        fixes_made += 1
                        print(f"Fixed lines {i+1} to {j+1}")
                    break
                j += 1
            i = j if j < len(lines) else i + 1
        else:
            i += 1

    print(f"\nFixes applied: {fixes_made}")

    # Write back
    print("Writing fixed file...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Done!")

if __name__ == "__main__":
    main()
