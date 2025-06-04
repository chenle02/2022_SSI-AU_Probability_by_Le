# 2022 Code Examples

This folder contains Python scripts for exploring the birthday problem.

Dependencies: Python 3 standard library (no external packages needed).

Scripts:
- **GenDOB.py**: Generate random dates of birth (month/day) for a class.
  Usage:
  ```bash
  python3 GenDOB.py [-n NUM_STUDENTS] [-o OUTPUT_CSV]
  ```
- **Checking.py**: Check for matching birthdays in a CSV file.
  Usage:
  ```bash
  python3 Checking.py [CSV_FILE]
  ```
- **BatchTest.py**: Run multiple trials to estimate the probability of shared birthdays.
  Usage:
  ```bash
  python3 BatchTest.py
  ```