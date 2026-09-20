# Contact Validator

A small Python library for validating and normalizing email addresses and phone numbers before they are stored in a database.

## Features

- Validate basic email addresses.
- Validate 10-digit phone numbers with optional dashes.
- Mask the local part of a valid email address.
- Normalize valid phone numbers to digits-only format.

## Project Layout

```text
src/
	contact_validator.py
tests/
	contact_validator_test.py
.github/workflows/
	tests.yml
	coverage.yml
requirements.txt
```

## Setup

Create and activate a virtual environment, then install the development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

```python
from src.contact_validator import (
		is_valid_email,
		is_valid_phone,
		mask_email,
		normalize_phone,
)

is_valid_email("student@example.com")       # True
is_valid_phone("555-123-4567")              # True
mask_email("priya@example.com")             # "pr***@example.com"
normalize_phone("555-123-4567")             # "5551234567"
```

Invalid non-string inputs raise `TypeError`. `mask_email` and `normalize_phone` raise `ValueError` when their input does not pass validation.

## Run Tests

Run the complete test suite:

```bash
python -m pytest
```

Run tests with coverage and enforce the project minimum of 85%:

```bash
python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=85
```

## Continuous Integration

This repository has two pull-request checks, both triggered only when a pull request targets `main`:

- **Tests** installs `requirements.txt` and runs the full pytest suite.
- **Coverage** runs the suite with coverage measured against `src` and fails when coverage is below 85%.

Keeping these checks on pull requests means broken code is detected before it is merged. The `coverage` check should be configured as a required status check in the `main` branch protection settings.

## Contributing

1. Create a branch for your change.
2. Add or update tests for the behavior you change.
3. Run the test and coverage commands locally.
4. Open a pull request targeting `main` and wait for both checks to pass.