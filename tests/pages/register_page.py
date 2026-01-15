"""
Register Page Object Model
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    """Page Object for Register Page"""

    # Locators
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "InputEmail")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "InputPassword")
    REPASSWORD_INPUT = (By.ID, "InputRePassword")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    VALIDATE_MESSAGE = (By.CSS_SELECTOR, ".text-danger")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='login.php']")
    SIGN_UP_TITLE = (By.CSS_SELECTOR, "h4")

    def __init__(self, driver):
        """Initialize Register Page"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, base_url="http://localhost/quiz"):
        """Navigate to register page"""
        self.driver.get(f"{base_url}/register.php")

    def enter_name(self, name):
        """Enter name"""
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

    def enter_email(self, email):
        """Enter email"""
        email_input = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

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

    def enter_repassword(self, repassword):
        """Enter confirm password"""
        repassword_input = self.wait.until(EC.presence_of_element_located(self.REPASSWORD_INPUT))
        repassword_input.clear()
        repassword_input.send_keys(repassword)

    def click_register_button(self):
        """Click Register button"""
        submit_button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_button.click()

    def get_error_message(self):
        """Get error message if displayed"""
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE), timeout=5)
            return error_element.text
        except:
            return None

    def get_validate_message(self):
        """Get validation message if displayed"""
        try:
            validate_elements = self.driver.find_elements(*self.VALIDATE_MESSAGE)
            if validate_elements:
                return validate_elements[0].text
            return None
        except:
            return None

    def get_page_title(self):
        """Get page title"""
        title_element = self.wait.until(EC.presence_of_element_located(self.SIGN_UP_TITLE))
        return title_element.text

    def click_login_link(self):
        """Click Login link"""
        login_link = self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK))
        login_link.click()

    def register(self, name, email, username, password, repassword):
        """Perform register action"""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_repassword(repassword)
        self.click_register_button()

    def is_page_title_correct(self):
        """Verify page title is 'Sign-Up'"""
        return self.get_page_title() == "Sign-Up"

    def wait_for_error_message(self, timeout=5):
        """Wait for error message to appear"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE), timeout=timeout)
            return True
        except:
            return False
