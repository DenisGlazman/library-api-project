import pytest
import requests
import allure

@allure.feature("Loans")
@allure.story("Successfully loan a book")
@pytest.mark.dependency(depends=["test_add_book_success"])
def test_loan_book_success(user_sample, created_book, loan_sample, base_url):
    with allure.step("Create a test user"):
        requests.post(f"{base_url}/users", json=user_sample)
    with allure.step("Create a test book"):
        requests.post(f"{base_url}/books", json=created_book)
    with allure.step("Send POST request to loan the book to the user"):
        res = requests.post(f"{base_url}/loan", json=loan_sample)
    with allure.step("Validate status code is 200"):
        assert res.status_code == 200


@allure.feature("Loans")
@allure.story("Fail to loan a non-existing book")
def test_loan_book_fail_book_not_found(user_sample, base_url):
    with allure.step("Send POST request to loan a non-existing book"):
        res = requests.post(f"{base_url}/loan", json={"book_id": 123456, "user_id": user_sample["id"]})
    with allure.step("Validate status code is 404"):
        assert res.status_code == 404
