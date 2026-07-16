# Log Analyzer

A Python-based log analysis tool that scans application log files, counts log levels (ERROR, WARNING, INFO), generates a structured JSON report, and validates functionality using automated unit tests with Pytest.

---

## Features

- Analyze application log files
- Count ERROR, WARNING, and INFO messages
- Export analysis results as a JSON report
- Handle empty and missing log files
- Automated unit testing with Pytest

---

## Project Structure

```text
log-analyzer/
│
├── logs/
│   ├── app.log
│   └── api.log
│
├── reports/
│   └── report.json
│
├── analyzer.py
├── test_analyzer.py
├── requirements.txt
└── README.md
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
git clone https://github.com/yourusername/log-analyzer.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analyzer:

```bash
python analyzer.py
```

---

## Running Tests

Execute the test suite using Pytest:

```bash
pytest
```

Example:

```text
======================== test session starts ========================

collected 3 items

test_analyzer.py ...

======================== 3 passed ========================
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
