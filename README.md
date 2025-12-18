# Custom CSV Reader and Writer in Python

## Overview

This project builds a CSV reader and writer from scratch in Python to understand how CSV parsing really works under the hood. It handles tricky cases like quoted text, escaped quotes, and line breaks within fields.

Creating this custom implementation shows how Python's built-in `csv` module works internally and helps understand the balance between performance and control when processing data.

---

## Features

- **Streaming CSV reader** implemented as an iterator
- **Robust parsing** handles:
  - Comma-separated fields
  - Quoted fields
  - Escaped double quotes (`""`)
  - Embedded newlines inside quoted fields
  - Windows-style CRLF (`\r\n`) line endings
- **Custom CSV writer** that produces standards-compliant CSV output
- **Performance benchmarking** against Python's built-in `csv` module

---

## Project Structure

```
custom-csv-parser/
├── src/
|   ├── __init__.py
│   ├── reader.py          # Custom CSV reader implementation
│   └── writer.py          # Custom CSV writer implementation
├── data/
│   └── sample.csv         # Sample CSV file for testing
├── benchmark/
│   ├── generate_data.py   # Generate benchmark CSV data
│   └── benchmark.py       # Performance comparison scripts
├── reader-test.py         # Test script for reader
├── writer-test.py         # Test script for writer
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher

### Installation

This project uses only Python's standard library—no external dependencies required.

```bash
git clone https://github.com/Ravindra-Reddy27/custom-csv-parser.git
cd custom-csv-parser
```

---

## Usage

### 1. Testing the CSV Reader

**Run the reader test:**

```bash
python reader-test.py
```

**What it does:**

- Reads `data/sample.csv` using the custom reader
- Compares output with Python's built-in `csv.reader`
- Prints each parsed row to the console

**Expected output:**

```
Standard CSV:
[['id', 'name', 'comment', 'amount'], ['1', 'Ravi', 'Hello, World', '100'], ...]

Custom CSV:
[['id', 'name', 'comment', 'amount'], ['1', 'Ravi', 'Hello, World', '100'], ...]

✅ Match successful!
```

**What this confirms:**

- ✓ Quoted fields parsed correctly
- ✓ Escaped quotes handled properly
- ✓ Embedded newlines preserved
- ✓ Output matches Python's standard library

---

### 2. Testing the CSV Writer

**Run the writer test:**

```bash
python writer-test.py
```

**What it does:**

- Runs 14 comprehensive test cases
- Compares custom writer output with Python's `csv.writer`
- Tests edge cases: commas, quotes, newlines, empty fields, special characters

**Expected output:**

```
======================================================================
CustomCsvWriter Test Suite
======================================================================

======================================================================
Test: Basic CSV
======================================================================
Data: [['name', 'age', 'city'], ['Alice', '30', 'NYC'], ['Bob', '25', 'LA']]

Custom output:
'name,age,city\nAlice,30,NYC\nBob,25,LA\n'

Stdlib csv output:
'name,age,city\nAlice,30,NYC\nBob,25,LA\n'

✓ MATCH - Test PASSED

...

======================================================================
SUMMARY
======================================================================
Passed: 14/14
✓ All tests PASSED! CSV Writer works correctly!
```

**What this confirms:**

- ✓ Fields with commas are properly quoted
- ✓ Quotes are escaped correctly (`"` becomes `""`)
- ✓ Newlines within fields are handled
- ✓ Output is standards-compliant

---

## Performance Benchmarking

### Step 1: Generate Test Data

**Create a large CSV file for benchmarking:**

```bash
python -m benchmark.generate_data
```

**What it does:**

- Generates `benchmark_data.csv` with 10,000 rows and 5 columns
- Includes realistic edge cases: commas, quotes, embedded newlines

**Expected output:**

```
Generating benchmark CSV data...
✓ Generated benchmark_data.csv with 10,000 rows
```

**Sample data:**

```csv
uPQlEsjCcTXXFSCcvksT,"Text with comma, rphbG","Line1
Line2 TuBhC","He said ""Hello"" MGqlH",ooOaTFyNOvsxcOULOHiL
```

---

### Step 2: Run Benchmark

**Compare performance:**

```bash
python -m benchmark.benchmark
```
**What it does:**

- Creates two output files: `csv_writer_out.csv` (standard library) and `custom_writer_out.csv` (custom implementation)
- Compares custom reader/writer performance against Python's built-in `csv` module
- Measures and reports execution time using `timeit`

**Expected output:**

```
Reader Benchmark:
Standard csv.reader: 0.1718 seconds
CustomCsvReader:     2.6351 seconds

Writer Benchmark:
Standard csv.writer: 0.2838 seconds
CustomCsvWriter:     0.2427 seconds
```

---

### Benchmark Analysis

**Reader Performance:**

- Python's built-in `csv.reader` is ~15x faster (implemented in optimized C)
- Custom reader prioritizes correctness and streaming behavior
- Trade-off: clarity and control vs. raw speed

**Writer Performance:**

- Custom writer performs comparably to the standard library
- Simpler logic and predictable output structure minimize overhead
- Demonstrates that pure Python can match C performance for certain tasks

**Key Takeaway:**

The results show the classic trade-off in software engineering—performance vs. control. The custom implementation sacrifices some speed for transparency, educational value, and fine-grained control over parsing behavior.

---

## How It Works

### Reader Architecture

- **State machine-based parsing**: Tracks whether currently inside/outside quotes
- **Character-by-character processing**: Handles edge cases precisely
- **Streaming design**: Processes files without loading everything into memory
- **Iterator pattern**: Yields one row at a time for memory efficiency

### Writer Architecture

- **Field inspection**: Checks each field for special characters (commas, quotes, newlines)
- **Automatic quoting**: Wraps fields in quotes when necessary
- **Quote escaping**: Doubles internal quotes (`"` → `""`)
- **Standards-compliant**: Matches RFC 4180 CSV specification

---

## Key Learning Points

1. **CSV isn't as simple as it looks**: Quoted fields, escaped quotes, and embedded newlines add significant complexity
2. **State machines are powerful**: Essential for parsing formats with context-dependent rules
3. **Streaming is efficient**: Processing data incrementally avoids memory issues with large files
4. **C is fast**: Native implementations have a huge performance advantage
5. **Trade-offs matter**: Sometimes clarity and control are worth the performance cost

---

## Conclusion

This project provides a clear, from-scratch implementation of CSV parsing and writing in Python. It demonstrates:

- State-machine-based parsing techniques
- Correct handling of real-world edge cases
- Performance benchmarking against production code
- The balance between educational clarity and production performance

Perfect for understanding how parsing libraries work internally and appreciating the engineering decisions behind Python's standard library.

---
## Contributing

Contributions welcome! Feel free to:

- Report bugs or edge cases
- Suggest performance improvements
- Add more test cases
- Improve documentation