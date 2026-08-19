# Test Cases - E-Tender

## 1. Authentication & Authorization

---

### ET-TC-001 - Login with Valid Credential

| Field | Details |
|---|---|
| Test Case ID | ET-TC-001 |
| Test Scenario | Verify user can login using valid credentials |
| Module | Authentication |
| Priority | High |
| Test Type | Positive |
| Precondition | Valid user account is available |
| Test Data | Valid username and password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Procurement login page | Login page is displayed |
| 2 | Enter a valid username | Username is accepted |
| 3 | Enter a valid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the application | OTP verification page is displayed |

#### Expected Result

User is successfully authenticated and directed to the OTP verification process.

---

### ET-TC-002 - Login with Invalid Credential

| Field | Details |
|---|---|
| Test Case ID | ET-TC-002 |
| Test Scenario | Verify login is rejected when invalid credentials are entered |
| Module | Authentication |
| Priority | High |
| Test Type | Negative |
| Precondition | Login page is accessible |
| Test Data | Invalid username and/or password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Procurement login page | Login page is displayed |
| 2 | Enter an invalid username | Username is accepted |
| 3 | Enter an invalid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the result | Appropriate error message is displayed |
| 6 | Check the application state | User is not authenticated |

#### Expected Result

The system rejects the login attempt and prevents unauthorized access.

---

### ET-TC-003 - OTP Verification

| Field | Details |
|---|---|
| Test Case ID | ET-TC-003 |
| Test Scenario | Verify user can complete authentication using a valid OTP |
| Module | Authentication |
| Priority | High |
| Test Type | Positive |
| Precondition | Valid username and password have been submitted |
| Test Data | Valid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using valid credentials | OTP verification page is displayed |
| 2 | Retrieve the OTP from the registered email | OTP is received |
| 3 | Enter the valid OTP | OTP values are accepted |
| 4 | Submit the OTP | OTP is validated |
| 5 | Observe the application | Role selection page is displayed |

#### Expected Result

The system successfully validates the OTP and allows the user to proceed.

---

### ET-TC-004 - Invalid OTP Verification

| Field | Details |
|---|---|
| Test Case ID | ET-TC-004 |
| Test Scenario | Verify system rejects an invalid OTP |
| Module | Authentication |
| Priority | High |
| Test Type | Negative |
| Precondition | User has reached the OTP verification page |
| Test Data | Invalid OTP |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter an invalid OTP | OTP is entered |
| 2 | Submit the OTP | OTP validation is performed |
| 3 | Observe the result | Error message is displayed |
| 4 | Check the application | User is not allowed to proceed |

#### Expected Result

The system rejects the invalid OTP and prevents the user from continuing.

---

### ET-TC-005 - OTP Not Received

| Field | Details |
|---|---|
| Test Case ID | ET-TC-005 |
| Test Scenario | Verify OTP is delivered to the registered email address |
| Module | Authentication |
| Priority | High |
| Test Type | Negative / Reliability |
| Precondition | Valid credentials have been submitted |
| Test Data | Valid user account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using valid credentials | OTP verification page is displayed |
| 2 | Check the registered email inbox | OTP email should be received |
| 3 | Enter the received OTP | OTP is accepted |
| 4 | Complete the verification process | User proceeds to role selection |

#### Expected Result

OTP should be delivered to the registered email within the expected time.

#### Actual Result

OTP is sometimes not received by the registered email.

#### Related Bug

`ET-BUG-001`

#### Defect Characteristic

Intermittent / Recurring

---

### ET-TC-006 - Application Role Selection

| Field | Details |
|---|---|
| Test Case ID | ET-TC-006 |
| Test Scenario | Verify user can select an authorized application role |
| Module | Authorization |
| Priority | High |
| Test Type | Positive |
| Precondition | User has successfully completed OTP verification |
| Test Data | FUNGSIONAL / PENGGUNA |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Observe the role selection page | Available roles are displayed |
| 2 | Select the authorized role | Selected role is marked |
| 3 | Click the Pilih button | System processes the selected role |
| 4 | Observe the application | User is redirected to the E-Procurement application |

#### Expected Result

The user is successfully logged in using the selected authorized role.

---

# 2. Work Package Management

---

### ET-TC-007 - Create Work Package with Valid Data

| Field | Details |
|---|---|
| Test Case ID | ET-TC-007 |
| Test Scenario | Verify user can create a work package using valid data |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | User is logged in and has permission to create a work package |
| Test Data | Valid work package information |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Tender module | E-Tender page is displayed |
| 2 | Select Create Work Package | Creation form is displayed |
| 3 | Enter valid work package information | Data is accepted |
| 4 | Complete all required fields | No mandatory validation error is displayed |
| 5 | Submit the work package | Work package is successfully created |
| 6 | Open the created work package | Entered information is displayed correctly |

#### Expected Result

Work package is successfully created and stored by the system.

---

### ET-TC-008 - Validate Mandatory Fields

