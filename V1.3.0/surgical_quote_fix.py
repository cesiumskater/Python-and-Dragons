#!/usr/bin/env python3
"""
Surgical fix for nested triple-quote issues
Only changes outer delimiters when conflicts detected
"""

import re

def find_teach_methods(content):
    """Find all teach() method boundaries"""
    pattern = r'(\s+def teach\(self\):.*?(?=\s+def\s|\Z))'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    return matches

def fix_teach_method(method_text):
    """Fix a single teach method if it has quote conflicts"""
    # Check if this teach method has print(''' ... ''') pattern
    if not ('print(' in method_text and "'''" in method_text):
        return method_text

    # Find first print statement
    print_match = re.search(r"print\('''", method_text)
    if not print_match:
        return method_text

    # Find the closing '''
    close_match = re.search(r"'''\)", method_text[print_match.end():])
    if not close_match:
        return method_text

    # Get the content between opening and closing
    start = print_match.end()
    end = print_match.end() + close_match.start()
    content_between = method_text[start:end]

    # Check if there are any ''' inside the content
    if "'''" in content_between:
        # Fix by changing outer quotes to """
        fixed = method_text[:print_match.start()] + 'print("""' + content_between + '""")' + method_text[end+3:]
        return fixed

    return method_text

def main():
    input_file = 'the_verdant_code_1.3.0.py'
    output_file = 'the_verdant_code_1.3.0_fixed.py'

    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Original size: {len(content):,} bytes")

    # Find all teach methods
    print("Finding teach() methods...")
    methods = find_teach_methods(content)
    print(f"Found {len(methods)} teach() methods")

    # Fix each method
    fixes = 0
    for match in reversed(methods):  # Reverse to maintain positions
        original = match.group(0)
        fixed = fix_teach_method(original)
        if fixed != original:
            content = content[:match.start()] + fixed + content[match.end():]
            fixes += 1
            print(f"Fixed teach() method at position {match.start()}")

    print(f"\nTotal fixes applied: {fixes}")

    # Write output
    print(f"Writing {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Done! Test with: python -m py_compile {output_file}")

if __name__ == '__main__':
    main()
