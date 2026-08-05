# Week 4 Performance Optimization in Python

A self-contained Python project that demonstrates how to identify performance bottlenecks, optimize code, and compare execution speed before and after improvement.

## Overview

This project uses a **Word Frequency Analyzer** to show the full performance optimization workflow in Python.

It includes:
- an intentionally slower baseline version,
- an optimized version with better performance,
- profiling data,
- correctness tests,
- and a detailed optimization report.

## Project Goals

- Build a real Python application with measurable performance issues.
- Profile the original code to find bottlenecks.
- Improve the code using efficient Python techniques.
- Verify that the optimized version produces the same results.
- Document the before-and-after performance clearly.

## Features

- Generates sample text automatically inside the program.
- Counts word frequency from large input text.
- Profiles execution time using `cProfile`.
- Compares original and optimized versions.
- Includes automated tests for correctness.
- Produces a clear report of optimization changes.

## Files in This Repository

- `original_app.py` — baseline implementation with slower logic.
- `optimized_app.py` — improved version using faster techniques.
- `tests.py` — checks that both versions produce the same output.
- `week4_performance_optimization_report.md` — detailed report of the optimization process.
- `profile_baseline.txt` — profiler output for the original version.
- `profile_optimized.txt` — profiler output for the optimized version.
- `benchmark_results.txt` — timing comparison between both versions.

## How It Works

### Original Version
The original code uses:
- manual loops,
- repeated comparisons,
- list-based checks,
- and redundant processing.

This makes it slower when the input becomes large.

### Optimized Version
The optimized code uses:
- `collections.Counter`,
- reduced repeated work,
- faster data handling,
- and cleaner logic.

This improves performance while keeping the same result.

## How to Run

### Run the original version
```bash
python original_app.py
```

### Run the optimized version
```bash
python optimized_app.py
```

### Run the tests
```bash
python tests.py
```

## Performance Optimization Summary

The project shows how a Python program can be improved by:
- identifying slow functions,
- replacing inefficient loops,
- using built-in data structures,
- and measuring the improvement with profiling tools.

## Expected Result

The optimized version should:
- return the same output as the original version,
- run faster,
- and demonstrate better code efficiency.

## Why This Project Is Useful

This project is a good portfolio piece because it shows:
- Python development skills,
- performance analysis,
- algorithm improvement,
- testing,
- and professional documentation.

## Author

Created for Week 4 performance optimization task.

---

If you want, I can also make it look even more professional with:
- badges,
- a table of contents,
- emojis,
- and a cleaner GitHub style layout.
