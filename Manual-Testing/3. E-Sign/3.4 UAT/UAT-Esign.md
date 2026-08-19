# User Acceptance Test (UAT) - E-Sign

## 1. UAT Overview

| Field | Details |
|---|---|
| Application | E-Sign |
| Integration | CMS, Vinotek |
| Business Process | Electronic Contract Signing |
| Document | Contract |
| Primary Users | Pengguna (Pihak 1), Vendor (Pihak 2) |
| Supporting System | CMS, Vinotek |
| UAT Objective | Verify the E-Sign process can be completed successfully by Vendor and Pengguna |
| UAT Status | In Progress |

---

# 2. UAT Scope

The UAT covers the following business processes:

- Contract E-Sign request from CMS
- Vendor E-Sign email notification
- Vendor registration validation
- Vinotek registration
- Registration quota purchase
- Payment and payment verification
- Vendor E-Sign
- e-Meterai placement
- OTP verification
- Email notification to Pengguna
- Pengguna E-Sign
- Final contract signing
- E-Sign status update
- CMS integration
- Vinotek integration

---

# 3. UAT Actors

| Actor | Responsibility |
|---|---|
| Vendor (Pihak 2) | Receive and complete the first E-Sign process |
| Pengguna (Pihak 1) | Complete the second E-Sign process |
| CMS | Generate and manage contract information |
| Vinotek | Provide E-Sign and e-Meterai services |

---

# 4. UAT Test Scenarios

## UAT-ES-001 - Contract E-Sign Request

| Field | Details |
|---|---|
| UAT ID | UAT-ES-001 |
| Scenario | Verify approved contract can be sent to E-Sign |
| Priority | Critical |
| Actor | CMS / Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete contract approval process in CMS | Contract approval is completed |
| 2 | Send the contract to E-Sign | E-Sign request is generated |
| 3 | Verify Vendor information | Correct Vendor information is displayed |
| 4 | Verify contract information | Correct contract is selected |

### Expected Result

Approved contract can be successfully sent to the E-Sign process with the correct Vendor and contract information.

---

## UAT-ES-002 - Vendor Receives E-Sign Email

| Field | Details |
|---|---|
| UAT ID | UAT-ES-002 |
| Scenario | Verify Vendor receives E-Sign email |
| Priority | Critical |
| Actor | Vendor |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open Vendor email | Email inbox is displayed |
| 2 | Check incoming email | E-Sign email is received |
| 3 | Open the E-Sign email | E-Sign information is displayed |
| 4 | Verify contract information | Correct contract information is displayed |
| 5 | Verify E-Sign link | E-Sign link is available |

### Expected Result

Vendor successfully receives the E-Sign email and can access the E-Sign link.

---

## UAT-ES-003 - Registered Vendor Access E-Sign

| Field | Details |
|---|---|
| UAT ID | UAT-ES-003 |
| Scenario | Verify registered Vendor can directly access E-Sign |
| Priority | Critical |
| Actor | Vendor |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | System validates registration |
| 3 | System detects registered email | Email is recognized |
| 4 | Observe the page | E-Sign page is displayed |

### Expected Result

Registered Vendor is directly directed to the E-Sign page without repeating the registration process.

---

## UAT-ES-004 - Unregistered Vendor Registration

| Field | Details |
|---|---|
| UAT ID | UAT-ES-004 |
| Scenario | Verify unregistered Vendor can complete Vinotek registration |
| Priority | Critical |
| Actor | Vendor |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | System checks registration status |
| 3 | System detects unregistered email | Vendor is directed to Vinotek |
| 4 | Open registration process | Registration page is displayed |
| 5 | Purchase required registration quota | Quota purchase is processed |
| 6 | Complete payment | Payment is processed |
| 7 | Verify payment | Payment is successfully verified |
| 8 | Complete registration form | Registration data is accepted |
| 9 | Submit registration | Registration is successfully completed |

### Expected Result

Unregistered Vendor successfully completes Vinotek registration and becomes eligible to continue the E-Sign process.

---

