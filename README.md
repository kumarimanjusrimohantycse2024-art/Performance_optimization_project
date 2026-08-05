# Week 4 Performance Optimization in Python

## Project Name
Word Frequency Analyzer: Original vs Optimized

## Objective
This project demonstrates how to identify performance bottlenecks in a Python application and improve the code using optimization techniques.

## Files Included
- `original_app.py` - slow baseline version
- `optimized_app.py` - faster optimized version
- `tests.py` - verification tests
- `profile_baseline.txt` - profiling results of original version
- `profile_optimized.txt` - profiling results of optimized version
- `benchmark_results.txt` - time comparison results

## How It Works
The program generates its own sample text, counts word frequencies, finds the top words, and measures execution time.

## Optimization Done
### Original version
- Uses manual loops for counting
- Uses list-based unique word checks
- Repeats work many times

### Optimized version
- Uses `Counter` for counting
- Reduces repeated processing
- Uses faster built-in methods

## How to Run
### Run original version
```bash
python original_app.py
```

### Run optimized version
```bash
python optimized_app.py
```

### Run tests
```bash
python tests.py
```

## Expected Output
The optimized version should produce the same result as the original version but run faster.

## Report Content
Your report should include:
- project overview
- baseline performance analysis
- bottlenecks found
- optimization methods used
- before and after timing results
- verification of correctness

## Notes
This project is self-contained and does not need any external input files.