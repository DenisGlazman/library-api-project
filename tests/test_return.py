import requests
import pytest
import allure

@allure.feature("Return Book")
@allure.story("Successfully return a borrowed book")
def test_return_book_success(base_url):
    user = {"id": 1001, "name": "Test User"}
    book = {"id": 2001, "title": "Test Book", "author": "Author"}

    requests.post(f"{base_url}/users", json=user)
    requests.post(f"{base_url}/books", json=book)

    loan_data = {"user_id": user["id"], "book_id": book["id"]}
    loan_response = requests.post(f"{base_url}/loan", json=loan_data)
    assert loan_response.status_code == 200, "Loan setup failed"

    res = requests.post(f"{base_url}/return", json=loan_data)

    assert res.status_code == 200
    assert res.json()["message"] == "Book returned"


@allure.feature("Return Book")
@allure.story("Fail to return book that was not borrowed by the user")
def test_return_book_fail_not_borrowed(base_url):
    user = {"id": 1002, "name": "Test User 2", "borrowed_books": []}
    book = {"id": 2002, "title": "Another Book", "author": "Author"}


    requests.post(f"{base_url}/users", json=user)
    requests.post(f"{base_url}/books", json=book)

    res = requests.post(f"{base_url}/return", json={
        "user_id": user["id"],
        "book_id": book["id"]
    })

    assert res.status_code == 400
    assert res.json()["error"] == "Book not borrowed by user"

@allure.feature("Return Book")
@allure.story("Fail to return when user or book not found")
@pytest.mark.parametrize("user_id, book_id", [
    (9999, 2003),
    (1003, 9999),
])
def test_return_book_user_or_book_not_found(base_url, user_id, book_id):

    if user_id == 1003:
        requests.post(f"{base_url}/users", json={"id": user_id, "name": "Partial User", "borrowed_books": []})
    if book_id == 2003:
        requests.post(f"{base_url}/books", json={"id": book_id, "title": "Partial Book", "author": "Author"})

    res = requests.post(f"{base_url}/return", json={
        "user_id": user_id,
        "book_id": book_id
    })

    assert res.status_code == 404
    assert res.json()["error"] == "User or book not found"
