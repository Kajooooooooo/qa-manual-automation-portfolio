# Bug Report - E-Tender

## Bug Summary

The following defects were identified during E-Tender functional testing. 
Some defects may occur intermittently and can reoccur after being resolved, 
therefore verification and regression testing are required.

---

# ET-BUG-001 - OTP Not Received via Email

| Field | Details |
|---|---|
| Bug ID | ET-BUG-001 |
| Title | OTP is not received via registered email during login |
| Module | E-Tender / Authentication |
| Severity | High |
| Priority | High |
| Environment | Test / Development |
| Browser | Google Chrome |
| Status | Intermittent / Recurring |
| Reporter | QA |

## Description

The OTP required during the login process is sometimes not received 
through the user's registered email address.

The issue does not occur consistently and may reoccur during subsequent 
testing cycles.

## Preconditions

- A valid user account is available.
- The user account has a registered email address.
- The application is accessible.
- The email service is available.

## Steps to Reproduce

1. Open the E-Procurement application.
2. Enter a valid username.
3. Enter a valid password.
4. Click the Login button.
5. Wait for the OTP verification page.
6. Check the registered email inbox.
7. If the OTP is not received, request another OTP.
8. Repeat the login process during another test cycle.

## Expected Result

The system should send an OTP to the user's registered email address 
within the expected time.

## Actual Result

The OTP is sometimes not received through the registered email address.

## Impact

The issue prevents the user from completing the authentication process 
and accessing the application.

## Defect History

The issue has been observed intermittently during testing. 
The defect may be resolved after a fix but can reoccur during subsequent 
testing or regression testing.

## Recommendation

Perform investigation on the OTP generation and email delivery process 
and perform regression testing after the fix.

## Test Case Reference

ET-TC-005

---

# ET-BUG-002 - Bid Document Cannot Be Uploaded

| Field | Details |
|---|---|
| Bug ID | ET-BUG-002 |
| Title | Vendor cannot upload bid document |
| Module | E-Tender / Bid Submission |
| Severity | High |
| Priority | High |
| Environment | Test / Development |
| Browser | Google Chrome |
| Status | Intermittent / Recurring |
| Reporter | QA |

## Description

The vendor is sometimes unable to upload the required bid document 
during the bid submission process.

## Preconditions

- Vendor account is available.
- Vendor is eligible to participate in the tender.
- Work package is available for bid submission.
- Valid bid document is available.

## Steps to Reproduce

1. Login using a valid vendor account.
2. Open the relevant E-Tender package.
3. Navigate to the bid submission page.
4. Select the required bid document.
5. Upload the document.
6. Submit the bid document.
7. Verify the upload result.

## Expected Result

The bid document should be uploaded successfully and displayed in 
the bid submission section.

## Actual Result

The bid document cannot be uploaded successfully.

## Impact

The vendor may be unable to complete the bid submission process 
within the available tender period.

## Defect History

The issue has been observed during testing and may reoccur after 
the issue is considered resolved.

## Recommendation

Verify the document upload process, file validation, server-side 
processing, and related application logs. Perform regression testing 
after the fix.

## Test Case Reference

ET-TC-008

---

# ET-BUG-003 - Bid Document Cannot Be Opened

| Field | Details |
|---|---|
| Bug ID | ET-BUG-003 |
| Title | Submitted bid document cannot be opened |
| Module | E-Tender / Bid Opening |
| Severity | High |
| Priority | High |
| Environment | Test / Development |
| Browser | Google Chrome |
| Status | Intermittent / Recurring |
| Reporter | QA |

## Description

An authorized user is sometimes unable to open a submitted bid document 
during the bid document opening process.

## Preconditions

- Vendor has submitted a bid document.
- Bid document submission has been completed.
- User has authorization to access the submitted document.

## Steps to Reproduce

1. Login using an authorized procurement account.
2. Open the relevant E-Tender package.
3. Navigate to the bid document opening section.
4. Select the submitted bid document.
5. Attempt to open the document.
6. Repeat the process during another test cycle.

## Expected Result

The submitted bid document should be opened successfully.

## Actual Result

The submitted bid document cannot be opened.

## Impact

The procurement process may be blocked because the submitted 
bid document cannot be reviewed.

## Defect History

The issue may be resolved after a fix but can reoccur during 
subsequent testing or regression testing.

## Recommendation

