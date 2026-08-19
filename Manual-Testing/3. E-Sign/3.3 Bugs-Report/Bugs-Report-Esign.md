# Bug Reports - E-Sign

## 1. Email E-Sign Tidak Diterima oleh User

---

### ES-BUG-001 - E-Sign Email Not Received

| Field | Details |
|---|---|
| Bug ID | ES-BUG-001 |
| Title | E-Sign email is not received by the intended recipient |
| Module | Email Notification |
| Severity | High |
| Priority | High |
| Status | Intermittent / Recurring |
| Environment | E-Sign / CMS Integration |
| Related Test Case | ES-TC-001, ES-TC-019, ES-TC-021 |

#### Description

E-Sign email is sometimes not received by the intended recipient after the E-Sign request is generated.

The issue may be caused by incorrect email data, user/human error, email delivery issues, or system/integration issues. Further investigation is required to determine the actual root cause.

#### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Complete the required contract approval process |
| 2 | Generate the E-Sign request |
| 3 | Verify the recipient email address |
| 4 | Check the recipient email inbox |
| 5 | Observe whether the E-Sign email is received |

#### Expected Result

E-Sign email should be successfully delivered to the intended recipient.

#### Actual Result

E-Sign email is sometimes not received by the intended recipient.

#### Impact

The recipient cannot continue the E-Sign process until the email/link is received.

#### Notes

Possible factors include:

- Incorrect recipient email address
- Email delivery issue
- User/human error
- System issue
- CMS and E-Sign integration issue

Root cause requires further investigation.

---

# 2. E-Sign Barcode Not Generated

---

### ES-BUG-002 - E-Sign Barcode Is Not Generated Due to Coordinate Issue

| Field | Details |
|---|---|
| Bug ID | ES-BUG-002 |
| Title | E-Sign barcode is not displayed because barcode coordinate is not detected |
| Module | E-Sign / Barcode |
| Severity | High |
| Priority | High |
| Status | Closed |
| Environment | E-Sign |
| Related Test Case | ES-TC-015, ES-TC-023, ES-TC-027 |

#### Description

The E-Sign barcode is not generated/displayed because the coordinate information required for barcode placement cannot be detected correctly.

#### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Open the E-Sign document |
| 2 | Initiate the Stamp process |
| 3 | Process the document for E-Sign |
| 4 | System attempts to determine the barcode coordinate |
| 5 | Observe the document |

#### Expected Result

The system successfully detects the required coordinate and generates/displays the E-Sign barcode in the appropriate location.

#### Actual Result

The barcode is not displayed because the required coordinate cannot be detected.

#### Impact

The E-Sign process cannot be completed correctly because the required barcode is unavailable.

#### Resolution

Issue has been resolved.

#### Status

**Closed**

---

# 3. E-Sign Status Not Updated After Successful Stamp

---

### ES-BUG-003 - E-Sign Status Not Updated After Stamp

| Field | Details |
|---|---|
| Bug ID | ES-BUG-003 |
| Title | E-Sign status is not updated after successful Stamp |
| Module | E-Sign Status |
| Severity | High |
| Priority | High |
| Status | Intermittent / Recurring |
| Environment | E-Sign / CMS Integration |
| Related Test Case | ES-TC-017, ES-TC-025, ES-TC-028, ES-TC-030 |

#### Description

After the user successfully completes the Stamp process, the E-Sign status is sometimes not updated accordingly.

The Stamp process is completed successfully, but the system still displays the previous signing status.

#### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Open the E-Sign document |
| 2 | Initiate the Stamp process |
| 3 | Apply the required e-Meterai |
| 4 | Enter the valid OTP |
| 5 | Complete the Stamp process |
| 6 | Return to the E-Sign/CMS page |
| 7 | Check the signing status |

#### Expected Result

After successful Stamp, the E-Sign status should automatically be updated to the appropriate status.

#### Actual Result

The Stamp process is successfully completed, but the signing status is sometimes not updated.

#### Impact

The system may consider the signing process incomplete even though the user has successfully completed the Stamp process.

This can potentially block the next signing process or cause inconsistency between the E-Sign system and CMS.

#### Notes

Issue is intermittent and may occur again after previously being resolved.

---

# 4. Vinotek Integration Issue

---

### ES-BUG-004 - E-Sign Process Fails Due to Vinotek Integration Issue

| Field | Details |
|---|---|
| Bug ID | ES-BUG-004 |
| Title | E-Sign process is intermittently affected by Vinotek integration issues |
| Module | E-Sign / Vinotek Integration |
| Severity | Critical |
| Priority | Critical |
| Status | Intermittent / Recurring |
| Environment | E-Sign / Vinotek |
| Related Test Case | ES-TC-003, ES-TC-004, ES-TC-009, ES-TC-015, ES-TC-017, ES-TC-025 |

#### Description

The E-Sign process sometimes encounters issues when communicating with or processing data through Vinotek.

The issue can affect several stages of the E-Sign process, including registration, payment verification, e-Meterai processing, Stamp, and signing status synchronization.

#### Possible Affected Processes

- Vendor registration validation
- Vinotek registration
- Registration quota purchase
- Payment verification
- e-Meterai processing
- Stamp process
- OTP verification
- Signing status synchronization

#### Steps to Reproduce

| Step | Action |
|---|---|
| 1 | Start the E-Sign process |
| 2 | Perform the required Vendor/Pengguna process |
| 3 | Trigger a process requiring Vinotek integration |
| 4 | Observe the system response |
| 5 | Check the transaction/status information |

#### Expected Result

E-Sign and Vinotek should communicate successfully and the requested transaction should be processed correctly.

#### Actual Result

The process may fail or the expected data/status may not be returned correctly due to Vinotek integration issues.

#### Impact

The issue can prevent or delay completion of the E-Sign process.

Depending on the affected integration point, the user may be unable to:

- Continue registration
- Complete payment verification
- Apply e-Meterai
- Complete Stamp
- Obtain the correct signing status

#### Notes

Issue is related to system integration with Vinotek and may require investigation of API/request-response, transaction status, or integration logs.

---

# 5. Bug Summary

| Bug ID | Bug Summary | Severity | Status | Characteristic |
|---|---|---|---|---|
| ES-BUG-001 | E-Sign email not received | High | Intermittent / Recurring | Possible human error / System |
| ES-BUG-002 | E-Sign barcode not generated due to coordinate issue | High | Closed | Resolved |
| ES-BUG-003 | E-Sign status not updated after successful Stamp | High | Intermittent / Recurring | Recurring |
| ES-BUG-004 | E-Sign process affected by Vinotek integration issue | Critical | Intermittent / Recurring | Integration |

# 6. Bug Coverage

The reported defects cover the following E-Sign areas:

- E-Sign Email Notification
- Vendor E-Sign Request
- Pengguna E-Sign Request
- Barcode Generation
- e-Meterai Processing
- Stamp Process
- OTP Verification
- Signing Status Update
- CMS Integration
- Vinotek Integration
- Registration
- Payment Verification