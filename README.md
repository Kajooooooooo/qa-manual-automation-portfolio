# QA Manual & Automation Portfolio

Portfolio ini berisi dokumentasi dan hasil pekerjaan Quality Assurance (QA), meliputi Manual Testing, Test Planning, Test Case, Bug Reporting, User Acceptance Testing (UAT), serta Automation Testing.

Portfolio dibuat berdasarkan beberapa project dan business flow yang pernah dikerjakan dalam proses testing aplikasi.

---

# 📁 Project Portfolio

## 1. E-Tender

E-Tender merupakan modul E-Procurement yang digunakan untuk mengelola proses tender dari pembuatan paket pekerjaan sampai dengan penetapan pemenang.

### Business Flow

1. Login
2. OTP Verification
3. Role Selection
4. Create Work Package
5. Publish Work Package
6. Vendor Registration
7. Vendor Registration Evaluation
8. Clarification
9. Bid Document Submission
10. Bid Document Opening
11. Bid Document Evaluation
12. Negotiation
13. Winner Determination

### Testing Documentation

- Test Plan
- Test Case
- Bug Report
- User Acceptance Test (UAT)

### Main Testing Focus

- Authentication & Authorization
- Work Package Management
- Vendor Registration
- Bid Document Management
- Bid Evaluation
- Negotiation
- Winner Determination
- System Integration
- Intermittent Issue Testing

### Known Issues

Beberapa issue yang ditemukan antara lain:

- OTP terkadang tidak diterima melalui email
- Dokumen penawaran terkadang gagal di-upload
- Dokumen penawaran terkadang tidak dapat dibuka
- Data dokumen terkadang tidak masuk ke tahap evaluasi
- Status evaluasi terkadang tidak ter-update

---

# 2. CMS - Contract Management System

CMS digunakan untuk mengelola proses kontrak setelah proses tender selesai dan pemenang telah ditetapkan.

### Business Flow

1. Paket pekerjaan dikirim dari E-Tender ke CMS
2. Setting Reviewer
   - Atasan
   - Pengguna / Pihak 1
   - Vendor / Pihak 2
3. Mengatur Tata Cara Pembayaran
4. Menetapkan Rekening Pembayaran Vendor
5. Generate Dokumen Kontrak
6. Mengirim Dokumen Kontrak kepada Reviewer
7. Reviewer melakukan Approval
8. Setelah seluruh Reviewer melakukan Approval, kontrak masuk ke tahap E-Sign
9. Pihak 1 dan Pihak 2 melakukan E-Sign pada kontrak final

### Testing Documentation

- Test Plan
- Test Case
- Bug Report
- User Acceptance Test (UAT)

### Main Testing Focus

- Contract Management
- Reviewer Management
- Payment Method
- Vendor Payment Account
- Contract Document Generation
- Contract Document Distribution
- Reviewer Approval
- Status Synchronization
- Integration with E-Sign

### Known Issues

Beberapa issue yang ditemukan:

- Data pekerja terkadang tidak muncul ketika melakukan Setting Reviewer
- Dokumen kontrak terkadang tidak masuk ke akun Reviewer
- Status Approval Reviewer terkadang tidak ter-update

---

# 3. Vendor Payment

Vendor Payment digunakan untuk mengelola proses pembayaran pekerjaan setelah kontrak selesai ditandatangani.

### Business Flow

1. Kontrak final selesai di-E-Sign
2. User CMS mengajukan PO ke SAP
3. PO di-approve melalui SAP
4. Data PO masuk ke Vendor Payment
5. Pengguna melakukan Drafting Vendor Payment
6. Mengatur Personil
   - Personil Pengguna
   - Personil Vendor
7. Membuat Berita Acara Mulai Pekerjaan
8. Membuat Berita Acara Serah Terima
9. Membuat Berita Acara Progress jika terdapat progress pekerjaan
10. Pengguna melakukan penerimaan GR/SES
11. Vendor melakukan submit dokumen tagihan
12. Pengguna melakukan approval dokumen tagihan
13. Pengguna membuat Nota Dinas Pembayaran
14. Nota Dinas dikirim untuk approval Pengguna dan Vendor
15. Setelah approval selesai, pembayaran diproses melalui SAP
16. Setelah pembayaran berhasil, Pengguna membuat Berita Acara Pembayaran

### Testing Documentation

- Test Plan
- Test Case
- Bug Report
- User Acceptance Test (UAT)

### Main Testing Focus

- PO Integration
- SAP Integration
- Vendor Payment Drafting
- Personil Management
- Berita Acara Management
- Progress Management
- GR/SES Acceptance
- Invoice Document Submission
- Invoice Approval
- Payment Approval
- Payment Processing
- Payment Status
- SAP Integration

### Known Issues

Beberapa issue yang ditemukan:

- Proses approval terkadang gagal
- Proses penerimaan GR/SES terkadang gagal karena masalah integrasi dengan SAP
- Proses submit pembayaran terkadang gagal
- Beberapa issue bersifat intermittent dan dapat muncul kembali setelah sebelumnya dinyatakan solved

---

# 4. P-Wellness

P-Wellness merupakan aplikasi yang digunakan untuk mengelola proses Medical Check Up (MCU), mulai dari pengajuan pra-MCU sampai dengan hasil MCU tersedia pada dashboard user.

### Business Flow

1. Login
   - Admin
   - User
   - Rumah Sakit
