# User Acceptance Testing (UAT) - P-Wellness

## 1. Document Information

| Field | Details |
|---|---|
| Project | P-Wellness |
| Application | P-Wellness |
| Application URL | https://p-well.pelindo.co.id/ |
| Testing Type | User Acceptance Testing (UAT) |
| Test Environment | UAT |
| Primary Roles | Admin, User, Hospital |
| UAT Status | Completed |
| Document Status | Final |

---

## 2. UAT Objective

The objective of User Acceptance Testing is to verify that the P-Wellness application supports the expected business process from user authentication through the MCU process and delivery of MCU results to the User Dashboard.

The UAT also validates that information displayed to users is consistent with the corresponding MCU transaction data.

---

## 3. Business Flow

The P-Wellness business process consists of:

1. Admin, User, and Hospital login.
2. User creates pre-MCU data.
3. User submits pre-MCU data.
4. Hospital reviews the submitted pre-MCU data.
5. Hospital creates the MCU schedule.
6. User attends the scheduled MCU.
7. Hospital uploads the MCU result document.
8. MCU result data becomes available.
9. User views the MCU information on the dashboard.

### End-to-End Flow

```text
Login
  ↓
User Creates Pre-MCU Data
  ↓
User Submits Pre-MCU
  ↓
Hospital Reviews Pre-MCU
  ↓
Hospital Creates MCU Schedule
  ↓
User Attends MCU
  ↓
Hospital Uploads MCU Result
  ↓
MCU Result Available
  ↓
User Dashboard
```

---

## 4. UAT Scope

The following business processes are included in UAT:

- Authentication
- Pre-MCU Data Creation
- Pre-MCU Submission
- Hospital Pre-MCU Review
- MCU Scheduling
- User MCU Process
- MCU Result Upload
- User Dashboard
- Data Consistency
- Role-Based Access

---

## 5. UAT Test Scenarios

### UAT-PW-001 - User Login

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-001 |
| Business Process | Authentication |
| Role | User |
| Priority | High |
| Related Test Case | PW-TC-002 |
| Expected Result | User can successfully login and access the User Dashboard |
| Actual Result | User successfully logged in and accessed the User Dashboard |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-002 - Hospital Login

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-002 |
| Business Process | Authentication |
| Role | Hospital |
| Priority | High |
| Related Test Case | PW-TC-003 |
| Expected Result | Hospital can successfully login and access the Hospital Dashboard |
| Actual Result | Hospital successfully logged in and accessed the Hospital Dashboard |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-003 - Create and Submit Pre-MCU Data

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-003 |
| Business Process | Pre-MCU |
| Role | User |
| Priority | Critical |
| Related Test Case | PW-TC-005, PW-TC-007 |
| Expected Result | User can create and submit complete pre-MCU information |
| Actual Result | User successfully created and submitted pre-MCU information |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-004 - Hospital Reviews Pre-MCU

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-004 |
| Business Process | Pre-MCU Review |
| Role | Hospital |
| Priority | High |
| Related Test Case | PW-TC-008 |
| Expected Result | Hospital can access and review submitted pre-MCU information |
| Actual Result | Hospital successfully accessed and reviewed submitted pre-MCU information |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-005 - Create MCU Schedule

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-005 |
| Business Process | MCU Scheduling |
| Role | Hospital |
| Priority | Critical |
| Related Test Case | PW-TC-009 |
| Expected Result | Hospital can create an MCU schedule for the user |
| Actual Result | Hospital successfully created the MCU schedule |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-006 - User Views MCU Schedule

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-006 |
| Business Process | MCU Scheduling |
| Role | User |
| Priority | High |
| Related Test Case | PW-TC-010 |
| Expected Result | User can view the correct MCU schedule |
| Actual Result | User successfully viewed the MCU schedule |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-007 - User Completes MCU

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-007 |
| Business Process | MCU |
| Role | User |
| Priority | High |
| Related Test Case | PW-TC-011 |
| Expected Result | User can complete the MCU process according to the scheduled appointment |
| Actual Result | User successfully completed the MCU process |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-008 - Hospital Uploads MCU Result

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-008 |
| Business Process | MCU Result |
| Role | Hospital |
| Priority | Critical |
| Related Test Case | PW-TC-012 |
| Expected Result | Hospital can successfully upload and submit MCU result documents |
| Actual Result | Hospital successfully uploaded and submitted the MCU result document |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-009 - User Views MCU Result

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-009 |
| Business Process | User Dashboard |
| Role | User |
| Priority | Critical |
| Related Test Case | PW-TC-013 |
| Expected Result | User can view the MCU result on the dashboard |
| Actual Result | User successfully viewed the MCU result on the dashboard |
| Status | PASS |
| Remarks | - |

