# User Stories

## Members (scope items 1, 3)

### S-1 Register a member
As a SACCO officer, I want to register a new member,
so that their details are recorded once and correctly.

Acceptance criteria
- Given valid details, when I submit the form, then the member is saved
  with status "pending" and a membership number is generated.
- Given a National ID that already exists, when I submit, then I see
  "A member with this National ID already exists" and nothing is saved.
- Given an invalid phone number or a missing required field, when I submit,
  then I see an error next to that field.
- Given the applicant is under 18, when I submit, then registration is rejected.
- Given I am not a SACCO officer, when I try to register a member,
  then I am refused.

### S-2 Approve a member
As an Administrator, I want to approve or reject pending members,
so that only verified people become active members.

Acceptance criteria
- Given a pending member, when I approve, then the status becomes "active"
  and the approval date and approver are recorded.
- Given I registered this member myself, when I try to approve,
  then I am refused (maker-checker).
- Given I reject, then I must enter a reason.

## Savings (scope item 4)

### S-3 Record a contribution
As a SACCO officer, I want to record a member's contribution with a payment
reference, so that their savings balance is accurate.

Acceptance criteria
- Given an active member, when I record an amount above zero with a
  reference, then a transaction is saved and the balance increases.
- Given a reference that was already used, when I submit,
  then it is rejected as a duplicate.
- Given a pending or suspended member, when I record a contribution,
  then it is rejected.
- Given a saved contribution, then it can never be edited or deleted,
  only reversed by an Accountant with a reason.

### S-4 View my balance and statement
As a Member, I want to see my savings balance and transaction history,
so that I can trust my records without visiting the office.

Acceptance criteria
- Given I am logged in, then I see only my own balance and transactions.
- Given I try to open another member's statement, then I am refused.

## Loans (scope items 5–8)

### S-5 Apply for a loan
As an active Member, I want to apply for a loan,
so that I can access credit based on my savings.

Acceptance criteria
- Given I have been a member for at least [confirm: 6] months, when I apply
  for up to [confirm: 3] times my savings, then the application is submitted.
- Given I request more than my limit, then I see my maximum allowed amount.
- Given I already have [confirm: an active loan of the same product],
  then the application is rejected with a reason.

### S-6 Respond to a guarantor request
As a Member, I want to accept or decline when someone asks me to guarantee
their loan, so that my savings are not committed without my consent.

Acceptance criteria
- Given a request, when I accept, then the guaranteed amount is held
  against my free savings.
- Given the amount exceeds my free guarantee capacity, then I cannot accept.

### S-7 Decide a loan
As a Loan officer, I want to approve or reject complete applications,
so that only eligible, fully guaranteed loans proceed.

Acceptance criteria
- Given guarantees cover less than [confirm: 100%] of the amount,
  then I cannot approve.
- Given I reject, then I must enter a reason, and the member is notified.
- Given I applied for or guaranteed this loan, then I am refused.

### S-8 Disburse a loan
As an Accountant, I want to release approved loans,
so that money only leaves after two people have checked it.

Acceptance criteria
- Given an approved loan, when I disburse with a reference, then a repayment
  schedule is generated and the loan becomes "active".
- Given the loan is not approved, then disbursement is refused.