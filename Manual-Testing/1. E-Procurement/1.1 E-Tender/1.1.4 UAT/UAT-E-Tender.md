# User Acceptance Test (UAT) - E-Tender

## 1. UAT Overview

### 1.1 Objective

The objective of this UAT is to verify that the E-Tender application
supports the required procurement business process and meets the
defined business expectations.

The UAT validates the end-to-end E-Tender process from user
authentication through tender winner determination.

### 1.2 Scope

The UAT covers:

- User Authentication
- OTP Verification
- Application Role Selection
- Work Package Creation
- Work Package Publication
- Vendor Registration
- Vendor Registration Evaluation
- Clarification Session
- Bid Document Submission
- Bid Document Opening
- Bid Document Evaluation
- Negotiation
- Winner Determination

---

# 2. UAT Environment

| Item | Details |
|---|---|
| Application | E-Procurement |
| Module | E-Tender |
| Environment | UAT / Test |
| Browser | Google Chrome |
| Operating System | Windows |
| Testing Type | User Acceptance Testing |

---

# 3. UAT Participants

| Role | Responsibility |
|---|---|
| Business User | Validate business requirements and process |
| Procurement User | Validate procurement workflow |
| Vendor User | Validate vendor-side activities |
| QA | Execute testing and document results |
| Developer | Investigate and resolve defects |

---

# 4. UAT Entry Criteria

UAT can begin when:

- Required E-Tender functionality is available.
- UAT environment is accessible.
- Required test accounts are available.
- Required test data is available.
- Critical system configuration is completed.
- Major blocking defects have been addressed or formally accepted.

---

# 5. UAT Scenarios

## UAT-ET-001 - User Login

### Business Objective

Verify that an authorized user can access the E-Procurement application
using valid credentials.

### Precondition

- Valid user account is available.
- Application is accessible.

### Steps

1. Open the E-Procurement application.
2. Enter valid username.
3. Enter valid password.
4. Click Login.
5. Complete the authentication process.

### Expected Result

The user can successfully authenticate and proceed to the next
authentication stage.

### Related Test Case

`ET-TC-001`

### Status

Pending

---

# UAT-ET-002 - OTP Verification

### Business Objective

Verify that the OTP authentication process works correctly.

### Precondition

User has successfully submitted valid username and password.

### Steps

1. Open the OTP verification page.
2. Retrieve the OTP from the registered email.
3. Enter the OTP.
4. Submit the OTP.

### Expected Result

The system validates the OTP and allows the user to proceed.

### Related Test Case

`ET-TC-003`

### Related Bug

`ET-BUG-001`

### Status

Pending

---

# UAT-ET-003 - Application Role Selection

### Business Objective

Verify that users can access the application using their authorized role.

### Precondition

User has successfully completed authentication.

### Steps

1. Open the role selection page.
2. Select the authorized application role.
3. Click the selection/confirmation button.

### Expected Result

The selected role is successfully activated and the user can access
the E-Procurement application.

### Related Test Case

`ET-TC-006`

### Status

Pending

---

# UAT-ET-004 - Work Package Creation

### Business Objective

Verify that procurement users can create a work package according
to the business requirements.

### Precondition

User has permission to create a work package.

### Steps

1. Open the E-Tender module.
2. Select the work package creation function.
3. Enter the required information.
4. Submit the work package.

### Expected Result

The work package is successfully created with the correct information.

### Related Test Case

`ET-TC-007`

### Status

Pending

---

# UAT-ET-005 - Work Package Publication

### Business Objective

Verify that an eligible work package can be published.

### Precondition

A valid work package has been created.

### Steps

1. Open the work package.
2. Review the package information.
3. Select Publish.
4. Confirm the publication.

### Expected Result

The work package is successfully published and becomes available
according to the configured business rules.

### Related Test Case

`ET-TC-009`

### Status

Pending

---

# UAT-ET-006 - Vendor Registration

### Business Objective

Verify that an eligible vendor can participate in a published
work package.

### Precondition

- Work package has been published.
- Vendor is eligible to participate.

### Steps

1. Login using a valid vendor account.
2. Open the published work package.
3. Select the registration function.
4. Submit the registration.

### Expected Result

Vendor registration is successfully submitted and recorded by the system.

### Related Test Case

`ET-TC-010`

### Status

Pending

---

# UAT-ET-007 - Vendor Registration Evaluation

### Business Objective

Verify that procurement users can evaluate vendor registrations.

### Precondition

Vendor registration has been submitted.

### Steps

1. Login using an authorized procurement account.
2. Open the vendor registration evaluation.
3. Review vendor information.
4. Approve or reject the registration.

### Expected Result

The registration result is recorded correctly and the vendor status
is updated accordingly.

### Related Test Cases

`ET-TC-011`

`ET-TC-012`

### Status

Pending

---

# UAT-ET-008 - Clarification Session

### Business Objective

Verify that the clarification process can be conducted according
to the procurement workflow.

### Precondition

- Work package has been published.
- Eligible vendors have registered.

### Steps

1. Open the clarification session.
2. Enter clarification information.
3. Submit the clarification.
4. Review the submitted information.

### Expected Result

Clarification information is successfully recorded and available
to authorized participants.

### Related Test Case

`ET-TC-013`

### Status

Pending

---

# UAT-ET-009 - Bid Document Submission

### Business Objective

Verify that eligible vendors can submit the required bid documents.

### Precondition

