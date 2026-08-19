# Test Plan - E-Sign

## 1. Document Information

| Field | Details |
|---|---|
| Project | E-Sign |
| Application | E-Sign |
| Integration | CMS & Vinotek |
| Testing Type | Manual Testing |
| Test Environment | UAT |
| Primary Users | Pihak 1 / User and Pihak 2 / Vendor |
| Main Function | Electronic Signature and e-Meterai |
| Application Purpose | Digital signing of contract documents |
| Test Status | Planned |
| Document Status | Final |

---

# 2. Project Overview

E-Sign is a digital contract signing system used to perform
electronic signatures and electronic stamping on contract
documents.

The E-Sign system is used as part of the Contract Management
System (CMS) business process.

After the contract has received the required approval from Pihak 1,
the contract is sent to the E-Sign process for signing by the
required parties.

The E-Sign process is integrated with Vinotek as the provider of
electronic signature and electronic stamp services.

The process supports:

- Pihak 1
- Pihak 2 / Vendor

The system also validates whether the signer has already been
registered with Vinotek.

---

# 3. Business Objective

The objective of the E-Sign system is to provide a digital process
for signing contract documents without requiring physical
signatures.

The system must ensure that:

- The correct signer receives the E-Sign request.
- The signer can access the correct contract.
- Registered users can directly access the E-Sign page.
- Unregistered users are directed to the Vinotek registration
  process.
- Users can complete the required registration process.
- Users can purchase the required registration quota.
- Payment can be completed successfully.
- Payment can be verified.
- Users can apply e-Meterai.
- OTP verification is performed before signing.
- Contract signing is successfully completed.
- Signing status is correctly updated.
- The signing process works for both Pihak 1 and Pihak 2.
- Integration between CMS, E-Sign, and Vinotek works correctly.

---

# 4. Test Objective

Testing will be performed to verify the functionality, integration,
security-related access behavior, and end-to-end business flow of
the E-Sign system.

The main objectives are:

1. Verify the E-Sign request is generated correctly.
2. Verify the E-Sign email is sent to the correct recipient.
3. Verify the E-Sign link opens the correct process.
4. Verify the system checks the user's registration status.
5. Verify registered users are directly redirected to the E-Sign
   page.
6. Verify unregistered users are redirected to Vinotek registration.
7. Verify users can receive the registration email.
8. Verify users can purchase registration quota.
9. Verify users can complete payment.
10. Verify payment status can be verified.
11. Verify users can complete the registration form.
12. Verify successful registration.
13. Verify registered users can access the E-Sign page.
14. Verify users can apply e-Meterai.
15. Verify OTP is sent to the registered email.
16. Verify valid OTP can be submitted.
17. Verify invalid OTP is rejected.
18. Verify the stamping process is completed successfully.
19. Verify the signing process works for Pihak 1.
20. Verify the signing process works for Pihak 2 / Vendor.
21. Verify the signing status is updated correctly.
22. Verify the final signed contract is available.
23. Verify integration between CMS, E-Sign, and Vinotek.

---

# 5. Business Flow

## 5.1 Overall Business Flow

The overall E-Sign process starts after the required contract
approval has been completed in CMS.

```text
CMS
 ↓
Contract Approval
 ↓
E-Sign Request
 ↓
E-Sign Email
 ↓
Signer Opens Email
 ↓
Click E-Sign Link
 ↓
System Checks Registration Status
 ↓
 ┌─────────────────────────────┐
 │ Email Already Registered?   │
 └──────────────┬──────────────┘
                │
       ┌────────┴────────┐
       │                 │
      YES               NO
       │                 │
       ↓                 ↓
 E-Sign Page       Vinotek Registration
       │                 ↓
       │          Registration Email
       │                 ↓
       │          Purchase Quota
       │                 ↓
       │             Payment
       │                 ↓
       │        Payment Verification
       │                 ↓
       │        Complete Registration
       │                 ↓
       │        Registration Success
       │                 ↓
       │        Open E-Sign Email
       │                 ↓
       └──────────→ E-Sign Page
                         ↓
                      Click Stamp
                         ↓
                    Apply e-Meterai
                         ↓
                     Enter OTP
                         ↓
                  OTP Sent to Email
                         ↓
                    Submit OTP
                         ↓
                  Stamp Successful
                         ↓
                 Contract Signed
                         ↓
                Status Updated
```

