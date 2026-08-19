# Test Cases - Contract Management System

## 1. Work Package Integration

---

### CMS-TC-001 - Receive Work Package from E-Tender

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-001 |
| Test Scenario | Verify CMS can receive a work package sent from E-Tender after winner determination |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Integration |
| Precondition | Winner has been determined in E-Tender and the work package is ready to be sent to CMS |
| Test Data | Valid completed E-Tender work package |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the completed E-Tender work package | Work package details are displayed |
| 2 | Verify the winning vendor | Winning vendor information is displayed correctly |
| 3 | Send the work package to CMS | System successfully processes the request |
| 4 | Open Contract Management System | CMS page is displayed |
| 5 | Search for the transferred work package | Work package is available in CMS |
| 6 | Open the work package | Work package information is displayed correctly |

#### Expected Result

The work package is successfully transferred from E-Tender to CMS and all relevant package and vendor information is available correctly.

---

### CMS-TC-002 - Validate Work Package Data

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-002 |
| Test Scenario | Verify work package data received from E-Tender is displayed correctly in CMS |
| Module | Contract Management |
| Priority | High |
| Test Type | Integration |
| Precondition | Work package has been successfully transferred from E-Tender to CMS |
| Test Data | Valid transferred work package |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the transferred work package in CMS | Work package details are displayed |
| 2 | Review work package information | Package information is displayed |
| 3 | Review winning vendor information | Vendor information is displayed correctly |
| 4 | Compare the information with E-Tender data | Data matches the source system |

#### Expected Result

Work package and winning vendor information received from E-Tender is displayed correctly in CMS.

---

# 2. Reviewer Configuration

---

### CMS-TC-003 - Set Atasan as Reviewer

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-003 |
| Test Scenario | Verify user can configure Atasan as a contract reviewer |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Work package is available in CMS |
| Test Data | Valid Atasan reviewer |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract management process | Contract management page is displayed |
| 2 | Open Reviewer Settings | Reviewer configuration page is displayed |
| 3 | Select Atasan as reviewer type | Atasan reviewer option is displayed |
| 4 | Select the appropriate Atasan | Selected reviewer is displayed |
| 5 | Save the configuration | Reviewer configuration is successfully saved |

#### Expected Result

The selected Atasan is successfully configured as a contract reviewer.

---

### CMS-TC-004 - Set Pihak 1 as Reviewer

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-004 |
| Test Scenario | Verify user can configure Pengguna / Pihak 1 as a contract reviewer |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Work package is available in CMS |
| Test Data | Valid Pihak 1 user |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Reviewer Settings | Reviewer configuration page is displayed |
| 2 | Select Pengguna / Pihak 1 | Pihak 1 option is displayed |
| 3 | Select the appropriate user | Selected user is displayed |
| 4 | Save the configuration | Reviewer configuration is successfully saved |
| 5 | Reopen Reviewer Settings | Saved Pihak 1 reviewer is displayed |

#### Expected Result

The selected Pihak 1 is successfully configured as a contract reviewer.

---

### CMS-TC-005 - Set Pihak 2 / Vendor as Reviewer

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-005 |
| Test Scenario | Verify vendor / Pihak 2 can be configured as a contract reviewer |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Work package has been received and vendor information is available |
| Test Data | Valid winning vendor |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Reviewer Settings | Reviewer configuration page is displayed |
| 2 | Select Vendor / Pihak 2 | Vendor reviewer option is displayed |
| 3 | Select the winning vendor | Selected vendor is displayed |
| 4 | Save the configuration | Reviewer configuration is successfully saved |
| 5 | Reopen Reviewer Settings | Selected vendor is displayed as Pihak 2 reviewer |

#### Expected Result

The winning vendor is successfully configured as Pihak 2 reviewer.

---

### CMS-TC-006 - Validate Complete Reviewer Configuration

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-006 |
| Test Scenario | Verify all required reviewers are configured correctly |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Atasan, Pihak 1, and Pihak 2 information are available |
| Test Data | Valid Atasan, Pihak 1, and Pihak 2 |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Reviewer Settings | Reviewer configuration page is displayed |
| 2 | Configure Atasan | Atasan is successfully selected |
| 3 | Configure Pihak 1 | Pihak 1 is successfully selected |
| 4 | Configure Pihak 2 | Pihak 2 is successfully selected |
| 5 | Save the configuration | Reviewer configuration is successfully saved |
| 6 | Reopen Reviewer Settings | All configured reviewers are displayed correctly |

