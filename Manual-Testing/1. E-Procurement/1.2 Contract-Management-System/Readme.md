# Contract Management System - QA Testing Portfolio

## Project Overview

This project demonstrates Quality Assurance activities performed
on a Contract Management System (CMS) within an E-Procurement
business process.

The CMS process begins after the winning vendor has been determined
in the E-Tender module and the work package is transferred to the
Contract Management System.

---

## Business Process

The Contract Management process covers:

1. Setting Contract Reviewers
2. Configuring Payment Terms
3. Assigning Vendor Payment Account
4. Generating Contract Documents
5. Sending Contract Documents to Reviewers
6. Reviewer Approval
7. Final Contract E-Signature

---

## End-to-End Workflow

```text
E-Tender Winner Determination
            ↓
Work Package Sent to CMS
            ↓
Setting Reviewer
            ↓
┌─────────────────────────────┐
│ Atasan                      │
│ Pengguna / Pihak 1          │
│ Vendor / Pihak 2            │
└─────────────────────────────┘
            ↓
Payment Method Configuration
            ↓
Vendor Payment Account
            ↓
Generate Contract Document
            ↓
Send Contract to Reviewers
            ↓
Reviewer Approval
            ↓
All Reviewers Approved?
        ↙           ↘
      No             Yes
      ↓               ↓
Review / Reject    Final Contract
                      ↓
              Pihak 1 E-Sign
                      +
              Pihak 2 E-Sign
                      ↓
              Contract Completed