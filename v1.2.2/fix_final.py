#!/usr/bin/env python3
"""
Final comprehensive fix script
"""
import re

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original: {len(lines)} lines")

# Task 1: Remove duplicates (lines 120647-124727, indices 120646-124726)
lines = lines[:120646] + lines[124727:]
print(f"After removing duplicates: {len(lines)} lines")

# Task 2: Update version info
for i in range(min(100, len(lines))):
    if lines[i].startswith('VERSION = '):
        lines[i] = 'VERSION = "1.3.0 Complete"\n'
    elif lines[i].startswith('RELEASE_TYPE = '):
        lines[i] = 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"\n'
    elif lines[i].startswith('TOPICS_COUNT = '):
        lines[i] = 'TOPICS_COUNT = 181\n'
    elif lines[i].startswith('TOTAL_XP_AVAILABLE = '):
        lines[i] = 'TOTAL_XP_AVAILABLE = 2715\n'

# Task 3: Add Act IX
for i in range(len(lines)):
    if '# Act 9 can be added if needed' in lines[i]:
        lines[i] = '''        9: [  # Act IX: The Master's Ascension (Advanced Python Mastery) - COMPLETE
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
        break

# Task 4: Fix the escaped quote issues
# Pattern: \""" should be """ (when inside ''' strings)
# Pattern: \' should be ' (when inside """ strings)
fixes = 0
for i in range(len(lines)):
    original = lines[i]
    # Fix \""" to """
    if r'\"\"\"' in lines[i]:
        lines[i] = lines[i].replace(r'\"\"\"', '"""')
        fixes += 1
    # Fix \' to ' in specific contexts
    if r"\'" in lines[i] and 'not escaped' not in lines[i]:
        # Only fix if it's clearly wrong (check context)
        if "use '" in lines[i] or "like '" in lines[i]:
            lines[i] = lines[i].replace(r"\'", "'")
            fixes += 1

print(f"Fixed {fixes} escaped quote issues")

# Write output
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
print(f"\nWriting to: {output_path}")
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")
