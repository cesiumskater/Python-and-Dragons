#!/usr/bin/env python3
"""
Fix teach() methods: change print with triple single quotes to triple double quotes.
This is needed because the content contains triple single quote examples.
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

# Task 4: Fix ALL teach() methods - change ''' to """
print("\nFixing teach() methods...")
in_teach = False
teach_start_line = -1
fixes = 0

for i in range(len(lines)):
    # Detect def teach(self):
    if 'def teach(self):' in lines[i]:
        in_teach = True
        teach_start_line = i
        continue

    # If we're in a teach method, look for print(''' and change to print("""
    if in_teach and "print('''" in lines[i]:
        lines[i] = lines[i].replace("print('''", 'print("""')
        fixes += 1
        # Now find the matching closing ''') and change to """)
        # Search forward from here
        for j in range(i+1, min(i+1000, len(lines))):
            if "''')" in lines[j] and 'print' not in lines[j]:
                # This is likely the closing quote
                lines[j] = lines[j].replace("''')", '""")')
                fixes += 1
                in_teach = False
                break

    # Also exit teach method if we hit another def
    if in_teach and i > teach_start_line + 1 and lines[i].strip().startswith('def '):
        in_teach = False

print(f"Fixed {fixes} teach() method quote pairs")

# Task 5: Fix the escaped quotes (\" should just be ")
escape_fixes = 0
for i in range(len(lines)):
    if '\\"""' in lines[i]:
        lines[i] = lines[i].replace('\\"""', '"""')
        escape_fixes += 1

print(f"Fixed {escape_fixes} escaped quote sequences")

# Write
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nWritten to: {output_path}")
print("Done!")
