# Performance Optimization Project (Python)

Demonstrates a practical optimization workflow by comparing a baseline and optimized word-frequency analyzer while preserving output correctness.

## Features

- Baseline implementation for word counting: [`original_app.py`](./original_app.py)
- Optimized implementation using `collections.Counter`: [`optimized_app.py`](./optimized_app.py)
- Profiling output generation with `cProfile` and `pstats`
- Correctness checks to ensure both implementations produce equivalent counts: [`tests.py`](./tests.py)
- Benchmark/profiling artifacts for comparison:
  - [`benchmark_results.txt`](./benchmark_results.txt)
  - [`profile_baseline.txt`](./profile_baseline.txt)
  - [`profile_optimized.txt`](./profile_optimized.txt)

## Tech Stack

- Python 3 (standard library only)
  - `collections`, `random`, `string`, `time`, `cProfile`, `pstats`

## Project Structure

```text
.
├── original_app.py
├── optimized_app.py
├── tests.py
├── benchmark_results.txt
├── profile_baseline.txt
└── profile_optimized.txt
```

## Prerequisites

- Python 3.9+ (Python 3.10+ recommended)

## Installation

```bash
git clone https://github.com/kumarimanjusrimohantycse2024-art/Performance_optimization_project.git
cd Performance_optimization_project
```

No third-party dependencies are required.

## Configuration

This project does not require environment variables or secrets.

You can tune input size by passing `num_sentences` to `generate_text(...)` in the app modules for local experimentation.

## Usage

Run baseline version:

```bash
python original_app.py
```

Run optimized version:

```bash
python optimized_app.py
```

Each script prints:
- total words
- unique words
- top words
- elapsed time
- profiler output (and writes profiler output to a text file)

## Testing

Run correctness checks:

```bash
python tests.py
```

## Troubleshooting

- **`python: command not found`**: use `python3` instead of `python`.
- **Unexpected counts**: confirm punctuation/case normalization behavior in [`normalize_word`](./original_app.py) and [`normalize_word`](./optimized_app.py).
- **Profiler output file not updated**: ensure you have write permission in the repository directory.

## CI

A GitHub Actions workflow runs `python tests.py` on pushes and pull requests:
- [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make focused changes with tests
4. Open a pull request with clear rationale and validation notes

## License / Status

- **License:** No license file is currently present in this repository.
- **Status:** Active learning/demo project focused on performance optimization techniques.