2. User membuat data Pra-MCU
3. User mengisi form Pra-MCU
4. User melakukan Submit Pra-MCU
5. Rumah Sakit memeriksa data Pra-MCU
6. Rumah Sakit membuat jadwal MCU
7. User mengikuti proses MCU
8. Rumah Sakit menerima hasil MCU
9. Rumah Sakit mengunggah dokumen hasil MCU
10. Data hasil MCU masuk ke dashboard User

### Testing Documentation

- Test Plan
- Test Case
- Bug Report
- User Acceptance Test (UAT)

### Main Testing Focus

- Authentication
- Role Management
- Pra-MCU
- Pra-MCU Submission
- Hospital Verification
- MCU Scheduling
- MCU Result
- Document Upload
- Dashboard
- Data Synchronization

### Known Issues

Issue utama yang ditemukan:

- Data yang ditampilkan pada dashboard terkadang tidak sesuai dengan data yang tersedia pada sistem/source data.

Issue tersebut dapat menyebabkan ketidaksesuaian informasi yang diterima oleh user.

---

# 5. E-Sign

E-Sign merupakan project yang digunakan untuk melakukan tanda tangan elektronik pada dokumen kontrak dan terintegrasi dengan CMS serta Vinotek sebagai penyedia E-Sign dan e-Meterai.

### Business Flow

#### Vendor / Pihak 2

1. Pihak 1 menyelesaikan approval kontrak
2. Email E-Sign dikirim kepada Pihak 2 / Vendor
3. Vendor membuka link E-Sign
4. Sistem melakukan pengecekan status registrasi email
5. Jika belum terdaftar, Vendor diarahkan ke Vinotek
6. Vendor menerima email registrasi
7. Vendor melakukan pembelian kuota registrasi
8. Vendor melakukan pembayaran
9. Pembayaran diverifikasi
10. Vendor mengisi form registrasi
11. Registrasi berhasil
12. Vendor membuka kembali email E-Sign
13. Vendor klik link E-Sign
14. Vendor masuk ke halaman E-Sign
15. Vendor melakukan Stamp
16. Vendor menggunakan e-Meterai
17. Vendor memasukkan OTP
18. OTP dikirim ke email Vendor
19. Vendor berhasil melakukan Stamp

#### Jika Vendor Sudah Terdaftar

Vendor yang sudah terdaftar tidak perlu melakukan registrasi ulang dan dapat langsung diarahkan ke halaman E-Sign.

#### Pengguna / Pihak 1

Setelah Vendor selesai melakukan Stamp:

1. Email E-Sign dikirim kepada Pengguna / Pihak 1
2. Pengguna membuka email E-Sign
3. Pengguna klik link E-Sign
4. Pengguna masuk ke halaman E-Sign
5. Pengguna melakukan Stamp
6. Pengguna menggunakan e-Meterai
7. Pengguna memasukkan OTP
8. OTP dikirim ke email Pengguna
9. Pengguna berhasil melakukan Stamp
10. Kontrak menjadi dokumen final yang telah ditandatangani kedua pihak

### Testing Documentation

- Test Plan
- Test Case
- Bug Report
- User Acceptance Test (UAT)

### Main Testing Focus

- E-Sign Email Notification
- Email Verification
- Vendor Registration
- Vinotek Integration
- Registration Quota
- Payment
- Payment Verification
- e-Meterai
- Stamp
- OTP Verification
- Vendor Signing
- Pengguna Signing
- Contract Finalization
- Signing Status
- CMS Integration

### Known Issues

Beberapa issue yang ditemukan:

- Email E-Sign terkadang tidak diterima oleh user
- Barcode E-Sign terkadang tidak muncul karena koordinat barcode tidak terbaca
- Status E-Sign terkadang tidak ter-update setelah proses Stamp selesai
- Terdapat intermittent issue pada integrasi dengan Vinotek

---

# 📊 Testing Documentation Summary

| Project | Test Plan | Test Case | Bug Report | UAT |
|---|---|---|---|---|
| E-Tender | ✅ | ✅ | ✅ | ✅ |
| CMS | ✅ | ✅ | ✅ | ✅ |
| Vendor Payment | ✅ | ✅ | ✅ | ✅ |
| P-Wellness | ✅ | ✅ | ✅ | ✅ |
| E-Sign | ✅ | ✅ | ✅ | ✅ |

---

# 🧪 QA Activities

Testing activities performed across the projects include:

- Requirement Analysis
- Test Planning
- Test Scenario Design
- Test Case Design
- Functional Testing
- Positive Testing
- Negative Testing
- Regression Testing
- Integration Testing
- System Testing
- User Acceptance Testing
- Defect Identification
- Defect Reporting
- Defect Verification
- Retesting
- Exploratory Testing
- End-to-End Testing
- Data Validation

---

# 🐞 Defect Management

Defects are documented with the following information:

- Bug ID
- Title
- Module
- Severity
- Priority
- Environment
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Impact
- Status
- Related Test Case
- Notes / Resolution

Defect status used in the portfolio includes:

- Open
- In Progress
- Fixed
- Retest
- Closed
- Intermittent / Recurring

---

# 📋 Test Documentation Structure

Each project contains the following QA documentation:

```text
Project/
│
├── Test-Plan/
│   └── Test-Plan.md
│
├── Test-Case/
│   └── Test-Cases.md
│
├── Bug-Report/
│   └── Bug-Reports.md
│
└── UAT/
    └── UAT.md