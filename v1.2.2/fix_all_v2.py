#!/usr/bin/env python3
"""
Comprehensive fix script - version 2
This time we'll be more careful about what we fix.
"""
import re

print("Reading original file...")
with open(r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_fresh.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file: {len(content)} characters")

# Task 1: Remove duplicate classes
# Find the exact positions
lines = content.split('\n')
print(f"Original lines: {len(lines)}")

# Remove lines 120647-124727 (1-indexed) = indices 120646-124726 (0-indexed)
# Keep lines 0-120645 and 124727+
lines_fixed = lines[:120646] + lines[124727:]
print(f"After removing duplicates: {len(lines_fixed)} lines")

# Join back
content = '\n'.join(lines_fixed)

# Task 2: Update version info
content = re.sub(r'^VERSION = .*$', 'VERSION = "1.3.0 Complete"', content, flags=re.MULTILINE)
content = re.sub(r'^RELEASE_TYPE = .*$', 'RELEASE_TYPE = "Acts 0-IX Complete (181 Lessons)"', content, flags=re.MULTILINE)
content = re.sub(r'^TOPICS_COUNT = .*$', 'TOPICS_COUNT = 181', content, flags=re.MULTILINE)
content = re.sub(r'^TOTAL_XP_AVAILABLE = .*$', 'TOTAL_XP_AVAILABLE = 2715', content, flags=re.MULTILINE)
print("Updated version info")

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
print("Added Act IX to registry")

# Task 4: DON'T change quotes - the file is already correct
# The issue is that we should use r-strings or different delimiters
# But actually the original file has proper escaping with \"\"\"
# Let's not touch the quotes at all

# Write output
output_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py'
print(f"\nWriting to: {output_path}")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! Output file written")
print("\nNOTE: Quote delimiters left as-is from original (with proper escaping)")
