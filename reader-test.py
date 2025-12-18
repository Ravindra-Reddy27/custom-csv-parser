"""
Compare CustomCsvReader output with Python's standard csv module.

This script validates that CustomCsvReader produces identical output
to the standard library's csv.reader for the same input file.
"""

import csv
from src.reader import CustomCsvReader


def compare_with_csv_module(file_path):
    """
    Compare CustomCsvReader with standard library csv.reader.
    """
    # Read with standard library
    with open(file_path, newline="", encoding="utf-8") as f:
        std_rows = list(csv.reader(f))

    # Read with custom reader
    with CustomCsvReader(file_path) as reader:
        custom_rows = list(reader)

    # Display results
    print("Standard CSV:")
    print(std_rows)

    print("\nCustom CSV:")
    print(custom_rows)

    # Validate match
    assert std_rows == custom_rows, "Mismatch found!"

    print("\n✅ Match successful!\n")


def main():
    """Main function to run the comparison."""
    compare_with_csv_module("data/sample.csv")


if __name__ == "__main__":
    main()