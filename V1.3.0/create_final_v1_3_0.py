#!/usr/bin/env python3
"""
Create Final Working v1.3.0 of The Verdant Code
Applies all necessary fixes to create a fully functional version
"""

def main():
    import re

    print("=" * 70)
    print("Creating The Verdant Code v1.3.0")
    print("=" * 70)

    # Step 1: Read the clean backup
    backup_path = r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_1.2.2.py.backup_before_dedup_fix'

    print("\n[1/7] Reading original backup file...")
    with open(backup_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"   Original lines: {len(lines):,}")

    # Step 2: Remove duplicate classes (lines 120646-124727)
    print("\n[2/7] Removing 7 duplicate lesson classes...")
    # Convert to 0-based indexing
    del lines[120645:124726]
    print(f"   Lines after removal: {len(lines):,}")
    print(f"   Removed ~4,081 duplicate lines")

    # Step 3: Update version information
    print("\n[3/7] Updating version information...")
    for i, line in enumerate(lines):
        if line.strip().startswith('VERSION = '):
            lines[i] = 'VERSION = "1.3.0"\n'
            print(f"   Updated VERSION at line {i+1}")
        elif line.strip().startswith('RELEASE_TYPE = '):
            lines[i] = 'RELEASE_TYPE = "Acts 0-IX Complete (All 181 Lessons)"\n'
            print(f"   Updated RELEASE_TYPE at line {i+1}")
        elif line.strip().startswith('TOPICS_COUNT = '):
            lines[i] = 'TOPICS_COUNT = 181\n'
            print(f"   Updated TOPICS_COUNT at line {i+1}")
        elif line.strip().startswith('TOTAL_XP_AVAILABLE = '):
            lines[i] = 'TOTAL_XP_AVAILABLE = 2715\n'
            print(f"   Updated TOTAL_XP_AVAILABLE at line {i+1}")

    # Step 4: Add Act IX to lesson registry
    print("\n[4/7] Registering Act IX lessons...")
    registry_found = False
    for i, line in enumerate(lines):
        if 'def get_lesson_registry():' in line:
            # Find where Act 8 ends
            for j in range(i, min(i + 500, len(lines))):
                # Look for the end of Act 8
                if '8: [' in ''.join(lines[max(0, j-20):j+1]) and '],\n' == lines[j]:
                    act_ix_block = """        9: [  # Act IX: The Master's Path (Advanced Python Mastery)
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
"""
                    lines.insert(j + 1, act_ix_block)
                    print(f"   Act IX registered at line {j+2}")
                    registry_found = True
                    break
            break

    if not registry_found:
        print("   WARNING: Could not find lesson registry!")

    # Step 5: Fix quote delimiter issues
    print("\n[5/7] Fixing quote delimiter conflicts...")
    fixes_made = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Find print statements with triple single quotes
        if "print('''" in line:
            # Find the closing
            j = i + 1
            has_internal_triple_single = False

            while j < len(lines) and j < i + 3000:
                # Check for internal triple single quotes (not at start of print)
                if "'''" in lines[j] and j != i:
                    has_internal_triple_single = True

                # Check for closing
                if "''')" in lines[j]:
                    if has_internal_triple_single:
                        # Fix by changing to triple double quotes
                        lines[i] = lines[i].replace("print('''", 'print("""')
                        lines[j] = lines[j].replace("''')", '""")')
                        fixes_made += 1
                        if fixes_made <= 10:  # Only print first 10
                            print(f"   Fixed quote conflict: lines {i+1} to {j+1}")
                    break
                j += 1
            i = j if j < len(lines) else i + 1
        else:
            i += 1

    print(f"   Total quote fixes applied: {fixes_made}")

    # Step 6: Fix escaped triple quotes that shouldn't be escaped
    print("\n[6/7] Fixing escaped quotes in content...")
    content = ''.join(lines)

    # Replace \""" with """ (was incorrectly escaped in original)
    escaped_count = content.count('\\"\\"\\"')
    content = content.replace('\\"\\"\\"', '"""')
    print(f"   Fixed {escaped_count} escaped triple-quote sequences")

    lines = content.split('\n')
    # Re-add newlines
    lines = [line + '\n' for line in lines[:-1]] + [lines[-1]]

    # Step 7: Write output
    output_path = 'the_verdant_code_1.3.0.py'
    print(f"\n[7/7] Writing {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"   Final size: {len(lines):,} lines")
    print(f"   File written successfully!")

    print("\n" + "=" * 70)
    print("v1.3.0 Creation Complete!")
    print("=" * 70)
    print(f"\nFile: {output_path}")
    print(f"Lessons: 181 (Acts 0-IX)")
    print(f"Total XP: 2,715")
    print(f"\nNext: python -m py_compile {output_path}")

if __name__ == '__main__':
    main()
