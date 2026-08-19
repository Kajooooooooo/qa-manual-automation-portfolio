# Test Cases - E-Sign

## 1. Vendor E-Sign Request

---

### ES-TC-001 - Send E-Sign Email to Vendor

| Field | Details |
|---|---|
| Test Case ID | ES-TC-001 |
| Test Scenario | Verify E-Sign email is sent to Vendor after contract approval |
| Module | E-Sign Integration |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Contract has been approved by the required process in CMS |
| Test Data | Approved contract and valid Vendor email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete the required contract approval process in CMS | Contract approval is completed |
| 2 | Observe the E-Sign process | E-Sign request is generated |
| 3 | Open the Vendor email account | Email inbox is displayed |
| 4 | Check incoming email | E-Sign email is received |
| 5 | Open the E-Sign email | E-Sign information is displayed |
| 6 | Verify the E-Sign link | Valid E-Sign link is available |

#### Expected Result

The system successfully sends an E-Sign email containing the correct contract and E-Sign link to the Vendor.

---

### ES-TC-002 - Open Vendor E-Sign Link

| Field | Details |
|---|---|
| Test Case ID | ES-TC-002 |
| Test Scenario | Verify Vendor can access the E-Sign process through the email link |
| Module | E-Sign Access |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor has received the E-Sign email |
| Test Data | Valid E-Sign link |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign email | E-Sign email is displayed |
| 2 | Click the E-Sign link | E-Sign request is processed |
| 3 | Observe the system response | System checks Vendor registration status |

#### Expected Result

The system successfully processes the E-Sign link and validates the Vendor registration status.

---

# 2. Vendor Registration Validation

---

### ES-TC-003 - Registered Vendor Directly Accesses E-Sign

| Field | Details |
|---|---|
| Test Case ID | ES-TC-003 |
| Test Scenario | Verify registered Vendor is directly redirected to the E-Sign page |
| Module | Registration Validation |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor email is already registered in Vinotek |
| Test Data | Registered Vendor email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Vendor E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | System checks the Vendor registration status |
| 3 | System identifies the email | Email is recognized as registered |
| 4 | Observe the page | Vendor is directly redirected to the E-Sign page |
| 5 | Check the contract | Correct contract is displayed |

#### Expected Result

A registered Vendor is directly redirected to the E-Sign page without going through the registration process again.

---

### ES-TC-004 - Unregistered Vendor Redirected to Vinotek Registration

| Field | Details |
|---|---|
| Test Case ID | ES-TC-004 |
| Test Scenario | Verify unregistered Vendor is redirected to Vinotek registration |
| Module | Registration Validation |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor email is not registered in Vinotek |
| Test Data | Unregistered Vendor email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Vendor E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | System checks registration status |
| 3 | System identifies the email | Email is recognized as unregistered |
| 4 | Observe the browser | Vendor is redirected to Vinotek |
| 5 | Check the page | Registration process is displayed |

#### Expected Result

An unregistered Vendor is redirected to Vinotek to complete the required registration process.

---

# 3. Vendor Vinotek Registration

---

### ES-TC-005 - Receive Vinotek Registration Email

| Field | Details |
|---|---|
| Test Case ID | ES-TC-005 |
| Test Scenario | Verify unregistered Vendor receives the Vinotek registration email |
| Module | Vinotek Registration |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor has been identified as an unregistered user |
| Test Data | Valid Vendor email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Initiate the Vinotek registration process | Registration request is created |
| 2 | Open the Vendor email | Email inbox is displayed |
| 3 | Check incoming email | Vinotek registration email is received |
| 4 | Open the email | Registration information is displayed |
| 5 | Verify the registration link | Valid registration link is available |

#### Expected Result

The Vendor successfully receives the Vinotek registration email.

---

### ES-TC-006 - Open Vinotek Registration Link

| Field | Details |
|---|---|
| Test Case ID | ES-TC-006 |
| Test Scenario | Verify Vendor can access the Vinotek registration page |
| Module | Vinotek Registration |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor has received the registration email |
| Test Data | Valid registration link |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Vinotek registration email | Email is displayed |
| 2 | Click the registration link | Registration page is opened |
| 3 | Observe the page | Vinotek registration page is displayed |

#### Expected Result

Vendor can successfully access the Vinotek registration process.

