"""
Comprehensive Test Suite for The Verdant Code v1.2.2
Tests syntax, imports, lesson registry, instantiation, and data integrity.
"""

import sys
import os
import py_compile
import importlib.util
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if sys.platform == "win32":
    os.system("")  # Enable ANSI escape sequences
    sys.stdout.reconfigure(encoding='utf-8')

# Test configuration
GAME_FILE = r"C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_1.2.2.py"
EXPECTED_LESSON_COUNTS = {
    0: 6,
    1: 16,
    2: 24,
    3: 19,
    4: 15,
    5: 19,
    6: 20,
    7: 12,
    8: 30,
    9: 20
}
EXPECTED_TOTAL = 181

class TestReport:
    def __init__(self):
        self.tests = []
        self.start_time = datetime.now()

    def add_result(self, test_name, passed, details="", error=None):
        self.tests.append({
            'name': test_name,
            'passed': passed,
            'details': details,
            'error': str(error) if error else None
        })

    def print_report(self):
        print("\n" + "="*80)
        print("COMPREHENSIVE TEST REPORT - The Verdant Code v1.2.2")
        print("="*80)
        print(f"Test Time: {datetime.now()}")
        print(f"Duration: {(datetime.now() - self.start_time).total_seconds():.2f} seconds")
        print("="*80 + "\n")

        passed_count = sum(1 for t in self.tests if t['passed'])
        total_count = len(self.tests)

        for i, test in enumerate(self.tests, 1):
            status = "✓ PASS" if test['passed'] else "✗ FAIL"
            print(f"{i}. {test['name']}: {status}")
            if test['details']:
                print(f"   {test['details']}")
            if test['error']:
                print(f"   Error: {test['error']}")
            print()

        print("="*80)
        print(f"SUMMARY: {passed_count}/{total_count} tests passed")
        print("="*80)

        if passed_count == total_count:
            print("\n🎉 ALL TESTS PASSED - FILE IS READY FOR PRODUCTION 🎉\n")
            return True
        else:
            print(f"\n⚠ {total_count - passed_count} TEST(S) FAILED - PLEASE REVIEW ⚠\n")
            return False

def test_1_syntax_check(report):
    """Test 1: Syntax Check"""
    print("Running Test 1: Syntax Check...")
    try:
        py_compile.compile(GAME_FILE, doraise=True)
        report.add_result("Syntax Check", True, "No syntax errors found")
        return True
    except py_compile.PyCompileError as e:
        report.add_result("Syntax Check", False, error=e)
        return False

