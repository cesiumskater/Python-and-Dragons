#!/usr/bin/env python3
"""
Ultra final fix - be very careful with escapes
"""

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original: {len(lines)} lines")

# Task 1: Remove duplicates
lines = lines[:120646] + lines[124727:]
print(f"After removing duplicates: {len(lines)} lines")

# Task 2: Update version
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

# Task 4: Fix escape sequences
# The issue: \""" is invalid. It should be just """
# When we're inside ''' strings, we don't need to escape """
# When we're inside """ strings, we don't need to escape '''
fixes = 0
for i in range(len(lines)):
    # Fix \""" -> """
    if '\\"""' in lines[i]:
        lines[i] = lines[i].replace('\\"""', '"""')
        fixes += 1
    # Also check for the version with single backslash
    if r'\"\"\"' in lines[i]:
        lines[i] = lines[i].replace(r'\"\"\"', '"""')
        fixes += 1

print(f"Fixed {fixes} backslash-quote issues")

# Write
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Written to: {output_path}")
