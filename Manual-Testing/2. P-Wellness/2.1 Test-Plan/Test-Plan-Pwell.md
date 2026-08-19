# Test Plan - P-Wellness

## 1. Document Information

| Field | Details |
|---|---|
| Project | P-Wellness |
| Application | P-Wellness |
| Application URL | https://p-well.pelindo.co.id/ |
| Testing Type | Manual Testing |
| Test Level | System Testing / Integration Testing / UAT |
| Test Approach | Functional Testing |
| Primary Roles | Admin, User, Hospital |
| Test Environment | UAT |
| Document Status | Completed |

---

# 2. Project Overview

P-Wellness is an application used to manage the MCU (Medical
Check-Up) process involving Users and Hospitals.

The application supports the process from user login and
pre-MCU data submission through MCU scheduling, MCU examination,
uploading MCU results, and displaying the final MCU information
on the user's dashboard.

---

# 3. Test Objective

The objective of testing is to verify that the P-Wellness
application:

- Allows Admin, User, and Hospital accounts to authenticate
  successfully.
- Allows users to create and submit pre-MCU data.
- Allows hospitals to review submitted pre-MCU data.
- Allows hospitals to create MCU schedules.
- Allows users to participate in the scheduled MCU.
- Allows hospitals to upload MCU result documents.
- Displays the correct MCU information on the user's dashboard.
- Maintains data consistency between the source transaction and
  the user's dashboard.

---

# 4. Scope of Testing

## 4.1 In Scope

The following processes are included in testing:

1. Authentication
2. Pre-MCU Data Management
3. Pre-MCU Submission
4. Hospital Review
5. MCU Scheduling
6. MCU Process
7. MCU Result Upload
8. User Dashboard
9. Data Consistency

---

## 4.2 Out of Scope

The following areas are outside the current testing scope unless
specifically required:

- Hospital's internal medical examination process
- External medical laboratory systems
- Medical device integration
- Third-party healthcare systems
- Infrastructure and server performance testing
- Security penetration testing

---

# 5. User Roles

## Admin

Admin is responsible for accessing and managing application
functions according to the permissions assigned to the
administrative role.

## User

User is responsible for:

- Creating pre-MCU data
- Submitting pre-MCU data
- Following the scheduled MCU
- Viewing MCU information and results on the dashboard

## Hospital

Hospital is responsible for:

- Reviewing pre-MCU submissions
- Creating MCU schedules
- Conducting the MCU process
- Uploading MCU result documents

---

# 6. Business Process

The P-Wellness business process consists of:

```text
User Login
     │
     ▼
Create Pre-MCU Data
     │
     ▼
Submit Pre-MCU
     │
     ▼
Hospital Reviews Pre-MCU
     │
     ▼
Hospital Creates MCU Schedule
     │
     ▼
User Attends MCU
     │
     ▼
Hospital Uploads MCU Result
     │
     ▼
Result Data Available
     │
     ▼
User Dashboard