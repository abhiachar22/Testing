SDET_testing — Automation Practice (Python + Playwright)

Overview
This repository contains example UI, API and data-driven tests implemented with Python and Playwright. It demonstrates Page Object Model, pytest-based organization, and simple API helpers to practice SDET skills.

Prerequisites
- Python 3.10 or newer
- Git (optional)
- Windows: PowerShell or CMD

Quick setup (Windows)
1. Open PowerShell and change to project folder:
   cd "C:\Users\v-avishwanat\OneDrive - Microsoft\Desktop\SDET_testing"
2. (Recommended) Create and activate virtualenv:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install dependencies:
   python -m pip install --upgrade pip
   pip install -r requirements.txt
4. Install Playwright browsers (if using playwright):
   python -m playwright install

Run tests
- Run all tests: pytest -v
- Run a single test file: pytest tests/test_example.py -q
- Run tests headless: pytest -k "name" --headless

Project layout (important folders)
- tests/: pytest test modules
- PageObjects/: Page Object classes for UI tests
- data/: test data (credentials, CSV/Excel samples)
- utils/: helper modules (API utils, browser helpers)
- reports/: generated test outputs (HTML, screenshots)

Notes & recommendations
- Remove the venv/ directory from source control and add it to .gitignore.
- Add a CI workflow (GitHub Actions or Azure Pipelines) to run tests and publish reports.
- Prefer parameterized pytest tests for data-driven scenarios and PageObject for maintainability.

If anything here is unclear or you want a different README layout, say which sections to change.