#!/usr/bin/env python3
"""
Script to fix the_verdant_code_fresh.py
1. Remove duplicate lesson classes (lines 120647-124727)
2. Add Act IX to get_lesson_registry()
3. Update version info
4. Fix quote delimiter issues
"""

# Read the file
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original file has {len(lines)} lines")

# Task 1: Remove duplicate classes (lines 120647-124727)
# Python uses 0-based indexing, so line 120647 is index 120646
# We want to keep lines up to 120646 (inclusive) and skip 120647-124727, then continue from 124728
start_delete = 120646  # line 120647 in 1-based
end_delete = 124727    # line 124727 in 1-based (inclusive)

# Keep everything before the duplicate section and everything after
lines_fixed = lines[:start_delete] + lines[end_delete:]

print(f"After removing duplicates: {len(lines_fixed)} lines")
print(f"Removed {len(lines) - len(lines_fixed)} lines")

# Task 2: Update version info (around lines 63-67)
for i in range(len(lines_fixed)):
    if lines_fixed[i].startswith('VERSION = '):
        lines_fixed[i] = 'VERSION = "1.3.0 Complete"\n'
        print(f"Updated VERSION at line {i+1}")
    elif lines_fixed[i].startswith('RELEASE_TYPE = '):
        lines_fixed[i] = 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"\n'
        print(f"Updated RELEASE_TYPE at line {i+1}")
    elif lines_fixed[i].startswith('TOPICS_COUNT = '):
        lines_fixed[i] = 'TOPICS_COUNT = 181\n'
        print(f"Updated TOPICS_COUNT at line {i+1}")
    elif lines_fixed[i].startswith('TOTAL_XP_AVAILABLE = '):
        lines_fixed[i] = 'TOTAL_XP_AVAILABLE = 2715\n'
        print(f"Updated TOTAL_XP_AVAILABLE at line {i+1}")

# Task 3: Add Act IX to get_lesson_registry()
# Find the line with "# Act 9 can be added if needed" and replace that section
for i in range(len(lines_fixed)):
    if '# Act 9 can be added if needed' in lines_fixed[i]:
        # Replace this line with Act 9 lessons
        act9_content = '''        9: [  # Act IX: The Master's Ascension (Advanced Python Mastery) - COMPLETE
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
        lines_fixed[i] = act9_content
        print(f"Added Act IX to get_lesson_registry() at line {i+1}")
        break

# Write the fixed content
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh_fixed.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines_fixed)

print(f"\nFixed file written to: {output_path}")
print(f"Total lines in fixed file: {len(lines_fixed)}")
