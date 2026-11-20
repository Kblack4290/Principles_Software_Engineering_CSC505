# Module 5 Critical Thinking: PHTRS Use Case Diagram and Summary Script

## Files

| File | Description |
| --- | --- |
| `phtrs_summary.py` | Python script that defines the actors, use cases, and relationships from the diagram and prints a summary |
| `phtrs_use_case_diagram.png` | UML use case diagram exported from UMLet |
| `phtrs_use_case_diagram.uxf` | Editable UMLet source for the diagram |
| `phtrs_summary_output.png` | Screenshot of the script running successfully |
| `README.md` | This file |

## How to Run

1. Open a terminal in this folder.
2. Run `python phtrs_summary.py`

## Design Assumptions

The brief describes four interfaces but leaves some behavior open, so I state each choice below as an assumption.

1. **Actors.** The diagram shows three primary actors (Citizen, Public Works Admin, and Repair Crew) and one secondary actor, the Notification Service. The brief never mentions notifications, so the Notification Service is an addition. It sends a confirmation for Report Pothole, a receipt for Submit Damage Claim, and messages for Assign Repair Crew and Update Repair Status.
2. **Login.** Every actor who uses a protected function signs in. The brief says citizens log on to report potholes and that the Admin interface is login-based, so I assumed crews sign in as well. Log In is an `<<include>>` of every use case that needs a signed-in user. The Notification Service does not sign in.
3. **Shared use case.** Both the Admin and Crew interfaces update repair status, so Update Repair Status is associated with both actors. Logging hours and filler material used is treated as part of this use case, not as separate use cases, to keep the diagram at its core functions.
4. **Optional photo.** Upload Photo is an `<<extend>>` of Report Pothole because the image is optional. Evidence upload for damage claims is treated as part of Submit Damage Claim.
5. **Admin functions.** View/Filter Potholes, Assign Repair Crew, and Generate Reports are Admin-only. The brief does not say what the reports contain, so I assumed summaries by district, priority, status, and repair cost.
6. **Out of scope.** The brief says damage claims route to the department's claims processing system. That system is not modeled as an actor, and neither are the system's own calculations (district from address, priority from size, and repair cost), which happen inside the use cases that need them. A use case diagram shows the system from the outside and does not say how a use case is carried out (Tutorials Point, 2020). It also shows only functional requirements, meaning what the system does. Qualities such as performance, reliability, usability, and security are non-functional requirements and are not drawn (GeeksforGeeks, 2026).
7.ra **Script.** The `associations`, `includes`, and `extends` lists in the script match the lines in the diagram. The `check_model` function raises an error if the script refers to an actor or use case that is not defined.

## References

GeeksforGeeks. (2026, January 25). *Requirements engineering process in software engineering*. https://www.geeksforgeeks.org/software-engineering/software-engineering-requirements-engineering-process/

Tutorials Point. (2020). *UML use case diagrams*. https://www.tutorialspoint.com/uml/uml_use_case_diagram.htm
