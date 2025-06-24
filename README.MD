# README.md

##  Library Management API Testing

This project contains automated tests for a mock Library Management API. The API allows managing books, users, and loan/return operations.

---

##  Project Structure

```
library_api_project/
├── app.py # Flask demo API implementation
├── tests/ # Automated API tests using pytest and Allure
│ ├── test_books.py
│ ├── test_users.py
│ ├── test_loans.py
│ └── test_return.py
├── requirements.txt # Python dependencies
├── TEST_PLAN.md # Detailed test plan and scenarios description
├── README.md # This file
```

---

##  How to Run Tests

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests with Allure reporting

```bash
pytest tests/ --alluredir=allure-results
```

### 4. Generate Allure report

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

> Make sure `allure` is installed: [https://docs.qameta.io/allure/#\_installing\_a\_commandline](https://docs.qameta.io/allure/#_installing_a_commandline)

---

## Tested Endpoints (via `https://github.com/LBS720/library-management-api`)

* Tested API Endpoints
GET /books — List all books
POST /books — Add a new book
PUT /books/{book_id} — Update book details
DELETE /books/{book_id} — Delete a book
GET /users — List all users
POST /users — Add a new user
POST /loan — Loan a book to a user
POST /return — Return a loaned book
---

## Test Coverage
Positive and negative test cases for all endpoints
Validation of HTTP status codes and response payloads
Dependency management between tests using pytest-dependency
Detailed step-by-step reporting using Allure steps
See TEST_PLAN.md for full test descriptions.
---

##  Notes

Tests expect the API server to be running locally at http://127.0.0.1:5000 by default.

To run the mock API server locally:

bash

git clone https://github.com/LBS720/library-management-api.git
cd library-management-api
python3 app.py
Adjust the base_url fixture in the tests if the server URL is different.

---

##  Author

Denis Glazman

---

