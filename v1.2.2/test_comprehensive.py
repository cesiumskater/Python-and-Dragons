"""
Comprehensive Test Suite for the_verdant_code_1.2.2.py
Tests syntax, imports, lesson registry, instantiation, and basic functionality.
"""

import sys
import ast
import traceback
from pathlib import Path

# Test file path
TEST_FILE = r"C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.2.2\the_verdant_code_1.2.2.py"

def print_header(text):
    """Print a formatted header."""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80)

def print_test(test_name, passed, details=""):
    """Print test result."""
    status = "PASS" if passed else "FAIL"
    symbol = "✓" if passed else "✗"
    print(f"\n{symbol} Test {test_name}: {status}")
    if details:
        print(f"  Details: {details}")

def test_1_syntax_check():
    """Test 1: Compile the file and check for syntax errors."""
    print_header("TEST 1: SYNTAX CHECK")

    try:
        with open(TEST_FILE, 'r', encoding='utf-8') as f:
            source_code = f.read()

        # Try to compile the code
        compile(source_code, TEST_FILE, 'exec')

        # Also try to parse it with ast
        ast.parse(source_code, filename=TEST_FILE)

        print_test("Syntax Check", True, "File compiles successfully with no syntax errors")
        return True
    except SyntaxError as e:
        print_test("Syntax Check", False, f"Syntax error at line {e.lineno}: {e.msg}")
        print(f"  Text: {e.text}")
        print(f"  Offset: {' ' * (e.offset - 1) if e.offset else ''}^")
        traceback.print_exc()
        return False
    except Exception as e:
        print_test("Syntax Check", False, f"Unexpected error: {str(e)}")
        traceback.print_exc()
        return False

def test_2_import_module():
    """Test 2: Import the module successfully."""
    print_header("TEST 2: IMPORT MODULE")

    try:
        # Add the directory to sys.path
        sys.path.insert(0, str(Path(TEST_FILE).parent))

        # Import the module
        import the_verdant_code_1_2_2

        print_test("Import Module", True, "Module imported successfully")
        return True, the_verdant_code_1_2_2
    except Exception as e:
        print_test("Import Module", False, f"Import failed: {str(e)}")
        traceback.print_exc()
        return False, None

def test_3_lesson_registry(module):
    """Test 3: Verify lesson registry contains all 181 lessons across Acts 0-9."""
    print_header("TEST 3: LESSON REGISTRY VERIFICATION")

    if not module:
        print_test("Lesson Registry", False, "Module not available")
        return False, None

    try:
        # Get the lesson registry
        registry = module.get_lesson_registry()

        total_lessons = len(registry)

        # Count lessons per act
        acts = {}
        for lesson_id in registry.keys():
            # Extract act number (format: "X.Y")
            act_num = lesson_id.split('.')[0]
            acts[act_num] = acts.get(act_num, 0) + 1

        # Print detailed breakdown
        print(f"\nTotal Lessons Found: {total_lessons}")
        print("\nBreakdown by Act:")
        for act in sorted(acts.keys(), key=lambda x: int(x)):
            print(f"  Act {act}: {acts[act]} lessons")

        # Verify we have all expected acts (0-9)
        expected_acts = set(str(i) for i in range(10))
        found_acts = set(acts.keys())

        if expected_acts != found_acts:
            missing = expected_acts - found_acts
            extra = found_acts - expected_acts
            details = ""
            if missing:
                details += f"Missing acts: {missing}. "
            if extra:
                details += f"Extra acts: {extra}. "
            print_test("Lesson Registry", False, details)
            return False, registry

        if total_lessons == 181:
            print_test("Lesson Registry", True, f"All 181 lessons found across Acts 0-9")
            return True, registry
        else:
            print_test("Lesson Registry", False, f"Expected 181 lessons, found {total_lessons}")
            return False, registry

    except Exception as e:
        print_test("Lesson Registry", False, f"Error accessing registry: {str(e)}")
        traceback.print_exc()
        return False, None

def test_4_duplicate_ids(registry):
    """Test 4: Check for duplicate lesson IDs."""
    print_header("TEST 4: DUPLICATE ID CHECK")

    if not registry:
        print_test("Duplicate ID Check", False, "Registry not available")
        return False

    try:
        # The registry is a dictionary, so by definition keys are unique
        # But let's also check the lesson classes themselves
        lesson_ids_seen = set()
        duplicates = []

        for lesson_id, lesson_class in registry.items():
            if hasattr(lesson_class, 'lesson_id'):
                class_lesson_id = lesson_class.lesson_id
                if class_lesson_id in lesson_ids_seen:
                    duplicates.append(class_lesson_id)
                lesson_ids_seen.add(class_lesson_id)

        if duplicates:
            print_test("Duplicate ID Check", False, f"Found duplicate IDs: {duplicates}")
            return False
        else:
            print_test("Duplicate ID Check", True, f"No duplicate lesson IDs found among {len(registry)} lessons")
            return True

    except Exception as e:
        print_test("Duplicate ID Check", False, f"Error checking duplicates: {str(e)}")
        traceback.print_exc()
        return False

