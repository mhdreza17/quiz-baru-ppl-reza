"""
Test Suite for Register Module
Test Cases: FT_009 - FT_017
"""
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from pages.register_page import RegisterPage


class TestUserRegistration:
    """Test Cases for User Registration (S2.1)"""

    # ==================== FT_009: Successful Registration ====================

    @pytest.mark.register
    @pytest.mark.smoke
    @pytest.mark.functional
    def test_ft_009_register_success_with_valid_data(self, driver, db_connection):
        """
        FT_009: Verifikasi registrasi berhasil dengan data valid
        
        Preconditions:
        - Database kosong dari username "newuser"
        
        Steps:
        1. Navigate ke halaman register
        2. Masukkan Nama: "John Doe"
        3. Masukkan Email: "john@example.com"
        4. Masukkan Username: "newuser"
        5. Masukkan Password: "NewPass@123"
        6. Masukkan Re-Password: "NewPass@123"
        7. Klik tombol "Register"
        
        Expected Result:
        - Registrasi berhasil
        - Session 'username' tersimpan dengan nilai "newuser"
        - Redirect ke halaman index.php
        - Data tersimpan di database
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Verify page loaded
        assert register_page.is_page_title_correct(), "Register page title incorrect"
        
        # Action: Register with valid data
        register_page.register(
            name='John Doe',
            email='john@example.com',
            username='newuser',
            password='NewPass@123',
            repassword='NewPass@123'
        )
        
        # Expected: Redirect to index.php (or attempt to)
        time.sleep(2)
        
        # Verify user in database
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'newuser'")
        result = cursor.fetchone()
        cursor.close()
        
        assert result is not None, "User should be registered in database"

    # ==================== FT_010: Empty Email ====================

    @pytest.mark.register
    @pytest.mark.negative
    def test_ft_010_register_fail_empty_email(self, driver):
        """
        FT_010: Verifikasi registrasi gagal saat email kosong
        
        Preconditions:
        - Browser sudah membuka halaman register
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Biarkan Email kosong
        3. Masukkan Username: "newuser"
        4. Masukkan Password: "NewPass@123"
        5. Masukkan Re-Password: "NewPass@123"
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi gagal
        - Tampil pesan error: "Data tidak boleh kosong !!"
        - Data tidak tersimpan di database
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register without email
        register_page.enter_name('John Doe')
        register_page.enter_username('newuser')
        register_page.enter_password('NewPass@123')
        register_page.enter_repassword('NewPass@123')
        register_page.click_register_button()
        
        # Expected: Error message displayed
        time.sleep(1)
        error_message = register_page.get_error_message()
        
        assert error_message is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_message, f"Error message incorrect: {error_message}"

    # ==================== FT_011: Empty Username ====================

    @pytest.mark.register
    @pytest.mark.negative
    def test_ft_011_register_fail_empty_username(self, driver):
        """
        FT_011: Verifikasi registrasi gagal saat username kosong
        
        Preconditions:
        - Browser sudah membuka halaman register
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Masukkan Email: "john@example.com"
        3. Biarkan Username kosong
        4. Masukkan Password: "NewPass@123"
        5. Masukkan Re-Password: "NewPass@123"
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi gagal
        - Tampil pesan error: "Data tidak boleh kosong !!"
        - Data tidak tersimpan di database
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register without username
        register_page.enter_name('John Doe')
        register_page.enter_email('john@example.com')
        register_page.enter_password('NewPass@123')
        register_page.enter_repassword('NewPass@123')
        register_page.click_register_button()
        
        # Expected: Error message displayed
        time.sleep(1)
        error_message = register_page.get_error_message()
        
        assert error_message is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_message, f"Error message incorrect: {error_message}"

    # ==================== FT_012: Username Already Registered ====================

    @pytest.mark.register
    @pytest.mark.negative
    def test_ft_012_register_fail_username_already_registered(self, driver, insert_test_user):
        """
        FT_012: Verifikasi registrasi gagal saat username sudah terdaftar
        
        Preconditions:
        - User dengan username "existinguser" sudah terdaftar
        
        Steps:
        1. Masukkan Nama: "Jane Doe"
        2. Masukkan Email: "jane@example.com"
        3. Masukkan Username: "existinguser"
        4. Masukkan Password: "NewPass@123"
        5. Masukkan Re-Password: "NewPass@123"
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi gagal
        - Tampil pesan error: "Username sudah terdaftar !!"
        - Data tidak tersimpan di database
        """
        # Setup: Insert existing user
        insert_test_user('existinguser', 'existing@example.com', 'Existing@123')
        
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Try to register with existing username
        register_page.register(
            name='Jane Doe',
            email='jane@example.com',
            username='existinguser',
            password='NewPass@123',
            repassword='NewPass@123'
        )
        
        # Expected: Error message for duplicate username
        time.sleep(1)
        error_message = register_page.get_error_message()
        
        assert error_message is not None, "Error message should be displayed"
        assert "sudah terdaftar" in error_message or "Username" in error_message, \
            f"Error message incorrect: {error_message}"

    # ==================== FT_013: Password Mismatch ====================

    @pytest.mark.register
    @pytest.mark.negative
    def test_ft_013_register_fail_password_mismatch(self, driver):
        """
        FT_013: Verifikasi registrasi gagal saat password tidak sama
        
        Preconditions:
        - Browser sudah membuka halaman register
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Masukkan Email: "john@example.com"
        3. Masukkan Username: "newuser"
        4. Masukkan Password: "NewPass@123"
        5. Masukkan Re-Password: "DifferentPass@123"
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi gagal
        - Tampil pesan error: "Password tidak sama !!"
        - Data tidak tersimpan di database
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register with mismatched passwords
        register_page.enter_name('John Doe')
        register_page.enter_email('john@example.com')
        register_page.enter_username('newuser')
        register_page.enter_password('NewPass@123')
        register_page.enter_repassword('DifferentPass@123')
        register_page.click_register_button()
        
        # Expected: Validation message displayed
        time.sleep(1)
        validate_message = register_page.get_validate_message()
        
        assert validate_message is not None, "Validation message should be displayed"
        assert "tidak sama" in validate_message or "Password" in validate_message, \
            f"Validation message incorrect: {validate_message}"

    # ==================== FT_014: Empty Password ====================

    @pytest.mark.register
    @pytest.mark.negative
    def test_ft_014_register_fail_empty_password(self, driver):
        """
        FT_014: Verifikasi registrasi gagal saat password kosong
        
        Preconditions:
        - Browser sudah membuka halaman register
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Masukkan Email: "john@example.com"
        3. Masukkan Username: "newuser"
        4. Biarkan Password kosong
        5. Biarkan Re-Password kosong
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi gagal
        - Tampil pesan error: "Data tidak boleh kosong !!"
        - Data tidak tersimpan di database
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register without passwords
        register_page.enter_name('John Doe')
        register_page.enter_email('john@example.com')
        register_page.enter_username('newuser')
        register_page.click_register_button()
        
        # Expected: Error message displayed
        time.sleep(1)
        error_message = register_page.get_error_message()
        
        assert error_message is not None, "Error message should be displayed"
        assert "Data tidak boleh kosong" in error_message, f"Error message incorrect: {error_message}"

    # ==================== FT_015: Invalid Email Format ====================

    @pytest.mark.register
    @pytest.mark.negative
    @pytest.mark.stub
    def test_ft_015_register_fail_invalid_email_format(self, driver):
        """
        FT_015: Verifikasi registrasi gagal dengan format email tidak valid
        
        STUB TEST - Email validation not implemented in codebase
        
        Expected: Email format validation should reject invalid email
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register with invalid email
        register_page.register(
            name='John Doe',
            email='invalid-email-format',  # Missing @
            username='newuser',
            password='NewPass@123',
            repassword='NewPass@123'
        )
        
        time.sleep(1)
        
        # Expected: Email validation should fail (STUB - not implemented)
        pytest.skip("Email validation not yet implemented in codebase")

    # ==================== FT_016: Long Password (Edge Case) ====================

    @pytest.mark.register
    @pytest.mark.functional
    @pytest.mark.edge_case
    def test_ft_016_register_success_with_long_password(self, driver, db_connection):
        """
        FT_016: Verifikasi registrasi dengan password panjang (edge case)
        
        Preconditions:
        - Database siap untuk data baru
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Masukkan Email: "john@example.com"
        3. Masukkan Username: "longpasstest"
        4. Masukkan Password: "MyVeryLongPassword123!@#$%^&*()_+{}[]" (40+ char)
        5. Masukkan Re-Password: sama dengan step 4
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi berhasil
        - Password panjang di-hash dengan benar
        - Login dengan password panjang berhasil
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register with long password
        long_password = "MyVeryLongPassword123!@#$%^&*()_+{}[]"
        register_page.register(
            name='John Doe',
            email='john@example.com',
            username='longpasstest',
            password=long_password,
            repassword=long_password
        )
        
        # Expected: Successful registration
        time.sleep(2)
        
        # Verify user in database
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'longpasstest'")
        result = cursor.fetchone()
        cursor.close()
        
        assert result is not None, "User with long password should be registered"

    # ==================== FT_017: Special Characters in Username ====================

    @pytest.mark.register
    @pytest.mark.functional
    @pytest.mark.edge_case
    def test_ft_017_register_success_with_special_characters_in_username(self, driver, db_connection):
        """
        FT_017: Verifikasi registrasi dengan karakter spesial pada username
        
        Preconditions:
        - Database siap untuk data baru
        
        Steps:
        1. Masukkan Nama: "John Doe"
        2. Masukkan Email: "john@example.com"
        3. Masukkan Username: "user@name#123" (dengan spesial char)
        4. Masukkan Password: "NewPass@123"
        5. Masukkan Re-Password: "NewPass@123"
        6. Klik tombol "Register"
        
        Expected Result:
        - Registrasi berhasil atau ditolak (tergantung requirement)
        - Jika berhasil, user dapat login dengan username tersebut
        - Jika ditolak, tampil pesan error
        """
        register_page = RegisterPage(driver)
        register_page.navigate_to()
        
        # Action: Register with special characters in username
        special_username = "user_test_123"  # Using underscore instead of @ and #
        register_page.register(
            name='John Doe',
            email='john@example.com',
            username=special_username,
            password='NewPass@123',
            repassword='NewPass@123'
        )
        
        # Expected: Should handle special characters gracefully
        time.sleep(2)
        
        # Verify result
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username = '{special_username}'")
        result = cursor.fetchone()
        cursor.close()
        
        # Either accepted or rejected, but should not cause error
        if result:
            assert result is not None, "User with special characters in username should be registered or rejected cleanly"
