# User Acceptance Test (UAT) - Vendor Payment

## 1. UAT Information

| Field | Details |
|---|---|
| Application | E-Procurement |
| Module | Vendor Payment |
| UAT Type | Business Process Validation |
| Test Objective | Validate the Vendor Payment business process from PO integration through payment completion |
| Environment | UAT |
| Test Role | User / Vendor |
| Integration | SAP |
| UAT Status | Completed |

---

# 2. UAT Objective

The objective of this UAT is to verify that the Vendor Payment
module supports the expected business process from the integration
of an approved Purchase Order (PO) from SAP through payment
processing and the creation of the Payment Minutes.

The UAT also validates the integration between Vendor Payment and
SAP throughout the payment process.

---

# 3. Business Process

The Vendor Payment business process consists of:

1. CMS user submits a PO to SAP.
2. PO is approved in SAP.
3. Approved PO data is received by Vendor Payment.
4. User creates a Vendor Payment draft.
5. User configures the required personnel.
6. User creates the Start Work Minutes.
7. User creates the Handover Minutes.
8. User creates Progress Minutes when required.
9. User performs GR / SES acceptance.
10. Vendor submits billing documents.
11. User approves billing documents.
12. User creates the Payment Memorandum.
13. User and vendor perform the required approval.
14. Payment is processed through SAP.
15. User creates the Payment Minutes after successful payment.

---

# 4. UAT Scenarios

## VP-UAT-001 - PO Integration from SAP

| Field | Details |
|---|---|
| UAT ID | VP-UAT-001 |
| Scenario | Verify approved PO data from SAP is received by Vendor Payment |
| Priority | Critical |
| Type | Integration |
| Preconditions | PO has been submitted and approved in SAP |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Submit PO from CMS to SAP | PO is successfully submitted | PASS |
| 2 | Approve the PO in SAP | PO is successfully approved | PASS |
| 3 | Open Vendor Payment | Vendor Payment module is accessible | PASS |
| 4 | Check incoming PO data | Approved PO data is available | PASS |

### Expected Result

Approved PO data from SAP is successfully received by Vendor
Payment.

---

# VP-UAT-002 - Create Vendor Payment Draft

| Field | Details |
|---|---|
| UAT ID | VP-UAT-002 |
| Scenario | Verify user can create a Vendor Payment draft |
| Priority | High |
| Type | Functional |
| Preconditions | Approved PO data is available |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open the available PO | PO information is displayed | PASS |
| 2 | Select the Vendor Payment process | Vendor Payment form is displayed | PASS |
| 3 | Create a payment draft | Draft is successfully created | PASS |
| 4 | Save the transaction | Draft data is stored correctly | PASS |

### Expected Result

User can successfully create and save a Vendor Payment draft.

---

# VP-UAT-003 - Configure Personnel

| Field | Details |
|---|---|
| UAT ID | VP-UAT-003 |
| Scenario | Verify user can configure user and vendor personnel |
| Priority | High |
| Type | Functional |
| Preconditions | Vendor Payment draft has been created |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open personnel configuration | Personnel configuration page is displayed | PASS |
| 2 | Add user personnel | User personnel is successfully added | PASS |
| 3 | Add vendor personnel | Vendor personnel is successfully added | PASS |
| 4 | Save personnel configuration | Personnel data is saved correctly | PASS |

### Expected Result

Required user and vendor personnel are successfully configured.

---

# VP-UAT-004 - Create Start Work Minutes

| Field | Details |
|---|---|
| UAT ID | VP-UAT-004 |
| Scenario | Verify user can create Start Work Minutes |
| Priority | High |
| Type | Functional |
| Preconditions | Vendor Payment personnel have been configured |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open Start Work Minutes | Form is displayed | PASS |
| 2 | Enter required information | Data is accepted | PASS |
| 3 | Submit the Start Work Minutes | Document is successfully created | PASS |
| 4 | Verify document status | Status is updated correctly | PASS |

### Expected Result

Start Work Minutes is successfully created and recorded.

---

# VP-UAT-005 - Create Handover Minutes