| Field | Details |
|---|---|
| Test Case ID | ET-TC-008 |
| Test Scenario | Verify mandatory fields are validated |
| Module | E-Tender |
| Priority | High |
| Test Type | Negative |
| Precondition | Work package creation form is accessible |
| Test Data | Mandatory fields left empty |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the work package creation form | Form is displayed |
| 2 | Leave required fields empty | Required fields remain empty |
| 3 | Click Submit | Validation is triggered |
| 4 | Observe the form | Validation messages are displayed |
| 5 | Check work package | Work package is not created |

#### Expected Result

The system prevents submission until all mandatory fields are completed.

---

### ET-TC-009 - Publish Work Package

| Field | Details |
|---|---|
| Test Case ID | ET-TC-009 |
| Test Scenario | Verify user can publish an eligible work package |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Eligible work package has been created |
| Test Data | Valid work package |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Tender module | E-Tender page is displayed |
| 2 | Search for the work package | Work package is displayed |
| 3 | Open the work package | Work package details are displayed |
| 4 | Select Publish | Publication process is displayed |
| 5 | Confirm publication | Work package is published |
| 6 | Check package status | Status is updated to Published |

#### Expected Result

Work package is successfully published and available according to the configured tender rules.

---

# 3. Vendor Registration

---

### ET-TC-010 - Vendor Registration

| Field | Details |
|---|---|
| Test Case ID | ET-TC-010 |
| Test Scenario | Verify eligible vendor can register for a published work package |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Work package has been published |
| Test Data | Valid vendor account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using a valid vendor account | Vendor successfully logs in |
| 2 | Open the published work package | Work package details are displayed |
| 3 | Select registration option | Registration process is displayed |
| 4 | Submit registration | Registration is successfully submitted |
| 5 | Check registration status | Registration status is displayed correctly |

#### Expected Result

Eligible vendor can successfully register for the work package.

---

### ET-TC-011 - Approve Vendor Registration

| Field | Details |
|---|---|
| Test Case ID | ET-TC-011 |
| Test Scenario | Verify procurement user can approve vendor registration |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor registration has been submitted |
| Test Data | Valid vendor registration |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using an authorized procurement account | User successfully logs in |
| 2 | Open vendor registration evaluation | Registration data is displayed |
| 3 | Review vendor information | Vendor information can be reviewed |
| 4 | Approve the registration | Registration is approved |
| 5 | Check registration status | Status is updated to Approved |

#### Expected Result

Vendor registration is successfully approved.

---

### ET-TC-012 - Reject Vendor Registration

| Field | Details |
|---|---|
| Test Case ID | ET-TC-012 |
| Test Scenario | Verify procurement user can reject vendor registration |
| Module | E-Tender |
| Priority | High |
| Test Type | Negative |
| Precondition | Vendor registration has been submitted |
| Test Data | Vendor registration that does not meet requirements |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using an authorized procurement account | User successfully logs in |
| 2 | Open vendor registration evaluation | Registration data is displayed |
| 3 | Review vendor information | Vendor information can be reviewed |
| 4 | Reject the registration | Registration is rejected |
| 5 | Check registration status | Status is updated to Rejected |

#### Expected Result

Vendor registration is successfully rejected and cannot proceed to the next stage.

---

# 4. Clarification Session

---

### ET-TC-013 - Conduct Clarification Session

| Field | Details |
|---|---|
| Test Case ID | ET-TC-013 |
| Test Scenario | Verify clarification session can be conducted |
| Module | E-Tender |
| Priority | Medium |
| Test Type | Positive |
| Precondition | Work package has been published and eligible vendors are registered |
| Test Data | Valid clarification information |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the clarification session | Clarification page is displayed |
| 2 | Enter clarification information | Information is accepted |
| 3 | Submit clarification | Clarification is successfully submitted |
| 4 | Review submitted clarification | Information is displayed correctly |

#### Expected Result

Clarification information is successfully submitted and available to authorized participants.

---

# 5. Bid Document Submission

---

### ET-TC-014 - Upload Bid Document

| Field | Details |
|---|---|
| Test Case ID | ET-TC-014 |
| Test Scenario | Verify vendor can upload a valid bid document |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor is approved to participate in the tender |
| Test Data | Valid bid document |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using an authorized vendor account | Vendor successfully logs in |
| 2 | Open the participating work package | Work package details are displayed |
| 3 | Open the bid submission page | Bid submission page is displayed |
| 4 | Select the required bid document | File is selected |
| 5 | Upload the document | Document is uploaded |
| 6 | Submit the bid | Bid submission is completed |
| 7 | Verify submission status | Bid submission status is updated correctly |

#### Expected Result

Bid document is successfully uploaded and submitted.

#### Known Defect

The document upload process has experienced intermittent issues.

#### Related Bug

`ET-BUG-002`

---

# 6. Bid Document Opening

---

### ET-TC-015 - Open Bid Documents