---

### ES-TC-007 - Purchase Registration Quota

| Field | Details |
|---|---|
| Test Case ID | ES-TC-007 |
| Test Scenario | Verify Vendor can purchase the required registration quota |
| Module | Vinotek Registration |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor is on the Vinotek registration process |
| Test Data | Valid quota purchase data |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the quota purchase page | Quota purchase page is displayed |
| 2 | Select the required quota | Selected quota is displayed |
| 3 | Review quota information | Quota information is displayed correctly |
| 4 | Continue to payment | Payment page is displayed |

#### Expected Result

Vendor can successfully select the required registration quota and proceed to payment.

---

### ES-TC-008 - Complete Registration Quota Payment

| Field | Details |
|---|---|
| Test Case ID | ES-TC-008 |
| Test Scenario | Verify Vendor can complete registration quota payment |
| Module | Payment |
| Priority | High |
| Test Type | Positive |
| Precondition | Registration quota has been selected |
| Test Data | Valid payment data |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the payment page | Payment page is displayed |
| 2 | Select an available payment method | Payment method is selected |
| 3 | Complete the payment | Payment is processed |
| 4 | Observe the payment result | Payment result is displayed |

#### Expected Result

The registration quota payment is successfully processed.

---

### ES-TC-009 - Verify Registration Payment

| Field | Details |
|---|---|
| Test Case ID | ES-TC-009 |
| Test Scenario | Verify successful payment allows Vendor to continue registration |
| Module | Payment Verification |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor has completed quota payment |
| Test Data | Successful payment transaction |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete the payment | Payment is completed |
| 2 | Check payment status | Payment status is displayed |
| 3 | Verify transaction information | Transaction is verified |
| 4 | Continue registration | Registration form can be accessed |

#### Expected Result

Successful payment is verified and Vendor can continue the registration process.

---

### ES-TC-010 - Complete Vendor Registration Form

| Field | Details |
|---|---|
| Test Case ID | ES-TC-010 |
| Test Scenario | Verify Vendor can complete the Vinotek registration form |
| Module | Registration |
| Priority | High |
| Test Type | Positive |
| Precondition | Payment has been successfully verified |
| Test Data | Valid Vendor registration data |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the registration form | Registration form is displayed |
| 2 | Enter valid Vendor information | Data is accepted |
| 3 | Complete all mandatory fields | No validation error is displayed |
| 4 | Submit the registration form | Registration is processed |
| 5 | Observe the result | Registration success message is displayed |

#### Expected Result

Vendor is successfully registered in Vinotek.

---

### ES-TC-011 - Validate Vendor Registration Mandatory Fields

| Field | Details |
|---|---|
| Test Case ID | ES-TC-011 |
| Test Scenario | Verify mandatory fields are validated during Vendor registration |
| Module | Registration |
| Priority | Medium |
| Test Type | Negative |
| Precondition | Vendor registration form is displayed |
| Test Data | Required fields left empty |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the registration form | Registration form is displayed |
| 2 | Leave required fields empty | Required fields remain empty |
| 3 | Click Submit | Validation is triggered |
| 4 | Observe the form | Validation messages are displayed |
| 5 | Check registration status | Registration is not completed |

#### Expected Result

The system prevents Vendor registration until all mandatory fields are completed.

---

### ES-TC-012 - Return to E-Sign After Vendor Registration

| Field | Details |
|---|---|
| Test Case ID | ES-TC-012 |
| Test Scenario | Verify registered Vendor can return to the E-Sign process |
| Module | E-Sign Integration |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor registration has been successfully completed |
| Test Data | Successfully registered Vendor |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the original E-Sign email | E-Sign email is displayed |
| 2 | Click the E-Sign link | System checks registration status |
| 3 | System identifies the email | Email is recognized as registered |
| 4 | Observe the page | Vendor is redirected to the E-Sign page |
| 5 | Check contract information | Correct contract is displayed |

#### Expected Result

After completing registration, Vendor can access the E-Sign page through the original E-Sign email.

---

# 4. Vendor E-Sign & e-Meterai

---

### ES-TC-013 - Display Vendor E-Sign Page

