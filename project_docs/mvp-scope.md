# MVP Scope

## Pilot outcome
A limited pilot in the first week of January 2027 with [confirm: number]
members of [confirm: SACCO name], using test or approved data only.

## Included
1. Member registration, review and approval
2. Login, roles and permissions
3. Member profiles and status (pending, active, suspended, exited)
4. Savings and contribution records
5. Loan products, applications and eligibility checks
6. Guarantor requests and guarantee capacity limits
7. Loan review, approval and rejection with reasons
8. Controlled disbursement and repayment schedules
9. Transaction history, statements and basic reports
10. In-app notifications, audit trail and activity logs

## Excluded (post-MVP)
- Live M-Pesa integration (payments are recorded manually with a reference)
- USSD and mobile apps
- Automated credit scoring
- Biometric login
- Full accounting and general ledger
- Multiple SACCOs on one system
- AI features
- Member self-registration

## Assumptions
- Staff have computers or tablets with internet access.
- The SACCO provides its loan rules (interest method, limits, fees) in writing.
- Contributions are received outside the system (cash, bank, M-Pesa) and
  recorded by an officer with a reference number.

## Risks
| Risk | Effect | How we reduce it |
|---|---|---|
| Loan rules unclear or change late | Wrong calculations | Get rules signed off before Dec 5 |
| Real member data used in testing | Privacy breach | Anonymised seed data only |
| One developer, tight timeline | Missed pilot date | Strict scope, Dec 25 buffer day |
| Calculation errors | Wrong balances | Reconciliation tests, maker-checker |