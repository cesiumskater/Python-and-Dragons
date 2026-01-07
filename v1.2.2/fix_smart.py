#!/usr/bin/env python3
"""Smart fix that handles quotes carefully"""

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original: {len(lines)} lines")

# Remove duplicates
lines = lines[:120646] + lines[124727:]
print(f"After removing duplicates: {len(lines)} lines")

# Update version
for i in range(min(100, len(lines))):
    if lines[i].startswith('VERSION = '):
        lines[i] = 'VERSION = "1.3.0 Complete"\n'
    elif lines[i].startswith('RELEASE_TYPE = '):
        lines[i] = 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"\n'
    elif lines[i].startswith('TOPICS_COUNT = '):
        lines[i] = 'TOPICS_COUNT = 181\n'
    elif lines[i].startswith('TOTAL_XP_AVAILABLE = '):
        lines[i] = 'TOTAL_XP_AVAILABLE = 2715\n'

# Add Act IX
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

print("Updated metadata")

# Smart quote replacement
# Only replace ''' when it's a string delimiter, not when it's inside strings
fixes = 0
for i in range(len(lines)):
    line = lines[i]

    # Skip lines that are clearly inside list definitions with quoted strings
    # e.g., "text with ''' inside"
    if line.strip().startswith('"') and "'''" in line and line.strip().endswith('",'):
        # This is a list item - don't replace ''' inside it
        continue

    # Replace ''' with """
    if "'''" in line:
        lines[i] = line.replace("'''", '"""')
        fixes += 1

print(f"Replaced ''' with \"\"\" in {fixes} lines")

# Fix escaped quotes
escape_fixes = 0
for i in range(len(lines)):
    if '\\"""' in lines[i]:
        lines[i] = lines[i].replace('\\"""', '"""')
        escape_fixes += 1

print(f"Fixed {escape_fixes} escaped quotes")

# Write
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nWritten to: {output_path}")
print("Done!")
