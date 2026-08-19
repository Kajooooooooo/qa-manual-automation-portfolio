# Bug Report - Contract Management System (CMS)

## Bug Summary

| Bug ID | Bug Title | Severity | Priority | Status |
|---|---|---|---|---|
| CMS-BUG-001 | Worker data not displayed during reviewer setting | Medium | High | Closed |
| CMS-BUG-002 | Contract document not received by reviewer | High | High | Resolved |
| CMS-BUG-003 | Reviewer approval status not updated | High | High | Closed |

---

# CMS-BUG-001

## Worker Data Not Displayed During Reviewer Setting

| Field | Details |
|---|---|
| Bug ID | CMS-BUG-001 |
| Module | Reviewer Setting |
| Severity | Medium |
| Priority | High |
| Status | Closed |
| Defect Type | Functional |
| Frequency | Intermittent / Recurring |

### Preconditions

1. User has successfully logged in to CMS.
2. A valid work package is available.
3. Reviewer Setting menu is accessible.

### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Open the CMS application |
| 2 | Open the relevant work package |
| 3 | Open Reviewer Setting |
| 4 | Select the reviewer type |
| 5 | Open the worker selection field |
| 6 | Check the available worker data |

### Expected Result

Worker data should be displayed and available for selection.

### Actual Result

Worker data is sometimes not displayed when configuring the reviewer.

### Impact

The user cannot configure the required reviewer and the contract
workflow cannot proceed to the next stage.

### Defect Characteristic

Intermittent / Recurring

### Resolution

The issue has been resolved.

### Retest Result

Passed.

---

# CMS-BUG-002

## Contract Document Not Received by Reviewer

| Field | Details |
|---|---|
| Bug ID | CMS-BUG-002 |
| Module | Contract Review |
| Severity | High |
| Priority | High |
| Status | Resolved |
| Defect Type | Workflow / Integration |
| Frequency | Intermittent / Recurring |

### Preconditions

1. Contract document has been generated.
2. Reviewer has been configured.
3. Contract document is ready to be sent.

### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Open the generated contract document |
| 2 | Verify the configured reviewers |
| 3 | Send the contract document to the reviewers |
| 4 | Confirm the submission |
| 5 | Login using the reviewer account |
| 6 | Open the reviewer task/inbox |
| 7 | Check the contract document |

### Expected Result

The contract document should be successfully delivered and
displayed in the reviewer's account.

### Actual Result

The contract document is sometimes not received or displayed
in the reviewer's account.

### Impact

The reviewer cannot review or approve the contract document,
causing delays in the contract workflow.

### Defect Characteristic

Intermittent / Recurring

### Resolution

The issue has been resolved.

### Retest Result

Passed.

### Additional Observation

The same issue may occasionally occur again after the issue
was previously resolved.

---

# CMS-BUG-003

## Reviewer Approval Status Not Updated

| Field | Details |
|---|---|
| Bug ID | CMS-BUG-003 |
| Module | Contract Approval |
| Severity | High |
| Priority | High |
| Status | Closed |
| Defect Type | Functional / Workflow |
| Frequency | Intermittent |

### Preconditions

1. Contract document has been sent to the reviewer.
2. Reviewer has access to the contract.
3. Reviewer is authorized to approve the contract.

### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Login using the reviewer account |
| 2 | Open the contract approval task |
| 3 | Review the contract document |
| 4 | Approve the contract |
| 5 | Confirm the approval |
| 6 | Return to the contract status |
| 7 | Check the reviewer approval status |

### Expected Result

The reviewer approval status should be updated to `Approved`.

### Actual Result

The reviewer successfully approves the contract, but the approval
status is sometimes not updated.

### Impact

The contract workflow may not proceed because the system still
considers the reviewer approval incomplete.

### Defect Characteristic

Intermittent

### Resolution

The issue has been resolved.

### Retest Result

Passed.

---

# Bug Statistics

| Category | Count |
|---|---:|
| Total Bugs | 3 |
| High Severity | 2 |
| Medium Severity | 1 |
| Closed | 2 |
| Resolved | 1 |
| Intermittent / Recurring | 2 |

---

# Defect Analysis

The identified CMS defects are mainly related to:

- Reviewer data availability
- Contract document delivery
- Reviewer approval status synchronization

The defects occurred intermittently, indicating that the
application workflow may experience data synchronization or
process execution issues between different CMS stages.