| Field | Details |
|---|---|
| UAT ID | VP-UAT-005 |
| Scenario | Verify user can create Handover Minutes |
| Priority | High |
| Type | Functional |
| Preconditions | Required work process has been completed |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open Handover Minutes | Form is displayed | PASS |
| 2 | Enter required information | Data is accepted | PASS |
| 3 | Submit the document | Handover Minutes is created | PASS |
| 4 | Verify document status | Status is updated correctly | PASS |

### Expected Result

Handover Minutes is successfully created.

---

# VP-UAT-006 - Create Progress Minutes

| Field | Details |
|---|---|
| UAT ID | VP-UAT-006 |
| Scenario | Verify user can record work progress |
| Priority | Medium |
| Type | Functional |
| Preconditions | Vendor Payment requires progress-based reporting |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open Progress Minutes | Progress form is displayed | PASS |
| 2 | Enter progress information | Progress data is accepted | PASS |
| 3 | Submit the progress | Progress data is successfully recorded | PASS |
| 4 | Verify progress information | Recorded progress is displayed correctly | PASS |

### Expected Result

User can record work progress through Progress Minutes.

---

# VP-UAT-007 - GR / SES Acceptance

| Field | Details |
|---|---|
| UAT ID | VP-UAT-007 |
| Scenario | Verify user can perform GR / SES acceptance |
| Priority | Critical |
| Type | Integration |
| Preconditions | Required work documentation has been completed |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open GR / SES process | GR / SES page is displayed | PASS |
| 2 | Enter required acceptance information | Data is accepted | PASS |
| 3 | Submit GR / SES | Transaction is submitted | PASS |
| 4 | Process SAP integration | SAP processes the transaction | PASS |
| 5 | Verify transaction status | GR / SES status is updated correctly | PASS |

### Expected Result

GR / SES is successfully processed and integrated with SAP.

### Known Issue

The GR / SES process may occasionally fail due to SAP integration
issues.

### Related Bug

`VP-BUG-002`

---

# VP-UAT-008 - Vendor Billing Document Submission

| Field | Details |
|---|---|
| UAT ID | VP-UAT-008 |
| Scenario | Verify vendor can submit billing documents |
| Priority | High |
| Type | Functional |
| Preconditions | GR / SES has been successfully processed |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Login using vendor account | Vendor successfully logs in | PASS |
| 2 | Open the Vendor Payment transaction | Transaction is displayed | PASS |
| 3 | Open billing document submission | Submission page is displayed | PASS |
| 4 | Upload required billing documents | Documents are uploaded successfully | PASS |
| 5 | Submit the billing documents | Documents are successfully submitted | PASS |
| 6 | Verify status | Billing status is updated | PASS |

### Expected Result

Vendor can successfully submit the required billing documents.

---

# VP-UAT-009 - Approve Billing Documents

| Field | Details |
|---|---|
| UAT ID | VP-UAT-009 |
| Scenario | Verify user can approve submitted billing documents |
| Priority | High |
| Type | Functional |
| Preconditions | Vendor has submitted billing documents |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open billing document approval | Approval page is displayed | PASS |
| 2 | Review submitted documents | Documents are available | PASS |
| 3 | Approve the documents | Approval is successfully processed | PASS |
| 4 | Verify status | Billing status is updated to approved | PASS |

### Expected Result

Billing documents are successfully approved.

---

# VP-UAT-010 - Create Payment Memorandum

| Field | Details |
|---|---|
| UAT ID | VP-UAT-010 |
| Scenario | Verify user can create Payment Memorandum |
| Priority | High |
| Type | Functional |
| Preconditions | Billing documents have been approved |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open Payment Memorandum | Payment Memorandum page is displayed | PASS |
| 2 | Create Payment Memorandum | Document is generated | PASS |
| 3 | Verify payment information | Payment information is displayed correctly | PASS |
| 4 | Submit the document for approval | Document is submitted successfully | PASS |

### Expected Result

Payment Memorandum is successfully created and submitted for
approval.

---

# VP-UAT-011 - Payment Memorandum Approval