- Vendor has been approved.
- Bid submission period is available.
- Required documents are available.

### Steps

1. Login using the vendor account.
2. Open the relevant work package.
3. Open the bid submission page.
4. Upload the required documents.
5. Submit the bid.

### Expected Result

Required bid documents are successfully uploaded and submitted.

### Related Test Case

`ET-TC-014`

### Related Bug

`ET-BUG-002`

### Status

Pending

---

# UAT-ET-010 - Bid Document Opening

### Business Objective

Verify that authorized procurement users can access submitted
bid documents.

### Precondition

Vendors have submitted their bid documents.

### Steps

1. Login using an authorized procurement account.
2. Open the relevant work package.
3. Navigate to the bid document opening stage.
4. Select a submitted bid document.
5. Open the document.

### Expected Result

The authorized user can successfully access and open the
submitted bid document.

### Related Test Case

`ET-TC-015`

### Related Bug

`ET-BUG-003`

### Status

Pending

---

# UAT-ET-011 - Bid Document Evaluation

### Business Objective

Verify that submitted bid documents can be evaluated according
to the defined procurement process.

### Precondition

- Bid documents have been submitted.
- Bid opening process has been completed.
- Evaluation stage is available.

### Steps

1. Login using an authorized evaluator account.
2. Open the relevant work package.
3. Navigate to the evaluation stage.
4. Select the vendor.
5. Review submitted documents.
6. Enter evaluation results.
7. Submit the evaluation.

### Expected Result

The evaluator can access the required bid data, complete the
evaluation, and submit the evaluation result successfully.

### Related Test Case

`ET-TC-016`

### Related Bugs

`ET-BUG-004`

`ET-BUG-005`

### Status

Pending

---

# UAT-ET-012 - Negotiation

### Business Objective

Verify that the negotiation process can be completed according
to the defined procurement workflow.

### Precondition

Required evaluation process has been completed.

### Steps

1. Open the negotiation stage.
2. Select the relevant vendor.
3. Enter negotiation information.
4. Submit the negotiation.
5. Review the negotiation result.

### Expected Result

The negotiation is successfully completed and the result is
recorded correctly.

### Related Test Case

`ET-TC-017`

### Status

Pending

---

# UAT-ET-013 - Winner Determination

### Business Objective

Verify that the authorized procurement user can determine
the tender winner based on the evaluation and negotiation results.

### Precondition

- Evaluation process has been completed.
- Negotiation process has been completed.
- Eligible vendor is available for winner determination.

### Steps

1. Open the winner determination stage.
2. Review evaluation results.
3. Review negotiation results.
4. Select the eligible winning vendor.
5. Submit the winner determination.

### Expected Result

The winning vendor is successfully determined and the tender
status is updated correctly.

### Related Test Case

`ET-TC-018`

### Status

Pending

---

# 6. UAT Execution Summary

| UAT ID | Scenario | Result | Remarks |
|---|---|---|---|
| UAT-ET-001 | User Login | Pending | |
| UAT-ET-002 | OTP Verification | Pending | ET-BUG-001 |
| UAT-ET-003 | Role Selection | Pending | |
| UAT-ET-004 | Work Package Creation | Pending | |
| UAT-ET-005 | Work Package Publication | Pending | |
| UAT-ET-006 | Vendor Registration | Pending | |
| UAT-ET-007 | Registration Evaluation | Pending | |
| UAT-ET-008 | Clarification Session | Pending | |
| UAT-ET-009 | Bid Document Submission | Pending | ET-BUG-002 |
| UAT-ET-010 | Bid Document Opening | Pending | ET-BUG-003 |
| UAT-ET-011 | Bid Document Evaluation | Pending | ET-BUG-004, ET-BUG-005 |
| UAT-ET-012 | Negotiation | Pending | |
| UAT-ET-013 | Winner Determination | Pending | |

---

# 7. UAT Result Summary

| Metric | Result |
|---|---:|
| Total UAT Scenarios | 13 |
| Passed | - |
| Failed | - |
| Blocked | - |
| Pending | 13 |
| Overall Result | Pending |

---

# 8. Defect Summary

| Bug ID | Description | Severity | Status |
|---|---|---|---|
| ET-BUG-001 | OTP is not received via email | High | Intermittent / Recurring |
| ET-BUG-002 | Bid document cannot be uploaded | High | Intermittent / Recurring |
| ET-BUG-003 | Bid document cannot be opened | High | Intermittent / Recurring |
| ET-BUG-004 | Bid document data is not available during evaluation | Critical | Intermittent / Recurring |
| ET-BUG-005 | Evaluation status is not updated | High | Intermittent / Recurring |

---

# 9. UAT Exit Criteria

UAT can be considered completed when:

- All planned UAT scenarios have been executed.
- Critical business processes have been validated.
- Critical defects have been resolved or formally accepted.
- Failed scenarios have been retested.
- Required regression testing has been completed.
- Business users have reviewed the results.
- Business users approve the system for the intended release.

---

# 10. UAT Acceptance

## Overall UAT Result

**Pending**

## Acceptance Decision

- [ ] Accepted
- [ ] Accepted with Conditions
- [ ] Rejected
- [ ] Pending Retest

## Sign-Off

| Role | Name | Date | Signature | Decision |
|---|---|---|---|---|
| Business User | - | - | - | Pending |
| Procurement User | - | - | - | Pending |
| QA | - | - | - | Pending |
| Project / Product Owner | - | - | - | Pending |