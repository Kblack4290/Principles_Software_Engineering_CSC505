# Lessons Learned Reflection: Outline

CSC505 Module 8 Portfolio Project (CSC505_M08_PP)

**Assignment:** A 2–3 page summary of the lessons learned in this course, how they apply to real-world problems or a specific real-world application, and how they have affected your life. APA format per the CSU Global Writing Center, with at least two credible references besides the textbook.

**Length budget:** 2–3 pages double-spaced is roughly 600–900 words of body text, not counting the title page or references. That is about 130–170 words per body section below. Keep each module's lesson to two or three sentences and spend the extra words on application.

**Rubric targets:**

- **Content (75):** Every module is named, and each one is correctly tied to a reading.
- **Synthesis & Evaluation (60):** Group modules into themes. Do not write one paragraph per module.
- **Problem Solving (60):** Tie each theme to a real problem, such as the ATM project, your coursework projects, or your new AI role at work.
- **Organization (25):** Introduction, body, and conclusion.
- **APA (10):** Use a title page, in-text citations, and a hanging-indent reference list.

**Voice notes, based on your Module 2 and Module 4 papers:**

- Open each section with a plain topic sentence.
- Introduce sources as "Pressman and Maxim (2020) describe/point out/warn that…"
- Use first person only in the application and "how it affected me" parts.
- Keep paragraphs short and concrete. Give an example ("A developer who says… in week one…") rather than an abstract claim.

---

# Working Title: Lessons Learned in Principles of Software Development

## Section 1: Introduction

**Topic sentence:** Before this course I treated software development as writing code that works. Eight modules later, I see it as an engineering discipline in which process, people, requirements, design, and quality all decide whether that code is worth anything.

**Structure/flow:**

1. Open with one short paragraph.
2. State the definition that framed the course.
3. Preview the four themes that the body covers.
4. End with a thesis stating that the lessons apply directly to the ATM project and to your new AI-focused role.

**Key points:**

- IEEE defines software engineering as a systematic, disciplined, quantifiable approach to development and maintenance.
- Software engineering is a layered technology with quality as its focus and process as its foundation.
- Thesis preview: process → people and agility → requirements and design → quality, security, and testing.

**Sources cited here:**

- Pressman & Maxim (2020), p. 9 (course page 1.2): the IEEE definition and the layered technology, with its quality focus and process foundation.

---

## Section 2: Process Before Code (Modules 1–2)

**Topic sentence:** The first lesson was that software needs a process because, unlike hardware, it does not wear out but keeps changing, and unmanaged change is what makes it deteriorate.

**Structure/flow:**

1. Module 1: what software is.
2. Module 2: why process models exist and how the Waterfall model breaks down.
3. Application: your own Black Adaptive Model and the Module 1 task tracker refactor.
4. This section sets up Section 3: if requirements change, the process has to absorb change.

**Key points:**

- **Module 1:** Software is logical, it does not rust, and legacy systems are costly to maintain and need constant modification. The seven software categories show that one approach does not fit every domain.
- **Module 1 application:** Instructor feedback on the task tracker (missing docstrings, a long if/elif chain) taught you that code that "works" is not finished. You refactored it into a dispatch table, which is maintainability in practice.
- **Module 2:** Waterfall's three weaknesses, which you identified yourself: frozen requirements, late testing, and late customer visibility.
- **Module 2 application:** The Black Adaptive Model combined proven process patterns rather than inventing a new model. Hachemi (2020) calls this process pattern reuse for modification.

**Sources cited here:**

- Pressman & Maxim (2020), p. 7 (course page 1.1): software categories and legacy software cost.
- Pressman & Maxim (2020): Waterfall limitations. Reuse the citations from your Module 2 paper.
- Hachemi (2020), Section 2, "Process Patterns Reuse," pp. 37–38: process patterns reuse, including reuse for modification of an existing model.

---

## Section 3: Agility and the People Who Build Software (Modules 3–4)

**Topic sentence:** Modules 3 and 4 showed that the answer to change is short feedback loops run by people who trust each other, not more documentation.

**Structure/flow:**

1. Module 3: agility, Scrum, and prototypes as the mechanism for feedback.
2. Module 4: the human side, meaning traits and team structure.
3. Real-world example: Kabbur et al.
4. Transition: feedback loops only work if the team knows what it is building, which leads to Section 4.

**Key points:**

- **Module 3:** The Agile values (individuals and interactions, working software, customer collaboration, responding to change), the Scrum sprint cycle, and prototypes as a cheap way to get customer feedback before construction. Your shopping list prototype is the example.
- **Module 4:** The traits that matter, such as brutal honesty, adaptability, and collaboration. Team-level communication matters as much as individual skill.
- **Real-world:** In Kabbur et al. (2020), each Scrum team met its own goals while the overall project was still failing, because the teams thought in silos. Peer accountability, shared goals, and visible scorecards turned this around.
- **Personal:** Relate this to being "the go-to AI person" at work. Being honest about what a tool can't do yet is the brutal-honesty trait.

