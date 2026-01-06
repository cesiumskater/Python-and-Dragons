#!/usr/bin/env python3
"""
Fix ALL print statements with triple quotes
"""

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content)} bytes")

# Task 1: Remove duplicates
lines = content.split('\n')
lines = lines[:120646] + lines[124727:]
content = '\n'.join(lines)

# Task 2: Update version
import re
content = re.sub(r'^VERSION = .*$', 'VERSION = "1.3.0 Complete"', content, flags=re.MULTILINE)
content = re.sub(r'^RELEASE_TYPE = .*$', 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"', content, flags=re.MULTILINE)
content = re.sub(r'^TOPICS_COUNT = .*$', 'TOPICS_COUNT = 181', content, flags=re.MULTILINE)
content = re.sub(r'^TOTAL_XP_AVAILABLE = .*$', 'TOTAL_XP_AVAILABLE = 2715', content, flags=re.MULTILINE)

# Task 3: Add Act IX
content = content.replace(
    '        # Act 9 can be added if needed',
    '''        9: [  # Act IX: The Master's Ascension (Advanced Python Mastery) - COMPLETE
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
        ],'''
)

# Task 4: Fix ALL print(''' statements
# Replace print(''' with print("""
count1 = content.count("print('''")
content = content.replace("print('''", 'print("""')
print(f"Changed {count1} occurrences of print(triple-single-quote) to print(triple-double-quote)")

# Now fix the closing quotes
# We need to be careful - only change '''

) that close a print statement
# Strategy: Replace ''')\n with """)\n  (most common pattern)
count2 = content.count("''')\n")
content = content.replace("''')\n", '""")\n')
count3 = content.count("        ''')")
content = content.replace("        ''')", '        """)')
print(f"Changed {count2 + count3} closing triple-single-quotes to triple-double-quotes")

# Task 5: Fix escaped quotes
count4 = content.count('\\"""')
content = content.replace('\\"""', '"""')
print(f"Fixed {count4} escaped triple-double-quotes")

# Write
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nWritten to: {output_path}")
print(f"Output size: {len(content)} bytes")