#### Expected Result

Atasan, Pihak 1, and Pihak 2 are successfully configured and stored in the system.

---

# 3. Payment Configuration

---

### CMS-TC-007 - Configure Payment Method

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-007 |
| Test Scenario | Verify user can configure the contract payment method |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Work package is available and contract configuration can be performed |
| Test Data | Valid payment method |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Payment Settings | Payment configuration page is displayed |
| 2 | Select the required payment method | Selected payment method is displayed |
| 3 | Enter required payment information | Payment information is accepted |
| 4 | Save the configuration | Payment configuration is successfully saved |
| 5 | Reopen Payment Settings | Saved payment method is displayed correctly |

#### Expected Result

The selected payment method is successfully configured and stored.

---

### CMS-TC-008 - Validate Payment Method

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-008 |
| Test Scenario | Verify configured payment method is displayed correctly |
| Module | Contract Management |
| Priority | Medium |
| Test Type | Positive |
| Precondition | Payment method has been configured |
| Test Data | Existing payment configuration |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Payment Settings | Payment configuration is displayed |
| 2 | Review the selected payment method | Correct payment method is displayed |
| 3 | Save or continue the contract process | System processes the configuration |
| 4 | Reopen the contract | Payment information remains available |

#### Expected Result

The configured payment method is stored and displayed correctly.

---

### CMS-TC-009 - Set Vendor Payment Account

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-009 |
| Test Scenario | Verify user can assign the correct payment account to the vendor |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Winning vendor has been transferred to CMS and valid payment account data is available |
| Test Data | Valid vendor payment account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Vendor Payment Account settings | Payment account page is displayed |
| 2 | Select the winning vendor | Vendor information is displayed |
| 3 | Select the appropriate payment account | Selected account is displayed |
| 4 | Save the configuration | Payment account is successfully saved |
| 5 | Reopen the payment account settings | Selected account is displayed correctly |

#### Expected Result

The correct vendor payment account is successfully assigned and stored.

---

### CMS-TC-010 - Validate Vendor Payment Account

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-010 |
| Test Scenario | Verify assigned vendor payment account is displayed correctly |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Vendor payment account has been configured |
| Test Data | Valid vendor payment account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open vendor payment account information | Payment account information is displayed |
| 2 | Review vendor information | Correct vendor is displayed |
| 3 | Review account information | Correct account is displayed |
| 4 | Compare the account with registered vendor data | Account information matches vendor data |

#### Expected Result

The vendor payment account is correctly stored and matches the registered vendor information.

---

# 4. Contract Document

---

### CMS-TC-011 - Generate Contract Document

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-011 |
| Test Scenario | Verify system can generate a contract document |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Reviewer configuration, payment method, and vendor payment account have been completed |
| Test Data | Valid contract configuration |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract document section | Contract document page is displayed |
| 2 | Verify contract information | Contract information is displayed correctly |
| 3 | Select Generate Contract | Document generation process starts |
| 4 | Wait for the generation process | Contract document is generated |
| 5 | Open the generated document | Document can be opened successfully |

#### Expected Result

The system successfully generates the contract document based on the configured contract information.

---

### CMS-TC-012 - Validate Generated Contract Document

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-012 |
| Test Scenario | Verify generated contract document contains correct contract information |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Contract document has been generated |
| Test Data | Generated contract document |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the generated contract document | Document is displayed |
| 2 | Review work package information | Package information is correct |
| 3 | Review Pihak 1 information | Pihak 1 information is correct |
| 4 | Review Pihak 2 information | Vendor information is correct |
| 5 | Review payment information | Payment information is correct |
| 6 | Review contract details | Contract details are complete and correct |

#### Expected Result

The generated contract document contains complete and accurate contract information.

---

### CMS-TC-013 - Send Contract Document to Reviewers

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-013 |
| Test Scenario | Verify contract document can be sent to configured reviewers |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Contract document has been generated and reviewers have been configured |
| Test Data | Valid generated contract document |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the generated contract document | Contract document is displayed |
| 2 | Verify reviewer configuration | Configured reviewers are displayed |
| 3 | Select Send to Reviewer | Submission process is displayed |
| 4 | Confirm the submission | Contract is successfully sent |
| 5 | Check contract status | Contract status is updated correctly |

