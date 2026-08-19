# Test Cases - P-Wellness

## 1. Authentication & Authorization

---

### PW-TC-001 - Admin Login with Valid Credential

| Field | Details |
|---|---|
| Test Case ID | PW-TC-001 |
| Test Scenario | Verify admin can login using valid credentials |
| Module | Authentication |
| Priority | High |
| Test Type | Positive |
| Precondition | Valid admin account is available |
| Test Data | Valid admin username and password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the P-Wellness login page | Login page is displayed |
| 2 | Enter a valid admin username | Username is accepted |
| 3 | Enter a valid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the application | Admin dashboard is displayed |

#### Expected Result

Admin is successfully authenticated and redirected to the
appropriate dashboard.

---

### PW-TC-002 - User Login with Valid Credential

| Field | Details |
|---|---|
| Test Case ID | PW-TC-002 |
| Test Scenario | Verify user can login using valid credentials |
| Module | Authentication |
| Priority | High |
| Test Type | Positive |
| Precondition | Valid user account is available |
| Test Data | Valid user username and password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the P-Wellness login page | Login page is displayed |
| 2 | Enter a valid user username | Username is accepted |
| 3 | Enter a valid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the application | User dashboard is displayed |

#### Expected Result

User is successfully authenticated and redirected to the user
dashboard.

---

### PW-TC-003 - Hospital Login with Valid Credential

| Field | Details |
|---|---|
| Test Case ID | PW-TC-003 |
| Test Scenario | Verify hospital can login using valid credentials |
| Module | Authentication |
| Priority | High |
| Test Type | Positive |
| Precondition | Valid hospital account is available |
| Test Data | Valid hospital username and password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the P-Wellness login page | Login page is displayed |
| 2 | Enter a valid hospital username | Username is accepted |
| 3 | Enter a valid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the application | Hospital dashboard is displayed |

#### Expected Result

Hospital account is successfully authenticated and redirected to
the appropriate dashboard.

---

### PW-TC-004 - Login with Invalid Credential

| Field | Details |
|---|---|
| Test Case ID | PW-TC-004 |
| Test Scenario | Verify login is rejected when invalid credentials are entered |
| Module | Authentication |
| Priority | High |
| Test Type | Negative |
| Precondition | Login page is accessible |
| Test Data | Invalid username and/or password |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the P-Wellness login page | Login page is displayed |
| 2 | Enter an invalid username | Username is accepted |
| 3 | Enter an invalid password | Password is accepted |
| 4 | Click the Login button | Login request is processed |
| 5 | Observe the result | Appropriate error message is displayed |
| 6 | Check the application | User is not authenticated |

#### Expected Result

The system rejects the invalid credentials and prevents
unauthorized access.

---

## 2. Pre-MCU Management

---

### PW-TC-005 - Create Pre-MCU Data

| Field | Details |
|---|---|
| Test Case ID | PW-TC-005 |
| Test Scenario | Verify user can create pre-MCU data using valid information |
| Module | Pre-MCU |
| Priority | High |
| Test Type | Positive |
| Precondition | User is successfully logged in |
| Test Data | Valid pre-MCU information |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using a valid user account | User dashboard is displayed |
| 2 | Open the Pre-MCU menu | Pre-MCU page is displayed |
| 3 | Select the create/add option | Pre-MCU form is displayed |
| 4 | Enter the required information | Data is accepted |
| 5 | Review the entered information | Information is displayed correctly |
| 6 | Save the data | Pre-MCU data is successfully saved |

#### Expected Result

User can successfully create and save pre-MCU data.

---

### PW-TC-006 - Validate Mandatory Pre-MCU Fields

| Field | Details |
|---|---|
| Test Case ID | PW-TC-006 |
| Test Scenario | Verify mandatory fields are validated |
| Module | Pre-MCU |
| Priority | High |
| Test Type | Negative |
| Precondition | Pre-MCU form is accessible |
| Test Data | Required fields left empty |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the Pre-MCU form | Form is displayed |
| 2 | Leave mandatory fields empty | Required fields remain empty |
| 3 | Click Submit | Validation is triggered |
| 4 | Observe the form | Validation messages are displayed |
| 5 | Check submission status | Data is not submitted |

#### Expected Result

The system prevents submission until all mandatory information
has been completed.

---

### PW-TC-007 - Submit Pre-MCU Data

| Field | Details |
|---|---|
| Test Case ID | PW-TC-007 |
| Test Scenario | Verify user can submit completed pre-MCU data |
| Module | Pre-MCU |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Pre-MCU data has been completed |
| Test Data | Valid completed pre-MCU data |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the completed pre-MCU data | Pre-MCU information is displayed |
| 2 | Review the information | Data is displayed correctly |
| 3 | Click Submit | Submission process is executed |
| 4 | Confirm submission if required | Data is successfully submitted |
| 5 | Check submission status | Status is updated accordingly |