| Field | Details |
|---|---|
| Test Case ID | ET-TC-015 |
| Test Scenario | Verify authorized user can open submitted bid documents |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendors have submitted bid documents |
| Test Data | Submitted bid documents |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using an authorized procurement account | User successfully logs in |
| 2 | Open the relevant work package | Work package details are displayed |
| 3 | Navigate to bid document opening | Bid opening page is displayed |
| 4 | Select the submitted document | Document information is displayed |
| 5 | Open the document | Document opens successfully |

#### Expected Result

Authorized user can open and review submitted bid documents.

#### Known Defect

Submitted bid documents have experienced intermittent issues when being opened.

#### Related Bug

`ET-BUG-003`

---

# 7. Bid Document Evaluation

---

### ET-TC-016 - Evaluate Bid Documents

| Field | Details |
|---|---|
| Test Case ID | ET-TC-016 |
| Test Scenario | Verify evaluator can evaluate submitted bid documents |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Bid documents have been opened and evaluation stage is available |
| Test Data | Valid submitted bid documents |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using an authorized evaluator account | User successfully logs in |
| 2 | Open the bid evaluation page | Evaluation page is displayed |
| 3 | Select the relevant vendor | Vendor bid information is displayed |
| 4 | Review submitted documents | Documents can be reviewed |
| 5 | Enter evaluation results | Evaluation data is accepted |
| 6 | Submit the evaluation | Evaluation is successfully submitted |
| 7 | Verify evaluation status | Evaluation status is updated correctly |

#### Expected Result

Evaluator can review the bid documents and successfully submit the evaluation result.

#### Known Defects

- Submitted bid document data may not be available during evaluation.
- Evaluation status may not be updated after submission.

#### Related Bugs

`ET-BUG-004`

`ET-BUG-005`

---

# 8. Negotiation

---

### ET-TC-017 - Perform Negotiation

| Field | Details |
|---|---|
| Test Case ID | ET-TC-017 |
| Test Scenario | Verify authorized user can perform negotiation |
| Module | E-Tender |
| Priority | High |
| Test Type | Positive |
| Precondition | Required evaluation process has been completed |
| Test Data | Valid negotiation information |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the negotiation module | Negotiation page is displayed |
| 2 | Select the relevant vendor | Vendor information is displayed |
| 3 | Enter negotiation information | Data is accepted |
| 4 | Submit the negotiation | Negotiation is successfully submitted |
| 5 | Verify negotiation result | Negotiation result is recorded correctly |

#### Expected Result

Negotiation can be completed and the result is stored correctly.

---

# 9. Winner Determination

---

### ET-TC-018 - Determine Tender Winner

| Field | Details |
|---|---|
| Test Case ID | ET-TC-018 |
| Test Scenario | Verify authorized user can determine the winning vendor |
| Module | E-Tender |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Evaluation and negotiation processes have been completed |
| Test Data | Valid evaluation and negotiation results |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the winner determination page | Winner determination page is displayed |
| 2 | Review evaluation results | Evaluation results are displayed correctly |
| 3 | Review negotiation results | Negotiation results are displayed correctly |
| 4 | Select the eligible winning vendor | Selected vendor is displayed |
| 5 | Submit winner determination | Winner determination is successfully submitted |
| 6 | Verify tender status | Tender status is updated correctly |

#### Expected Result

The authorized user can determine the winning vendor and the tender status is updated correctly.

---

# 10. Test Case Summary

| Test Case ID | Test Scenario | Type | Priority |
|---|---|---|---|
| ET-TC-001 | Login with Valid Credential | Positive | High |
| ET-TC-002 | Login with Invalid Credential | Negative | High |
| ET-TC-003 | OTP Verification | Positive | High |
| ET-TC-004 | Invalid OTP Verification | Negative | High |
| ET-TC-005 | OTP Not Received | Reliability | High |
| ET-TC-006 | Application Role Selection | Positive | High |
| ET-TC-007 | Create Work Package | Positive | High |
| ET-TC-008 | Mandatory Field Validation | Negative | High |
| ET-TC-009 | Publish Work Package | Positive | High |
| ET-TC-010 | Vendor Registration | Positive | High |
| ET-TC-011 | Approve Vendor Registration | Positive | High |
| ET-TC-012 | Reject Vendor Registration | Negative | High |
| ET-TC-013 | Clarification Session | Positive | Medium |
| ET-TC-014 | Upload Bid Document | Positive | High |
| ET-TC-015 | Open Bid Documents | Positive | High |
| ET-TC-016 | Evaluate Bid Documents | Positive | High |
| ET-TC-017 | Perform Negotiation | Positive | High |
| ET-TC-018 | Determine Tender Winner | Positive | Critical |

## Test Coverage

The test cases cover the following E-Tender processes:

- Authentication
- OTP Verification
- Authorization / Role Selection
- Work Package Creation
- Mandatory Field Validation
- Work Package Publication
- Vendor Registration
- Vendor Registration Evaluation
- Clarification
- Bid Document Submission
- Bid Document Opening
- Bid Document Evaluation
- Negotiation
- Winner Determination
