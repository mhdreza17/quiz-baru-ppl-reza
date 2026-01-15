"""
Test Suite for Navigation & UI Flow
Test Cases: FT_018 - FT_021
"""
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestNavigationAndUI:
    """Test Cases for Navigation & UI Flow (UI.1)"""

    # ==================== FT_018: Redirect Register to Login ====================

    @pytest.mark.ui
    @pytest.mark.functional
    def test_ft_018_register_page_link_to_login(self, driver):
        """
        FT_018: Verifikasi redirect register ke login
        
        Preconditions:
        - User belum login
        
        Steps:
        1. Navigate ke halaman register.php
        2. Scroll down untuk melihat link login
        3. Klik link "Login" di footer
        
        Expected Result:
        - Navigate ke halaman login.php
        - URL berubah ke login.php
        - Form login ditampilkan
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Verify on register page
        assert register_page.is_page_title_correct(), "Should be on register page"
        
        # Action: Click login link
        register_page.click_login_link()
        time.sleep(1)
        
        # Expected: Redirect to login page
        assert "login.php" in driver.current_url, "Should redirect to login.php"
        
        # Verify login form is displayed
        login_page = LoginPage(driver)
        assert login_page.is_page_title_correct(), "Should display login form"

    # ==================== FT_019: Login Page Link to Register ====================

    @pytest.mark.ui
    @pytest.mark.functional
    def test_ft_019_login_page_link_to_register(self, driver):
        """
        FT_019: Verifikasi link Register pada halaman Login
        
        Preconditions:
        - User membuka halaman login
        
        Steps:
        1. Navigate ke halaman login.php
        2. Cari text "Belum punya account?"
        3. Klik link "Register"
        
        Expected Result:
        - Navigate ke halaman register.php
        - URL berubah ke register.php
        - Form register ditampilkan dengan input: Nama, Email, Username, Password, Re-Password
        """
        login_page = LoginPage(driver)
        login_page.navigate_to()
        
        # Verify on login page
        assert login_page.is_page_title_correct(), "Should be on login page"
        
        # Action: Click register link
        login_page.click_register_link()
        time.sleep(1)
        
        # Expected: Redirect to register page
        assert "register.php" in driver.current_url, "Should redirect to register.php"
        
        # Verify register form is displayed
        register_page = RegisterPage(driver)
        assert register_page.is_page_title_correct(), "Should display register form"

    # ==================== FT_020: Register Page Link to Login ====================

    @pytest.mark.ui
    @pytest.mark.functional
    def test_ft_020_register_page_header_link_to_login(self, driver):
        """
        FT_020: Verifikasi link Login pada halaman Register
        
        Preconditions:
        - User membuka halaman register
        
        Steps:
        1. Navigate ke halaman register.php
        2. Cari text "Sudah punya account?"
        3. Klik link "Login"
        
        Expected Result:
        - Navigate ke halaman login.php
        - URL berubah ke login.php
        - Form login ditampilkan dengan input: Username, Password
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Verify on register page
        assert register_page.is_page_title_correct(), "Should be on register page"
        
        # Verify login link exists (via page source)
        page_source = driver.page_source
        assert "login.php" in page_source, "Register page should have link to login"
        
        # Action: Click login link
        register_page.click_login_link()
        time.sleep(1)
        
        # Expected: Redirect to login page
        assert "login.php" in driver.current_url, "Should redirect to login.php"
        
        # Verify login form
        login_page = LoginPage(driver)
        assert login_page.is_page_title_correct(), "Should display login form"

    # ==================== FT_021: Logout and Page Protection ====================

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.stub
    def test_ft_021_logout_and_protected_pages(self, driver, insert_test_user):
        """
        FT_021: Verifikasi proses Logout dan proteksi halaman
        
        STUB TEST - Requires index.php implementation
        
        Preconditions:
        - User sudah login dan redirect ke index.php
        - halaman index.php memiliki tombol logout
        
        Steps:
        1. Login berhasil ke sistem
        2. Klik tombol Logout
        3. Session di-destroy
        4. Redirect ke halaman login
        5. Coba akses halaman index.php langsung
        
        Expected Result:
        - Session dihapus
        - Logout berhasil, redirect ke login.php
        - Direct access ke index.php redirect ke login.php
        - Halaman proteksi bekerja dengan baik
        """
        # Setup: Insert test user
        insert_test_user('testuser', 'test@example.com', 'Test@123')
        
        login_page = LoginPage(driver)
        login_page.navigate_to()
        
        # Action: Login
        login_page.login('testuser', 'Test@123')
        time.sleep(2)
        
        # At this point, should redirect to index.php
        current_url = driver.current_url
        
        # Note: index.php doesn't exist yet, so we skip this test
        # When index.php is implemented, this test should:
        # 1. Find and click logout button
        # 2. Verify redirect to login.php
        # 3. Verify session is destroyed
        
        pytest.skip("index.php not yet implemented - test requires complete implementation")

    # ==================== Additional Navigation Tests ====================

    @pytest.mark.ui
    @pytest.mark.functional
    def test_ui_navigation_consistency(self, driver):
        """
        Test to verify navigation consistency between login and register pages
        """
        login_page = LoginPage(driver)
        register_page = RegisterPage(driver)
        
        # Test 1: Login -> Register -> Login cycle
        login_page.navigate_to()
        assert login_page.is_page_title_correct()
        
        login_page.click_register_link()
        time.sleep(1)
        assert register_page.is_page_title_correct()
        
        register_page.click_login_link()
        time.sleep(1)
        assert login_page.is_page_title_correct()
        
        # Test 2: Register -> Login -> Register cycle
        register_page.navigate_to()
        assert register_page.is_page_title_correct()
        
        register_page.click_login_link()
        time.sleep(1)
        assert login_page.is_page_title_correct()
        
        login_page.click_register_link()
        time.sleep(1)
        assert register_page.is_page_title_correct()

    @pytest.mark.ui
    @pytest.mark.functional
    def test_ui_form_elements_display(self, driver):
        """
        Test to verify all form elements are properly displayed
        """
        login_page = LoginPage(driver)
        register_page = RegisterPage(driver)
        
        # Test Login page elements
        login_page.navigate_to()
        assert login_page.get_page_title() == "Sign-In"
        
        # Check input fields exist and are visible
        try:
            username_field = driver.find_element(By.ID, "username")
            password_field = driver.find_element(By.ID, "InputPassword")
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[name='submit']")
            
            assert username_field.is_displayed()
            assert password_field.is_displayed()
            assert submit_button.is_displayed()
        except:
            pytest.fail("Login form elements not properly displayed")
        
        # Test Register page elements
        register_page.navigate_to()
        assert register_page.get_page_title() == "Sign-Up"
        
        # Check input fields exist and are visible
        try:
            name_field = driver.find_element(By.ID, "name")
            email_field = driver.find_element(By.ID, "InputEmail")
            username_field = driver.find_element(By.ID, "username")
            password_field = driver.find_element(By.ID, "InputPassword")
            repassword_field = driver.find_element(By.ID, "InputRePassword")
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[name='submit']")
            
            assert name_field.is_displayed()
            assert email_field.is_displayed()
            assert username_field.is_displayed()
            assert password_field.is_displayed()
            assert repassword_field.is_displayed()
            assert submit_button.is_displayed()
        except:
            pytest.fail("Register form elements not properly displayed")
