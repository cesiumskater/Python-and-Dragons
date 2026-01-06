#!/usr/bin/env python3
"""Minimal fix - only touch what absolutely needs changing"""
import re

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original size: {len(content)} chars")

# 1. Remove duplicates
lines = content.split('\n')
lines = lines[:120646] + lines[124727:]
content = '\n'.join(lines)
print(f"Removed duplicates")

# 2. Update version
content = re.sub(r'^VERSION = .*$', 'VERSION = "1.3.0 Complete"', content, flags=re.MULTILINE)
content = re.sub(r'^RELEASE_TYPE = .*$', 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"', content, flags=re.MULTILINE)
content = re.sub(r'^TOPICS_COUNT = .*$', 'TOPICS_COUNT = 181', content, flags=re.MULTILINE)
content = re.sub(r'^TOTAL_XP_AVAILABLE = .*$', 'TOTAL_XP_AVAILABLE = 2715', content, flags=re.MULTILINE)
print("Updated version")

# 3. Add Act IX
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

# 4. The REAL fix: Use r-strings (raw strings) for all teach() methods
# Find all `print('''` and change to `print(r"""`
# Find all matching `''')` and change to `""")`
content = re.sub(r"print\('''", 'print(r"""', content)
content = re.sub(r"'''\)", '""")', content)
print("Changed print(triple-quote) to use raw strings")

# Write
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nWritten to: {output_path}")
print("Done!")