## UAT-ES-005 - Vendor Return to E-Sign

| Field | Details |
|---|---|
| UAT ID | UAT-ES-005 |
| Scenario | Verify Vendor can return to E-Sign after registration |
| Priority | Critical |
| Actor | Vendor |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the original E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | System validates registration |
| 3 | System detects registered email | Email is recognized |
| 4 | Observe the page | E-Sign page is displayed |
| 5 | Verify contract | Correct contract is displayed |

### Expected Result

Vendor can access the E-Sign page after successfully completing registration.

---

## UAT-ES-006 - Vendor Stamp and e-Meterai

| Field | Details |
|---|---|
| UAT ID | UAT-ES-006 |
| Scenario | Verify Vendor can complete Stamp with e-Meterai |
| Priority | Critical |
| Actor | Vendor |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign contract | Contract is displayed |
| 2 | Click Stamp | Stamp process is displayed |
| 3 | Select e-Meterai | e-Meterai is selected |
| 4 | Place e-Meterai in the required location | e-Meterai is placed correctly |
| 5 | Continue the process | OTP verification is displayed |
| 6 | Open Vendor email | OTP email is received |
| 7 | Enter valid OTP | OTP is accepted |
| 8 | Submit OTP | Stamp is completed |

### Expected Result

Vendor successfully completes Stamp and e-Meterai on the contract.

---

## UAT-ES-007 - Email Sent to Pengguna After Vendor Stamp

| Field | Details |
|---|---|
| UAT ID | UAT-ES-007 |
| Scenario | Verify Pengguna receives E-Sign email after Vendor completes Stamp |
| Priority | Critical |
| Actor | Vendor / Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Vendor completes Stamp | Vendor signing is completed |
| 2 | Observe E-Sign system | Vendor signing status is updated |
| 3 | Open Pengguna email | Email inbox is displayed |
| 4 | Check incoming email | E-Sign email is received |
| 5 | Open the email | Contract and E-Sign information are displayed |
| 6 | Verify E-Sign link | Valid link is available |

### Expected Result

After Vendor successfully completes Stamp, the system automatically sends the E-Sign request to Pengguna.

---

## UAT-ES-008 - Pengguna Access E-Sign

| Field | Details |
|---|---|
| UAT ID | UAT-ES-008 |
| Scenario | Verify Pengguna can access the E-Sign contract |
| Priority | Critical |
| Actor | Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the E-Sign email | Email is displayed |
| 2 | Click the E-Sign link | E-Sign page is opened |
| 3 | Verify contract information | Correct contract is displayed |
| 4 | Verify Vendor information | Vendor information is displayed correctly |
| 5 | Verify available action | Stamp action is available |

### Expected Result

Pengguna can successfully access the correct contract for signing.

---

## UAT-ES-009 - Pengguna Stamp and e-Meterai

| Field | Details |
|---|---|
| UAT ID | UAT-ES-009 |
| Scenario | Verify Pengguna can complete Stamp with e-Meterai |
| Priority | Critical |
| Actor | Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Open the contract | Contract is displayed |
| 2 | Click Stamp | Stamp process is displayed |
| 3 | Select e-Meterai | e-Meterai is selected |
| 4 | Place e-Meterai | e-Meterai is placed correctly |
| 5 | Continue the process | OTP verification is displayed |
| 6 | Open Pengguna email | OTP email is received |
| 7 | Enter valid OTP | OTP is accepted |
| 8 | Submit OTP | Stamp is completed |

### Expected Result

Pengguna successfully completes Stamp and e-Meterai on the contract.

---

## UAT-ES-010 - Final Contract Signing

| Field | Details |
|---|---|
| UAT ID | UAT-ES-010 |
| Scenario | Verify contract is fully signed by Vendor and Pengguna |
| Priority | Critical |
| Actor | Vendor / Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Verify Vendor signing | Vendor signing is completed |
| 2 | Verify Pengguna signing | Pengguna signing is completed |
| 3 | Open the final contract | Final contract is displayed |
| 4 | Verify Vendor signature | Vendor signature is present |
| 5 | Verify Pengguna signature | Pengguna signature is present |
| 6 | Verify e-Meterai | Required e-Meterai is present |
| 7 | Verify document content | Contract content remains correct |

