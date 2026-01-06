#!/usr/bin/env python3
# Fix mismatched quote delimiters in multi-line print statements
# Finds print(OPEN_QUOTE ... CLOSE_QUOTE) mismatches and fixes them

def fix_mismatched_quotes(filename):
    print(f"Reading {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines):,}")
    fixes = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for print statement with triple double quotes
        if 'print("""' in line:
            # Find the closing
            j = i + 1
            while j < len(lines) and j < i + 5000:
                if '""")' in lines[j]:
                    # Found matching close
                    break
                elif "''')" in lines[j]:
                    # Found mismatched close - fix it
                    lines[j] = lines[j].replace("''')", '""")')
                    fixes += 1
                    print(f"Fixed mismatch at lines {i+1} to {j+1}: ''' -> \"\"\"")
                    break
                j += 1
            i = j if j < len(lines) else i + 1

        # Check for print statement with triple single quotes
        elif "print('''" in line:
            # Find the closing
            j = i + 1
            while j < len(lines) and j < i + 5000:
                if "''')" in lines[j]:
                    # Found matching close
                    break
                elif '""")' in lines[j]:
                    # Found mismatched close - fix it
                    lines[j] = lines[j].replace('""")', "''')")
                    fixes += 1
                    print(f"Fixed mismatch at lines {i+1} to {j+1}: \"\"\" -> '''")
                    break
                j += 1
            i = j if j < len(lines) else i + 1
        else:
            i += 1

    print(f"\nTotal fixes applied: {fixes}")

    # Write back
    print(f"Writing fixed file...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Done!")
    print(f"Test with: python -m py_compile {filename}")

if __name__ == "__main__":
    fix_mismatched_quotes("the_verdant_code_master.py")
