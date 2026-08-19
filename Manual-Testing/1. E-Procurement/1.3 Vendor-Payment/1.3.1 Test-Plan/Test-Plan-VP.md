# Test Plan - Vendor Payment

## 1. Document Information

| Field | Details |
|---|---|
| Document Name | Vendor Payment Test Plan |
| Application | E-Procurement |
| Module | Vendor Payment |
| Testing Type | Functional Testing, Integration Testing, Workflow Testing |
| Test Level | System Testing |
| Objective | Verify that the Vendor Payment process works according to business requirements |
| Status | Completed |

---

# 2. Test Objective

The objective of this test is to verify that the Vendor Payment
module can successfully support the payment process from
Purchase Order integration through SAP until the payment
completion and payment report.

The testing also verifies the integration between Vendor Payment
and SAP and validates the workflow between users and vendors.

---

# 3. Scope of Testing

The testing covers the following Vendor Payment processes:

1. Purchase Order submission to SAP
2. SAP Purchase Order approval
3. Vendor Payment data synchronization
4. Vendor Payment drafting
5. User personnel configuration
6. Vendor personnel configuration
7. Work commencement report
8. Work handover report
9. Progress report
10. GR / SES acceptance
11. Vendor billing document submission
12. Billing document approval
13. Payment memorandum creation
14. Payment memorandum approval
15. Payment processing through SAP
16. Payment report creation

---

# 4. Business Flow

The Vendor Payment business flow is:

```text
Final Contract E-Signature
          │
          ▼
     Submit PO to SAP
          │
          ▼
      SAP Approval
          │
          ▼
   Data Received by
    Vendor Payment
          │
          ▼
 Draft Vendor Payment
          │
          ▼
   Configure Personnel
    ┌────────┴────────┐
    ▼                 ▼
  User             Vendor
 Personnel         Personnel
    └────────┬────────┘
             ▼
   Work Commencement
        Report
             │
             ▼
      Work Progress
        (if any)
             │
             ▼
       Work Handover
         Report
             │
             ▼
         GR / SES
             │
             ▼
   Vendor Submit Billing
         Documents
             │
             ▼
   User Approves Billing
         Documents
             │
             ▼
   Create Payment Memo
             │
             ▼
      Approval Process
       User & Vendor
             │
             ▼
      Process Payment
          through SAP
             │
             ▼
       Payment Success
             │
             ▼
      Payment Report