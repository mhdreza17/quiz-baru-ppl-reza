# Test Cases Documentation
## Quiz Pengupil - Login & Register Module Testing

**Repository:** https://github.com/mhdreza17/quiz-baru-ppl-reza

### Test Environment Setup
- **Framework:** Selenium WebDriver
- **Language:** Python
- **Test Runner:** Pytest
- **Browser:** Chrome (Headless mode untuk CI/CD)
- **Database:** MySQL (quiz_pengupil)
- **Base URL:** http://localhost/quiz

---

## 1. Test Cases - User Authentication & Authorization (S1.1)

### FT_001: Verifikasi login berhasil dengan kredensial peserta yang valid

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_001 |
| Requirement | S1.1 |
| Test Type | Functional Test |
| Priority | Critical |
| **Preconditions** | - User sudah terdaftar dengan username "testuser" dan password "Test@123" |
| **Steps** | 1. Navigate ke halaman login (http://localhost/quiz/login.php) |
| | 2. Masukkan username: "testuser" |
| | 3. Masukkan password: "Test@123" |
| | 4. Klik tombol "Sign In" |
| **Expected Result** | - Login berhasil |
| | - Session 'username' tersimpan dengan nilai "testuser" |
| | - Redirect ke halaman index.php |
| **Test Data** | username: testuser, password: Test@123 |
| **Status** | ✓ Automated |

---

### FT_002: Verifikasi sistem menolak login saat password kosong

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_002 |
| Requirement | S1.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman login |
| **Steps** | 1. Masukkan username: "testuser" |
| | 2. Biarkan password kosong |
| | 3. Klik tombol "Sign In" |
| **Expected Result** | - Login gagal |
| | - Tampil pesan error: "Data tidak boleh kosong !!" |
| | - Session tidak tersimpan |
| | - Tetap di halaman login.php |
| **Test Data** | username: testuser, password: (kosong) |
| **Status** | ✓ Automated |

---

### FT_003: Verifikasi sistem menolak login saat username kosong

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_003 |
| Requirement | S1.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman login |
| **Steps** | 1. Biarkan username kosong |
| | 2. Masukkan password: "Test@123" |
| | 3. Klik tombol "Sign In" |
| **Expected Result** | - Login gagal |
| | - Tampil pesan error: "Data tidak boleh kosong !!" |
| | - Session tidak tersimpan |
| | - Tetap di halaman login.php |
| **Test Data** | username: (kosong), password: Test@123 |
| **Status** | ✓ Automated |

---

### FT_004: Verifikasi login gagal dengan user tidak terdaftar

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_004 |
| Requirement | S1.1 |
| Test Type | Negative Test |
| Priority | High |
| **Preconditions** | - User "nonexistentuser" tidak terdaftar di database |
| **Steps** | 1. Masukkan username: "nonexistentuser" |
| | 2. Masukkan password: "Test@123" |
| | 3. Klik tombol "Sign In" |
| **Expected Result** | - Login gagal |
| | - Tampil pesan error: "Register User Gagal !!" |
| | - Session tidak tersimpan |
| **Test Data** | username: nonexistentuser, password: Test@123 |
| **Status** | ✓ Automated |

---

### FT_005: Verifikasi login gagal dengan password salah

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_005 |
| Requirement | S1.1 |
| Test Type | Negative Test |
| Priority | High |
| **Preconditions** | - User "testuser" terdaftar dengan password "Test@123" |
| **Steps** | 1. Masukkan username: "testuser" |
| | 2. Masukkan password: "WrongPassword" |
| | 3. Klik tombol "Sign In" |
| **Expected Result** | - Login gagal |
| | - Tidak ada pesan error spesifik (keamanan) |
| | - Session tidak tersimpan |
| | - Tetap di halaman login.php |
| **Test Data** | username: testuser, password: WrongPassword |
| **Status** | ✓ Automated |

---

### FT_006: Verifikasi login gagal saat kombinasi username dan password tidak cocok

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_006 |
| Requirement | S1.1 |
| Test Type | Negative Test |
| Priority | High |
| **Preconditions** | - Multiple users terdaftar dengan password berbeda |
| **Steps** | 1. Masukkan username: "testuser" |
| | 2. Masukkan password: "DifferentPassword123" |
| | 3. Klik tombol "Sign In" |
| **Expected Result** | - Login gagal |
| | - Session tidak tersimpan |
| **Test Data** | username: testuser, password: DifferentPassword123 |
| **Status** | ✓ Automated |

---

### FT_007: Verifikasi penerapan rate limiting pada login gagal berulang

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_007 |
| Requirement | S1.1 |
| Test Type | Security Test |
| Priority | Medium |
| **Preconditions** | - Sistem telah mengimplementasi rate limiting (STUB/FUTURE) |
| **Steps** | 1. Lakukan login gagal sebanyak 5 kali dengan password salah |
| | 2. Coba login yang ke-6 |
| **Expected Result** | - Akun terkunci sementara atau menampilkan pesan rate limit |
| | - User tidak bisa login selama periode tertentu |
| **Test Data** | username: testuser, multiple wrong passwords |
| **Status** | ⏳ Stub (Belum diimplementasi di code) |

---

### FT_008: Verifikasi session expired mengarahkan ke login

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_008 |
| Requirement | S1.1 |
| Test Type | Session Test |
| Priority | Medium |
| **Preconditions** | - User sudah login dan session tersimpan |
| | - Session timeout sudah diset di code |
| **Steps** | 1. Login berhasil dan redirect ke index.php |
| | 2. Tunggu session expire (simulasi dengan destroy session) |
| | 3. Akses halaman yang memerlukan session |
| **Expected Result** | - Session expired detected |
| | - Redirect ke halaman login |
| | - Message: "Session telah berakhir, silahkan login kembali" |
| **Test Data** | Username yang sudah login |
| **Status** | ⏳ Stub (Perlu session timeout handler) |

---

## 2. Test Cases - User Registration (S2.1)

### FT_009: Verifikasi registrasi berhasil dengan data valid

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_009 |
| Requirement | S2.1 |
| Test Type | Functional Test |
| Priority | Critical |
| **Preconditions** | - Database kosong dari username "newuser" |
| **Steps** | 1. Navigate ke halaman register (http://localhost/quiz/register.php) |
| | 2. Masukkan Nama: "John Doe" |
| | 3. Masukkan Email: "john@example.com" |
| | 4. Masukkan Username: "newuser" |
| | 5. Masukkan Password: "NewPass@123" |
| | 6. Masukkan Re-Password: "NewPass@123" |
| | 7. Klik tombol "Register" |
| **Expected Result** | - Registrasi berhasil |
| | - Session 'username' tersimpan dengan nilai "newuser" |
| | - Redirect ke halaman index.php |
| | - Data tersimpan di database |
| **Test Data** | name: John Doe, email: john@example.com, username: newuser, password: NewPass@123 |
| **Status** | ✓ Automated |

---

### FT_010: Verifikasi registrasi gagal saat email kosong

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_010 |
| Requirement | S2.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman register |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Biarkan Email kosong |
| | 3. Masukkan Username: "newuser" |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "NewPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi gagal |
| | - Tampil pesan error: "Data tidak boleh kosong !!" |
| | - Data tidak tersimpan di database |
| **Test Data** | name: John Doe, email: (kosong), username: newuser, password: NewPass@123 |
| **Status** | ✓ Automated |

---

### FT_011: Verifikasi registrasi gagal saat username kosong

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_011 |
| Requirement | S2.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman register |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "john@example.com" |
| | 3. Biarkan Username kosong |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "NewPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi gagal |
| | - Tampil pesan error: "Data tidak boleh kosong !!" |
| | - Data tidak tersimpan di database |
| **Test Data** | name: John Doe, email: john@example.com, username: (kosong), password: NewPass@123 |
| **Status** | ✓ Automated |

---

### FT_012: Verifikasi registrasi gagal saat username sudah terdaftar

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_012 |
| Requirement | S2.1 |
| Test Type | Negative Test |
| Priority | High |
| **Preconditions** | - User dengan username "existinguser" sudah terdaftar |
| **Steps** | 1. Masukkan Nama: "Jane Doe" |
| | 2. Masukkan Email: "jane@example.com" |
| | 3. Masukkan Username: "existinguser" |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "NewPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi gagal |
| | - Tampil pesan error: "Username sudah terdaftar !!" |
| | - Data tidak tersimpan di database |
| **Test Data** | name: Jane Doe, email: jane@example.com, username: existinguser, password: NewPass@123 |
| **Status** | ✓ Automated |

---

### FT_013: Verifikasi registrasi gagal saat password tidak sama

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_013 |
| Requirement | S2.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman register |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "john@example.com" |
| | 3. Masukkan Username: "newuser" |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "DifferentPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi gagal |
| | - Tampil pesan error: "Password tidak sama !!" |
| | - Data tidak tersimpan di database |
| **Test Data** | password: NewPass@123, repassword: DifferentPass@123 |
| **Status** | ✓ Automated |

---

### FT_014: Verifikasi registrasi gagal saat password kosong

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_014 |
| Requirement | S2.1 |
| Test Type | Validation Test |
| Priority | High |
| **Preconditions** | - Browser sudah membuka halaman register |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "john@example.com" |
| | 3. Masukkan Username: "newuser" |
| | 4. Biarkan Password kosong |
| | 5. Biarkan Re-Password kosong |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi gagal |
| | - Tampil pesan error: "Data tidak boleh kosong !!" |
| | - Data tidak tersimpan di database |
| **Test Data** | password: (kosong), repassword: (kosong) |
| **Status** | ✓ Automated |

---

### FT_015: Verifikasi registrasi gagal dengan format email tidak valid

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_015 |
| Requirement | S2.1 |
| Test Type | Validation Test |
| Priority | Medium |
| **Preconditions** | - Browser sudah membuka halaman register |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "invalid-email-format" (tanpa @) |
| | 3. Masukkan Username: "newuser" |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "NewPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Browser validation atau Server validation menolak format |
| | - Tampil pesan error format email tidak valid |
| | - Data tidak tersimpan |
| **Test Data** | email: invalid-email-format |
| **Status** | ⏳ Stub (Perlu validasi email di code) |

---

### FT_016: Verifikasi registrasi dengan password panjang (edge case)

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_016 |
| Requirement | S2.1 |
| Test Type | Edge Case Test |
| Priority | Low |
| **Preconditions** | - Database siap untuk data baru |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "john@example.com" |
| | 3. Masukkan Username: "longpasstest" |
| | 4. Masukkan Password: "MyVeryLongPassword123!@#$%^&*()_+{}[]" (40+ char) |
| | 5. Masukkan Re-Password: sama dengan step 4 |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi berhasil |
| | - Password panjang di-hash dengan benar |
| | - Login dengan password panjang berhasil |
| **Test Data** | password: MyVeryLongPassword123!@#$%^&*()_+{}[] |
| **Status** | ✓ Automated |

---

### FT_017: Verifikasi registrasi dengan karakter spesial pada username

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_017 |
| Requirement | S2.1 |
| Test Type | Edge Case Test |
| Priority | Low |
| **Preconditions** | - Database siap untuk data baru |
| **Steps** | 1. Masukkan Nama: "John Doe" |
| | 2. Masukkan Email: "john@example.com" |
| | 3. Masukkan Username: "user@name#123" (dengan spesial char) |
| | 4. Masukkan Password: "NewPass@123" |
| | 5. Masukkan Re-Password: "NewPass@123" |
| | 6. Klik tombol "Register" |
| **Expected Result** | - Registrasi berhasil atau ditolak (tergantung requirement) |
| | - Jika berhasil, user dapat login dengan username tersebut |
| | - Jika ditolak, tampil pesan error |
| **Test Data** | username: user@name#123 |
| **Status** | ✓ Automated |

---

## 3. Test Cases - Navigation & UI Flow (UI.1)

### FT_018: Verifikasi redirect register ke login

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_018 |
| Requirement | UI.1 |
| Test Type | Navigation Test |
| Priority | High |
| **Preconditions** | - User belum login |
| **Steps** | 1. Navigate ke halaman register.php |
| | 2. Scroll down untuk melihat link login |
| | 3. Klik link "Login" di footer |
| **Expected Result** | - Navigate ke halaman login.php |
| | - URL berubah ke login.php |
| | - Form login ditampilkan |
| **Test Data** | URL: http://localhost/quiz/register.php → login.php |
| **Status** | ✓ Automated |

---

### FT_019: Verifikasi link Register pada halaman Login

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_019 |
| Requirement | UI.1 |
| Test Type | Navigation Test |
| Priority | High |
| **Preconditions** | - User membuka halaman login |
| **Steps** | 1. Navigate ke halaman login.php |
| | 2. Cari text "Belum punya account?" |
| | 3. Klik link "Register" |
| **Expected Result** | - Navigate ke halaman register.php |
| | - URL berubah ke register.php |
| | - Form register ditampilkan dengan input: Nama, Email, Username, Password, Re-Password |
| **Test Data** | URL: http://localhost/quiz/login.php → register.php |
| **Status** | ✓ Automated |

---

### FT_020: Verifikasi link Login pada halaman Register

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_020 |
| Requirement | UI.1 |
| Test Type | Navigation Test |
| Priority | High |
| **Preconditions** | - User membuka halaman register |
| **Steps** | 1. Navigate ke halaman register.php |
| | 2. Cari text "Sudah punya account?" |
| | 3. Klik link "Login" |
| **Expected Result** | - Navigate ke halaman login.php |
| | - URL berubah ke login.php |
| | - Form login ditampilkan dengan input: Username, Password |
| **Test Data** | URL: http://localhost/quiz/register.php → login.php |
| **Status** | ✓ Automated |

---

### FT_021: Verifikasi proses Logout dan proteksi halaman

| Attribute | Value |
|-----------|-------|
| Test Case ID | FT_021 |
| Requirement | UI.1 |
| Test Type | Security Test |
| Priority | High |
| **Preconditions** | - User sudah login dan redirect ke index.php |
| | - halaman index.php memiliki tombol logout |
| **Steps** | 1. Login berhasil ke sistem |
| | 2. Klik tombol Logout |
| | 3. Session di-destroy |
| | 4. Redirect ke halaman login |
| | 5. Coba akses halaman index.php langsung |
| **Expected Result** | - Session dihapus |
| | - Logout berhasil, redirect ke login.php |
| | - Direct access ke index.php redirect ke login.php |
| | - Halaman proteksi bekerja dengan baik |
| **Test Data** | Session: destroy |
| **Status** | ⏳ Stub (index.php belum ada) |

---

## Test Execution Summary

| Category | Total | Automated | Stub |
|----------|-------|-----------|------|
| Login (S1.1) | 8 | 6 | 2 |
| Register (S2.1) | 9 | 7 | 2 |
| Navigation (UI.1) | 4 | 3 | 1 |
| **TOTAL** | **21** | **16** | **5** |

---

## Notes

1. **Stub Test Cases:** FT_007, FT_008, FT_015, FT_021 memerlukan fitur tambahan yang belum diimplementasikan
2. **Database Name Field:** Sengaja tidak diisi per requirement
3. **Index.php:** File belum ada, perlu dibuat untuk prototype lengkap
4. **Password Hashing:** Menggunakan `password_hash()` dengan algorithm default (bcrypt)
5. **Security:** Username di-escape dengan `mysqli_real_escape_string()` dan prepared statements belum digunakan

