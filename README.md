# Log Analyzer

A Python-based log analysis tool developed as part of my QA Automation learning journey. The project analyzes application log files, counts log levels (ERROR, WARNING, INFO), generates structured JSON reports, and includes automated unit tests using Pytest.

---

## Features

- Analyze application log files
- Count ERROR, WARNING, and INFO log entries
- Generate structured JSON reports
- Handle empty log files
- Handle missing files using exception handling
- Automated testing with Pytest

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
- Pytest
- JSON
- Regular Expressions (Regex)
- File Handling
- Exception Handling
- Git & GitHub

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

## Installation

Clone the repository:

```bash
git clone https://github.com/asifpirimov/Log-Analyzer.git
cd Log-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the analyzer:

```bash
python analyzer.py
```

A JSON report will be generated inside the `reports` directory.

---

## Running Tests

Run all tests:

```bash
pytest
```

Example output:

```text
========================= test session starts =========================

collected 3 items

tests/test_analyzer.py ...

========================== 3 passed ==========================
```

---

## Current Test Coverage

The current test suite verifies:

- Valid log file analysis
- Empty log file handling
- Missing file handling
- JSON report generation

---

## Future Improvements

- Parse timestamps, log levels, and messages separately
- Support multiple log files
- Read configuration from a JSON file
- Command-line interface (CLI)
- HTML and CSV report generation
- Advanced regular expression parsing
- Increase unit test coverage
- Continuous Integration with GitHub Actions

---

## Learning Objectives

This project was developed to strengthen practical skills in:

- Python
- File processing
- Exception handling
- JSON serialization
- Regular Expressions
- Unit testing with Pytest
- Software testing fundamentals
- Git & GitHub workflow

---

## Requirements

- Python 3.10+
- Pytest

Install Pytest if needed:

```bash
pip install pytest
```

---

## License

This project is intended for learning, portfolio, and educational purposes.
