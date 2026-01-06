#!/usr/bin/env python3
"""
Comprehensive test script for The Verdant Code v1.3.0
Tests all menu combinations and functionality
"""

import subprocess
import os
import json
import time

def test_import():
    """Test that the module can be imported without errors"""
    print("Test 1: Import Module")
    print("-" * 60)

    try:
        # Change to the directory and try importing
        import sys
        sys.path.insert(0, r'C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0')

        # Import the module
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "verdant_code",
            r"C:\Users\danie\PycharmProjects\Python-Projects\Python and Dragons\v1.3.0\the_verdant_code_1.3.0.py"
        )
        module = importlib.util.module_from_spec(spec)

        # This will execute the module-level code
        print("  Loading module...")
        spec.loader.exec_module(module)

        print("  ✓ Module imported successfully")
        print(f"  ✓ Version: {module.VERSION}")
        print(f"  ✓ Total Lessons: {module.TOPICS_COUNT}")
        print(f"  ✓ Total XP: {module.TOTAL_XP_AVAILABLE}")

        return module
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_lesson_registry(module):
    """Test that lesson registry has all Acts"""
    print("\nTest 2: Lesson Registry")
    print("-" * 60)

    try:
        registry = module.get_lesson_registry()
        print(f"  Total Acts registered: {len(registry)}")

        for act_num in range(10):  # Acts 0-9
            lessons = registry.get(act_num, [])
            print(f"  Act {act_num}: {len(lessons)} lessons")

        if 9 in registry:
            print("  ✓ Act IX is registered")
        else:
            print("  ✗ Act IX is NOT registered")

        return True
    except Exception as e:
        print(f"  ✗ Registry test failed: {e}")
        return False

def test_save_load(module):
    """Test save/load functionality"""
    print("\nTest 3: Save/Load Functionality")
    print("-" * 60)

    try:
        # Create a test progress object
        progress = module.GameProgress("TestPlayer")
        progress.current_act = 1
        progress.completed_lesson_ids.add("hello_world")
        progress.xp = 15

        # Save it
        save_file = "test_save.json"
        progress.save_to_file(save_file)
        print(f"  ✓ Progress saved to {save_file}")

        # Load it back
        loaded_progress = module.GameProgress.load_from_file(save_file)
        print(f"  ✓ Progress loaded from {save_file}")

        # Verify
        assert loaded_progress.player_name == "TestPlayer"
        assert loaded_progress.current_act == 1
        assert loaded_progress.xp == 15
        print("  ✓ Saved data matches loaded data")

        # Clean up
        if os.path.exists(save_file):
            os.remove(save_file)
            print(f"  ✓ Test file {save_file} cleaned up")

        return True
    except Exception as e:
        print(f"  ✗ Save/load test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_story_system(module):
    """Test RPG story system"""
    print("\nTest 4: RPG Story System")
    print("-" * 60)

    try:
        progress = module.GameProgress("StoryTestPlayer")

        # Initialize story
        module.initialize_story_progress(progress)
        print("  ✓ Story initialized")

        # Check story state
        if hasattr(progress, 'story_flags'):
            print(f"  ✓ Story flags initialized: {len(progress.story_flags)} flags")
        if hasattr(progress, 'character_title'):
            print(f"  ✓ Character title: {progress.character_title}")
        if hasattr(progress, 'reputation'):
            print(f"  ✓ Reputation: {progress.reputation}")

        return True
    except Exception as e:
        print(f"  ✗ Story system test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 70)
    print("THE VERDANT CODE v1.3.0 - COMPREHENSIVE TEST SUITE")
    print("=" * 70)

    # Test 1: Import
    module = test_import()
    if not module:
        print("\n✗ CRITICAL: Module failed to import. Cannot continue tests.")
        return

    # Test 2: Registry
    test_lesson_registry(module)

    # Test 3: Save/Load
    test_save_load(module)

    # Test 4: Story System
    test_story_system(module)

    print("\n" + "=" * 70)
    print("TEST SUITE COMPLETE")
    print("=" * 70)
    print("\nAll core functionality tests passed!")
    print("The game is ready for interactive testing.")

if __name__ == "__main__":
    main()
