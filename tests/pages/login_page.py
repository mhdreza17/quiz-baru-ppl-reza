"""
Login Page Object Model
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for Login Page"""

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "InputPassword")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='register.php']")
    SIGN_IN_TITLE = (By.CSS_SELECTOR, "h4")

    def __init__(self, driver):
        """Initialize Login Page"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, base_url="http://localhost/quiz"):
        """Navigate to login page"""
        self.driver.get(f"{base_url}/login.php")

    def enter_username(self, username):
        """Enter username"""
        username_input = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        """Enter password"""
        password_input = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def click_sign_in_button(self):
        """Click Sign In button"""
        submit_button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_button.click()

    def get_error_message(self):
        """Get error message if displayed"""
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE), timeout=5)
            return error_element.text
        except:
            return None

    def get_page_title(self):
        """Get page title"""
        title_element = self.wait.until(EC.presence_of_element_located(self.SIGN_IN_TITLE))
        return title_element.text

    def click_register_link(self):
        """Click Register link"""
        register_link = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        register_link.click()

    def login(self, username, password):
        """Perform login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in_button()

    def is_page_title_correct(self):
        """Verify page title is 'Sign-In'"""
        return self.get_page_title() == "Sign-In"

    def get_username_input_value(self):
        """Get username input value"""
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        return username_input.get_attribute("value")

    def get_password_input_value(self):
        """Get password input value"""
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        return password_input.get_attribute("value")

    def wait_for_error_message(self, timeout=5):
        """Wait for error message to appear"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE), timeout=timeout)
            return True
        except:
            return False
