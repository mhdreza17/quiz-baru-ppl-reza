# Push ke GitHub & Setup Guide

## 📌 Repository Information
**Repository:** https://github.com/mhdreza17/quiz-baru-ppl-reza

---

## 🔄 Cara Push Testing Suite ke GitHub

### 1. Initialize Git Repository (Jika belum ada)
```bash
cd c:\xampp\htdocs\quizppl
git init
git config user.name "Nama Anda"
git config user.email "email@example.com"
```

### 2. Add Remote Repository
```bash
git remote add origin https://github.com/mhdreza17/quiz-baru-ppl-reza.git
git branch -M main
```

### 3. Add Files dan Commit
```bash
# Add semua file
git add .

# Commit dengan pesan deskriptif
git commit -m "Add comprehensive test suite with Selenium

- Created 21 test cases (16 automated, 5 stub)
- Implemented Page Object Model pattern
- Setup GitHub Actions CI/CD pipeline
- Added pytest fixtures and helpers
- Complete testing documentation

Test Coverage:
- Login Module (S1.1): 8 tests
- Register Module (S2.1): 9 tests
- Navigation UI (UI.1): 4 tests"
```

### 4. Push ke GitHub
```bash
git push -u origin main
```

---

## ✅ File Structure untuk GitHub

```
quiz-baru-ppl-reza/
├── .github/
│   └── workflows/
│       └── test.yml                    # ← GitHub Actions Workflow
├── .gitignore                          # ← Ignore rules
├── tests/                              # ← Test files
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py                   # FT_001-FT_008
│   ├── test_register.py                # FT_009-FT_017
│   ├── test_ui_navigation.py           # FT_018-FT_021
│   ├── test_helpers.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   └── register_page.py
│   └── fixtures/
│       ├── __init__.py
│       └── conftest.py
├── db/
│   └── quiz_pengupil.sql
├── login.php
├── register.php
├── koneksi.php
├── style.css
├── pytest.ini                          # ← Pytest config
├── requirements.txt                    # ← Dependencies
├── .env.example                        # ← Environment template
├── TEST_CASES.md                       # ← Detailed test cases
├── TESTING.md                          # ← Complete guide
├── README_TESTING.md                   # ← Quick start
├── IMPLEMENTATION_SUMMARY.md           # ← Summary
├── PUSH_GUIDE.md                       # ← This file
└── README.md                           # ← Original README
```

---

## 🔍 Verifikasi di GitHub

### 1. Cek Repository
- Buka: https://github.com/mhdreza17/quiz-baru-ppl-reza
- Verifikasi semua file sudah tertera

### 2. Setup GitHub Actions
```
Repository → Settings → Actions → General
- Ensure "Allow all actions and reusable workflows" dipilih
```

### 3. Trigger Workflow
```
Push code atau Edit file → workflow akan trigger otomatis
```

### 4. Monitor Workflow
```
Repository → Actions → quiz-pengupil-automated-tests
- Lihat status test execution
- Download reports dan artifacts
```

---

## 🚀 Pertama Kali Run di Local

### 1. Clone Repository
```bash
git clone https://github.com/mhdreza17/quiz-baru-ppl-reza.git
cd quiz-baru-ppl-reza
```

### 2. Setup Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env dengan config lokal
# DATABASE_HOST=localhost
# DATABASE_USER=root
# DATABASE_PASSWORD=
# DATABASE_NAME=quiz_pengupil
```

### 3. Install Dependencies
```bash
# Python packages
pip install -r requirements.txt

# Atau untuk development
pip install -r requirements.txt --upgrade
```

### 4. Setup Database
```bash
# MySQL
mysql -u root -p quiz_pengupil < db/quiz_pengupil.sql

# Verify
mysql -u root -p -e "SHOW TABLES FROM quiz_pengupil;"
```

### 5. Start Server
```bash
# Terminal 1: Start PHP server
php -S localhost:80

# Terminal 2: Run tests
pytest tests/ -v
```

---

## 📊 GitHub Actions Workflow Setup

### File: `.github/workflows/test.yml`

**Auto-runs on:**
- Push ke main/develop branch
- Create Pull Request
- Setiap hari jam 2 AM UTC

**Jobs:**
```
test
  └─ Setup MySQL
  └─ Setup PHP
  └─ Install dependencies
  └─ Run tests
  └─ Upload reports

code-quality
  └─ PHP Lint
  └─ Security checks

security-scan
  └─ OWASP Dependency Check

integration-test
  └─ Smoke tests
  └─ Coverage report

status-check
  └─ Final summary
