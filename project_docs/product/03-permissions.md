# Permissions Matrix

Key: ✅ allowed · 👁 view only · 🔒 own records only · — not allowed

| Action | Member | Officer | Loan officer | Accountant | Admin | Auditor |
|---|---|---|---|---|---|---|
| Register member | — | ✅ | — | — | — | — |
| Approve new member | — | — | — | — | ✅ | — |
| View member profile | 🔒 | ✅ | 👁 | 👁 | 👁 | 👁 |
| Edit member contact details | — | ✅ | — | — | — | — |
| Record contribution | — | ✅ | — | — | — | — |
| Reverse contribution | — | — | — | ✅ | — | — |
| View balances and statements | 🔒 | 👁 | 👁 | ✅ | — | 👁 |
| Apply for loan | 🔒 | — | — | — | — | — |
| Accept or decline guarantor request | 🔒 | — | — | — | — | — |
| Review and decide loan | — | — | ✅ | — | — | 👁 |
| Disburse loan | — | — | — | ✅ | — | 👁 |
| Post repayment | — | — | — | ✅ | — | 👁 |
| Run reports | — | — | 👁 | ✅ | — | 👁 |
| Manage staff accounts and roles | — | — | — | — | ✅ | — |
| View audit log | — | — | — | — | 👁 | 👁 |

## Separation-of-duty rules (maker-checker)
- The officer who registers a member cannot approve that member.
- A loan officer cannot decide a loan they applied for or guaranteed.
- Disbursement needs a decision by a Loan officer AND release by an
  Accountant: two different people.
- Nobody can approve their own transaction.