def test_2_import_test(report):
    """Test 2: Import Test"""
    print("Running Test 2: Import Test...")
    try:
        spec = importlib.util.spec_from_file_location("verdant_code", GAME_FILE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        report.add_result("Import Test", True, "Module imported successfully")
        return True, module
    except Exception as e:
        report.add_result("Import Test", False, error=e)
        return False, None

def test_3_lesson_registry(report, module):
    """Test 3: Lesson Registry Test"""
    print("Running Test 3: Lesson Registry Test...")
    if module is None:
        report.add_result("Lesson Registry Test", False, "Module not loaded")
        return False, None

    try:
        registry = module.get_lesson_registry()

        # Check each act
        all_acts_correct = True
        details = []

        for act_num, expected_count in EXPECTED_LESSON_COUNTS.items():
            actual_count = len(registry.get(act_num, []))
            if actual_count == expected_count:
                details.append(f"Act {act_num}: {actual_count}/{expected_count} ✓")
            else:
                details.append(f"Act {act_num}: {actual_count}/{expected_count} ✗")
                all_acts_correct = False

        # Check total
        total_lessons = sum(len(lessons) for lessons in registry.values())
        details.append(f"Total: {total_lessons}/{EXPECTED_TOTAL}")

        if total_lessons != EXPECTED_TOTAL:
            all_acts_correct = False

        details_str = "\n   " + "\n   ".join(details)

        if all_acts_correct:
            report.add_result("Lesson Registry Test", True, details_str)
            return True, registry
        else:
            report.add_result("Lesson Registry Test", False, details_str)
            return False, registry

    except Exception as e:
        report.add_result("Lesson Registry Test", False, error=e)
        return False, None

def test_4_lesson_instantiation(report, module, registry):
    """Test 4: Lesson Instantiation Test"""
    print("Running Test 4: Lesson Instantiation Test...")
    if module is None or registry is None:
        report.add_result("Lesson Instantiation Test", False, "Prerequisites not met")
        return False, []

    try:
        all_lessons = []
        failed_instantiations = []

        for act_num, lesson_classes in registry.items():
            for lesson_class in lesson_classes:
                try:
                    lesson_instance = lesson_class()
                    all_lessons.append(lesson_instance)
                except Exception as e:
                    failed_instantiations.append(f"{lesson_class.__name__}: {str(e)}")

        if not failed_instantiations:
            report.add_result(
                "Lesson Instantiation Test",
                True,
                f"All {len(all_lessons)} lessons instantiated successfully"
            )
            return True, all_lessons
        else:
            details = f"Failed to instantiate {len(failed_instantiations)} lessons:\n   " + "\n   ".join(failed_instantiations[:10])
            if len(failed_instantiations) > 10:
                details += f"\n   ... and {len(failed_instantiations) - 10} more"
            report.add_result("Lesson Instantiation Test", False, details)
            return False, all_lessons

    except Exception as e:
        report.add_result("Lesson Instantiation Test", False, error=e)
        return False, []

def test_5_duplicate_id_check(report, lessons):
    """Test 5: Duplicate ID Check"""
    print("Running Test 5: Duplicate ID Check...")
    if not lessons:
        report.add_result("Duplicate ID Check", False, "No lessons to check")
        return False

    try:
        lesson_ids = []
        duplicates = []

        for lesson in lessons:
            lesson_id = lesson.lesson_id
            if lesson_id in lesson_ids:
                duplicates.append(lesson_id)
            else:
                lesson_ids.append(lesson_id)

        if not duplicates:
            report.add_result(
                "Duplicate ID Check",
                True,
                f"All {len(lesson_ids)} lesson IDs are unique"
            )
            return True
        else:
            details = f"Found {len(duplicates)} duplicate IDs: {', '.join(duplicates[:10])}"
            if len(duplicates) > 10:
                details += f" ... and {len(duplicates) - 10} more"
            report.add_result("Duplicate ID Check", False, details)
            return False

    except Exception as e:
        report.add_result("Duplicate ID Check", False, error=e)
        return False

def test_6_lesson_attributes(report, lessons):
    """Test 6: Lesson Attributes Test"""
    print("Running Test 6: Lesson Attributes Test...")
    if not lessons:
        report.add_result("Lesson Attributes Test", False, "No lessons to check")
        return False

    try:
        required_attrs = ['title', 'description', 'lesson_id']
        lessons_missing_attrs = []

        for lesson in lessons:
            missing_attrs = []
            for attr in required_attrs:
                if not hasattr(lesson, attr) or getattr(lesson, attr) is None:
                    missing_attrs.append(attr)

            if missing_attrs:
                lessons_missing_attrs.append(
                    f"{lesson.__class__.__name__}: missing {', '.join(missing_attrs)}"
                )

        if not lessons_missing_attrs:
            report.add_result(
                "Lesson Attributes Test",
                True,
                f"All {len(lessons)} lessons have required attributes"
            )
            return True
        else:
            details = f"{len(lessons_missing_attrs)} lessons missing attributes:\n   " + "\n   ".join(lessons_missing_attrs[:10])
            if len(lessons_missing_attrs) > 10:
                details += f"\n   ... and {len(lessons_missing_attrs) - 10} more"
            report.add_result("Lesson Attributes Test", False, details)
            return False

    except Exception as e:
        report.add_result("Lesson Attributes Test", False, error=e)
        return False

def run_all_tests():
    """Run all tests in order"""
    report = TestReport()

    print("\n" + "="*80)
    print("STARTING COMPREHENSIVE TESTS")
    print("="*80 + "\n")

    # Test 1: Syntax Check
    syntax_ok = test_1_syntax_check(report)
    if not syntax_ok:
        print("\n⚠ Syntax errors detected. Stopping tests.\n")
        report.print_report()
        return

    # Test 2: Import Test
    import_ok, module = test_2_import_test(report)
    if not import_ok:
        print("\n⚠ Import failed. Stopping tests.\n")
        report.print_report()
        return

    # Test 3: Lesson Registry Test
    registry_ok, registry = test_3_lesson_registry(report, module)

    # Test 4: Lesson Instantiation Test
    instantiation_ok, lessons = test_4_lesson_instantiation(report, module, registry)

    # Test 5: Duplicate ID Check
    test_5_duplicate_id_check(report, lessons)

    # Test 6: Lesson Attributes Test
    test_6_lesson_attributes(report, lessons)

    # Print final report
    all_passed = report.print_report()

    return all_passed

if __name__ == "__main__":
    try:
        result = run_all_tests()
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n✗ CRITICAL ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
