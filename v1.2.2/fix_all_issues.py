#!/usr/bin/env python3
"""
Comprehensive fix script for the_verdant_code_fresh.py
"""
import re

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_work.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original file: {len(lines)} lines")

# Task 1: Remove duplicate classes (lines 120647-124727, 0-indexed: 120646-124726)
start_delete = 120646
end_delete = 124727
lines_fixed = lines[:start_delete] + lines[end_delete:]
print(f"After removing duplicates: {len(lines_fixed)} lines (removed {len(lines) - len(lines_fixed)} lines)")

# Task 2: Update version info
for i in range(min(100, len(lines_fixed))):
    if lines_fixed[i].startswith('VERSION = '):
        lines_fixed[i] = 'VERSION = "1.3.0 Complete"\n'
    elif lines_fixed[i].startswith('RELEASE_TYPE = '):
        lines_fixed[i] = 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"\n'
    elif lines_fixed[i].startswith('TOPICS_COUNT = '):
        lines_fixed[i] = 'TOPICS_COUNT = 181\n'
    elif lines_fixed[i].startswith('TOTAL_XP_AVAILABLE = '):
        lines_fixed[i] = 'TOTAL_XP_AVAILABLE = 2715\n'

# Task 3: Add Act IX to registry
for i in range(len(lines_fixed)):
    if '# Act 9 can be added if needed' in lines_fixed[i]:
        lines_fixed[i] = '''        9: [  # Act IX: The Master's Ascension (Advanced Python Mastery) - COMPLETE
            MetaclassesLesson(),
            DescriptorsLesson(),
            ASTLesson(),
            ProtocolsLesson(),
            AsyncFoundationsLesson(),
            AsyncAdvancedLesson(),
            GeneratorsAdvancedLesson(),
            ContextManagersAdvancedLesson(),
            DesignPatternsCreationalLesson(),
            DesignPatternsStructuralLesson(),
            DesignPatternsBehavioralLesson(),
            DesignPatternsFunctionalLesson(),
            MemoryManagementLesson(),
            PerformanceOptimizationLesson(),
            SecurityBestPracticesLesson(),
            ArchitecturePatternsLesson(),
            ConcurrencyPatternsLesson(),
            DistributedSystemsLesson(),
            FinalBattlePartOneLesson(),
            FinalBattlePartTwoLesson(),
        ],
'''
        print(f"Added Act IX at line {i+1}")
        break

# Task 4: Fix quote issues in teach() methods
# The issue is: print('''...text with ''' inside...''')
# We need to find teach() methods and change outer ''' to """
print("\nSearching for teach() methods with quote issues...")

in_teach_method = False
teach_start = -1
quote_fixes = 0

i = 0
while i < len(lines_fixed):
    line = lines_fixed[i]

    # Detect start of teach() method with print('''
    if 'def teach(self):' in line:
        # Check if next few lines have print('''
        for j in range(i+1, min(i+5, len(lines_fixed))):
            if "print('''" in lines_fixed[j]:
                in_teach_method = True
                teach_start = j
                # Change ''' to """
                lines_fixed[j] = lines_fixed[j].replace("print('''", 'print("""')
                quote_fixes += 1
                break

    # If we're in a teach method with """, find the closing ''' and change to """
    if in_teach_method:
        # Look for closing ''')
        if "''')" in line and teach_start != i:
            # This is likely the closing quote
            lines_fixed[i] = lines_fixed[i].replace("''')", '""")')
            quote_fixes += 1
            in_teach_method = False
            teach_start = -1

    i += 1

print(f"Fixed {quote_fixes} quote delimiters in teach() methods")

# Write output
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
print(f"\nWriting to: {output_path}")
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines_fixed)

print(f"Done! Output file: {len(lines_fixed)} lines")
