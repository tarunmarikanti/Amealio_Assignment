# Amealio Assignment - IMDb Automation Tests

## Project Overview

This project contains automated tests for IMDb login and UI interactions using Selenium WebDriver and pytest. It verifies login scenarios, menu hover flows, and validation behaviors on IMDb.

---

## Features

- Automated login tests: successful login, failed login, and validation of empty fields.
- Hover menu interaction test on IMDb homepage.
- Screenshot capture during tests for visual verification.
- Uses Python, Selenium, and pytest.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- pip for Python package management

### Installation

1. Clone the repository:

git clone https://github.com/tarunmarikanti/Amealio_Assignment.git
cd Amealio_Assignment


2. Install dependencies:

pip install -r requirements.txt

---

## Running Tests

Run all tests using pytest:

pytest --html=report.html --self-contained-html


- This will generate an HTML report named `report.html` in the project root.
- Open the `report.html` file in a browser to view the test results.

Run a specific test file:

pytest tests/test_login.py --html=report.html --self-contained-html




---

## Project Structure

Amealio_Assignment/
├── pages/ # Page Object classes
├── tests/ # Test cases
├── utils/ # Helper utilities like screenshot capture
├── requirements.txt # Python dependencies
├── README.md # Project documentation