**Sources cited here:**

- Beck et al. (2001), the Manifesto for Agile Software Development: the four values. Optional, and counts as a credible non-textbook reference.
- Pressman & Maxim (2020): Agile, Scrum, and prototyping. Reuse your Module 3 citations.
- Pressman & Maxim (2020): engineer traits and team communication. Reuse your Module 4 paper's citations.
- Kabbur et al. (2020), Section 4.3, "Increasing attention to results," p. 69: silo thinking, scorecards, and weekly project reviews.

---

## Section 4: Knowing What to Build and How to Structure It (Modules 5–7)

**Topic sentence:** Requirements and design turned out to be where most failures are prevented, because an error caught in a use case or a component interface costs far less than one caught in running code.

**Structure/flow:**

1. Module 5: requirements engineering and use cases.
2. Module 6: design concepts and architecture.
3. Module 7: component-level design, UI, and UX.
4. Tie all three to the ATM diagram, which is a requirements-and-design artifact before it is code.

**Key points:**

- **Module 5:** Requirements engineering covers elicitation, analysis, specification, validation, and management.
  - Your PHTRS use case diagram forced you to state assumptions explicitly, such as Login as an `<<include>>` and Upload Photo as an `<<extend>>`. This is your best concrete example.
  - Chanin et al. (2019): collaboration improves requirements gathering because no one person sees every requirement.
- **Module 6:** Design concepts: abstraction, modularity, information hiding, and functional independence.
  - Agile teams still need architecture for complex systems. They can use a "walking skeleton" architectural prototype.
  - Architecture decisions drive the system's nonfunctional qualities.
- **Module 7:** Components should be cohesive, encapsulated, and loosely coupled.
  - The UI golden rules: place the user in control, reduce memory load, and be consistent.
- **ATM tie-in:** In the ATM state diagram, each state is a cohesive unit with clear entry/exit actions. Labeling transitions as `Event [guard] / action` is precise requirements specification, for example `CheckPin [incorrect PIN] / increment error counter`.

**Sources cited here:**

- Pressman & Maxim (2020): requirements engineering and use cases. Reuse your Module 5 citations.
- Chanin et al. (2019), Section IV, "Conclusions," p. 32: collaborative practices enhance requirements gathering.
- Pressman & Maxim (2020), p. 186 (course page 6.3): architectural prototype or "walking skeleton."
- Pressman & Maxim (2020), p. 196 (course page 6.4): scope of architecture decisions.
- Pressman & Maxim (2020) (course pages 6.2, 7.1–7.3): the design concepts list and the UI golden rules.

---

## Section 5: Quality Is Built In, Not Tested In (Module 8)

**Topic sentence:** The final module brought the course together: quality is not a phase at the end but an umbrella over every activity, and security and testing have to be planned from the start.

**Structure/flow:**

1. Definition of quality.
2. SQA as an umbrella activity.
3. Security risk and threat modeling, applied to the ATM.
4. Testing strategy, applied to your Python script.
5. This section bridges into the conclusion.

**Key points:**

- **Quality:** An effective process that creates a useful product with measurable value for producers and users. McCall's factors cover product operation, revision, and transition.
- **SQA:** An umbrella activity applied throughout the software process, covering standards, reviews and audits, testing, change management, security management, and more.
- **Security, applied to the ATM:** Threat modeling defines attackers' abilities and goals. Map the ATM to STRIDE:
  - **Spoofing → authentication:** the PIN check.
  - **Denial of service and brute force:** the failed-attempt counter and its rejection limit.
  - **Integrity:** closing the account at zero balance prevents invalid withdrawals.
  - Your diagram's requirements are security controls.
- **Testing:** Testing moves from unit to integration to validation to system tests. Verification asks whether you built the product right; validation asks whether you built the right product.
- **Testing applied:** Your ATM script should be tested on both PIN outcomes and on the lockout and zero-balance paths, not only the happy path.
- **Callback:** This answers the Waterfall "late testing" weakness from Section 2.

**Sources cited here:**

- Pressman & Maxim (2020), pp. 313–314 (course page 8.1): definition of quality and McCall's factors.
- Pressman & Maxim (2020), pp. 341, 343 (course page 8.2): SQA as an umbrella activity and its elements.
- Pressman & Maxim (2020), pp. 365–366 (course page 8.3): the NIST RMF steps, threat modeling, and STRIDE.
- Pressman & Maxim (2020), pp. 374, 377 (course page 8.4): testing strategy and the testing steps.
- Optional, for a stronger security citation: Shostack (2014), *Threat Modeling: Designing for Security*, which is the STRIDE source book. Only add it if you can access it.

