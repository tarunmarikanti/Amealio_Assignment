from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    SIGNIN_URL = "https://www.imdb.com/registration/signin"
    
    # Locator for the 'Sign in with IMDb' button on the initial sign-in page
    EMAIL_BTN = (By.XPATH, "//span[contains(text(),'Sign in with IMDb')]")
    EMAIL_FIELD = (By.ID, "ap_email")
    PWD_FIELD = (By.ID, "ap_password")
    SIGNIN_SUBMIT = (By.ID, "signInSubmit")
    ERROR_MSG = (By.CLASS_NAME, "a-alert-content")  # IMDb error message container

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.SIGNIN_URL)

    def login_flow(self, email, password):
        # Click the 'Sign in with IMDb' button and wait for email field to appear
        self.driver.find_element(*self.EMAIL_BTN).click()
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PWD_FIELD).send_keys(password)
        self.driver.find_element(*self.SIGNIN_SUBMIT).click()

    def error_visible(self):
        return len(self.driver.find_elements(*self.ERROR_MSG)) > 0
