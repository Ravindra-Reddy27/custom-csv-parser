"""
Comprehensive test suite for CustomCsvWriter.
Tests various CSV writing scenarios and edge cases.
"""

import csv
import os
import tempfile
from src.writer import CustomCsvWriter


def test_case(name, data):
    """Test a specific CSV writing scenario against standard library."""
    print(f"\n{'='*70}")
    print(f"Test: {name}")
    print(f"{'='*70}")
    print(f"Data: {data}")
    print()

    # Create temp files
    custom_path = tempfile.mktemp(suffix='.csv')
    stdlib_path = tempfile.mktemp(suffix='.csv')

    try:
        # Write with custom writer
        writer = CustomCsvWriter(custom_path)
        writer.write(data)

        # Write with standard library
        with open(stdlib_path, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(data)

        # Read both files
        with open(custom_path, 'r') as f:
            custom_content = f.read()

        with open(stdlib_path, 'r') as f:
            stdlib_content = f.read()

        # Compare
        print(f"Custom output:\n{repr(custom_content)}")
        print(f"\nStdlib csv output:\n{repr(stdlib_content)}")

        if custom_content == stdlib_content:
            print("\n✓ MATCH - Test PASSED")
            return True
        else:
            print("\n✗ MISMATCH - Test FAILED")
            print(f"\nExpected:\n{repr(stdlib_content)}")
            print(f"\nGot:\n{repr(custom_content)}")
            return False

    finally:
        # Cleanup
        if os.path.exists(custom_path):
            os.unlink(custom_path)
        if os.path.exists(stdlib_path):
            os.unlink(stdlib_path)


def run_all_tests():
    """Run all test cases."""
    print("=" * 70)
    print("CustomCsvWriter Test Suite")
    print("=" * 70)

    results = []

    # Test 1: Basic CSV
    results.append(test_case(
        "Basic CSV",
        [
            ['name', 'age', 'city'],
            ['Alice', '30', 'NYC'],
            ['Bob', '25', 'LA']
        ]
    ))

    # Test 2: Fields with commas
    results.append(test_case(
        "Fields with commas",
        [
            ['name', 'address', 'city'],
            ['Alice', '123 Main St, Apt 4', 'NYC'],
            ['Bob', '456 Oak Ave, Suite 100', 'LA']
        ]
    ))

    # Test 3: Fields with quotes
    results.append(test_case(
        "Fields with quotes",
        [
            ['name', 'quote'],
            ['Alice', 'She said "Hello"'],
            ['Bob', 'He said "Goodbye"']
        ]
    ))

    # Test 4: Fields with newlines
    results.append(test_case(
        "Fields with newlines",
        [
            ['name', 'address'],
            ['Alice', '123 Main St\nApt 4'],
            ['Bob', '456 Oak Ave\nSuite 100']
        ]
    ))

    # Test 5: Mixed special characters
    results.append(test_case(
        "Mixed special characters",
        [
            ['name', 'description'],
            ['Alice', 'Works at "Tech Corp", loves coding\nand hiking'],
            ['Bob', 'Freelancer, designer, "creative"']
        ]
    ))

    # Test 6: Empty fields
    results.append(test_case(
        "Empty fields",
        [
            ['name', 'age', 'city'],
            ['Alice', '', 'NYC'],
            ['', '25', ''],
            ['Bob', '30', 'LA']
        ]
    ))

    # Test 7: Numbers and mixed types
    results.append(test_case(
        "Numbers and mixed types",
        [
            ['name', 'age', 'salary'],
            ['Alice', 30, 50000],
            ['Bob', 25, 45000]
        ]
    ))

    # Test 8: Single column
    results.append(test_case(
        "Single column",
        [
            ['name'],
            ['Alice'],
            ['Bob'],
            ['Charlie']
        ]
    ))

    # Test 9: Single row
    results.append(test_case(
        "Single row",
        [
            ['name', 'age', 'city']
        ]
    ))

    # Test 10: Special characters
    results.append(test_case(
        "Special characters",
        [
            ['name', 'symbols'],
            ['Alice', '!@#$%^&*()'],
            ['Bob', '<>?/\\|[]{}=']
        ]
    ))

    # Test 11: Very long field
    results.append(test_case(
        "Very long field",
        [
            ['name', 'description'],
            ['Alice', 'A' * 1000],
            ['Bob', 'This is a very long description ' * 50]
        ]
    ))

    # Test 12: Escaped quotes
    results.append(test_case(
        "Multiple quotes",
        [
            ['name', 'quote'],
            ['Alice', '"""Hello"""'],
            ['Bob', '"Test"']
        ]
    ))

    # Test 13: CRLF in field
    results.append(test_case(
        "CRLF in field",
        [
            ['name', 'address'],
            ['Alice', '123 Main St\r\nApt 4']
        ]
    ))

    # Test 14: Empty row
    results.append(test_case(
        "Row with empty strings",
        [
            ['', '', ''],
            ['Alice', 'Bob', 'Charlie']
        ]
    ))

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("✓ All tests PASSED! CSV Writer works correctly!")
    else:
        print(f"✗ {total - passed} test(s) FAILED")

    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)