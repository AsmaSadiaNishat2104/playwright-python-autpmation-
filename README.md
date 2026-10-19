
# Python Playwright Automation Practice

A hands-on UI test automation project using Python,
Playwright, and Pytest.

## Technologies Used

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- CSV Data-Driven Testing
- Pytest Fixtures
- Pytest Markers
- Allure Reporting

## Features Implemented

- Positive and negative login scenarios
- Data-driven testing using CSV files
- Parameterized test execution
- Reusable Page Object Model
- Reusable Pytest fixtures
- Smoke and regression test categorization
- Allure test reporting

## Project Structure

- `pages/` - Page objects and locators
- `test/` - Automated test cases and fixtures
- `test_data/` - CSV test data
- `pytest.ini` - Pytest configuration
- `requirements.txt` - Python dependencies

## Installation

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run Tests

Run all tests:

```bash
python -m pytest -v
```

Run login tests:

```bash
python -m pytest test/Login/test_login.py -v
```

Run Smoke tests:

```bash
python -m pytest -m smoke -v
```

Run Regression tests:

```bash
python -m pytest -m regression -v
```

## Allure Reporting

Execute tests and collect results:

```bash
python -m pytest test/Login/test_login.py \
  --alluredir=allure-results --clean-alluredir
```

Open the Allure Report:

```bash
allure serve allure-results
```

The Allure CLI must be installed separately.

## Learning Progress

This repository documents my practical learning
journey in Python Playwright test automation.
