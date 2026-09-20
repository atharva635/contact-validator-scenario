# Contact Validator

[![Tests](https://github.com/atharva635/contact-validator-scenario/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/atharva635/contact-validator-scenario/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/badge/coverage-required%2085%25-brightgreen)](https://github.com/atharva635/contact-validator-scenario/actions/workflows/coverage.yml)
[![Python](https://img.shields.io/badge/python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-not%20specified-lightgrey)](#project-status)

A lightweight Python library for validating and formatting contact data before it is saved to a database. The project currently focuses on basic email validation, phone validation, email masking, and phone normalization.

## What This Project Does

| Capability | Description | Example result |
| --- | --- | --- |
| Email validation | Checks a string against a basic email pattern. | `student@example.com` -> `True` |
| Phone validation | Accepts exactly 10 digits, with optional dashes. | `555-123-4567` -> `True` |
| Email masking | Keeps the first two local-part characters and masks the rest. | `priya@example.com` -> `pr***@example.com` |
| Phone normalization | Removes dashes from a valid phone number. | `555-123-4567` -> `5551234567` |

## Technology Stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Language | Python 3.x | Application and test code |
| Runtime dependency | Python standard library (`re`) | Email pattern matching |
| Test framework | `pytest 8.4.1` | Test discovery and assertions |
| Coverage engine | `coverage 7.9` | Measures executed source lines |
| Pytest integration | `pytest-cov 6.2.1` | Runs coverage through pytest |
| CI platform | GitHub Actions | Runs automated checks on pull requests |
| Development environment | GitHub Codespaces or Python virtualenv | Reproducible local development |
| External services | None | No database or API is required to run this project |

## Project Structure

```text
contact-validator-scenario/
├── src/
│   └── contact_validator.py       # Validation and formatting functions
├── tests/
│   └── contact_validator_test.py  # pytest test suite
├── .github/
│   └── workflows/
│       ├── tests.yml              # Pull-request test check
│       └── coverage.yml           # Pull-request coverage gate
├── requirements.txt               # Pinned development dependencies
└── README.md
```

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Run the test suite

```bash
python -m pytest
```

### 4. Run the enforced coverage check

```bash
python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=85
```

The command exits with a non-zero status when total coverage is below 85%.

## API Reference

### `is_valid_email(email)`

Returns `True` when `email` is a string matching the library's basic email pattern; otherwise returns `False`.

```python
is_valid_email("student@example.com")  # True
is_valid_email("not-an-email")          # False
```

Raises `TypeError` when `email` is not a string.

### `is_valid_phone(phone)`

Returns `True` when `phone` contains exactly 10 digits, optionally separated by dashes.

```python
is_valid_phone("5551234567")     # True
is_valid_phone("555-123-4567")   # True
is_valid_phone("12345")          # False
```

Raises `TypeError` when `phone` is not a string.

### `mask_email(email)`

Validates an email and masks characters in its local part. The domain remains unchanged.

```python
mask_email("priya@example.com")  # "pr***@example.com"
mask_email("a@example.com")      # "a@example.com"
```

Raises `ValueError` when the email is invalid.

### `normalize_phone(phone)`

Validates a phone number and returns it without dashes.

```python
normalize_phone("555-123-4567")  # "5551234567"
```

Raises `ValueError` when the phone number is invalid.

## Continuous Integration

The repository has two GitHub Actions workflows. Both use `pull_request` events targeting `main`, so code is checked before it is merged:

### Tests workflow

Defined in `.github/workflows/tests.yml`:

1. Checks out the pull-request branch.
2. Installs Python 3.x.
3. Installs the pinned dependencies from `requirements.txt`.
4. Runs the complete pytest suite.

Any failing test makes the workflow fail.

### Coverage workflow

Defined in `.github/workflows/coverage.yml`:

1. Repeats the clean Python setup and dependency installation.
2. Measures coverage specifically against the `src` directory.
3. Fails with `--cov-fail-under=85` when coverage drops below 85%.
4. Adds the coverage report to the GitHub Actions step summary.

The `coverage` check should be configured as a required status check in the branch protection settings for `main`. This prevents a pull request with insufficient coverage from being merged.

## Why Pull Requests Instead of Pushes?

The workflows deliberately run on pull requests targeting `main`. A push-only workflow could report that code is broken only after it has already been merged. Pull-request checks give maintainers a pass/fail result while the change is still reviewable and can block the merge when a required check fails.

## CI Exercise Results

The initial test suite measured 52% coverage. After adding tests for the previously untested email masking and phone normalization behavior, the suite reached 95.65% coverage with all tests passing.

The exercise also verified that:

- A pull request can produce a real failing coverage check.
- The failure is visible in the Actions logs and pull-request checks.
- Adding the missing tests makes the coverage check pass.

## Contributing

1. Create a feature branch.
2. Add or update tests for every behavior change.
3. Run `python -m pytest` locally.
4. Run the 85% coverage command locally.
5. Open a pull request targeting `main`.
6. Merge only after the `Tests` and `Coverage` checks pass.

## Project Status

This is a small practice project. It has no published package metadata and no license file yet. The validation rules are intentionally basic and should not be treated as complete email or international phone-number validation.