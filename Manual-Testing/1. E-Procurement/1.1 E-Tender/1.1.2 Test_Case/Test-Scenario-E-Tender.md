# Test Scenarios - E-Tender

## 1. Work Package Creation

| ID | Test Scenario |
|---|---|
| ET-TS-001 | Verify user can create a work package with valid data |
| ET-TS-002 | Verify mandatory fields are validated when creating a work package |
| ET-TS-003 | Verify invalid work package data is rejected |
| ET-TS-004 | Verify created work package is saved successfully |

## 2. Work Package Publication

| ID | Test Scenario |
|---|---|
| ET-TS-005 | Verify user can publish an eligible work package |
| ET-TS-006 | Verify unpublished work package cannot be accessed by vendors |
| ET-TS-007 | Verify published work package is visible to eligible vendors |
| ET-TS-008 | Verify package status changes correctly after publication |

## 3. Vendor Registration

| ID | Test Scenario |
|---|---|
| ET-TS-009 | Verify eligible vendor can register for a published work package |
| ET-TS-010 | Verify vendor cannot register for an unpublished package |
| ET-TS-011 | Verify duplicate vendor registration is prevented |
| ET-TS-012 | Verify registration status is displayed correctly |

## 4. Registration Evaluation

| ID | Test Scenario |
|---|---|
| ET-TS-013 | Verify procurement user can review vendor registration |
| ET-TS-014 | Verify procurement user can approve vendor registration |
| ET-TS-015 | Verify procurement user can reject vendor registration |
| ET-TS-016 | Verify vendor registration status is updated correctly |

## 5. Clarification Session

| ID | Test Scenario |
|---|---|
| ET-TS-017 | Verify procurement user can conduct a clarification session |
| ET-TS-018 | Verify vendor can submit questions during the clarification session |
| ET-TS-019 | Verify procurement user can provide responses to vendor questions |
| ET-TS-020 | Verify clarification information is available to eligible participants |

## 6. Bid Document Upload

| ID | Test Scenario |
|---|---|
| ET-TS-021 | Verify vendor can upload valid bid documents |
| ET-TS-022 | Verify mandatory bid documents are validated |
| ET-TS-023 | Verify unsupported file formats are rejected |
| ET-TS-024 | Verify uploaded documents are displayed correctly |

## 7. Bid Document Opening

| ID | Test Scenario |
|---|---|
| ET-TS-025 | Verify authorized user can open submitted bid documents |
| ET-TS-026 | Verify only submitted bid documents can be opened |
| ET-TS-027 | Verify bid opening status is updated correctly |
| ET-TS-028 | Verify opened bid documents can be accessed by authorized users |

## 8. Bid Document Evaluation

| ID | Test Scenario |
|---|---|
| ET-TS-029 | Verify evaluator can review submitted bid documents |
| ET-TS-030 | Verify evaluator can provide evaluation results |
| ET-TS-031 | Verify evaluation criteria are applied correctly |
| ET-TS-032 | Verify evaluation status is updated correctly |

## 9. Negotiation

| ID | Test Scenario |
|---|---|
| ET-TS-033 | Verify authorized user can initiate negotiation |
| ET-TS-034 | Verify vendor can respond to negotiation |
| ET-TS-035 | Verify negotiation results are recorded correctly |
| ET-TS-036 | Verify unauthorized users cannot perform negotiation |

## 10. Winner Determination

| ID | Test Scenario |
|---|---|
| ET-TS-037 | Verify authorized user can determine the winning vendor |
| ET-TS-038 | Verify winner determination follows the evaluation result |
| ET-TS-039 | Verify winner status is displayed correctly |
| ET-TS-040 | Verify non-winning vendors receive the correct status |