| Field | Details |
|---|---|
| Test Case ID | ES-TC-013 |
| Test Scenario | Verify Vendor can access the correct E-Sign contract |
| Module | E-Sign |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor is registered and E-Sign link is accessible |
| Test Data | Valid contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign link | E-Sign page is displayed |
| 2 | Review contract information | Correct contract information is displayed |
| 3 | Review Vendor information | Correct Vendor information is displayed |
| 4 | Review available action | Stamp action is available |

#### Expected Result

Vendor can access the correct contract and Stamp function.

---

### ES-TC-014 - Vendor Click Stamp

| Field | Details |
|---|---|
| Test Case ID | ES-TC-014 |
| Test Scenario | Verify Vendor can initiate the Stamp process |
| Module | E-Sign |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor is on the E-Sign page |
| Test Data | Valid contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract | Contract is displayed |
| 2 | Click Stamp | Stamp process is opened |
| 3 | Observe the document | Stamp/e-Meterai interface is displayed |

#### Expected Result

Vendor can successfully initiate the electronic stamping process.

---

### ES-TC-015 - Vendor Apply e-Meterai

| Field | Details |
|---|---|
| Test Case ID | ES-TC-015 |
| Test Scenario | Verify Vendor can apply e-Meterai to the contract |
| Module | e-Meterai |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor has initiated the Stamp process |
| Test Data | Valid e-Meterai |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Stamp interface | Stamp interface is displayed |
| 2 | Select e-Meterai | e-Meterai is selected |
| 3 | Place e-Meterai on the required area | e-Meterai is placed |
| 4 | Review the document | e-Meterai is displayed correctly |
| 5 | Continue the process | OTP verification is requested |

#### Expected Result

Vendor successfully applies e-Meterai and proceeds to OTP verification.

---

### ES-TC-016 - Vendor Receive OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-016 |
| Test Scenario | Verify Vendor receives OTP for E-Sign verification |
| Module | OTP |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor has completed the Stamp process |
| Test Data | Registered Vendor email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Continue the Stamp process | OTP verification is displayed |
| 2 | Open the registered Vendor email | Email inbox is displayed |
| 3 | Check incoming email | OTP email is received |
| 4 | Verify OTP information | OTP is available |

#### Expected Result

OTP is successfully sent to the registered Vendor email.

---

### ES-TC-017 - Vendor Submit Valid OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-017 |
| Test Scenario | Verify Vendor can complete Stamp using a valid OTP |
| Module | OTP |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Valid OTP has been received |
| Test Data | Valid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter the valid OTP | OTP is accepted |
| 2 | Submit the OTP | OTP is validated |
| 3 | Observe the result | Stamp process is completed |
| 4 | Check the contract | Vendor signature and e-Meterai are applied |

#### Expected Result

Vendor successfully completes the Stamp process.

---

### ES-TC-018 - Vendor Submit Invalid OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-018 |
| Test Scenario | Verify system rejects invalid OTP entered by Vendor |
| Module | OTP |
| Priority | High |
| Test Type | Negative |
| Precondition | OTP verification page is displayed |
| Test Data | Invalid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter an invalid OTP | OTP is entered |
| 2 | Submit the OTP | OTP validation is performed |
| 3 | Observe the result | Error message is displayed |
| 4 | Check the contract | Vendor signing is not completed |

#### Expected Result

The system rejects the invalid OTP and prevents Vendor from completing the signing process.

---

# 5. Email Notification to Pengguna

---

### ES-TC-019 - Send E-Sign Email to Pengguna After Vendor Stamp

| Field | Details |
|---|---|
| Test Case ID | ES-TC-019 |
| Test Scenario | Verify E-Sign email is sent to Pengguna after Vendor successfully completes Stamp |
| Module | Email Notification |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor has successfully completed Stamp and e-Meterai |
| Test Data | Successfully stamped contract and valid Pengguna email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor Stamp process | Vendor Stamp is successful |
| 2 | Observe the E-Sign system | Signing status is updated |
| 3 | Open Pengguna email account | Email inbox is displayed |
| 4 | Check incoming email | E-Sign email is received |
| 5 | Open the email | E-Sign information is displayed |
| 6 | Verify the E-Sign link | Valid E-Sign link is available |

#### Expected Result

After Vendor successfully completes Stamp, the system automatically sends an E-Sign email to Pengguna.

---

