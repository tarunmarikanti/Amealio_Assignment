import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from tests.utils import save_screenshot


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login_flow("tarunm", "tarunm@9")  # Replace with valid credentials
    time.sleep(3)  # Wait for login to complete 
    save_screenshot(driver, "login_success")
    # TODO: Add assertions verifying successful login 


def test_failed_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login_flow("wrongUN", "wrong_password")
    time.sleep(3)  # Wait for error message display
    save_screenshot(driver, "login_failed")
    assert login.error_visible(), "Expected error message for invalid login"


def test_login_empty_fields_two_step(driver):
    login = LoginPage(driver)
    login.open()
    # Sending empty strings simulates empty fields submission using your existing flow
    login.login_flow("", "")
    time.sleep(2)  # Give time for validation errors to appear
    save_screenshot(driver, "login_empty_fields_two_step")
    assert login.error_visible(), "Expected validation error messages when submitting empty login fields"
