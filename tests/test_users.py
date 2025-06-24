import pytest
import requests
import allure
import random


def generate_unique_user():
    return {
        "id": random.randint(10000, 99999),
        "name": f"User{random.randint(1000, 9999)}"
    }


@pytest.mark.users
@allure.feature("Users")
@allure.story("Get all users")
def test_get_users(base_url):
    with allure.step("Send GET request to fetch all users"):
        res = requests.get(f"{base_url}/users")

    with allure.step("Validate status code is 200"):
        assert res.status_code == 200

    with allure.step("Validate response is a list of users"):
        users = res.json()
        assert isinstance(users, list)

    with allure.step("Check structure of user objects if list is not empty"):
        if users:
            user = users[0]
            assert "id" in user
            assert "name" in user


@pytest.mark.users
@allure.feature("Users")
@allure.story("Add new user successfully")
def test_add_user_success(base_url):
    test_user = generate_unique_user()

    with allure.step("Send POST request to add a new user"):
        res = requests.post(f"{base_url}/users", json=test_user)

    with allure.step("Validate status code is 201 and response contains user data"):
        assert res.status_code == 201
        data = res.json()
        assert data["id"] == test_user["id"]
        assert data["name"] == test_user["name"]
        assert data["borrowed_books"] == []


@pytest.mark.users
@allure.feature("Users")
@allure.story("Add user without name (validation error)")
def test_add_user_missing_name(base_url):
    test_user = {
        "id": random.randint(10000, 99999)
    }

    with allure.step("Send POST request with missing name"):
        res = requests.post(f"{base_url}/users", json=test_user)

    with allure.step("Validate status code is 400 and error message present"):
        assert res.status_code == 400
        assert "error" in res.json()
        assert "Missing name" in res.json()["error"]


@pytest.mark.users
@allure.feature("Users")
@allure.story("Add duplicate user")
def test_add_user_duplicate(base_url):
    test_user = generate_unique_user()


    first_res = requests.post(f"{base_url}/users", json=test_user)
    assert first_res.status_code in [200, 201]

    with allure.step("Send POST request with same user ID again"):
        res = requests.post(f"{base_url}/users", json=test_user)

    with allure.step("Validate status code is 400 and duplicate error message"):
        assert res.status_code == 400
        assert "User already exists" in res.json().get("error", "")
