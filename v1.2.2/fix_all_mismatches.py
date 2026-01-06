#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fix all identified quote mismatches

def fix_mismatches(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Mismatches to fix (line numbers are 1-indexed)
    fixes = [
        (4125, '"""', "'''"),  # story example
        (7345, '"""', "'''"),  # f-string message
        (16681, '"""', "'''"), # f-string message
        (97446, '"""', "'''"), # exclude variable
        (100501, '"""', "'''"),# setup variable
        (104158, '"""', "'''") # log variable
    ]

    total_fixed = 0
    for line_num, old_quote, new_quote in fixes:
        idx = line_num - 1  # Convert to 0-indexed
        if idx < len(lines):
            if old_quote in lines[idx]:
                lines[idx] = lines[idx].replace(old_quote, new_quote)
                total_fixed += 1
                print(f"Fixed line {line_num}: {old_quote} -> {new_quote}")

    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"\nTotal fixes applied: {total_fixed}")
    return total_fixed

if __name__ == '__main__':
    filename = 'the_verdant_code_1.2.2.py'
    print("=" * 70)
    print("  FIXING ALL QUOTE MISMATCHES")
    print("=" * 70)
    print()

    fix_mismatches(filename)

    print("\nDone! Now verifying syntax...")
    import subprocess
    result = subprocess.run(['python', '-m', 'py_compile', filename],
                          capture_output=True, text=True, timeout=10)
    if result.returncode == 0:
        print("SUCCESS: File compiles without syntax errors!")
    else:
        print("ERROR: Still has syntax errors:")
        print(result.stderr)
