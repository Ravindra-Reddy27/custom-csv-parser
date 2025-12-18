"""
Benchmark script for comparing custom CSV parser
with Python's built-in csv module.
"""
import csv
import timeit

from src.reader import CustomCsvReader
from src.writer import CustomCsvWriter


FILE_PATH = "benchmark_data.csv"


def read_with_csv():
    """Reads the benchmark file using the standard Python csv module."""
    with open(FILE_PATH, newline="") as f:
        list(csv.reader(f))


def read_with_custom():
    """Reads the benchmark file using the custom CSV reader."""
    list(CustomCsvReader(FILE_PATH))


# --- Reader Benchmark ---
csv_time = timeit.timeit(read_with_csv, number=5)
custom_time = timeit.timeit(read_with_custom, number=5)

print("Reader Benchmark:")
print(f"Standard csv.reader: {csv_time:.4f} seconds")
print(f"CustomCsvReader:     {custom_time:.4f} seconds")


def write_with_csv():
    """Writes data using the standard Python csv module."""
    with open("csv_writer_out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def write_with_custom():
    """Writes data using the custom CSV writer."""
    writer = CustomCsvWriter("custom_writer_out.csv")
    writer.write(data)


# Prepare data once by reading it (this happens outside the timer)
with open(FILE_PATH, newline="") as f:
    data = list(csv.reader(f))


# --- Writer Benchmark ---
csv_write_time = timeit.timeit(write_with_csv, number=5)
custom_write_time = timeit.timeit(write_with_custom, number=5)

print("\nWriter Benchmark:")
print(f"Standard csv.writer: {csv_write_time:.4f} seconds")
print(f"CustomCsvWriter:     {custom_write_time:.4f} seconds")