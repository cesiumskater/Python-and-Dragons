#!/usr/bin/env python3
# Final comprehensive quote fix - escape all ''' in code examples within print blocks

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Specific fixes based on what we found
    fixes = [
        # Line 4121-4125: story example - need to escape
        (4121, "    story = '''\n", "    story = \\'''\n"),
        (4125, "    '''\n", "    \\'''\n"),

        # Line 97439-97446: exclude example
        (97439, "    exclude = '''\n", "    exclude = \\'''\n"),
        (97446, "    '''\n", "    \\'''\n"),

        # Line 100499-100501: setup example
        (100499, "    setup = '''\n", "    setup = \\'''\n"),
        (100501, "    '''\n", "    \\'''\n"),

        # Line 104154-104158: log example
        (104154, "    log = '''\n", "    log = \\'''\n"),
        (104158, "    '''\n", "    \\'''\n"),

        # Line 104187-104191: save_text example
        (104187, "    save_text = '''\n", "    save_text = \\'''\n"),
        (104191, "    '''\n", "    \\'''\n"),
    ]

    fixed = 0
    for line_num, expected, replacement in fixes:
        idx = line_num - 1
        if idx < len(lines) and lines[idx] == expected:
            lines[idx] = replacement
            fixed += 1
            print(f"Fixed line {line_num}")
        else:
            print(f"WARNING: Line {line_num} didn't match expected content")
            if idx < len(lines):
                print(f"  Expected: {repr(expected)}")
                print(f"  Found: {repr(lines[idx])}")

    if fixed > 0:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"\nTotal lines fixed: {fixed}")
        return True
    return False

if __name__ == '__main__':
    filename = 'the_verdant_code_1.2.2.py'
    print("=" * 70)
    print("  FINAL QUOTE FIX")
    print("=" * 70)
    print()

    if fix_file(filename):
        print("\nVerifying syntax...")
        import subprocess
        result = subprocess.run(['python', '-m', 'py_compile', filename],
                              capture_output=True, text=True, timeout=20)
        if result.returncode == 0:
            print("\nSUCCESS: File compiles without syntax errors!")
        else:
            print("\nStill has errors:")
            print(result.stderr[:1000])
