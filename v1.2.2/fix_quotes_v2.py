#!/usr/bin/env python3
"""
Script to fix quote delimiter issues.
Simply replace all \\" with actual quotes.
"""

# Read the file
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh_fixed.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Count escaped quotes
escaped_count = content.count(r'\"')
print(f"Found {escaped_count} escaped double-quote characters (\\\")")

# Replace all \\" with "
content = content.replace(r'\"', '"')

print(f"Replaced all \\\" with \"")

# Write the fixed content
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh_fixed.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed file size: {len(content)} characters")
print("Fixed content written back to: the_verdant_code_fresh_fixed.py")