Verify document storage, document retrieval, access permissions, 
and document preview/download functionality.

## Test Case Reference

ET-TC-009

---

# ET-BUG-004 - Bid Document Data Not Available for Evaluation

| Field | Details |
|---|---|
| Bug ID | ET-BUG-004 |
| Title | Submitted bid document data is not displayed during evaluation |
| Module | E-Tender / Bid Evaluation |
| Severity | Critical |
| Priority | High |
| Environment | Test / Development |
| Browser | Google Chrome |
| Status | Intermittent / Recurring |
| Reporter | QA |

## Description

Submitted bid document data is sometimes not available in the 
bid evaluation stage after the bid opening process has been completed.

## Preconditions

- Vendor has successfully submitted a bid document.
- Bid document opening process has been completed.
- Evaluation stage is available.
- Evaluator has the required authorization.

## Steps to Reproduce

1. Login using an authorized evaluator account.
2. Open the relevant E-Tender package.
3. Navigate to the bid evaluation section.
4. Select a vendor that has submitted a bid.
5. Review the submitted bid document data.
6. Repeat the process during another testing cycle.

## Expected Result

The submitted bid document data should be available and displayed 
correctly in the evaluation stage.

## Actual Result

The submitted bid document data is not displayed in the evaluation stage.

## Impact

The evaluator cannot perform the required evaluation, which may 
block the E-Tender process.

## Defect History

The issue has been observed during testing and may reoccur after 
being resolved.

## Recommendation

Verify data synchronization between bid submission, bid opening, 
and bid evaluation stages. Perform end-to-end regression testing 
after the fix.

## Test Case Reference

ET-TC-010

---

# ET-BUG-005 - Evaluation Status Not Updated

| Field | Details |
|---|---|
| Bug ID | ET-BUG-005 |
| Title | Evaluation status is not updated after evaluation submission |
| Module | E-Tender / Bid Evaluation |
| Severity | High |
| Priority | High |
| Environment | Test / Development |
| Browser | Google Chrome |
| Status | Intermittent / Recurring |
| Reporter | QA |

## Description

The evaluation status is sometimes not updated after the evaluator 
successfully submits the evaluation result.

## Preconditions

- Bid document evaluation is available.
- Evaluator has the required authorization.
- Required evaluation data is available.

## Steps to Reproduce

1. Login using an authorized evaluator account.
2. Open the relevant E-Tender package.
3. Navigate to the evaluation section.
4. Select the relevant vendor.
5. Complete the required evaluation.
6. Submit the evaluation result.
7. Refresh or reopen the evaluation page.
8. Check the evaluation status.

## Expected Result

The evaluation status should be updated according to the submitted 
evaluation result.

## Actual Result

The evaluation status is sometimes not updated after the evaluation 
is submitted.

## Impact

Incorrect evaluation status may affect the subsequent E-Tender 
workflow and can cause inconsistencies between the evaluation 
result and the displayed process status.

## Defect History

The issue has been observed intermittently during testing. 
Although the issue may be resolved after a fix, the same behavior 
can reoccur during subsequent testing or regression testing.

## Recommendation

Verify the status update mechanism and data synchronization after 
evaluation submission. Perform regression testing across the 
complete evaluation workflow.

## Test Case Reference

ET-TC-010

---

# Defect Lifecycle

The defects documented above may follow the following lifecycle:

Found
→ Reported
→ Assigned
→ Fixed
→ Retested
→ Closed

If the defect occurs again:

Resolved
→ Regression Testing
→ Defect Reoccurs
→ Reopened
→ Fixed
→ Retested

## Defect Status Definitions

| Status | Description |
|---|---|
| Open | Defect has been reported and is awaiting investigation or fixing |
| In Progress | Defect is currently being investigated or fixed |
| Resolved | Developer has implemented a fix and the defect is ready for retesting |
| Closed | QA has verified the fix and confirmed that the defect no longer occurs |
| Reopened | Previously resolved or closed defect has occurred again |
| Intermittent | Defect occurs inconsistently and cannot always be reproduced |
| Recurring | Previously resolved defect occurs again during subsequent testing |

## Severity Definitions

| Severity | Description |
|---|---|
| Critical | Defect blocks a critical business process or makes the system unusable |
| High | Defect significantly affects an important business function |
| Medium | Defect affects functionality but a workaround may be available |
| Low | Minor functional or UI issue with limited business impact |
