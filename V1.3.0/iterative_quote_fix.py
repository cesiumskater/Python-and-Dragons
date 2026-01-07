#!/usr/bin/env python3
"""
Iterative Quote Fix - keeps fixing until no more fixes are needed
"""

def fix_quotes_once(filename):
    """Run one pass of quote fixes, return number of fixes made"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixes_made = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Find print statements with triple single quotes
        if "print('''" in line:
            # Find the closing
            j = i + 1
            has_internal_triple_single = False

            while j < len(lines) and j < i + 3000:
                # Check for internal triple single quotes
                if "'''" in lines[j] and j != i:
                    has_internal_triple_single = True

                # Check for closing
                if "''')" in lines[j]:
                    if has_internal_triple_single:
                        # Fix it
                        lines[i] = lines[i].replace("print('''", 'print("""', 1)
                        lines[j] = lines[j].replace("''')", '""")', 1)
                        fixes_made += 1
                    break
                j += 1
            i = j if j < len(lines) else i + 1
        else:
            i += 1

    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return fixes_made

def main():
    filename = "the_verdant_code_1.3.0.py"

    print(f"Iterative Quote Fix for {filename}")
    print("=" * 60)

    total_fixes = 0
    iteration = 1

    while True:
        print(f"\nIteration {iteration}...", end=" ")
        fixes = fix_quotes_once(filename)
        total_fixes += fixes
        print(f"{fixes} fixes")

        if fixes == 0:
            break

        iteration += 1

        if iteration > 20:  # Safety limit
            print("\nReached iteration limit!")
            break

    print(f"\n{'=' * 60}")
    print(f"Complete! Total fixes across all iterations: {total_fixes}")
    print(f"\nTest with: python -m py_compile {filename}")

if __name__ == "__main__":
    main()