---

# 6. Pihak 2 / Vendor Business Flow

After Pihak 1 approves the contract, the E-Sign request is sent to
Pihak 2 / Vendor.

```text
Pihak 1 Approves Contract
        ↓
E-Sign Request Created
        ↓
E-Sign Email Sent to Vendor
        ↓
Vendor Opens Email
        ↓
Vendor Clicks E-Sign Link
        ↓
System Checks Vendor Registration
        ↓
        ┌─────────────────────┐
        │ Registered?         │
        └──────────┬──────────┘
                   │
            ┌──────┴──────┐
            │             │
           YES           NO
            │             │
            ↓             ↓
       E-Sign Page     Vinotek
                         ↓
                  Registration Email
                         ↓
                  Purchase Quota
                         ↓
                      Payment
                         ↓
                 Payment Verification
                         ↓
                 Complete Registration
                         ↓
                 Registration Success
                         ↓
                 Open E-Sign Email
                         ↓
                    E-Sign Page
                         ↓
                     Click Stamp
                         ↓
                    Apply e-Meterai
                         ↓
                       OTP
                         ↓
                  OTP Sent to Email
                         ↓
                   Enter OTP
                         ↓
                 Stamp Successful
                         ↓
                Contract Signed
```

---

# 7. Pihak 1 Business Flow

Pihak 1 follows the same E-Sign process.

```text
Pihak 1 Receives E-Sign Request
        ↓
Pihak 1 Opens Email
        ↓
Click E-Sign Link
        ↓
System Checks Registration
        ↓
        ┌─────────────────────┐
        │ Registered?         │
        └──────────┬──────────┘
                   │
            ┌──────┴──────┐
            │             │
           YES           NO
            │             │
            ↓             ↓
       E-Sign Page     Vinotek
                         ↓
                  Registration Process
                         ↓
                    E-Sign Page
                         ↓
                     Click Stamp
                         ↓
                    Apply e-Meterai
                         ↓
                       OTP
                         ↓
                  OTP Sent to Email
                         ↓
                    Enter OTP
                         ↓
                 Stamp Successful
                         ↓
                 Contract Signed
```

---

# 8. Registration Logic

The system must determine the registration status of the signer
when the E-Sign link is opened.

## 8.1 Registered User

If the email is already registered in Vinotek:

```text
Click E-Sign Link
       ↓
Registration Check
       ↓
Email Registered
       ↓
Directly Open E-Sign Page
```

The user must not be required to:

- Register again.
- Purchase registration quota.
- Perform payment.
- Complete the registration form again.

---

## 8.2 Unregistered User

If the email is not registered:

```text
Click E-Sign Link
       ↓
Registration Check
       ↓
Email Not Registered
       ↓
Redirect to Vinotek
       ↓
Registration Email
       ↓
Purchase Registration Quota
       ↓
Payment
       ↓
Payment Verification
       ↓
Registration Form
       ↓
Registration Successful
       ↓
Open E-Sign Email
       ↓
Click E-Sign Link
       ↓
E-Sign Page
```

---

# 9. E-Sign Process

After the signer successfully accesses the E-Sign page:

1. User opens the contract.
2. User reviews the contract information.
3. User selects the Stamp function.
4. User applies the required e-Meterai.
5. System requests OTP verification.
6. OTP is sent to the registered email.
7. User enters the OTP.
8. System validates the OTP.
9. System completes the stamping process.
10. Signing status is updated.
11. Signed contract becomes available.

---

# 10. Scope

## 10.1 In Scope

### Contract Integration

- Contract approval trigger.
- E-Sign request creation.
- Contract document transmission.
- Signer information.
- Contract information.

### Email Notification

- E-Sign email generation.
- Email recipient validation.
- Email delivery.
- E-Sign link.
- Registration email.
- OTP email.

### Registration

- Registration status checking.
- Registered user flow.
- Unregistered user flow.
- Vinotek registration.
- Registration email.
- Registration quota.
- Payment.
- Payment verification.
- Registration form.
- Registration completion.

### E-Sign

- E-Sign page.
- Contract display.
- Stamp function.
- e-Meterai.
- OTP generation.
- OTP delivery.
- OTP validation.
- Successful stamping.
- Signing status.

