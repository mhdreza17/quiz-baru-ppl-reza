"""
Test Fixtures and Configuration
"""
import pytest
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# ==================== Database Fixtures ====================

@pytest.fixture(scope="session")
def db_connection():
    """Create database connection for test setup and teardown"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='quiz_pengupil'
        )
        yield conn
        conn.close()
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        raise


@pytest.fixture(autouse=True)
def db_cleanup(db_connection):
    """Clean up test data before and after each test"""
    cursor = db_connection.cursor()
    
    # Delete test users before test
    test_usernames = ['testuser', 'newuser', 'existinguser', 'longpasstest', 
                     'user@name#123', 'nonexistentuser', 'testuser2']
    for username in test_usernames:
        try:
            cursor.execute(f"DELETE FROM users WHERE username = '{username}'")
            db_connection.commit()
        except:
            pass
    
    yield
    
    # Clean up after test
    for username in test_usernames:
        try:
            cursor.execute(f"DELETE FROM users WHERE username = '{username}'")
            db_connection.commit()
        except:
            pass
    
    cursor.close()


@pytest.fixture
def insert_test_user(db_connection):
    """Insert test user into database"""
    def _insert_user(username, email, password, name="Test User"):
        cursor = db_connection.cursor()
        hashed_password = __hash_password(password)
        try:
            # First delete if exists
            cursor.execute(f"DELETE FROM users WHERE username = %s", (username,))
            db_connection.commit()
            
            # Then insert
            query = f"INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, name, email, hashed_password))
            db_connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error inserting user: {e}")
            cursor.close()
            return False
    
    return _insert_user


def __hash_password(password):
    """
    Hash password using PHP compatible algorithm
    Note: In real scenario, you should call PHP function or use compatible library
    For testing, we'll use a stub implementation
    """
    import subprocess
    import json
    
    # Call PHP to hash password
    php_code = f"""<?php echo password_hash('{password}', PASSWORD_DEFAULT); ?>"""
    try:
        result = subprocess.run(
            ['php', '-r', f"echo password_hash('{password}', PASSWORD_DEFAULT);"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except:
        # Fallback: return password as is for testing (NOT SECURE)
        print(f"Warning: Could not hash password with PHP, using plain password for testing")
        return password


# ==================== Selenium Fixtures ====================

@pytest.fixture(scope="session")
def chrome_driver_options():
    """Configure Chrome WebDriver options"""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for CI/CD
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-web-resources")
    return options


@pytest.fixture
def driver(chrome_driver_options):
    """Setup WebDriver for each test"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_driver_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def driver_ui(chrome_driver_options):
    """Setup WebDriver for UI tests (non-headless for debugging)"""
    # Uncomment the next line to run UI tests in non-headless mode
    # chrome_driver_options.headless = False
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_driver_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# ==================== Test Data Fixtures ====================

@pytest.fixture
def valid_login_data():
    """Valid login test data"""
    return {
        'username': 'testuser',
        'password': 'Test@123'
    }


@pytest.fixture
def valid_register_data():
    """Valid register test data"""
    return {
        'name': 'John Doe',
        'email': 'john@example.com',
        'username': 'newuser',
        'password': 'NewPass@123',
        'repassword': 'NewPass@123'
    }


@pytest.fixture
def existing_user_data(db_connection):
    """Create and return existing user data"""
    username = 'existinguser'
    email = 'existing@example.com'
    password = 'Existing@123'
    name = 'Existing User'
    
    cursor = db_connection.cursor()
    hashed_password = __hash_password(password)
    
    try:
        # Delete first if exists
        cursor.execute(f"DELETE FROM users WHERE username = %s", (username,))
        db_connection.commit()
        
        # Insert test user
        query = f"INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, name, email, hashed_password))
        db_connection.commit()
    except Error as e:
        print(f"Error creating existing user: {e}")
    finally:
        cursor.close()
    
    return {
        'username': username,
        'email': email,
        'password': password,
        'name': name
    }


# ==================== Marker Fixtures ====================

def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "login: mark test as login module test"
    )
    config.addinivalue_line(
        "markers", "register: mark test as register module test"
    )
    config.addinivalue_line(
        "markers", "ui: mark test as UI/navigation test"
    )
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test (critical)"
    )
    config.addinivalue_line(
        "markers", "functional: mark test as functional test"
    )
    config.addinivalue_line(
        "markers", "negative: mark test as negative test"
    )
    config.addinivalue_line(
        "markers", "edge_case: mark test as edge case test"
    )
    config.addinivalue_line(
        "markers", "stub: mark test as stub (not yet implemented)"
    )