### ES-TC-020 - Do Not Send Pengguna E-Sign Email Before Vendor Stamp

| Field | Details |
|---|---|
| Test Case ID | ES-TC-020 |
| Test Scenario | Verify Pengguna does not receive E-Sign email before Vendor completes Stamp |
| Module | Email Notification |
| Priority | High |
| Test Type | Negative |
| Precondition | Vendor has received the E-Sign request but has not completed Stamp |
| Test Data | Pending Vendor signing |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Vendor E-Sign process | E-Sign page is displayed |
| 2 | Do not complete the Stamp process | Vendor signing remains pending |
| 3 | Open Pengguna email | Email inbox is displayed |
| 4 | Check for E-Sign email | E-Sign email should not be sent |

#### Expected Result

The system does not send the E-Sign request to Pengguna until Vendor successfully completes the Stamp process.

---

# 6. Pengguna E-Sign

---

### ES-TC-021 - Pengguna Open E-Sign Email

| Field | Details |
|---|---|
| Test Case ID | ES-TC-021 |
| Test Scenario | Verify Pengguna can access the E-Sign process from the email |
| Module | Pengguna E-Sign |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor has successfully completed Stamp and Pengguna has received E-Sign email |
| Test Data | Valid Pengguna email and E-Sign link |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | E-Sign process is opened |
| 3 | Observe the page | Pengguna is directed to the E-Sign page |
| 4 | Review contract information | Correct contract is displayed |

#### Expected Result

Pengguna can successfully access the correct E-Sign contract.

---

### ES-TC-022 - Pengguna Click Stamp

| Field | Details |
|---|---|
| Test Case ID | ES-TC-022 |
| Test Scenario | Verify Pengguna can initiate the Stamp process |
| Module | Pengguna E-Sign |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Pengguna is on the E-Sign page |
| Test Data | Valid contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract | Contract is displayed |
| 2 | Click Stamp | Stamp process is opened |
| 3 | Observe the document | Stamp/e-Meterai interface is displayed |

#### Expected Result

Pengguna can successfully initiate the Stamp process.

---

### ES-TC-023 - Pengguna Apply e-Meterai

| Field | Details |
|---|---|
| Test Case ID | ES-TC-023 |
| Test Scenario | Verify Pengguna can apply e-Meterai to the contract |
| Module | e-Meterai |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Pengguna has initiated the Stamp process |
| Test Data | Valid e-Meterai |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Stamp interface | Stamp interface is displayed |
| 2 | Select e-Meterai | e-Meterai is selected |
| 3 | Place e-Meterai on the required area | e-Meterai is placed |
| 4 | Review the document | e-Meterai is displayed correctly |
| 5 | Continue the process | OTP verification is requested |

#### Expected Result

Pengguna successfully applies e-Meterai and proceeds to OTP verification.

---

### ES-TC-024 - Pengguna Receive OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-024 |
| Test Scenario | Verify Pengguna receives OTP for E-Sign verification |
| Module | OTP |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Pengguna has initiated the Stamp process |
| Test Data | Registered Pengguna email |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Continue the Stamp process | OTP verification page is displayed |
| 2 | Open Pengguna email | Email inbox is displayed |
| 3 | Check incoming email | OTP email is received |
| 4 | Verify OTP information | OTP is available |

#### Expected Result

OTP is successfully sent to the registered Pengguna email.

---

### ES-TC-025 - Pengguna Submit Valid OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-025 |
| Test Scenario | Verify Pengguna can complete Stamp using a valid OTP |
| Module | OTP |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Valid OTP has been received |
| Test Data | Valid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter the valid OTP | OTP is accepted |
| 2 | Submit the OTP | OTP is validated |
| 3 | Observe the result | Stamp process is completed |
| 4 | Check the contract | Pengguna signature and e-Meterai are applied |

#### Expected Result

Pengguna successfully completes the Stamp process.

---

### ES-TC-026 - Pengguna Submit Invalid OTP

| Field | Details |
|---|---|
| Test Case ID | ES-TC-026 |
| Test Scenario | Verify system rejects invalid OTP entered by Pengguna |
| Module | OTP |
| Priority | High |
| Test Type | Negative |
| Precondition | OTP verification page is displayed |
| Test Data | Invalid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter an invalid OTP | OTP is entered |
| 2 | Submit the OTP | OTP validation is performed |
| 3 | Observe the result | Error message is displayed |
| 4 | Check the contract | Pengguna signing is not completed |

