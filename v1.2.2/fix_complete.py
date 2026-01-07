#!/usr/bin/env python3
"""Fix all issues in the_verdant_code_fresh.py"""

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content)} bytes")

# Remove duplicates
lines = content.split('\n')
lines = lines[:120646] + lines[124727:]
content = '\n'.join(lines)
print("Removed duplicate classes")

# Update version
import re
content = re.sub(r'^VERSION = .*$', 'VERSION = "1.3.0 Complete"', content, flags=re.MULTILINE)
content = re.sub(r'^RELEASE_TYPE = .*$', 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"', content, flags=re.MULTILINE)
content = re.sub(r'^TOPICS_COUNT = .*$', 'TOPICS_COUNT = 181', content, flags=re.MULTILINE)
content = re.sub(r'^TOTAL_XP_AVAILABLE = .*$', 'TOTAL_XP_AVAILABLE = 2715', content, flags=re.MULTILINE)
print("Updated version info")

# Add Act IX
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
print("Added Act IX")

# Fix ALL triple-single-quote strings to triple-double-quotes
# This is needed because content contains triple-single-quote examples
count1 = content.count("'''")
content = content.replace("'''", '"""')
print(f"Replaced all {count1} triple-single-quotes with triple-double-quotes")

# Fix escaped quotes
count4 = content.count('\\"""')
content = content.replace('\\"""', '"""')
print(f"Fixed {count4} escaped quotes")

# Write output
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nWritten to: {output_path}")
print(f"Output size: {len(content)} bytes")
print("Done!")