#### Expected Result

The contract document is successfully sent to all configured reviewers.

---

# 5. Contract Review & Approval

---

### CMS-TC-014 - Reviewer Accesses Contract Document

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-014 |
| Test Scenario | Verify configured reviewer can access the contract document |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Contract document has been sent to the reviewer |
| Test Data | Valid reviewer account |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the reviewer account | Reviewer successfully logs in |
| 2 | Open the contract approval task | Contract task is displayed |
| 3 | Select the relevant contract | Contract information is displayed |
| 4 | Open the contract document | Document opens successfully |

#### Expected Result

The configured reviewer can access and review the contract document.

---

### CMS-TC-015 - Approve Contract Document

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-015 |
| Test Scenario | Verify reviewer can approve the contract document |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Contract document has been sent to the reviewer |
| Test Data | Valid contract document |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the reviewer account | Reviewer successfully logs in |
| 2 | Open the contract approval task | Contract task is displayed |
| 3 | Review the contract document | Contract can be reviewed |
| 4 | Select Approve | Approval confirmation is displayed |
| 5 | Confirm the approval | Approval is successfully submitted |
| 6 | Check approval status | Reviewer status is updated to Approved |

#### Expected Result

The reviewer successfully approves the contract and the approval status is updated correctly.

---

### CMS-TC-016 - Reject Contract Document

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-016 |
| Test Scenario | Verify reviewer can reject the contract document |
| Module | Contract Management |
| Priority | High |
| Test Type | Negative |
| Precondition | Contract document has been sent to the reviewer |
| Test Data | Contract document that requires revision |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the reviewer account | Reviewer successfully logs in |
| 2 | Open the contract approval task | Contract task is displayed |
| 3 | Review the contract document | Contract can be reviewed |
| 4 | Select Reject | Rejection form is displayed |
| 5 | Enter the rejection reason | Rejection reason is accepted |
| 6 | Submit the rejection | Contract is successfully rejected |
| 7 | Check contract status | Contract status is updated accordingly |

#### Expected Result

The reviewer can reject the contract and the rejection information is recorded correctly.

---

### CMS-TC-017 - Validate Reviewer Approval Status

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-017 |
| Test Scenario | Verify reviewer approval status is updated correctly |
| Module | Contract Management |
| Priority | High |
| Test Type | Positive |
| Precondition | Contract has been sent to configured reviewers |
| Test Data | Reviewer approval results |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract approval status | Approval status page is displayed |
| 2 | Review Atasan status | Atasan status is displayed correctly |
| 3 | Review Pihak 1 status | Pihak 1 status is displayed correctly |
| 4 | Review Pihak 2 status | Pihak 2 status is displayed correctly |
| 5 | Compare status with actual reviewer actions | Status matches each reviewer action |

#### Expected Result

The system displays the correct approval status for each reviewer.

---

### CMS-TC-018 - Validate Multiple Reviewer Approval

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-018 |
| Test Scenario | Verify system processes approval from multiple reviewers correctly |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Integration |
| Precondition | Atasan, Pihak 1, and Pihak 2 have been configured as reviewers |
| Test Data | Valid reviewer accounts |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Atasan approves the contract | Atasan status is updated to Approved |
| 2 | Pihak 1 approves the contract | Pihak 1 status is updated to Approved |
| 3 | Pihak 2 approves the contract | Pihak 2 status is updated to Approved |
| 4 | Open the contract approval status | All reviewer statuses are displayed |
| 5 | Check overall approval status | System recognizes that all required approvals are completed |

#### Expected Result

All required reviewer approvals are recorded correctly and the contract is recognized as fully approved.

---

### CMS-TC-019 - Prevent Contract Progress Before All Approvals

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-019 |
| Test Scenario | Verify contract cannot proceed before all required reviewers approve |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Negative |
| Precondition | At least one required reviewer has not approved the contract |
| Test Data | Incomplete reviewer approval |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract approval status | Approval status is displayed |
| 2 | Verify at least one reviewer has not approved | Incomplete approval is displayed |
| 3 | Attempt to proceed to final contract | System validates approval requirements |
| 4 | Observe the application | System prevents the contract from proceeding |

#### Expected Result

The system prevents the contract from proceeding until all required reviewers have completed their approval.

---

# 6. Final Contract & E-Signature

---

### CMS-TC-020 - Generate Final Contract

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-020 |
| Test Scenario | Verify final contract can be generated after all reviewer approvals |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Atasan, Pihak 1, and Pihak 2 have approved the contract |
| Test Data | Fully approved contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract | Contract information is displayed |
| 2 | Verify all reviewer statuses | All required reviewers are Approved |
| 3 | Select the final contract generation function | Final contract generation is available |
| 4 | Generate the final contract | Final contract is successfully generated |
| 5 | Open the final contract | Final contract can be opened |

#### Expected Result

The final contract is successfully generated after all required reviewer approvals have been completed.

---

### CMS-TC-021 - Pihak 1 E-Signs Final Contract

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-021 |
| Test Scenario | Verify Pihak 1 can perform e-signature on the final contract |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | All required reviewer approvals have been completed and final contract is available |
| Test Data | Valid Pihak 1 account and final contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using Pihak 1 account | Pihak 1 successfully logs in |
| 2 | Open the final contract | Final contract is displayed |
| 3 | Review the final contract | Contract information is displayed correctly |
| 4 | Select the e-signature function | E-signature process is displayed |
| 5 | Complete the e-signature process | Signature is successfully submitted |
| 6 | Check signature status | Pihak 1 signature status is updated |

#### Expected Result

Pihak 1 successfully performs e-signature on the final contract.

---

### CMS-TC-022 - Pihak 2 E-Signs Final Contract

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-022 |
| Test Scenario | Verify Pihak 2 / Vendor can perform e-signature on the final contract |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | All required reviewer approvals have been completed and final contract is available |
| Test Data | Valid vendor account and final contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using Pihak 2 / Vendor account | Vendor successfully logs in |
| 2 | Open the final contract | Final contract is displayed |
| 3 | Review the final contract | Contract information is displayed correctly |
| 4 | Select the e-signature function | E-signature process is displayed |
| 5 | Complete the e-signature process | Signature is successfully submitted |
| 6 | Check signature status | Pihak 2 signature status is updated |

#### Expected Result

Pihak 2 / Vendor successfully performs e-signature on the final contract.

---

### CMS-TC-023 - Prevent E-Sign Before Approval Completion

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-023 |
| Test Scenario | Verify e-signature cannot be performed before all required approvals are completed |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Negative |
| Precondition | At least one required reviewer has not approved the contract |
| Test Data | Contract with incomplete approval |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract | Contract information is displayed |
| 2 | Check reviewer approval status | At least one approval is incomplete |
| 3 | Attempt to access the e-signature function | System validates approval requirements |
| 4 | Observe the application | E-signature function is unavailable or blocked |

#### Expected Result

The system prevents e-signature until all required reviewer approvals have been completed.

---

### CMS-TC-024 - Validate Final Contract Status

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-024 |
| Test Scenario | Verify final contract status is updated after required parties complete e-signature |
| Module | Contract Management |
| Priority | Critical |
| Test Type | Positive |
| Precondition | All reviewers have approved and Pihak 1 and Pihak 2 have completed e-signature |
| Test Data | Fully signed final contract |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the final contract | Final contract is displayed |
| 2 | Review reviewer approval status | All required reviewers are Approved |
| 3 | Review Pihak 1 signature status | Pihak 1 is marked as Signed |
| 4 | Review Pihak 2 signature status | Pihak 2 is marked as Signed |
| 5 | Check the overall contract status | Final contract status is updated correctly |

#### Expected Result

The system records all required approvals and signatures and updates the contract to the appropriate final status.

---

# 7. End-to-End Contract Management

---

### CMS-TC-025 - Complete Contract Management Process

| Field | Details |
|---|---|
| Test Case ID | CMS-TC-025 |
| Test Scenario | Verify complete contract management process from E-Tender winner determination to final e-signature |
| Module | Contract Management |
| Priority | Critical |
| Test Type | End-to-End |
| Precondition | E-Tender process has been completed and a winning vendor has been determined |
| Test Data | Valid completed work package and winning vendor |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Send the winning work package from E-Tender to CMS | Work package is successfully transferred |
| 2 | Open the work package in CMS | Work package information is displayed correctly |
| 3 | Configure Atasan as reviewer | Atasan is successfully configured |
| 4 | Configure Pihak 1 as reviewer | Pihak 1 is successfully configured |
| 5 | Configure Pihak 2 / Vendor as reviewer | Pihak 2 is successfully configured |
| 6 | Configure the payment method | Payment method is successfully saved |
| 7 | Set the vendor payment account | Vendor payment account is successfully saved |
| 8 | Generate the contract document | Contract document is successfully generated |
| 9 | Validate the contract document | Contract information is correct |
| 10 | Send the contract to reviewers | Contract is successfully sent to reviewers |
| 11 | Atasan reviews and approves the contract | Atasan approval is recorded |
| 12 | Pihak 1 reviews and approves the contract | Pihak 1 approval is recorded |
| 13 | Pihak 2 reviews and approves the contract | Pihak 2 approval is recorded |
| 14 | Verify all reviewer approval statuses | All required reviewers are Approved |
| 15 | Generate the final contract | Final contract is successfully generated |
| 16 | Pihak 1 performs e-signature | Pihak 1 signature is successfully recorded |
| 17 | Pihak 2 performs e-signature | Pihak 2 signature is successfully recorded |
| 18 | Verify final contract status | Contract reaches the expected final status |

#### Expected Result

The complete Contract Management process is successfully completed from work package transfer through reviewer approval and final e-signature by Pihak 1 and Pihak 2.

---

# 8. Test Case Summary

| Test Case ID | Test Scenario | Type | Priority |
|---|---|---|---|
| CMS-TC-001 | Receive Work Package from E-Tender | Integration | Critical |
| CMS-TC-002 | Validate Work Package Data | Integration | High |
| CMS-TC-003 | Set Atasan as Reviewer | Positive | High |
| CMS-TC-004 | Set Pihak 1 as Reviewer | Positive | High |
| CMS-TC-005 | Set Pihak 2 / Vendor as Reviewer | Positive | High |
| CMS-TC-006 | Validate Complete Reviewer Configuration | Positive | High |
| CMS-TC-007 | Configure Payment Method | Positive | High |
| CMS-TC-008 | Validate Payment Method | Positive | Medium |
| CMS-TC-009 | Set Vendor Payment Account | Positive | High |
| CMS-TC-010 | Validate Vendor Payment Account | Positive | High |
| CMS-TC-011 | Generate Contract Document | Positive | Critical |
| CMS-TC-012 | Validate Generated Contract Document | Positive | Critical |
| CMS-TC-013 | Send Contract Document to Reviewers | Positive | High |
| CMS-TC-014 | Reviewer Accesses Contract Document | Positive | High |
| CMS-TC-015 | Approve Contract Document | Positive | Critical |
| CMS-TC-016 | Reject Contract Document | Negative | High |
| CMS-TC-017 | Validate Reviewer Approval Status | Positive | High |
| CMS-TC-018 | Validate Multiple Reviewer Approval | Integration | Critical |
| CMS-TC-019 | Prevent Contract Progress Before All Approvals | Negative | Critical |
| CMS-TC-020 | Generate Final Contract | Positive | Critical |
| CMS-TC-021 | Pihak 1 E-Signs Final Contract | Positive | Critical |
| CMS-TC-022 | Pihak 2 E-Signs Final Contract | Positive | Critical |
| CMS-TC-023 | Prevent E-Sign Before Approval Completion | Negative | Critical |
| CMS-TC-024 | Validate Final Contract Status | Positive | Critical |
| CMS-TC-025 | Complete Contract Management Process | End-to-End | Critical |

## Test Coverage

The test cases cover the following Contract Management processes:

- Work Package Transfer from E-Tender
- Work Package Data Validation
- Reviewer Configuration
- Atasan Reviewer
- Pihak 1 Reviewer
- Pihak 2 / Vendor Reviewer
- Payment Method Configuration
- Vendor Payment Account
- Contract Document Generation
- Contract Document Validation
- Contract Document Submission
- Reviewer Access
- Contract Approval
- Contract Rejection
- Multiple Reviewer Approval
- Approval Status Validation
- Approval Workflow Validation
- Final Contract Generation
- Pihak 1 E-Signature
- Pihak 2 E-Signature
- E-Signature Workflow Validation
- Final Contract Status
- End-to-End Contract Management