---

### UAT-PW-010 - Validate Dashboard Data Consistency

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-010 |
| Business Process | Data Consistency |
| Role | User / Hospital |
| Priority | Critical |
| Related Test Case | PW-TC-014 |
| Expected Result | Dashboard data matches the corresponding MCU transaction data |
| Actual Result | Dashboard data was found to be inconsistent with the corresponding source data |
| Status | FAIL |
| Remarks | Related to PW-BUG-001 |

---

### UAT-PW-011 - Role-Based Access

| Field | Details |
|---|---|
| Scenario ID | UAT-PW-011 |
| Business Process | Authorization |
| Role | Admin / User / Hospital |
| Priority | High |
| Related Test Case | PW-TC-015 |
| Expected Result | Each role can access only authorized functions |
| Actual Result | Each role can access functions according to the assigned permissions |
| Status | PASS |
| Remarks | - |

---

## 6. UAT Execution Summary

| Scenario ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| UAT-PW-001 | User Login | Successful login | Successfully logged in | PASS |
| UAT-PW-002 | Hospital Login | Successful login | Successfully logged in | PASS |
| UAT-PW-003 | Create & Submit Pre-MCU | Data submitted successfully | Successfully submitted | PASS |
| UAT-PW-004 | Hospital Reviews Pre-MCU | Data can be reviewed | Successfully reviewed | PASS |
| UAT-PW-005 | Create MCU Schedule | Schedule created successfully | Successfully created | PASS |
| UAT-PW-006 | View MCU Schedule | Correct schedule displayed | Correct schedule displayed | PASS |
| UAT-PW-007 | Complete MCU | MCU completed successfully | Successfully completed | PASS |
| UAT-PW-008 | Upload MCU Result | Result uploaded successfully | Successfully uploaded | PASS |
| UAT-PW-009 | View MCU Result | Result displayed correctly | Result displayed | PASS |
| UAT-PW-010 | Dashboard Data Consistency | Data matches source | Data did not always match source | FAIL |
| UAT-PW-011 | Role-Based Access | Access follows role permissions | Access follows assigned permissions | PASS |

---

## 7. UAT Result Summary

| Result | Count |
|---|---:|
| PASS | 10 |
| FAIL | 1 |
| Total | 11 |

### UAT Completion Rate

**90.91%**

Calculation:

```text
10 Passed / 11 Total × 100 = 90.91%
```

---

## 8. Failed UAT Scenario

### UAT-PW-010 - Validate Dashboard Data Consistency

The dashboard data was found to be inconsistent with the corresponding MCU transaction data.

#### Expected Result

The data displayed on the User Dashboard should match the corresponding source transaction.

#### Actual Result

The dashboard may display different information from the corresponding source transaction.

#### Impact

The issue can cause users to view inaccurate MCU information and affects data consistency between the transaction and dashboard.

#### Related Bug

`PW-BUG-001 - User Dashboard Data Does Not Match Source Data`

---

## 9. UAT Acceptance Criteria

The P-Wellness application is considered acceptable when:

- Users can successfully login.
- Hospital users can successfully login.
- Users can create and submit pre-MCU data.
- Hospital users can review pre-MCU data.
- Hospital users can create MCU schedules.
- Users can view MCU schedules.
- Users can complete the MCU process.
- Hospital users can upload MCU results.
- Users can view MCU results.
- Role-based access works according to assigned permissions.
- Dashboard information accurately reflects the corresponding MCU transaction data.

The identified dashboard data inconsistency remains an issue that requires resolution and regression testing before the application is considered fully accepted.

---

## 10. Known Defect

### PW-BUG-001 - User Dashboard Data Does Not Match Source Data

| Field | Details |
|---|---|
| Bug ID | PW-BUG-001 |
| Severity | High |
| Priority | High |
| Status | Open |
| Frequency | Intermittent |
| Module | User Dashboard |
| Impact | Data consistency issue |

The defect is linked to:

- `PW-TC-013`
- `PW-TC-014`
- `UAT-PW-010`

---

## 11. UAT Sign-Off

| Role | Name | Status | Date | Signature |
|---|---|---|---|---|
| QA Tester | - | Pending | - | - |
| Business/User Representative | - | Pending | - | - |
| Hospital Representative | - | Pending | - | - |
| Project/Business Owner | - | Pending | - | - |

---

## 12. UAT Conclusion

Based on the UAT execution, the majority of the core P-Wellness business processes can be completed successfully.

10 out of 11 UAT scenarios passed, while 1 scenario failed due to an intermittent data consistency issue on the User Dashboard.

The identified defect is documented as:

`PW-BUG-001 - User Dashboard Data Does Not Match Source Data`

The defect should be resolved and regression tested before the application is considered fully accepted.