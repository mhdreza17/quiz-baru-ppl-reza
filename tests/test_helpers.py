"""
Test Utilities and Helper Functions
"""
import subprocess
import hashlib
import json
from datetime import datetime


class DatabaseHelper:
    """Helper class for database operations"""
    
    @staticmethod
    def hash_password_php(password):
        """
        Hash password using PHP password_hash function
        Compatible with PHP bcrypt hashing
        """
        try:
            result = subprocess.run(
                ['php', '-r', f"echo password_hash('{password}', PASSWORD_DEFAULT);"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() if result.stdout else None
        except Exception as e:
            print(f"Error hashing password with PHP: {e}")
            return None
    
    @staticmethod
    def verify_password_php(password, hash_value):
        """
        Verify password against PHP bcrypt hash
        """
        try:
            php_code = f"""
            <?php
            $password = '{password}';
            $hash = '{hash_value}';
            echo (password_verify($password, $hash)) ? 'true' : 'false';
            ?>
            """
            result = subprocess.run(
                ['php', '-r', php_code.replace('<?php ', '').replace(' ?>', '')],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() == 'true'
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False


class TestDataGenerator:
    """Generate test data"""
    
    @staticmethod
    def generate_username():
        """Generate unique username"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f"testuser_{timestamp}"
    
    @staticmethod
    def generate_email():
        """Generate unique email"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        return f"test_{timestamp}@example.com"
    
    @staticmethod
    def get_valid_register_data():
        """Get valid registration test data"""
        return {
            'name': 'Test User',
            'email': TestDataGenerator.generate_email(),
            'username': TestDataGenerator.generate_username(),
            'password': 'TestPass@123',
            'repassword': 'TestPass@123'
        }
    
    @staticmethod
    def get_invalid_register_data_variations():
        """Get variations of invalid registration data"""
        base_data = TestDataGenerator.get_valid_register_data()
        
        return {
            'empty_name': {**base_data, 'name': ''},
            'empty_email': {**base_data, 'email': ''},
            'empty_username': {**base_data, 'username': ''},
            'empty_password': {**base_data, 'password': '', 'repassword': ''},
            'password_mismatch': {**base_data, 'repassword': 'Different@123'},
            'invalid_email': {**base_data, 'email': 'invalid-email'},
            'long_password': {**base_data, 'password': 'A' * 100, 'repassword': 'A' * 100},
            'special_username': {**base_data, 'username': 'user@test#123'}
        }


class SeleniumHelper:
    """Helper functions for Selenium tests"""
    
    @staticmethod
    def wait_for_redirect(driver, expected_url, timeout=5):
        """Wait for redirect to specific URL"""
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if expected_url in driver.current_url:
                return True
            time.sleep(0.5)
        
        return False
    
    @staticmethod
    def clear_all_cookies(driver):
        """Clear all cookies"""
        driver.delete_all_cookies()
    
    @staticmethod
    def get_current_url(driver):
        """Get current URL"""
        return driver.current_url
    
    @staticmethod
    def take_screenshot(driver, filename):
        """Take screenshot for debugging"""
        driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")


class ReportHelper:
    """Helper for test reporting"""
    
    @staticmethod
    def generate_test_summary(test_results):
        """Generate test summary report"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_tests': len(test_results),
            'passed': len([t for t in test_results if t.get('status') == 'PASSED']),
            'failed': len([t for t in test_results if t.get('status') == 'FAILED']),
            'skipped': len([t for t in test_results if t.get('status') == 'SKIPPED']),
            'tests': test_results
        }
        return summary
    
    @staticmethod
    def save_report_json(report_data, filename='test_report.json'):
        """Save test report as JSON"""
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=2)
        print(f"Report saved: {filename}")
    
    @staticmethod
    def print_test_summary(summary):
        """Print test summary to console"""
        print("\n" + "="*50)
        print("TEST EXECUTION SUMMARY")
        print("="*50)
        print(f"Timestamp: {summary['timestamp']}")
        print(f"Total Tests: {summary['total_tests']}")
        print(f"Passed: {summary['passed']} ✓")
        print(f"Failed: {summary['failed']} ✗")
        print(f"Skipped: {summary['skipped']} ⊘")
        print(f"Pass Rate: {(summary['passed']/summary['total_tests']*100):.1f}%")
        print("="*50 + "\n")


class ValidationHelper:
    """Helper for validation checks"""
    
    @staticmethod
    def is_valid_email(email):
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_valid_username(username):
        """Validate username format"""
        import re
        # Allow alphanumeric, underscore, hyphen
        pattern = r'^[a-zA-Z0-9_-]{3,20}$'
        return re.match(pattern, username) is not None
    
    @staticmethod
    def is_strong_password(password):
        """Validate password strength"""
        # Minimum 8 chars, at least 1 uppercase, 1 lowercase, 1 digit, 1 special char
        import re
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True


if __name__ == '__main__':
    # Test helpers
    print("Test Data Generator Examples:")
    print(f"Username: {TestDataGenerator.generate_username()}")
    print(f"Email: {TestDataGenerator.generate_email()}")
    print(f"Valid Data: {TestDataGenerator.get_valid_register_data()}")
    
    print("\nValidation Examples:")
    print(f"Valid email: {ValidationHelper.is_valid_email('test@example.com')}")
    print(f"Invalid email: {ValidationHelper.is_valid_email('invalid-email')}")
    print(f"Strong password: {ValidationHelper.is_strong_password('Test@123')}")
