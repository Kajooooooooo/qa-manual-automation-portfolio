# Bug Report - P-Wellness

## 1. Dashboard Data Inconsistency

---

### PW-BUG-001 - User Dashboard Data Does Not Match Source Data

| Field | Details |
|---|---|
| Bug ID | PW-BUG-001 |
| Title | User Dashboard Data Does Not Match Source Data |
| Module | User Dashboard |
| Severity | High |
| Priority | High |
| Bug Type | Data Integrity / Integration |
| Environment | UAT |
| Status | Open |
| Frequency | Intermittent |
| Related Test Case | PW-TC-013, PW-TC-014 |

#### Description

Data displayed on the User Dashboard does not always match the
corresponding data stored or displayed in the source transaction.

The issue may occur intermittently, where the dashboard displays
different information from the actual MCU transaction data.

#### Precondition

- User account is available.
- Hospital account is available.
- User has completed the MCU process.
- Hospital has uploaded the MCU result.
- MCU transaction data is available.

#### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Login using a valid Hospital account |
| 2 | Open the completed MCU record |
| 3 | Review the user's MCU information and result data |
| 4 | Login using the corresponding User account |
| 5 | Open the User Dashboard |
| 6 | Open the MCU result information |
| 7 | Compare the dashboard data with the source transaction |

#### Expected Result

The data displayed on the User Dashboard should exactly match
the corresponding MCU transaction data, including relevant user,
MCU, result, and status information.

#### Actual Result

The data displayed on the User Dashboard sometimes does not match
the corresponding source transaction data.

#### Impact

- User may receive incorrect MCU information.
- Users may lose confidence in the accuracy of the application.
- Incorrect information may affect the interpretation of the MCU
  result.
- Data consistency between the transaction and dashboard cannot
  always be guaranteed.

#### Frequency

Intermittent.

The issue does not occur consistently and may require repeated
testing or multiple transactions to reproduce.

#### Status

**Open**

#### Evidence

Add supporting screenshots or screen recordings here.

Example:

```text
Evidence:
- Screenshot of source MCU data
- Screenshot of User Dashboard
- Screenshot highlighting the data discrepancy