#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Escape all triple quotes in code examples

import re

def escape_quotes_in_examples(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: Find code examples with = ''' and replace with = \"\"\"
    # This handles cases like: variable = '''
    pattern = r"(\s+\w+\s*=\s*)'''"
    replacement = r'\1"""'

    new_content, count = re.subn(pattern, replacement, content)

    if count > 0:
        print(f"Replaced {count} instances of = ''' with = \"\"\"")

        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True
    else:
        print("No replacements needed")
        return False

if __name__ == '__main__':
    filename = 'the_verdant_code_1.2.2.py'
    print("=" * 70)
    print("  ESCAPING TRIPLE QUOTES IN CODE EXAMPLES")
    print("=" * 70)
    print()

    if escape_quotes_in_examples(filename):
        print("\nVerifying syntax...")
        import subprocess
        result = subprocess.run(['python', '-m', 'py_compile', filename],
                              capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            print("SUCCESS: File compiles without syntax errors!")
        else:
            print("Still has syntax errors:")
            print(result.stderr[:500])
    else:
        print("No changes made")