### User Types

- Pihak 1.
- Pihak 2 / Vendor.

### Integration

- CMS → E-Sign.
- E-Sign → Vinotek.
- Vinotek → E-Sign.
- E-Sign → CMS.

---

# 11. Out of Scope

The following processes are outside the primary E-Sign testing
scope:

- E-Tender package creation.
- Vendor registration in E-Tender.
- Tender evaluation.
- Negotiation.
- Winner determination.
- Contract creation in CMS.
- Contract approval workflow in CMS.
- Vendor Payment.
- SAP payment processing.

These processes are documented and tested under their respective
projects.

---

# 12. User Roles

| Role | Responsibility |
|---|---|
| Pihak 1 | Contract approval and E-Sign |
| Pihak 2 / Vendor | E-Sign and e-Meterai |
| CMS | Generate contract and initiate E-Sign |
| E-Sign | Manage electronic signing process |
| Vinotek | Registration, e-Meterai, electronic signing, quota, and payment |

---

# 13. Test Scenario Coverage

## 13.1 Contract and E-Sign Request

- Verify contract approval triggers E-Sign.
- Verify correct signer is selected.
- Verify correct email address is used.
- Verify E-Sign email is generated.
- Verify E-Sign email is delivered.
- Verify E-Sign link is available.
- Verify E-Sign link opens the correct contract.

---

## 13.2 Registration Validation

- Verify system checks signer registration status.
- Verify registered email is identified correctly.
- Verify unregistered email is identified correctly.

---

## 13.3 Registered User

- Verify registered user is directly redirected to E-Sign.
- Verify registered user does not need to register again.
- Verify registered user does not need to purchase quota.
- Verify registered user does not need to make payment.
- Verify registered user can access the contract.
- Verify registered user can proceed with stamping.

---

## 13.4 Unregistered User

- Verify unregistered user is redirected to Vinotek.
- Verify registration email is sent.
- Verify registration link works.
- Verify registration quota can be purchased.
- Verify payment can be completed.
- Verify payment status can be verified.
- Verify registration form can be completed.
- Verify registration succeeds.
- Verify user can return to the E-Sign process.

---

## 13.5 Payment

- Verify quota purchase.
- Verify valid payment.
- Verify payment failure.
- Verify payment status.
- Verify successful payment verification.
- Verify unsuccessful payment verification.

---

## 13.6 E-Meterai

- Verify Stamp function is available.
- Verify e-Meterai can be selected.
- Verify e-Meterai is applied to the correct document.
- Verify e-Meterai information is displayed correctly.
- Verify stamping is completed successfully.

---

## 13.7 OTP

- Verify OTP is generated.
- Verify OTP is sent to the correct email.
- Verify valid OTP is accepted.
- Verify invalid OTP is rejected.
- Verify expired OTP is rejected.
- Verify OTP resend functionality if available.
- Verify signing cannot continue without valid OTP.

---

## 13.8 Pihak 1

- Verify Pihak 1 receives the E-Sign email.
- Verify Pihak 1 can access the E-Sign link.
- Verify registered Pihak 1 is directly redirected to E-Sign.
- Verify unregistered Pihak 1 can complete registration.
- Verify Pihak 1 can apply e-Meterai.
- Verify Pihak 1 receives OTP.
- Verify Pihak 1 can complete stamping.
- Verify Pihak 1 signing status is updated.

---

## 13.9 Pihak 2 / Vendor

- Verify Vendor receives the E-Sign email.
- Verify Vendor can access the E-Sign link.
- Verify registered Vendor is directly redirected to E-Sign.
- Verify unregistered Vendor can complete registration.
- Verify Vendor can purchase quota.
- Verify Vendor can complete payment.
- Verify Vendor can apply e-Meterai.
- Verify Vendor receives OTP.
- Verify Vendor can complete stamping.
- Verify Vendor signing status is updated.

---

## 13.10 Integration

- Verify CMS sends the correct contract to E-Sign.
- Verify E-Sign receives correct signer information.
- Verify E-Sign receives correct contract information.
- Verify E-Sign communicates correctly with Vinotek.
- Verify registration status is synchronized.
- Verify payment status is synchronized.
- Verify signing status is synchronized.
- Verify final signed document is available.
- Verify CMS receives the completed signing status.

