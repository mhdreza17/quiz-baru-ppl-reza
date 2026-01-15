# Quick Start Guide - Quiz Pengupil Testing

## 🎯 Repository

📌 **GitHub Repository:** https://github.com/mhdreza17/quiz-baru-ppl-reza

---

## ⚡ 5-Minute Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
mysql -u root -p quiz_pengupil < db/quiz_pengupil.sql
```

### 3. Start Server
```bash
php -S localhost:80
# Di folder yang sama dengan login.php, register.php
```

### 4. Run Tests
```bash
# All tests
pytest tests/ -v

# Login only
pytest tests/test_login.py -v

# Register only
pytest tests/test_register.py -v

# Navigation only
pytest tests/test_ui_navigation.py -v
```

---

## 📋 Test Cases Summary

### Login Module (8 tests)
```
✅ FT_001: Successful login with valid credentials
✅ FT_002: Reject login when password is empty
✅ FT_003: Reject login when username is empty
✅ FT_004: Reject login with unregistered user
✅ FT_005: Reject login with wrong password
✅ FT_006: Reject login with mismatched credentials
⏳ FT_007: Rate limiting on repeated failures (STUB)
⏳ FT_008: Session expiration redirects to login (STUB)
```

### Register Module (9 tests)
```
✅ FT_009: Successful registration with valid data
✅ FT_010: Reject when email is empty
✅ FT_011: Reject when username is empty
✅ FT_012: Reject when username already registered
✅ FT_013: Reject when password mismatch
✅ FT_014: Reject when password is empty
⏳ FT_015: Reject with invalid email format (STUB)
✅ FT_016: Success with long password (edge case)
✅ FT_017: Success with special characters in username (edge case)
```

### Navigation & UI (4 tests)
```
✅ FT_018: Register page link to login
✅ FT_019: Login page link to register
✅ FT_020: Register page link to login (verify)
⏳ FT_021: Logout and page protection (STUB)
```

---

## 🚀 Common Commands

```bash
# Run with markers
pytest tests/ -m smoke           # Critical tests
pytest tests/ -m negative        # Error cases
pytest tests/ -m edge_case       # Edge cases
pytest tests/ -m "not stub"      # Exclude stubs

# Generate reports
pytest tests/ --html=report.html --self-contained-html
pytest tests/ --cov=. --cov-report=html

# Run with debugging
pytest tests/test_login.py -v -s --tb=long

# Run specific test
pytest tests/test_login.py::TestLoginAuthentication::test_ft_001_login_success_with_valid_credentials -v

# Parallel execution
pytest tests/ -v -n auto
```

---

## 📁 Directory Structure

```
.
├── tests/
│   ├── test_login.py          # Login tests (FT_001-FT_008)
│   ├── test_register.py       # Register tests (FT_009-FT_017)
│   ├── test_ui_navigation.py  # UI tests (FT_018-FT_021)
│   ├── pages/
│   │   ├── login_page.py      # Login Page Object
│   │   └── register_page.py   # Register Page Object
│   ├── fixtures/
│   │   └── conftest.py        # Database & Selenium fixtures
│   └── conftest.py            # Main pytest configuration
├── .github/workflows/
│   └── test.yml               # GitHub Actions CI/CD
├── TEST_CASES.md              # Detailed test cases
├── TESTING.md                 # Full testing documentation
├── pytest.ini                 # Pytest config
├── requirements.txt           # Python dependencies
└── .env.example               # Environment template
```

---

## 🔧 Troubleshooting

### MySQL Connection Error
```bash
# Check MySQL is running
mysql -u root -p -e "SELECT 1"

# Verify database exists
mysql -u root -p -e "SHOW DATABASES LIKE 'quiz_pengupil'"
```

### PHP Server Not Responding
```bash
# Check server is running
curl http://localhost/quiz/login.php

# Kill process on port 80
# Windows: netstat -ano | findstr :80
# Linux: lsof -i :80
```

### Tests Timeout
```bash
# Increase timeout (in seconds)
pytest tests/ --timeout=60
```

### WebDriver Issues
```bash
# Update Chrome
webdriver-manager chrome --download-version

# Check Chrome version
google-chrome --version
```

---

## 📊 Test Status

| Category | Count | Automated | Stub |
|----------|-------|-----------|------|
| Login | 8 | 6 | 2 |
| Register | 9 | 7 | 2 |
| Navigation | 4 | 3 | 1 |
| **TOTAL** | **21** | **16** | **5** |

**Automated Rate: 76.2%**

---

## 🎓 Key Features

### Page Object Model (POM)
- Separate page classes for login and register
- Reusable locators and methods
- Easy maintenance and updates

### Fixtures & Setup
- Automatic database cleanup before/after tests
- Test user creation and deletion
- Selenium WebDriver configuration
- MySQL connection management

### CI/CD Pipeline
- Automated testing on push/PR
- Code quality checks
- Security scanning
- Test reports generation

### Test Organization
- Markers for categorization
- Clear test naming
- Comprehensive assertions
- Error message validation

---

## 📚 Documentation Files

1. **TEST_CASES.md** - Detailed test cases with requirements and steps
2. **TESTING.md** - Complete testing guide with examples
3. **README.md** - This quick reference
4. **pytest.ini** - Pytest configuration
5. **requirements.txt** - Python dependencies

---

## 🔗 Useful Links

- **GitHub:** https://github.com/mhdreza17/quiz-baru-ppl-reza
- **Selenium Docs:** https://selenium-python.readthedocs.io/
- **Pytest Docs:** https://docs.pytest.org/
- **GitHub Actions:** https://docs.github.com/en/actions

---

## ⚙️ GitHub Actions Setup

### Auto-run on Push
Workflow runs automatically when:
- Push ke main/develop branch
- Pull request dibuat
- Schedule: Daily at 2 AM UTC

### View Results
1. Go to: https://github.com/mhdreza17/quiz-baru-ppl-reza/actions
2. Click on workflow run
3. View logs dan artifacts

### Download Reports
- JUnit XML: junit-*.xml
- HTML Report: report.html
- Dependency Check: dependency-check-report.json

---

## 💡 Tips

1. **Use Page Object Model** for maintainability
2. **Keep tests independent** - no cross-test dependencies
3. **Use descriptive names** - test purpose should be clear
4. **Validate error messages** - ensure proper error handling
5. **Test edge cases** - long passwords, special characters
6. **Run smoke tests first** - critical functionality
7. **Check CI/CD logs** - for debugging failures

---

## 🎯 Next Steps

1. Review TEST_CASES.md for detailed test specifications
2. Run tests locally: `pytest tests/ -v`
3. Check GitHub Actions workflow at: https://github.com/mhdreza17/quiz-baru-ppl-reza/actions
4. Create index.php untuk mengaktifkan stub tests
5. Implement rate limiting untuk FT_007
6. Add email validation untuk FT_015

---

**Last Updated:** 2026-01-15  
**Status:** ✅ Ready for Testing