### Expected Result

Contract is successfully signed by both Vendor and Pengguna and the final signed document is available.

---

## UAT-ES-011 - E-Sign Status Update

| Field | Details |
|---|---|
| UAT ID | UAT-ES-011 |
| Scenario | Verify E-Sign status is updated after successful signing |
| Priority | Critical |
| Actor | Vendor / Pengguna |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor Stamp | Vendor status is updated |
| 2 | Complete Pengguna Stamp | Pengguna status is updated |
| 3 | Check overall E-Sign status | Status indicates signing completion |
| 4 | Refresh the page | Status remains correct |

### Expected Result

E-Sign status is correctly updated after both parties complete the signing process.

---

## UAT-ES-012 - Synchronization with CMS

| Field | Details |
|---|---|
| UAT ID | UAT-ES-012 |
| Scenario | Verify final E-Sign result is synchronized with CMS |
| Priority | Critical |
| Actor | Pengguna / CMS |

### Steps

| Step | Action | Expected Result |
|---|---|---|
| 1 | Complete Vendor signing | Vendor signing is successful |
| 2 | Complete Pengguna signing | Pengguna signing is successful |
| 3 | Open CMS | CMS is accessible |
| 4 | Open the related contract | Contract data is displayed |
| 5 | Check E-Sign status | Final E-Sign status is displayed |
| 6 | Check signed document | Final signed contract is available |

### Expected Result

Final E-Sign status and signed contract are successfully synchronized and available in CMS.

---

# 5. UAT Result Summary

| UAT ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| UAT-ES-001 | Contract E-Sign Request | E-Sign request generated successfully | - | Not Tested |
| UAT-ES-002 | Vendor Receives E-Sign Email | Email received successfully | - | Not Tested |
| UAT-ES-003 | Registered Vendor Access E-Sign | Directly access E-Sign | - | Not Tested |
| UAT-ES-004 | Unregistered Vendor Registration | Registration completed successfully | - | Not Tested |
| UAT-ES-005 | Vendor Return to E-Sign | Vendor can access E-Sign | - | Not Tested |
| UAT-ES-006 | Vendor Stamp and e-Meterai | Vendor signing completed | - | Not Tested |
| UAT-ES-007 | Email Sent to Pengguna | Pengguna receives E-Sign email | - | Not Tested |
| UAT-ES-008 | Pengguna Access E-Sign | Pengguna can access contract | - | Not Tested |
| UAT-ES-009 | Pengguna Stamp and e-Meterai | Pengguna signing completed | - | Not Tested |
| UAT-ES-010 | Final Contract Signing | Contract fully signed | - | Not Tested |
| UAT-ES-011 | E-Sign Status Update | Status updated correctly | - | Not Tested |
| UAT-ES-012 | Synchronization with CMS | Final result synchronized to CMS | - | Not Tested |

---

# 6. UAT Acceptance Criteria

The E-Sign process is considered **Accepted** when:

- Vendor successfully receives the E-Sign request.
- Registered Vendor can directly access the E-Sign page.
- Unregistered Vendor can complete the required Vinotek registration.
- Vendor can successfully apply e-Meterai and complete Stamp.
- OTP is successfully delivered and validated.
- Pengguna receives the E-Sign request after Vendor completes Stamp.
- Pengguna can successfully apply e-Meterai and complete Stamp.
- Contract is successfully signed by both parties.
- E-Sign status is updated correctly.
- Final signed contract is available.
- Final E-Sign result is successfully synchronized with CMS.
- No Critical business-blocking defect remains open.

---

# 7. UAT Final Sign-Off

| Role | Name | Result | Date | Signature |
|---|---|---|---|---|
| Vendor | - | Pending | - | - |
| Pengguna | - | Pending | - | - |
| Business Owner | - | Pending | - | - |
| QA | - | Pending | - | - |

### Final UAT Status