---

# 14. Test Types

| Test Type | Description |
|---|---|
| Functional Testing | Verify each E-Sign function works according to requirements |
| Integration Testing | Verify CMS, E-Sign, and Vinotek integration |
| End-to-End Testing | Verify complete contract signing flow |
| Positive Testing | Verify valid business scenarios |
| Negative Testing | Verify invalid and failed scenarios |
| Regression Testing | Verify previously fixed defects |
| Data Validation | Verify signer and contract information |
| Email Testing | Verify E-Sign, registration, and OTP emails |
| Payment Testing | Verify quota purchase and payment process |
| Compatibility Testing | Verify E-Sign works in supported browsers |

---

# 15. Test Data

The following test data is required:

### User Data

- Valid Pihak 1 email.
- Valid Pihak 2 / Vendor email.
- Registered Vinotek email.
- Unregistered email.

### Contract Data

- Valid contract document.
- Contract with Pihak 1 signer.
- Contract with Pihak 2 signer.
- Contract requiring both parties to sign.

### OTP Data

- Valid OTP.
- Invalid OTP.
- Expired OTP.

### Payment Data

- Valid payment transaction.
- Failed payment transaction.
- Payment pending transaction.
- Successfully verified payment.

### Registration Data

- Valid user information.
- Valid email.
- Valid phone number.
- Required registration fields.

---

# 16. Entry Criteria

Testing can begin when:

- CMS contract has been generated.
- Required contract approval has been completed.
- E-Sign request can be generated.
- Pihak 1 and Pihak 2 test accounts are available.
- Test email accounts are accessible.
- Vinotek environment is available.
- Payment testing environment is available.
- e-Meterai testing data is available.
- OTP service is available.
- Integration between CMS, E-Sign, and Vinotek is available.

---

# 17. Exit Criteria

Testing can be completed when:

- All critical test cases have been executed.
- Registered user flow has been tested.
- Unregistered user flow has been tested.
- Pihak 1 flow has been tested.
- Pihak 2 / Vendor flow has been tested.
- Payment flow has been tested.
- e-Meterai flow has been tested.
- OTP flow has been tested.
- CMS integration has been verified.
- Vinotek integration has been verified.
- Critical and High severity defects are resolved or formally
  accepted.
- Regression testing has been completed.
- UAT has been completed.

---

# 18. Risk and Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| E-Sign email is not received | High | Verify email service and notification logs |
| E-Sign link is invalid | High | Validate link generation |
| Registered email is incorrectly identified as unregistered | High | Validate registration status integration |
| Unregistered user cannot register | High | Test complete Vinotek registration flow |
| Registration email is not received | Medium | Verify email notification |
| Quota purchase fails | High | Verify quota transaction |
| Payment fails | High | Verify payment integration |
| Payment status is not updated | High | Verify payment callback/status |
| e-Meterai cannot be applied | Critical | Verify Vinotek e-Meterai integration |
| OTP is not received | High | Verify OTP email service |
| OTP validation fails | High | Verify OTP validation service |
| Signing status is not updated | Critical | Verify E-Sign and CMS synchronization |
| Final document is not available | Critical | Verify document generation and storage |
| Wrong signer receives email | Critical | Validate signer and email mapping |

---

# 19. Defect Management

Every defect identified during testing must be documented in the
E-Sign Bug Report.

Each defect should contain:

| Field | Description |
|---|---|
| Bug ID | Unique defect identifier |
| Title | Short description |
| Module | Affected module |
| Severity | Impact level |
| Priority | Fix priority |
| Environment | Testing environment |
| Preconditions | Required conditions |
| Steps to Reproduce | Steps to reproduce the issue |
| Expected Result | Expected system behavior |
| Actual Result | Actual system behavior |
| Evidence | Screenshot/video/log |
| Status | Open / In Progress / Fixed / Closed |
| Related Test Case | Related test case ID |

---

# 20. Severity Classification

| Severity | Description |
|---|---|
| Critical | E-Sign process cannot be completed or contract integrity is affected |
| High | Major signing or integration functionality is affected |
| Medium | Functionality is affected but workaround is available |
| Low | Minor UI, validation, or cosmetic issue |

---

