# Test Plan - Contract Management System

## 1. Objective

The objective of this test plan is to verify that the Contract
Management System correctly processes contract preparation,
review, approval, and electronic signing after the E-Tender
winner determination process.

---

## 2. Scope

Testing covers:

- Work package transfer from E-Tender to CMS
- Reviewer configuration
- Payment method configuration
- Vendor payment account assignment
- Contract document generation
- Contract document submission
- Reviewer approval
- Approval status validation
- Final contract generation
- Pihak 1 e-signature
- Pihak 2 e-signature

---

## 3. Testing Approach

- Functional Testing
- Positive Testing
- Negative Testing
- Integration Testing
- End-to-End Testing
- Regression Testing
- User Acceptance Testing

---

## 4. Test Environment

| Item | Details |
|---|---|
| Application | Contract Management System |
| Integration | E-Tender |
| Browser | Google Chrome |
| Operating System | Windows |
| Testing Type | Manual Testing |

---

## 5. Entry Criteria

- E-Tender winner has been determined.
- Work package is available for CMS processing.
- CMS environment is accessible.
- Required user accounts are available.
- Required test data is available.
- Reviewer accounts are available.
- Vendor payment account data is available.

---

## 6. Exit Criteria

- All planned test cases have been executed.
- Critical business flows have been validated.
- Critical defects have been resolved or accepted.
- Failed test cases have been retested.
- Regression testing has been completed.
- UAT has been completed.

---

## 7. Test Roles

| Role | Responsibility |
|---|---|
| QA Tester | Execute testing and report defects |
| Atasan | Review and approve contract |
| Pengguna / Pihak 1 | Review, approve and e-sign contract |
| Vendor / Pihak 2 | Review, approve and e-sign contract |
| Developer | Analyze and resolve defects |
| Business User | Validate business process |

---

## 8. Test Coverage

| Area | Coverage |
|---|---|
| Integration | E-Tender to CMS |
| Reviewer | Reviewer configuration |
| Payment | Payment method and account |
| Contract | Contract document generation |
| Review | Reviewer approval |
| E-Signature | Pihak 1 and Pihak 2 |
| Completion | Final contract status |

---

## 9. Deliverables

- Test Plan
- Test Cases
- Bug Reports
- UAT
- Test Execution Results
- Retest Results
- Regression Results