#### Expected Result

The system rejects the invalid OTP and prevents Pengguna from completing the signing process.

---

# 7. Final Contract

---

### ES-TC-027 - Complete Contract Signing by Both Parties

| Field | Details |
|---|---|
| Test Case ID | ES-TC-027 |
| Test Scenario | Verify contract is successfully signed by Vendor and Pengguna |
| Module | Final Contract |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor and Pengguna have completed their respective Stamp processes |
| Test Data | Signed contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor Stamp | Vendor signing is completed |
| 2 | Complete Pengguna Stamp | Pengguna signing is completed |
| 3 | Open the final contract | Final contract is displayed |
| 4 | Verify Vendor signature | Vendor signature is present |
| 5 | Verify Pengguna signature | Pengguna signature is present |
| 6 | Verify e-Meterai | Required e-Meterai is present |
| 7 | Verify contract content | Contract content remains correct |

#### Expected Result

The contract is successfully signed by both Vendor and Pengguna and the final signed document is available.

---

### ES-TC-028 - Verify Final Contract Status

| Field | Details |
|---|---|
| Test Case ID | ES-TC-028 |
| Test Scenario | Verify E-Sign status is updated after both parties complete signing |
| Module | E-Sign |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor and Pengguna have completed signing |
| Test Data | Fully signed contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor signing | Vendor status is updated |
| 2 | Complete Pengguna signing | Pengguna status is updated |
| 3 | Observe overall signing status | Contract status is updated to completed/signed |
| 4 | Check final document | Signed contract is available |

#### Expected Result

The overall E-Sign status is updated to indicate that the contract has been fully signed.

---

# 8. CMS Integration

---

### ES-TC-029 - Verify Contract Data from CMS

| Field | Details |
|---|---|
| Test Case ID | ES-TC-029 |
| Test Scenario | Verify contract data transferred from CMS to E-Sign is correct |
| Module | CMS Integration |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Contract has been approved and sent to E-Sign |
| Test Data | Approved CMS contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the approved contract in CMS | Contract information is displayed |
| 2 | Open the related E-Sign process | E-Sign page is displayed |
| 3 | Compare contract number | Contract number matches CMS |
| 4 | Compare Vendor information | Vendor information matches CMS |
| 5 | Compare Pengguna information | Pengguna information matches CMS |
| 6 | Compare contract document | Document matches CMS |

#### Expected Result

Contract data transferred from CMS to E-Sign is accurate and complete.

---

### ES-TC-030 - Synchronize Final Signing Status to CMS

| Field | Details |
|---|---|
| Test Case ID | ES-TC-030 |
| Test Scenario | Verify final E-Sign status is synchronized to CMS |
| Module | CMS Integration |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Vendor and Pengguna have successfully completed E-Sign |
| Test Data | Fully signed contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor signing | Vendor signing is successful |
| 2 | Complete Pengguna signing | Pengguna signing is successful |
| 3 | Observe E-Sign status | Status is updated to completed/signed |
| 4 | Open CMS | CMS is accessible |
| 5 | Open the related contract | Contract information is displayed |
| 6 | Check E-Sign status | CMS displays the correct final signing status |
| 7 | Check final document | Final signed contract is available |

#### Expected Result

The final E-Sign status and signed contract are successfully synchronized back to CMS.

---

# 9. Security & Negative Scenarios

---

### ES-TC-031 - Access E-Sign Using Invalid Link

| Field | Details |
|---|---|
| Test Case ID | ES-TC-031 |
| Test Scenario | Verify system rejects an invalid or expired E-Sign link |
| Module | E-Sign Security |
| Priority | High |
| Test Type | Negative |
| Precondition | Invalid or expired E-Sign link is available |
| Test Data | Invalid E-Sign link |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the invalid E-Sign link | System processes the request |
| 2 | Observe the result | Appropriate error message is displayed |
| 3 | Check contract access | Contract cannot be accessed |

#### Expected Result

The system rejects invalid or expired E-Sign links.

---

### ES-TC-032 - Unauthorized User Cannot Access Contract