# 21. Test Deliverables

The following documents will be produced:

```text
E-Sign/
├── Test-Plan/
│   └── E-Sign-Test-Plan.md
│
├── Test-Cases/
│   └── E-Sign-Test-Cases.md
│
├── Bug-Report/
│   └── E-Sign-Bug-Report.md
│
└── UAT/
    └── E-Sign-UAT.md
```

---

# 22. Test Coverage

The E-Sign test coverage includes the complete business flow:

```text
CMS Contract Approval
        ↓
E-Sign Email
        ↓
E-Sign Link
        ↓
Registration Status Check
        ↓
 ┌──────────────────────┐
 │                      │
Registered          Unregistered
 │                      │
 ↓                      ↓
E-Sign Page        Vinotek Registration
 │                      ↓
 │                 Registration Email
 │                      ↓
 │                 Purchase Quota
 │                      ↓
 │                    Payment
 │                      ↓
 │               Payment Verification
 │                      ↓
 │               Complete Registration
 │                      ↓
 │               Registration Success
 │                      ↓
 └────────────────→ E-Sign Page
                         ↓
                      Stamp
                         ↓
                     e-Meterai
                         ↓
                       OTP
                         ↓
                  OTP Verification
                         ↓
                 Stamp Successful
                         ↓
                 Contract Signed
                         ↓
                Status Synchronization
                         ↓
                       CMS
```

---

# 23. Acceptance Criteria

The E-Sign system is considered functionally acceptable when:

1. The E-Sign request is sent to the correct signer.
2. The E-Sign email is successfully delivered.
3. The E-Sign link opens the correct process.
4. The system correctly identifies registered users.
5. Registered users are directly redirected to the E-Sign page.
6. Registered users are not required to register again.
7. Registered users are not required to purchase quota again.
8. Registered users are not required to make payment again.
9. Unregistered users are redirected to Vinotek.
10. Unregistered users can complete registration.
11. Users can purchase the required quota.
12. Users can complete payment.
13. Payment status can be verified.
14. Users can complete the registration form.
15. Successful registration allows the user to continue to E-Sign.
16. Users can access the contract document.
17. Users can apply e-Meterai.
18. OTP is delivered to the registered email.
19. Valid OTP is accepted.
20. Invalid OTP is rejected.
21. Users can successfully complete the stamping process.
22. Pihak 1 can complete the E-Sign process.
23. Pihak 2 / Vendor can complete the E-Sign process.
24. Signing status is updated correctly.
25. Final signed contract is available.
26. CMS receives the appropriate E-Sign status.

---

# 24. End-to-End Acceptance Flow

The complete successful scenario is:

```text
1. Contract approved in CMS
             ↓
2. E-Sign request generated
             ↓
3. Signer receives E-Sign email
             ↓
4. Signer clicks E-Sign link
             ↓
5. System checks registration status
             ↓
       ┌─────┴─────┐
       ↓           ↓
   Registered   Unregistered
       ↓           ↓
   E-Sign      Registration
    Page          ↓
       │       Quota Purchase
       │           ↓
       │        Payment
       │           ↓
       │    Payment Verification
       │           ↓
       │       Registration
       │           ↓
       └──────→ E-Sign Page
                    ↓
                 Stamp
                    ↓
                e-Meterai
                    ↓
                  OTP
                    ↓
             OTP Verification
                    ↓
             Stamp Successful
                    ↓
             Contract Signed
                    ↓
            Status Updated
                    ↓
                   CMS
```

---

# 25. Conclusion

The E-Sign testing scope covers the end-to-end electronic contract
signing process integrated with CMS and Vinotek.

Testing focuses on two main user conditions:

### Registered User

The user clicks the E-Sign link and is directly redirected to the
E-Sign page without repeating the registration, quota purchase,
or payment process.

### Unregistered User

The user clicks the E-Sign link and is redirected to Vinotek to
complete the registration process, including quota purchase,
payment, payment verification, and registration form completion.

After successful registration, the user can return to the E-Sign
process and continue with electronic stamping and OTP verification.

The same E-Sign process applies to both Pihak 1 and Pihak 2 /
Vendor.

The final objective is to ensure that the contract is successfully
signed, the e-Meterai is correctly applied, and the signing status
is properly synchronized back to CMS.