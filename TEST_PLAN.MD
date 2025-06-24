# TEST_PLAN.md

## 📋 Overview

This test plan outlines the test coverage for the Library Management API. The tests are written in `pytest` and focus on verifying the functional behavior and error handling of all supported endpoints. The main goal is to ensure API reliability, correctness, and resilience.

---

## 🔌 Tested Endpoints

| Endpoint           | Method | Description                           |
|--------------------|--------|---------------------------------------|
| `/books`           | GET    | Retrieve a list of all books          |
| `/books`           | POST   | Add a new book                        |
| `/books/{book_id}` | PUT    | Update details of a specific book     |
| `/books/{book_id}` | DELETE | Delete a book by ID                   |
| `/users`           | GET    | Retrieve a list of all users          |
| `/users`           | POST   | Add a new user                        |
| `/loan`            | POST   | Loan a book to a user                 |
| `/return`          | POST   | Return a previously loaned book       |

---

## ✅ Positive Test Scenarios

- **POST /books** — Add a new book with a unique ID → `201 Created`
- **GET /books** — Retrieve the list of all books → `200 OK`
- **PUT /books/{book_id}** — Update an existing book → `200 OK`
- **DELETE /books/{book_id}** — Delete an existing book → `200 OK`
- **GET /users** — Get all registered users → `200 OK`
- **POST /users** — Add a new user → `201 Created`
- **POST /loan** — Loan a valid book to a valid user → `200 OK`
- **POST /return** — Return a valid loaned book → `200 OK`

---

## ❌ Negative Test Scenarios

- **POST /books** — Add a duplicate book (same ID) → `400 Bad Request`
- **PUT /books/{book_id}** — Update non-existent book → `404 Not Found`
- **DELETE /books/{book_id}** — Delete non-existent book → `404 Not Found`
- **POST /loan** — Loan a non-existent book → `404 Not Found`
- **POST /loan** — Loan a book to a non-existent user → `404 Not Found`
- **POST /loan** — Loan a book that is already borrowed → `400 Bad Request`
- **POST /return** — Return a book not loaned to the user → `400 Bad Request`
- **POST /return** — Return a non-existent book or from non-existent user → `404 Not Found`

---

## 🛡️ Importance of Tests

- **Positive tests** ensure core functionality works as intended.
- **Negative tests** validate that the API responds correctly to invalid operations and inputs.
- **Response code checks (200/201/400/404)** ensure correct client feedback and prevent silent failures.

This suite increases development confidence and reduces risk when deploying backend changes or refactoring code.

---

## 📂 File Location

This file should be placed at the root of the project alongside `README.md`:


