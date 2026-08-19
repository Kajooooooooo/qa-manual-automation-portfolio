# User Acceptance Test (UAT) - Contract Management System

## 1. UAT Overview

| Field | Details |
|---|---|
| Application | E-Procurement |
| Module | Contract Management System (CMS) |
| Testing Type | User Acceptance Testing |
| Objective | Verify that the CMS contract workflow meets business requirements |
| Status | Completed |

---

# 2. UAT Scope

The UAT covers the following Contract Management System processes:

1. Receive work package from E-Tender
2. Setting Reviewer
3. Setting Payment Method
4. Setting Vendor Payment Account
5. Generate Contract Document
6. Send Contract Document to Reviewer
7. Reviewer Approval
8. Final Contract E-Signature

---

# 3. UAT Scenarios

## UAT-CMS-001 - Receive Work Package

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-001 |
| Scenario | Verify work package can be received from E-Tender |
| Priority | High |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Complete the winner determination process in E-Tender | Winning vendor is determined | Pass |
| 2 | Send the work package to CMS | Package is sent successfully | Pass |
| 3 | Open CMS | CMS application is displayed | Pass |
| 4 | Search for the transferred package | Work package is available in CMS | Pass |

### UAT Result

**PASS**

The work package can be successfully transferred from E-Tender
to CMS.

---

## UAT-CMS-002 - Setting Reviewer

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-002 |
| Scenario | Verify reviewer can be configured |
| Priority | High |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Open the work package in CMS | Package details are displayed | Pass |
| 2 | Open Reviewer Setting | Reviewer configuration is displayed | Pass |
| 3 | Set Atasan as reviewer | Reviewer is selected | Pass |
| 4 | Set Pengguna (Pihak 1) as reviewer | Reviewer is selected | Pass |
| 5 | Set Vendor (Pihak 2) as reviewer | Reviewer is selected | Pass |
| 6 | Save reviewer configuration | Reviewer configuration is saved | Pass |

### UAT Result

**PASS**

The required reviewers can be configured successfully.

### Related Bug

`CMS-BUG-001`

---

## UAT-CMS-003 - Setting Payment Method

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-003 |
| Scenario | Verify payment method can be configured |
| Priority | High |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Open Payment Method configuration | Payment configuration is displayed | Pass |
| 2 | Select the required payment method | Payment method is selected | Pass |
| 3 | Save the configuration | Payment method is successfully saved | Pass |
| 4 | Reopen the configuration | Saved payment method is displayed | Pass |

### UAT Result

**PASS**

The payment method can be configured and saved successfully.

---

## UAT-CMS-004 - Setting Vendor Payment Account

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-004 |
| Scenario | Verify vendor payment account can be configured |
| Priority | High |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Open vendor payment account configuration | Account configuration is displayed | Pass |
| 2 | Select the vendor | Vendor information is displayed | Pass |
| 3 | Select the vendor payment account | Account is selected | Pass |
| 4 | Save the configuration | Payment account is successfully saved | Pass |
| 5 | Reopen the configuration | Selected account is displayed correctly | Pass |

### UAT Result

**PASS**

The vendor payment account can be successfully configured.

---

## UAT-CMS-005 - Generate Contract Document

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-005 |
| Scenario | Verify contract document can be generated |
| Priority | High |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Open the contract document menu | Contract document page is displayed | Pass |
| 2 | Verify contract information | Contract information is displayed correctly | Pass |
| 3 | Select Generate Contract | Contract generation process starts | Pass |
| 4 | Wait for the generation process | Contract document is generated | Pass |
| 5 | Open the generated document | Contract document can be opened | Pass |

### UAT Result

**PASS**

The system successfully generates the contract document.

---

## UAT-CMS-006 - Send Contract Document to Reviewer

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-006 |
| Scenario | Verify contract document can be sent to configured reviewers |
| Priority | Critical |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Open the generated contract document | Contract document is displayed | Pass |
| 2 | Verify reviewer configuration | Configured reviewers are displayed | Pass |
| 3 | Select Send to Reviewer | Send process is displayed | Pass |
| 4 | Confirm submission | Contract document is sent | Pass |
| 5 | Login using reviewer account | Reviewer can access CMS | Pass |
| 6 | Open reviewer task/inbox | Contract task is displayed | Pass |

### UAT Result

**PASS**

The contract document can be sent and received by the configured
reviewers.

### Related Bug

`CMS-BUG-002`

### UAT Observation

The issue has previously occurred intermittently but passed
during the latest UAT execution.

---

## UAT-CMS-007 - Reviewer Approval

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-007 |
| Scenario | Verify reviewer can approve the contract document |
| Priority | Critical |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Login using the reviewer account | Reviewer successfully logs in | Pass |
| 2 | Open the contract approval task | Contract document is displayed | Pass |
| 3 | Review the contract document | Document can be reviewed | Pass |
| 4 | Approve the contract | Approval process is executed | Pass |
| 5 | Confirm approval | Approval is successfully submitted | Pass |
| 6 | Check contract status | Approval status is updated | Pass |

### UAT Result

**PASS**

The reviewer can successfully review and approve the contract.

### Related Bug

`CMS-BUG-003`

### UAT Observation

The approval status issue has previously occurred intermittently
but passed during the latest UAT execution.

---

## UAT-CMS-008 - Final Contract E-Signature

| Field | Details |
|---|---|
| UAT ID | UAT-CMS-008 |
| Scenario | Verify Pihak 1 and Pihak 2 can perform final e-signature |
| Priority | Critical |
| Result | Pass |

### Steps

| Step | Action | Expected Result | Result |
|---|---|---|---|
| 1 | Verify all required reviewers have approved the contract | All required approvals are completed | Pass |
| 2 | Open the final contract document | Final document is displayed | Pass |
| 3 | Pihak 1 performs e-signature | Pihak 1 signature is successfully recorded | Pass |
| 4 | Pihak 2 performs e-signature | Pihak 2 signature is successfully recorded | Pass |
| 5 | Open the final contract document | Final signed document is available | Pass |
| 6 | Verify the signatures | Both signatures are displayed correctly | Pass |

### UAT Result

**PASS**

Pihak 1 and Pihak 2 can successfully perform e-signature on the
final contract document.

---

# 4. UAT Summary

| UAT ID | Scenario | Priority | Result |
|---|---|---|---|
| UAT-CMS-001 | Receive Work Package | High | Pass |
| UAT-CMS-002 | Setting Reviewer | High | Pass |
| UAT-CMS-003 | Setting Payment Method | High | Pass |
| UAT-CMS-004 | Setting Vendor Payment Account | High | Pass |
| UAT-CMS-005 | Generate Contract Document | High | Pass |
| UAT-CMS-006 | Send Contract to Reviewer | Critical | Pass |
| UAT-CMS-007 | Reviewer Approval | Critical | Pass |
| UAT-CMS-008 | Final Contract E-Signature | Critical | Pass |

---

# 5. UAT Conclusion

Based on the UAT execution, the Contract Management System
successfully supports the main contract workflow from receiving
the work package from E-Tender through final contract
e-signature.

Previously identified intermittent defects related to reviewer
configuration, contract document delivery, and reviewer approval
status were verified during testing.

The latest UAT execution passed all defined scenarios.