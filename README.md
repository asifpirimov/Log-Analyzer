# Log Analyzer

A Python-based log analysis tool that scans application log files, counts log levels (ERROR, WARNING, INFO), generates a structured JSON report, and validates functionality using automated unit tests with Pytest.

---

## Features

- Analyze application log files
- Count ERROR, WARNING, and INFO log entries
- Generate JSON reports automatically
- Handle empty log files
- Handle missing log files using exception handling
- Automated testing with Pytest

## Project Structure

```text
log-analyzer/
│
├── logs/
│   ├── app.log
│   └── api.log
│
├── reports/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_analyzer.py
│
├── .gitignore
├── analyzer.py
├── README.md
└── requirements.txt
```

---

## Technologies

- Python 3
- JSON
- Pytest
- Regular Expressions (Regex)
- File Handling

---

## Example Log

```text
2026-07-12 10:12:31 ERROR Database connection failed
2026-07-12 10:13:10 WARNING High memory usage
2026-07-12 10:13:40 ERROR Timeout while calling API
2026-07-12 10:14:00 INFO User logged in
```

---

## Example Output

```json
{
    "ERRORS": [
        "2026-07-12 10:12:31 ERROR Database connection failed",
        "2026-07-12 10:13:40 ERROR Timeout while calling API"
    ],
    "Number of ERRORS": 2,
    "Number of WARNINGS": 1,
    "Number of INFO": 1
}
```

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/asifpirimov/Log-Analyzer.git
cd Log-Analyzer
```

---

## Running Tests

Run all tests:

```bash
pytest
```

or

```bash
pytest tests/
```

---

## Current Test Coverage

The current test suite validates:

- Valid log analysis
- Empty log file handling
- Missing file handling

---

## Future Improvements

- Parse timestamps and log messages
- Support custom log levels
- Configuration file support
- CLI interface
- HTML report generation
- CSV export
- Performance optimization for large log files
- GitHub Actions CI integration

---

## Learning Objectives

This project demonstrates practical experience with:

- Python functions
- Exception handling
- File processing
- JSON serialization
- Data structures
- Unit testing with Pytest
- Project organization
