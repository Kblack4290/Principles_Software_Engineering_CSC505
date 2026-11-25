# Module 8 Portfolio Project: ATM UML Diagram, Python Script, and Lessons Learned

Submission name: `CSC505_M08_PP_Black_Keith.zip`

## Deliverables Checklist

| Deliverable | File(s) | Status |
| --- | --- | --- |
| ATM UML diagram (UMLet) | `atm_state_diagram.uxf`, `atm_state_diagram.png` | Not started |
| Python script that prints every ATM step in diagram order | `atm_simulation.py` | Not started |
| Screenshots of a successful run | `screenshots/` | Not started |
| Lessons Learned reflection (2–3 pages, APA) | `lessons_learned_outline.md` → `Black_Module8_Lessons_Learned.docx` | Draft complete |

## Diagram Requirements

- The customer must pass authentication (a PIN check) before any withdrawal.
- The diagram shows both PIN outcomes: correct and incorrect.
- Failed attempts are counted, and the customer is rejected once the counter passes the limit.
- The account closes when the balance reaches zero.
- State boxes use `entry/Action` and `exit/Action`.
- Transitions are labeled `Event [guard] / action`.