#### Expected Result

Pre-MCU data is successfully submitted and becomes available
for hospital review.

---

## 3. Hospital Pre-MCU Review

---

### PW-TC-008 - Review Pre-MCU Data

| Field | Details |
|---|---|
| Test Case ID | PW-TC-008 |
| Test Scenario | Verify hospital can review submitted pre-MCU data |
| Module | Pre-MCU |
| Priority | High |
| Test Type | Positive |
| Precondition | User has submitted pre-MCU data |
| Test Data | Submitted pre-MCU data |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using a valid hospital account | Hospital dashboard is displayed |
| 2 | Open the Pre-MCU menu | Pre-MCU page is displayed |
| 3 | Search for submitted user data | Submitted data is displayed |
| 4 | Open the pre-MCU record | Complete information is displayed |
| 5 | Review the information | Data can be reviewed successfully |

#### Expected Result

Hospital can successfully access and review the submitted
pre-MCU information.

---

## 4. MCU Scheduling

---

### PW-TC-009 - Create MCU Schedule

| Field | Details |
|---|---|
| Test Case ID | PW-TC-009 |
| Test Scenario | Verify hospital can create an MCU schedule |
| Module | MCU Scheduling |
| Priority | Critical |
| Test Type | Positive |
| Precondition | User's pre-MCU data has been reviewed |
| Test Data | Valid MCU schedule information |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the reviewed pre-MCU record | User information is displayed |
| 2 | Select the MCU scheduling option | Scheduling form is displayed |
| 3 | Enter MCU schedule information | Schedule data is accepted |
| 4 | Select the MCU date and time | Date and time are displayed |
| 5 | Save the schedule | MCU schedule is successfully created |
| 6 | Verify the schedule | Schedule information is displayed correctly |

#### Expected Result

Hospital can successfully create an MCU schedule for the user.

---

### PW-TC-010 - Verify MCU Schedule on User Account

| Field | Details |
|---|---|
| Test Case ID | PW-TC-010 |
| Test Scenario | Verify scheduled MCU information is available to the user |
| Module | MCU Scheduling |
| Priority | High |
| Test Type | Positive |
| Precondition | Hospital has created an MCU schedule |
| Test Data | Valid MCU schedule |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the user account | User dashboard is displayed |
| 2 | Open MCU information | MCU information is displayed |
| 3 | Check the scheduled date | Date matches the hospital schedule |
| 4 | Check the scheduled time | Time matches the hospital schedule |
| 5 | Check hospital information | Correct hospital information is displayed |

#### Expected Result

The user can view the MCU schedule and the information matches
the schedule created by the hospital.

---

## 5. MCU Process

---

### PW-TC-011 - User Attends MCU

| Field | Details |
|---|---|
| Test Case ID | PW-TC-011 |
| Test Scenario | Verify user can proceed with the scheduled MCU |
| Module | MCU |
| Priority | High |
| Test Type | Positive |
| Precondition | MCU schedule has been created |
| Test Data | Valid scheduled MCU |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the user account | User dashboard is displayed |
| 2 | Open MCU information | Scheduled MCU is displayed |
| 3 | Attend the MCU according to the schedule | User participates in the MCU |
| 4 | Complete the MCU process | MCU process is completed |

#### Expected Result

User successfully completes the MCU according to the scheduled
appointment.

---

## 6. MCU Result Management

---

### PW-TC-012 - Upload MCU Result

| Field | Details |
|---|---|
| Test Case ID | PW-TC-012 |
| Test Scenario | Verify hospital can upload MCU result documents |
| Module | MCU Result |
| Priority | Critical |
| Test Type | Positive |
| Precondition | User has completed the MCU |
| Test Data | Valid MCU result document |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using a valid hospital account | Hospital dashboard is displayed |
| 2 | Open the relevant MCU record | User MCU information is displayed |
| 3 | Open the MCU result section | Result upload page is displayed |
| 4 | Select the MCU result document | File is selected |
| 5 | Upload the document | Document is uploaded successfully |
| 6 | Save or submit the result | MCU result is successfully recorded |
| 7 | Verify the result status | Result status is updated correctly |

#### Expected Result

Hospital can successfully upload and submit the user's MCU result
document.

---

### PW-TC-013 - Verify MCU Result on User Dashboard

