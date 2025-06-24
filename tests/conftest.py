import time
import pytest
import requests


@pytest.fixture(scope="module")
def base_url():
    return "http://127.0.0.1:5000"



@pytest.fixture(scope="module")
def unique_book_sample():
    return {
        "id": 91383,
        "title": "Test Book",
        "author": "Author"
    }

@pytest.fixture(scope="module")
def created_book(unique_book_sample, base_url):
    # Delete the book with this id if it already exists
    requests.delete(f"{base_url}/books/{unique_book_sample['id']}")

    res = requests.post(f"{base_url}/books", json=unique_book_sample)
    assert res.status_code in [200, 201]
    return unique_book_sample


@pytest.fixture(scope="module")
def user_sample():
    return {"id": 1999, "name": "Test User", "borrowed_books": []}


@pytest.fixture(scope="module")
def loan_sample(created_book, user_sample):
    return {"book_id": created_book["id"], "user_id": user_sample["id"]}
