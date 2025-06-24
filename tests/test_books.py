import pytest
import requests
import allure


@allure.feature("Books")
@allure.story("Add new book successfully")
@pytest.mark.smoke
def test_add_book_success(unique_book_sample, base_url):

    with allure.step("Send POST request to add a new book"):
        res = requests.post(f"{base_url}/books", json=unique_book_sample)
    with allure.step("Validate status code is 200 or 201"):
        assert res.status_code in [200, 201]


@allure.feature("Books")
@allure.story("Try to add duplicate book (should fail)")
@pytest.mark.dependency(depends=["test_add_book_success"])
def test_add_book_conflict(unique_book_sample, base_url):
    with allure.step("Send POST request with duplicate book"):
        res = requests.post(f"{base_url}/books", json=unique_book_sample)
    with allure.step("Validate status code is 400"):
        assert res.status_code == 400


@allure.feature("Books")
@allure.story("Get list of books")
def test_get_books(base_url):
    with allure.step("Send GET request to fetch all books"):
        res = requests.get(f"{base_url}/books")
    with allure.step("Validate response is a list and status code is 200"):
        assert res.status_code == 200
        assert isinstance(res.json(), list)


@allure.feature("Books")
@allure.story("Update book successfully")
@pytest.mark.dependency(depends=["test_add_book_success"])
def test_update_book_success(created_book, base_url):
    updated = {**created_book, "title": "Updated Title"}
    with allure.step("Send PUT request to update the book"):
        res = requests.put(f"{base_url}/books/{created_book['id']}", json=updated)
    with allure.step("Validate status code is 200"):
        assert res.status_code == 200


@allure.feature("Books")
@allure.story("Update non-existing book (should fail)")
def test_update_book_not_found(created_book, base_url):
    with allure.step("Send PUT request to non-existing book ID"):
        res = requests.put(f"{base_url}/books/123456", json=created_book)
    with allure.step("Validate status code is 404"):
        assert res.status_code == 404


@allure.feature("Books")
@allure.story("Delete existing book")
@pytest.mark.dependency(depends=["test_add_book_success"])
def test_delete_book_success(created_book, base_url):
    with allure.step("Send DELETE request to remove the book"):
        res = requests.delete(f"{base_url}/books/{created_book['id']}")
    with allure.step("Validate status code is 200"):
        assert res.status_code == 200


@allure.feature("Books")
@allure.story("Delete non-existing book (should fail)")
def test_delete_book_not_found(base_url):
    with allure.step("Send DELETE request with invalid book ID"):
        res = requests.delete(f"{base_url}/books/123456")
    with allure.step("Validate status code is 404"):
        assert res.status_code == 404