def test_5_lesson_instantiation(module, registry):
    """Test 5: Verify all lesson classes can be instantiated."""
    print_header("TEST 5: LESSON INSTANTIATION TEST")

    if not module or not registry:
        print_test("Lesson Instantiation", False, "Module or registry not available")
        return False

    try:
        failed_lessons = []
        success_count = 0

        for lesson_id, lesson_class in registry.items():
            try:
                # Try to instantiate the lesson
                lesson_instance = lesson_class()

                # Verify it has required attributes
                if not hasattr(lesson_instance, 'lesson_id'):
                    failed_lessons.append((lesson_id, "Missing lesson_id attribute"))
                elif not hasattr(lesson_instance, 'display'):
                    failed_lessons.append((lesson_id, "Missing display method"))
                else:
                    success_count += 1

            except Exception as e:
                failed_lessons.append((lesson_id, str(e)))

        if failed_lessons:
            print_test("Lesson Instantiation", False,
                      f"{len(failed_lessons)} lessons failed to instantiate")
            print("\nFailed lessons:")
            for lesson_id, error in failed_lessons[:10]:  # Show first 10
                print(f"  {lesson_id}: {error}")
            if len(failed_lessons) > 10:
                print(f"  ... and {len(failed_lessons) - 10} more")
            return False
        else:
            print_test("Lesson Instantiation", True,
                      f"All {success_count} lessons instantiated successfully")
            return True

    except Exception as e:
        print_test("Lesson Instantiation", False, f"Error during instantiation test: {str(e)}")
        traceback.print_exc()
        return False

def test_6_basic_functionality(module):
    """Test 6: Test basic functionality - create GameProgress instance."""
    print_header("TEST 6: BASIC FUNCTIONALITY TEST")

    if not module:
        print_test("Basic Functionality", False, "Module not available")
        return False

    try:
        # Create a GameProgress instance
        game_progress = module.GameProgress()

        # Verify initial state
        if not hasattr(game_progress, 'current_lesson_id'):
            print_test("Basic Functionality", False, "GameProgress missing current_lesson_id")
            return False

        if not hasattr(game_progress, 'completed_lessons'):
            print_test("Basic Functionality", False, "GameProgress missing completed_lessons")
            return False

        # Try to get current lesson
        current_lesson_id = game_progress.current_lesson_id
        print(f"\n  Initial lesson: {current_lesson_id}")

        # Try to mark a lesson as complete
        initial_completed = len(game_progress.completed_lessons)
        game_progress.mark_lesson_complete("0.1")
        after_completed = len(game_progress.completed_lessons)

        if after_completed != initial_completed + 1:
            print_test("Basic Functionality", False,
                      f"Mark complete failed: {initial_completed} -> {after_completed}")
            return False

        print(f"  Lessons completed: {initial_completed} -> {after_completed}")
        print(f"  GameProgress is fully functional")

        print_test("Basic Functionality", True,
                  "GameProgress created and functions correctly")
        return True

    except Exception as e:
        print_test("Basic Functionality", False, f"Error testing functionality: {str(e)}")
        traceback.print_exc()
        return False

def generate_final_report(results):
    """Generate final test report."""
    print_header("FINAL TEST REPORT")

    total_tests = len(results)
    passed_tests = sum(1 for r in results if r)
    failed_tests = total_tests - passed_tests

    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"\nSuccess Rate: {(passed_tests/total_tests)*100:.1f}%")

    if failed_tests == 0:
        print("\n" + "="*80)
        print("  ✓ ALL TESTS PASSED!")
        print("  THE FILE IS READY FOR PRODUCTION")
        print("="*80)
        return True
    else:
        print("\n" + "="*80)
        print(f"  ✗ {failed_tests} TEST(S) FAILED")
        print("  THE FILE NEEDS ADDITIONAL FIXES")
        print("="*80)
        return False

def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("  COMPREHENSIVE TEST SUITE FOR the_verdant_code_1.2.2.py")
    print("="*80)
    print(f"\nTest File: {TEST_FILE}")

    results = []

    # Test 1: Syntax Check
    result1 = test_1_syntax_check()
    results.append(result1)
    if not result1:
        print("\n⚠ CRITICAL: Syntax check failed. Cannot proceed with further tests.")
        generate_final_report(results)
        return

    # Test 2: Import Module
    result2, module = test_2_import_module()
    results.append(result2)
    if not result2:
        print("\n⚠ CRITICAL: Import failed. Cannot proceed with further tests.")
        generate_final_report(results)
        return

    # Test 3: Lesson Registry
    result3, registry = test_3_lesson_registry(module)
    results.append(result3)

    # Test 4: Duplicate IDs (can run even if registry count is off)
    result4 = test_4_duplicate_ids(registry)
    results.append(result4)

    # Test 5: Lesson Instantiation
    result5 = test_5_lesson_instantiation(module, registry)
    results.append(result5)

    # Test 6: Basic Functionality
    result6 = test_6_basic_functionality(module)
    results.append(result6)

    # Generate final report
    generate_final_report(results)

if __name__ == "__main__":
    main()
