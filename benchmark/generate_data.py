"""
Generate synthetic CSV data for benchmarking.

This module creates CSV files with various edge cases including:
- Quoted fields with commas
- Multiline fields
- Escaped quotes
- Random text data

Useful for testing CSV reader/writer performance and correctness.
"""

import random
import string


def random_text(length=20):
    """
    Generate random text string.

    Args:
        length: Length of the random text string. Default is 20.

    Returns:
        Random string of ASCII letters with specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_csv(file_path, rows=10000, cols=5):
    """
    Generate a CSV file with synthetic data for benchmarking.

    Creates a CSV file with various edge cases including quoted fields,
    commas, newlines, and escaped quotes to test CSV parser robustness.

    Args:
        file_path: Path where the CSV file will be created.
        rows: Number of rows to generate. Default is 10000.
        cols: Number of columns per row. Default is 5.
            (Note: Currently fixed at 5 columns regardless of parameter)
    """
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        for _ in range(rows):
            row = [
                random_text(),
                f'"Text with comma, {random_text(5)}"',
                f'"Line1\r\nLine2 {random_text(5)}"',
                f'"He said ""Hello"" {random_text(5)}"',
                random_text()
            ]
            f.write(",".join(row) + "\n")


def main():
    """Main function to generate benchmark data."""
    print("Generating benchmark CSV data...")
    generate_csv("benchmark_data.csv")
    print("✓ Generated benchmark_data.csv with 10,000 rows")


if __name__ == "__main__":
    main()