| Field | Details |
|---|---|
| Test Case ID | PW-TC-013 |
| Test Scenario | Verify MCU result is displayed on the user dashboard |
| Module | User Dashboard |
| Priority | Critical |
| Test Type | Positive |
| Precondition | Hospital has successfully uploaded the MCU result |
| Test Data | Valid MCU result |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the user account | User dashboard is displayed |
| 2 | Open the MCU result section | MCU result information is displayed |
| 3 | Check the user information | User information is correct |
| 4 | Check the MCU information | MCU information is correct |
| 5 | Check the uploaded result | MCU result is displayed correctly |
| 6 | Compare the dashboard data with the source data | Data matches the original MCU information |

#### Expected Result

The user's MCU result is correctly displayed on the dashboard
and matches the corresponding source data.

#### Known Defect

Dashboard data may sometimes differ from the corresponding source
data.

#### Related Bug

`PW-BUG-001`

---

## 7. Data Consistency

---

### PW-TC-014 - Validate Dashboard Data Consistency

| Field | Details |
|---|---|
| Test Case ID | PW-TC-014 |
| Test Scenario | Verify data displayed on the user dashboard matches source data |
| Module | User Dashboard |
| Priority | Critical |
| Test Type | Data Validation / Integration |
| Precondition | MCU process has been completed and result data is available |
| Test Data | Completed MCU transaction |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using the hospital account | Hospital dashboard is displayed |
| 2 | Open the completed MCU record | MCU source data is displayed |
| 3 | Record the relevant MCU information | Source data is available for comparison |
| 4 | Login using the corresponding user account | User dashboard is displayed |
| 5 | Open the MCU result information | Dashboard data is displayed |
| 6 | Compare user information | User information matches source data |
| 7 | Compare MCU information | MCU information matches source data |
| 8 | Compare MCU result information | Result information matches source data |
| 9 | Compare document/result status | Status matches source transaction |

#### Expected Result

All relevant data displayed on the user dashboard matches the
corresponding source transaction data.

#### Known Defect

The dashboard may occasionally display data that does not match
the corresponding source data.

#### Related Bug

`PW-BUG-001`

---

## 8. Role-Based Access

---

### PW-TC-015 - Verify Role-Based Access

| Field | Details |
|---|---|
| Test Case ID | PW-TC-015 |
| Test Scenario | Verify each role can access only authorized functions |
| Module | Authorization |
| Priority | High |
| Test Type | Negative / Security |
| Precondition | Valid Admin, User, and Hospital accounts are available |
| Test Data | Admin, User, and Hospital accounts |

#### Test Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Login using Admin account | Admin dashboard is displayed |
| 2 | Verify available menus | Admin functions are displayed |
| 3 | Login using User account | User dashboard is displayed |
| 4 | Verify available menus | User functions are displayed |
| 5 | Login using Hospital account | Hospital dashboard is displayed |
| 6 | Verify available menus | Hospital functions are displayed |
| 7 | Attempt to access an unauthorized function | Access is denied or function is unavailable |

#### Expected Result

Each role can access only the functions permitted by its
assigned authorization.

---

# 9. Test Case Summary

| Test Case ID | Test Scenario | Type | Priority |
|---|---|---|---|
| PW-TC-001 | Admin Login with Valid Credential | Positive | High |
| PW-TC-002 | User Login with Valid Credential | Positive | High |
| PW-TC-003 | Hospital Login with Valid Credential | Positive | High |
| PW-TC-004 | Login with Invalid Credential | Negative | High |
| PW-TC-005 | Create Pre-MCU Data | Positive | High |
| PW-TC-006 | Validate Mandatory Pre-MCU Fields | Negative | High |
| PW-TC-007 | Submit Pre-MCU Data | Positive | Critical |
| PW-TC-008 | Review Pre-MCU Data | Positive | High |
| PW-TC-009 | Create MCU Schedule | Positive | Critical |
| PW-TC-010 | Verify MCU Schedule on User Account | Positive | High |
| PW-TC-011 | User Attends MCU | Positive | High |
| PW-TC-012 | Upload MCU Result | Positive | Critical |
| PW-TC-013 | Verify MCU Result on User Dashboard | Positive | Critical |
| PW-TC-014 | Validate Dashboard Data Consistency | Data Validation | Critical |
| PW-TC-015 | Verify Role-Based Access | Negative / Security | High |

---

# Test Coverage

The test cases cover the following P-Wellness processes:

- Authentication
- Role-Based Authorization
- Pre-MCU Data Creation
- Pre-MCU Submission
- Hospital Pre-MCU Review
- MCU Scheduling
- User MCU Process
- MCU Result Upload
- User Dashboard
- Data Consistency
- Integration Between Hospital and User