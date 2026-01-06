#!/usr/bin/env python3
"""
Find all quote mismatches in print statements
"""

def main():
    filename = "the_verdant_code_1.3.0.py"

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print("Finding quote mismatches...")
    print("=" * 70)

    mismatches = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for print("""
        if 'print("""' in line:
            start = i
            j = i + 1
            found_close = False

            while j < len(lines) and j < i + 3000:
                if '""")' in lines[j]:
                    found_close = True
                    break
                elif "''')" in lines[j]:
                    # Mismatch!
                    mismatches.append((start + 1, j + 1, '"""', "'''"))
                    found_close = True
                    break
                j += 1

            if not found_close:
                mismatches.append((start + 1, min(i + 3000, len(lines)), '"""', 'NOT FOUND'))

            i = j if j < len(lines) else i + 1

        # Check for print('''
        elif "print('''" in line:
            start = i
            j = i + 1
            found_close = False

            while j < len(lines) and j < i + 3000:
                if "''')" in lines[j]:
                    found_close = True
                    break
                elif '""")' in lines[j]:
                    # Mismatch!
                    mismatches.append((start + 1, j + 1, "'''", '"""'))
                    found_close = True
                    break
                j += 1

            if not found_close:
                mismatches.append((start + 1, min(i + 3000, len(lines)), "'''", 'NOT FOUND'))

            i = j if j < len(lines) else i + 1
        else:
            i += 1

    if mismatches:
        print(f"Found {len(mismatches)} mismatched print statements:\n")
        for start, end, open_q, close_q in mismatches[:20]:  # Show first 20
            print(f"  Lines {start:5} to {end:5}: opened with {open_q}, closed with {close_q}")

        # Now fix them
        print(f"\n{'=' * 70}")
        print("Fixing mismatches...")

        fixes = 0
        for start, end, open_q, close_q in mismatches:
            if close_q in ['"""', "'''"]:  # Skip "NOT FOUND" cases
                # Fix by changing the closer to match the opener
                if open_q == '"""' and close_q == "'''":
                    lines[end - 1] = lines[end - 1].replace("''')", '""")', 1)
                    fixes += 1
                elif open_q == "'''" and close_q == '"""':
                    lines[end - 1] = lines[end - 1].replace('""")', "''')", 1)
                    fixes += 1

        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print(f"Applied {fixes} fixes")
    else:
        print("No mismatches found!")

    print(f"\nTest with: python -m py_compile {filename}")

if __name__ == "__main__":
    main()
