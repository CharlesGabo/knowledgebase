# SRC-019 - Payment reconciliation question and Alex's W76 reply

- Question author: User
- Answer author: Alex, as identified by the user/context
- Original communication date(s): Unknown
- Intake date: 2026-11-16 (Asia/Manila)
- Original subject: Unknown
- Descriptive subject: Payments recorded outside CC and QuickBooks/CC alignment
- Type: Manually supplied question and Alex reply, preserved as provided
- Redactions: None required

## Question (user, verbatim including formatting escape)

```text
yeah about the payments, When a staff member charges a card inside the CC, the CC knows right away that the invoice is paid. But when a customer pays another way, like through the "Pay now" link, by check or by bank transfer, the payment is only recorded in QuickBooks, and the CC doesn't know about it unless someone checks.\
Do you plan to automate this in the CC, for example by having it check QuickBooks regularly and mark invoices as paid? Or should the customer website handle it?
```

## Answer (Alex, verbatim including formatting escapes)

```text
Yes, I do want to add more of the accounting side of things to CC. I just haven't gotten that far yet. One of the biggest/longest work trees I've been working on is W76. The work tree has been about keeping QB and CC aligned. Ideally we edit orders in CC but in the event an invoice or PO is edited in QB (which should be rare but can happen), CC scans documents and records it in CC.\
\
Keeping QB and CC aligned with sort of a two way read has been difficult 😅\
\
But I think I've finally gotten W76 almost done. There's a flaw I have to fix tomorrow but it took me nearly two months to get some kind of solution
```

## Interpretation and limits

QB means QuickBooks; CC means Command Center; PO means purchase order. The question's account of card and external payments is the user's premise, not independently verified or explicitly confirmed in full by Alex's answer. Alex confirms accounting expansion intent and describes W76's document-alignment work, preferred editing in CC and detection of invoice/PO changes made in QB. "Almost done" is reported progress, not completion or deployment evidence. No polling interval or automatic payment-status coverage is confirmed.

Alex's remaining flaw fix is her own pending work, not an assignment to Charles. Her original message date is unknown, so "tomorrow" is retained without assigning a calendar date or hard deadline. See [T-007](../tasks.md#t-007), [accounting status](../workflows.md#accounting-and-quickbooks-alignment) and [Q-016](../questions.md#q-016).