| Field | Details |
|---|---|
| UAT ID | VP-UAT-011 |
| Scenario | Verify required parties can approve Payment Memorandum |
| Priority | Critical |
| Type | Functional |
| Preconditions | Payment Memorandum has been submitted |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open Payment Memorandum | Document is available | PASS |
| 2 | User reviews the document | Document can be reviewed | PASS |
| 3 | User performs approval | User approval is recorded | PASS |
| 4 | Vendor performs approval | Vendor approval is recorded | PASS |
| 5 | Verify approval status | Approval status is updated correctly | PASS |

### Expected Result

All required parties can successfully approve the Payment
Memorandum.

### Known Issue

Approval may occasionally fail even though the issue has previously
been resolved.

### Related Bug

`VP-BUG-001`

---

# VP-UAT-012 - Process Payment Through SAP

| Field | Details |
|---|---|
| UAT ID | VP-UAT-012 |
| Scenario | Verify approved payment can be processed through SAP |
| Priority | Critical |
| Type | Integration |
| Preconditions | Payment Memorandum has been fully approved |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open approved payment transaction | Payment information is displayed | PASS |
| 2 | Submit payment for processing | Payment is submitted | PASS |
| 3 | Send payment transaction to SAP | Transaction is sent successfully | PASS |
| 4 | Process payment in SAP | SAP processes the payment | PASS |
| 5 | Verify payment status | Payment status is updated correctly | PASS |

### Expected Result

Payment is successfully processed through SAP.

### Known Issue

Payment submission may occasionally fail during the payment
process.

### Related Bug

`VP-BUG-003`

---

# VP-UAT-013 - Create Payment Minutes

| Field | Details |
|---|---|
| UAT ID | VP-UAT-013 |
| Scenario | Verify user can create Payment Minutes after successful payment |
| Priority | High |
| Type | Functional |
| Preconditions | Payment has been successfully completed |

### Steps

| Step | Action | Expected Result | Status |
|---|---|---|---|
| 1 | Open the completed payment transaction | Payment information is displayed | PASS |
| 2 | Select Payment Minutes | Payment Minutes form is displayed | PASS |
| 3 | Generate Payment Minutes | Document is successfully generated | PASS |
| 4 | Verify payment information | Information is displayed correctly | PASS |
| 5 | Save the document | Payment Minutes is successfully stored | PASS |

### Expected Result

Payment Minutes is successfully created after the payment has been
completed.

---

# 5. UAT Summary

| UAT ID | Scenario | Priority | Result |
|---|---|---|---|
| VP-UAT-001 | PO Integration from SAP | Critical | PASS |
| VP-UAT-002 | Create Vendor Payment Draft | High | PASS |
| VP-UAT-003 | Configure Personnel | High | PASS |
| VP-UAT-004 | Create Start Work Minutes | High | PASS |
| VP-UAT-005 | Create Handover Minutes | High | PASS |
| VP-UAT-006 | Create Progress Minutes | Medium | PASS |
| VP-UAT-007 | GR / SES Acceptance | Critical | PASS* |
| VP-UAT-008 | Vendor Billing Document Submission | High | PASS |
| VP-UAT-009 | Approve Billing Documents | High | PASS |
| VP-UAT-010 | Create Payment Memorandum | High | PASS |
| VP-UAT-011 | Payment Memorandum Approval | Critical | PASS* |
| VP-UAT-012 | Process Payment Through SAP | Critical | PASS* |
| VP-UAT-013 | Create Payment Minutes | High | PASS |

> *PASS indicates the main business flow can be completed, while
> the related intermittent defects remain documented in the Bug
> Report.

---

# 6. UAT Coverage

The UAT covers the complete Vendor Payment business process:

- SAP PO Integration
- Vendor Payment Drafting
- Personnel Configuration
- Start Work Minutes
- Handover Minutes
- Progress Minutes
- GR / SES Acceptance
- Vendor Billing Document Submission
- Billing Document Approval
- Payment Memorandum
- Payment Memorandum Approval
- SAP Payment Processing
- Payment Minutes

---

# 7. UAT Conclusion

The Vendor Payment module supports the expected end-to-end
business process from SAP PO integration through payment
completion.

The main business flow can be executed successfully. However,
intermittent issues remain around approval, SAP integration during
GR / SES processing, and payment submission.

These issues should be monitored during regression and integration
testing to ensure they do not recur in the production environment.