---

## Section 6: Applying These Lessons and How They Affected Me

**Topic sentence:** The clearest sign that these lessons stuck is that I now use them at work, where my new AI-focused role means building tools and features end to end for other people.

**Structure/flow:**

1. Make this the "how has it affected your life" section the rubric asks for.
2. Write it in first person.
3. Use two or three concrete examples.
4. This is where the Problem Solving and Synthesis points are earned.

**Key points (choose two or three that are true for you):**

- **Requirements first:** You now ask "who are the actors and what are the use cases?" before building an AI tool or agent for a team workflow.
- **Iterate with feedback:** Ship a small version, demo it, and adjust. This is the Black Adaptive Model and Scrum applied to internal tools.
- **Quality and security from day one:** AI tools touch company data, so threat modeling and SQA thinking apply directly. Ask who could misuse the tool and what data it can reach.
- **People:** As the person others come to for AI, the Module 4 traits apply daily: honest limits, adaptability, and sharing knowledge instead of hoarding it.
- **Personal habit change:** You now write docstrings and READMEs and state your design assumptions. Your Module 5 README is evidence of this.

**Sources cited here:**

- No new source is needed. Briefly refer back to concepts already cited, for example "(Pressman & Maxim, 2020)" for SQA and "(Kabbur et al., 2020)" for team trust.

---

## Section 7: Conclusion

**Topic sentence:** Software engineering is less about any single technique than about a chain in which process, people, requirements, design, and quality each depend on the one before it.

**Structure/flow:**

1. Write one short paragraph.
2. Restate the chain.
3. Name the ATM project as the place where all of it met.
4. Close with how you will carry it forward in your master's program and at work.
5. Do not add new citations here.

**Key points:**

- The ATM diagram and script combine requirements, design, security controls, and testable behavior.
- The biggest single takeaway: quality is planned, not inspected in at the end.

---

## Reference List (Draft, APA 7)

Verify every entry against the actual source before submitting. These details come from the PDFs in the course project.

Beck, K., Beedle, M., van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., Grenning, J., Highsmith, J., Hunt, A., Jeffries, R., Kern, J., Marick, B., Martin, R. C., Mellor, S., Schwaber, K., Sutherland, J., & Thomas, D. (2001). *Manifesto for agile software development*. https://agilemanifesto.org/

Chanin, R., Pompermaier, L., Sales, A., & Prikladnicki, R. (2019). Collaborative practices for software requirements gathering in software startups. In *Proceedings of the 12th International Workshop on Cooperative and Human Aspects of Software Engineering* (pp. 31–32). IEEE. *(Confirm the year, venue, and DOI from the PDF's footer or the library record.)*

Hachemi, A. (2020). Software development process modeling with patterns. In *Proceedings of the 2020 2nd World Symposium on Software Engineering (WSSE '20)* (pp. 37–41). Association for Computing Machinery. https://doi.org/10.1145/3425329.3425339 *(Confirm the end page.)*

Kabbur, P. K., Mani, V. S., & Schuelein, J. (2020). Prioritizing trust in a globally distributed software engineering team to overcome complexity and make releases a non-event. In *Proceedings of the 15th IEEE/ACM International Conference on Global Software Engineering (ICGSE '20)* (pp. 66–70). Association for Computing Machinery. https://doi.org/10.1145/3372787.3390434

Pressman, R. S., & Maxim, B. R. (2020). *Software engineering: A practitioner's approach* (9th ed.). McGraw-Hill Education.

---

## Source Fit Check

**Strong fits.** Each of these supports a specific claim and is credible:

- Pressman & Maxim (2020)
- Kabbur et al. (2020): a real-world team case
- Hachemi (2020): process patterns, and it connects to your Module 2 model
- Chanin et al. (2019): collaborative requirements gathering

These three give you the required two-plus non-textbook references. You have used Kabbur and Hachemi in earlier modules, so the citations are already familiar to you.

**Weak or no fit for a scholarly reference list:**

- **GeeksforGeeks, "Requirements Engineering Process."** It covers RE stages clearly, but it is a tutorial site, not a credible scholarly source. Use it for your own understanding, but don't cite it as one of your two credible references.
- **Tutorials Point, "User Interface" and "Software User Interface Design."** These have the same problem. The UI golden rules they list originate with Shneiderman and Plaisant. Cite the textbook's version of the UI rules instead.
- **Ren et al. (2020), "Toward Gamification to Software Engineering."** It is about motivating engineers through gamification, which doesn't line up with any lesson above. Leave it out unless you want a sentence on team motivation in Section 3.
- **Pluralsight "20 Patterns" ebook.** It is vendor marketing material. Don't cite it.