```

---

## 📝 Update Files di GitHub

### Edit File via GitHub Web
1. Open file di repository
2. Click pencil icon (Edit)
3. Make changes
4. Commit dengan message

### Edit via Git
```bash
# Edit file locally
nano tests/test_login.py

# Commit dan push
git add tests/test_login.py
git commit -m "Update login tests"
git push origin main
```

---

## 🐛 Troubleshooting GitHub Actions

### 1. Workflow Tidak Trigger
```
Settings → Actions → Ensure permissions correct
```

### 2. Test Failures
```
Actions → Click workflow → View logs
```

### 3. Database Error
```
Check MySQL service running in GitHub Actions
Verify credentials di .github/workflows/test.yml
```

### 4. Download Artifacts
```
Actions → workflow run → Artifacts
Download: test-reports, dependency-check-report
```

---

## 📈 Monitoring & Reporting

### View Test Results
```
Repository → Actions → Select workflow run
- View detailed logs
- Check artifacts
- Download reports (HTML, XML, JSON)
```

### Email Notifications
```
GitHub → Settings → Notifications
Enable workflow notifications
```

### Create Badge for README
```markdown
![Tests](https://github.com/mhdreza17/quiz-baru-ppl-reza/workflows/Quiz%20Pengupil%20-%20Automated%20Tests/badge.svg)
```

---

## 🎯 Next Steps After Push

### 1. Verify Workflow
- [ ] Workflow appears in Actions tab
- [ ] First run completes successfully
- [ ] Reports are generated

### 2. Review Results
- [ ] Check test execution summary
- [ ] Download and review reports
- [ ] Verify all 16 automated tests pass

### 3. Setup Branch Protection
```
Settings → Branches → Add rule
- Require status checks before merge
- Select: test, code-quality, security-scan
```

### 4. Create Issues for Stubs
```
Create GitHub issues untuk stub tests:
- FT_007: Implement rate limiting
- FT_008: Create index.php with session
- FT_015: Add email validation
- FT_021: Complete logout feature
```

---

## 📚 Documentation Links

### In Repository
- TEST_CASES.md - Detailed test specifications
- TESTING.md - Complete testing guide
- README_TESTING.md - Quick start guide
- IMPLEMENTATION_SUMMARY.md - Overview

### External
- [Selenium Docs](https://selenium-python.readthedocs.io/)
- [Pytest Docs](https://docs.pytest.org/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## 🔐 Security Notes

### GitHub Secrets (Optional)
Jika ingin secure sensitive data:
```
Settings → Secrets and variables → Actions → New repository secret
```

### Protected Files
- .env (add ke .gitignore) ✓
- Database password (use secrets)
- API keys (use secrets)

---

## 📋 Checklist Final

- [ ] Git repository initialized
- [ ] All test files created
- [ ] .gitignore configured
- [ ] requirements.txt updated
- [ ] GitHub Actions workflow created
- [ ] Documentation complete
- [ ] Repository pushed to GitHub
- [ ] Workflow runs successfully
- [ ] All 16 automated tests pass
- [ ] Reports generated correctly
- [ ] README dengan testing info updated

---

## 🎓 Learning Path

1. **Understand Structure**
   - Review IMPLEMENTATION_SUMMARY.md
   - Check file structure di GitHub

2. **Learn Testing**
   - Read TEST_CASES.md untuk test specifications
   - Review test_login.py, test_register.py untuk implementation

3. **Understand CI/CD**
   - Review .github/workflows/test.yml
   - Monitor workflow runs di Actions tab

4. **Extend Tests**
   - Add new test cases di tests/ folder
   - Update pytest.ini dengan markers baru
   - Push changes ke GitHub

---

## 📞 Support

### Debugging Locally
```bash
pytest tests/test_login.py -v -s --tb=long
```

### Check GitHub Logs
Repository → Actions → Click workflow → View detailed logs

### Common Issues
1. MySQL connection → Check database running
2. WebDriver issues → Update chromedriver
3. Import errors → Check PYTHONPATH

---

## 🎉 Summary

**Repository:** https://github.com/mhdreza17/quiz-baru-ppl-reza

**Test Suite Deployed:**
✅ 21 Test Cases Created
✅ 16 Tests Automated (76.2%)
✅ 5 Stub Tests (23.8%)
✅ GitHub Actions CI/CD Setup
✅ Complete Documentation

**Ready for:**
✅ Local Testing
✅ GitHub Automation
✅ Continuous Integration
✅ Team Collaboration

---

**Status:** ✅ READY TO PUSH
**Last Updated:** 2026-01-15
