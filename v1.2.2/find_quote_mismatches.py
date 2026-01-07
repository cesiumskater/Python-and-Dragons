#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Find all quote mismatches in the file

import re

def find_mismatches(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    mismatches = []
    triple_single = "'" * 3
    triple_double = '"' * 3

    i = 0
    while i < len(lines):
        line = lines[i]

        if ("= f" + triple_single) in line or ("= " + triple_single) in line:
            start_line = i + 1
            j = i + 1
            found_close = False
            while j < len(lines):
                if triple_double in lines[j] and triple_single not in lines[j]:
                    mismatches.append({
                        'start': start_line,
                        'end': j + 1,
                        'start_text': line.strip(),
                        'end_text': lines[j].strip(),
                        'type': 'Mismatched closing quote'
                    })
                    found_close = True
                    break
                elif triple_single in lines[j] and j != i:
                    found_close = True
                    break
                j += 1

                if j - i > 100:
                    break

            if not found_close:
                mismatches.append({
                    'start': start_line,
                    'end': None,
                    'start_text': line.strip(),
                    'end_text': None,
                    'type': 'Unclosed quote'
                })

        i += 1

    return mismatches

if __name__ == '__main__':
    filename = 'the_verdant_code_1.2.2.py'
    print("=" * 70)
    print("  QUOTE MISMATCH FINDER")
    print("=" * 70)

    mismatches = find_mismatches(filename)

    if mismatches:
        print(f"\nFound {len(mismatches)} potential quote mismatches:\n")
        for i, mismatch in enumerate(mismatches, 1):
            print(f"{i}. {mismatch['type']}")
            print(f"   Start line {mismatch['start']}: {mismatch['start_text']}")
            if mismatch['end']:
                print(f"   End line {mismatch['end']}: {mismatch['end_text']}")
            print()
    else:
        print("\nNo obvious mismatches found!")