| Field | Details |
|---|---|
| Test Case ID | ES-TC-032 |
| Test Scenario | Verify unauthorized user cannot access another user's contract |
| Module | Authorization |
| Priority | Critical |
| Test Type | Negative |
| Precondition | E-Sign request belongs to another user |
| Test Data | Unauthorized user account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Attempt to access another user's E-Sign link | System validates authorization |
| 2 | Observe the result | Access is denied |
| 3 | Check contract data | Contract information is not displayed |
| 4 | Check signing action | User cannot perform Stamp |

#### Expected Result

Unauthorized users cannot access or sign another user's contract.

---

# 10. Test Case Summary

| Test Case ID | Test Scenario | Type | Priority |
|---|---|---|---|
| ES-TC-001 | Send E-Sign Email to Vendor | Positive | Critical |
| ES-TC-002 | Open Vendor E-Sign Link | Positive | High |
| ES-TC-003 | Registered Vendor Directly Accesses E-Sign | Positive | Critical |
| ES-TC-004 | Unregistered Vendor Redirected to Vinotek Registration | Positive | Critical |
| ES-TC-005 | Receive Vinotek Registration Email | Positive | High |
| ES-TC-006 | Open Vinotek Registration Link | Positive | High |
| ES-TC-007 | Purchase Registration Quota | Positive | High |
| ES-TC-008 | Complete Registration Quota Payment | Positive | High |
| ES-TC-009 | Verify Registration Payment | Positive | Critical |
| ES-TC-010 | Complete Vendor Registration Form | Positive | High |
| ES-TC-011 | Validate Vendor Registration Mandatory Fields | Negative | Medium |
| ES-TC-012 | Return to E-Sign After Vendor Registration | Positive | Critical |
| ES-TC-013 | Display Vendor E-Sign Page | Positive | Critical |
| ES-TC-014 | Vendor Click Stamp | Positive | Critical |
| ES-TC-015 | Vendor Apply e-Meterai | Positive | Critical |
| ES-TC-016 | Vendor Receive OTP | Positive | Critical |
| ES-TC-017 | Vendor Submit Valid OTP | Positive | Critical |
| ES-TC-018 | Vendor Submit Invalid OTP | Negative | High |
| ES-TC-019 | Send E-Sign Email to Pengguna After Vendor Stamp | Positive | Critical |
| ES-TC-020 | Do Not Send Pengguna Email Before Vendor Stamp | Negative | High |
| ES-TC-021 | Pengguna Open E-Sign Email | Positive | Critical |
| ES-TC-022 | Pengguna Click Stamp | Positive | Critical |
| ES-TC-023 | Pengguna Apply e-Meterai | Positive | Critical |
| ES-TC-024 | Pengguna Receive OTP | Positive | Critical |
| ES-TC-025 | Pengguna Submit Valid OTP | Positive | Critical |
| ES-TC-026 | Pengguna Submit Invalid OTP | Negative | High |
| ES-TC-027 | Complete Contract Signing by Both Parties | Positive | Critical |
| ES-TC-028 | Verify Final Contract Status | Positive | Critical |
| ES-TC-029 | Verify Contract Data from CMS | Positive | Critical |
| ES-TC-030 | Synchronize Final Signing Status to CMS | Positive | Critical |
| ES-TC-031 | Access E-Sign Using Invalid Link | Negative | High |
| ES-TC-032 | Unauthorized User Cannot Access Contract | Negative | Critical |

---

# 11. Test Coverage

The test cases cover the following E-Sign processes:

- CMS Contract Approval
- E-Sign Request Generation
- Vendor E-Sign Email
- Vendor E-Sign Link
- Vendor Registration Status Validation
- Registered Vendor Flow
- Unregistered Vendor Flow
- Vinotek Registration
- Registration Email
- Registration Quota Purchase
- Registration Payment
- Payment Verification
- Vendor Registration Form
- Vendor E-Sign
- Vendor Stamp
- Vendor e-Meterai
- Vendor OTP Verification
- Vendor Signing Validation
- Email Notification to Pengguna
- Pengguna E-Sign
- Pengguna Stamp
- Pengguna e-Meterai
- Pengguna OTP Verification
- Final Contract Signing
- Final Contract Status
- CMS Integration
- E-Sign Status Synchronization
- Invalid E-Sign Link
- Authorization