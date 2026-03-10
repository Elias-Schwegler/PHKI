# PHKI – Week 04: Critical Theory
**Module:** Philosophy, Art, and Artificial Intelligence (PHKI, HSLU FS26)
**Date:** 10.03.2026 | **Lecturer:** Catherine Hayden (CH)
**Topic:** Critical Theory – Bias, Ideology, and Power Embedded in Data and Algorithms

---

## 🎯 Learning Objectives

By the end of this week, students should be able to:

- **Explain** how data and algorithms can reproduce social biases and shape who benefits and who is marginalised or disproportionately affected.
- **Identify** who is represented, misrepresented, or invisible in real-world AI applications (e.g., facial recognition technologies, hiring systems).
- **Apply** a critical theory lens to analyse an algorithmic system, considering issues such as power, ideology, and structural inequality.
- **Critically assess** the regulatory and ethical limits of AI technologies (EU DSA, EU AI Act).
- **Connect** the hidden labour theme from Week 3 to the broader question of what else is hidden inside AI systems.

---

## 🧠 Key Concepts & Definitions

| Concept / Term | Definition | Origin / Thinker | Relevance to AI |
|---|---|---|---|
| **Critical Theory** | A framework that analyses how power operates in modern societies. It aims to unmask, critique, and transform the ideologies and power structures that govern societies. | Frankfurt School (Celikates & Flynn, 2023; Shuster, 2024) | Gives us language to ask *whose* patterns AI learns, *who* they benefit, and *who* they harm. Bias in algorithms is not a neutral glitch but reflects deliberate human choices. |
| **Ideology** | The set of taken-for-granted beliefs about what is "normal" or "possible," shaped by social structures and power relations. It can make certain harms hard to see or question. | Critical Theory / Sociology | Makes algorithmic harm invisible: if a biased training dataset "just reflects reality," the structural cause of that bias is never challenged. |
| **Algorithmic Bias** | Systematic and repeatable errors in a computer system that create unfair outcomes, such as privileging one arbitrary group over others. | AI Ethics / Kate Crawford / Joy Buolamwini | When AI is trained on skewed historical data, it amplifies these biases at scale — with measurable harm in facial recognition, hiring, and criminal justice. |
| **Word Embeddings** | Mathematical representations of words as vectors of numbers, capturing semantic relationships. Early models (Word2Vec) used one fixed vector per word; modern models (BERT) produce context-dependent embeddings. | NLP / Bolukbasi et al. (2016); Zhang et al. (2025) | Researchers found these vectors capture and amplify social stereotypes present in training data (e.g., "Man is to computer programmer as woman is to homemaker?"). |
| **Structural Inequality** | A condition where social systems, institutions, and norms disadvantage some groups and advantage others in a persistent, self-reinforcing way. | Sociology / Critical Theory | AI systems do not create inequality from scratch but take existing structural inequalities and automate them at scale, distributing errors and harms unevenly. |
| **EU Digital Services Act (DSA)** | EU regulation requiring large platforms to identify and reduce risks from illegal content, including non-consensual sexual deepfakes. | European Union (2022) | The Grok/X case tests whether such regulation can be effectively enforced against powerful AI companies. |
| **EU AI Act (Article 5)** | EU law that, among other things, prohibits the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage. | European Union | An explicit legal response to facial recognition bias, making some deployments of this technology illegal. |

---

## 💡 Philosophical Arguments & Positions

### Argument 1: AI Bias Is Not a Neutral Technical Glitch — It Is a Manifestation of Structural Power

- **Thesis:** Biased algorithms reflect deliberate (often unchecked) human choices about which data is collected, whose problems the system is designed to solve, and what counts as "fair" or "accurate."
- **Reasoning:** AI datasets are snapshots of society. A dataset scraped from the internet mirrors historical inequalities: publicly available images of faces are 77.5% male and 83.5% white (Kate Crawford, cited in Mitchell, 2020), because online images skew toward the famous and powerful.
- **Counter-arguments:** Some developers argue that models simply reflect reality objectively, and that "un-biasing" a dataset is a subjective political intervention — who decides what "fair" representation looks like?
- **Application to AI:** We must treat bias as a *systemic design problem*, not a bug to be patched. Choosing which data to collect, and for whose benefit, is itself a political act.

### Argument 2: Technologies Are Deployed Within Existing Power Structures, Not Neutrally

- **Thesis:** The risks and errors of an AI system are distributed unevenly across society, disproportionately harming marginalised groups.
- **Reasoning:** The Gender Shades study (Buolamwini & Gebru, 2018) showed error rates for commercial facial recognition reached up to 34.7% for darker-skinned women, versus near-perfect accuracy for lighter-skinned men. Despite this being public knowledge for years, governments still expand police use of these systems (UK, 2025–2026).
- **Counter-arguments:** Proponents argue that even imperfect technology assists in crime prevention, and that human officers always have final authority. The UK police stated: "officers made the final decision."
- **Application to AI:** Poses the critical question — if technology "flags" a suspect and an officer "confirms" the match, where does decision-making power actually lie? Who bears the consequences when it goes wrong?

### Argument 3: "Intelligence" Is an Ideological Label That Deflects Responsibility

- **Thesis:** Labelling an AI output as "intelligence" shifts perceived authority away from human decision-makers toward the machine, making it easier to avoid accountability.
- **Reasoning:** In the UK wrongful arrest case (Feb 2026), police stated the AI "provided intelligence" while claiming human officers made the final call. This linguistic framing subtly masks systemic failure behind algorithmic authority.
- **Counter-arguments (from class discussion, notes.md):** Kant's categorical imperative demands critical thinking at every step. Accepting AI-generated "intelligence" uncritically violates the imperative to reason for oneself. As discussed in class: *"using a non-deterministic system and then believing it wholeheartedly — Emmanuel Kant would get up from his coffin."*
- **Application to AI:** Systems used in high-stakes decisions (policing, sentencing) should be open-source, transparent, and independently auditable. The police's argument that "we relied on intelligence" is insufficient justification.

### Argument 4: Societal Biases in AI Are Not Always Simply "Wrong" — But Scale and Context Matter (Class Discussion, notes.md)

- **Thesis:** Some degree of contextual bias in AI outputs may be demographically appropriate (e.g., using regional cultural representations), but systematic bias that causes harm at scale is a fundamentally different problem.
- **Reasoning (from class):** A student raised that AI outputs representing a "blond, six-foot man" in the context of Asian users would be wrong the other way around. Social context matters. However, who decides where "appropriate cultural representation" ends and "harmful stereotyping" begins?
- **Counter-arguments:** "Society should decide what's fair, but in the end it is the investors who have the longest handle" (class discussion). People may also not fact-check enough, falling unintentionally for political biases embedded in algorithmic outputs.
- **Application to AI:** Design decisions cannot be purely technical — they require democratic input, cross-cultural consultation, and transparency about who funded and designed the system.

### Argument 5: Needless Suffering Exists Because of How We Have Organised Society — and It Can Be Changed

- **Thesis:** Critical Theory's core claim: suffering produced by biased AI is not natural or inevitable. Because humans made the systems, humans can remake them.
- **Reasoning:** The 2018 Gender Shades study exposed the problem. The 2020 *Coded Bias* documentary brought it to a mass audience. Yet biased facial recognition systems continue to be deployed by police in 2025–2026. This is a political choice, not technical necessity.
- **Application to AI:** Demands not just technical fixes but structural reforms: mandatory transparency, external audits, democratic input into deployment decisions, and outright bans in the highest-risk contexts.

---

## 🎨 Art & Media References

| Work / Reference | Creator | Year | Medium | Relevance to Week's Theme |
|---|---|---|---|---|
| **Coded Bias** | Shalini Kantayya | 2020 | Documentary (Netflix) | Follows researcher Joy Buolamwini's discovery of racial bias in facial recognition algorithms and links it to civil rights, surveillance, and calls for new regulation. Essential viewing for Assignment 2. |
| **Gender Shades Study** | Joy Buolamwini & Timnit Gebru | 2018 | Academic Paper | Foundational study showing error rates up to 34.7% for darker-skinned women (vs. near-perfect for lighter-skinned men) in commercial systems from Microsoft, IBM, and Face++. |
| **"Man is to computer programmer as woman is to homemaker?"** | Bolukbasi et al. | 2016 | Academic Paper | Revealed that Word2Vec embeddings trained on Google News data encoded strong gender stereotypes. Seminal paper on bias in word embeddings. |
| **Empire of AI** | Karen Hao | 2025 | Book | Detailed account of the Sama/OpenAI/Meta content moderation cases — hidden, traumatic labour powering AI's "magic." |
| **Inside Facebook's African Sweatshop** | Billy Perrigo | 2022 | TIME Magazine Article | Exposed Sama's moderation operations for Meta: $1.50/hour wages, psychological trauma, unionisation suppression. |
| **Grok AI Tool (X/Twitter)** | Elon Musk / X | 2026 | Generative AI Tool | In early 2026, users discovered Grok could "undress" people and generate non-consensual sexual imagery. Triggered EU DSA investigation and geoblocking response. |
| **Meta Smart Glasses** | Meta + Sama | 2026 | Consumer Hardware / AI | Data annotators at Sama (a Meta subcontractor) reviewed intimate home video footage from users' smart glasses, raising serious consent and privacy ethics questions. |
| **ChatGPT Image Prompts (University Students)** | PHKI Class / CH | 2025–2026 | AI Image Generation | Prompts about "girls walking into a university campus" used in class to demonstrate how AI generates racially homogenous, predominantly white outputs — a live demonstration of training data bias. |

---

## 🖼️ Key Slide Visuals — Image Analysis

These images carry argumentative content beyond the text. Each was deliberately chosen by the lecturer to make a philosophical point.

### Image Set 1: The Hidden Labour Triptych (Slide 8, GPT-generated via ChatGPT 5.2 / Perplexity Pro)

The slide used three AI-generated images in sequence to expose the visual ideology embedded in AI itself:

| Image | Prompt Used | What It Shows | What It Reveals |
|---|---|---|---|
| **Image A** | *"Generate an image showing a typical person who works in the field of AI"* | A young, white, bespectacled man in a stylish open-plan office smiling at a laptop, with code on screens — clean, comfortable, clearly Western | AI's *default image* of AI work is affluent, white, male, and tech-polished. The bias is not hypothetical — it is literally the first thing the model produces. |
| **Image B** | *"Generate an image showing invisible remote digital labour"* | A brown-skinned woman with headphones working alone at night, labelling images (video thumbnails visible on screen) in dim, modest surroundings | The prompt forces the model to acknowledge the hidden layer — but note that even "invisible" labour is still depicted in a clean, warm domestic setting, not in a bare office in Nairobi. |
| **Image C** | *"Now edit this image to take into account the hidden cost of AI labour"* | The same woman, now visibly exhausted, head in hand, screen showing "WARNING: Your account has been banned" and "MISLABELED DATA: Your task has been rejected" alerts | The final image shows the psychological toll: rejection, anxiety, precariousness. The NDA-bound worker, paid $1.50/hour, who produces one error gets flagged. The suffering is now visible — but only because we explicitly demanded it. |

> **Critical insight:** The triptych is a meta-demonstration of the entire week's argument. The model's *first* response (Image A) is the ideological default. Only by iteratively and explicitly demanding acknowledgement of invisible labour does the model produce the uncomfortable truth (Image C). This mirrors exactly how Critical Theory works: you must push past the surface "normal" to reveal the structural reality underneath.

---

### Image: Word Embedding Vector Diagram (Slide 18, hand-drawn educational diagram)

A hand-drawn sketch illustrating how word embedding systems map relationships between words as vectors in geometric space:

- **Blue arrows (gender axis):** `man → woman`, `him → her`, `he → she` — all pointing in the same direction, demonstrating a consistent learned "gender direction" in the vector space.
- **Occupational bias:** `doctor` sits close to `he/man`, and has an arrow implicitly pointing toward `nurse` (following the gender direction). The model encodes the stereotype: "doctor" defaults male, "nurse" defaults female.
- **Neutral semantic relation:** `cat → dog` (drawn in pink/red) shows a relationship of *similarity* (both are domestic animals) — a benign, non-biased semantic link for contrast.

> **Critical insight:** The diagram makes abstract mathematics viscerally concrete. The gender bias is not metaphorical — it is *literally encoded as a direction in mathematical space*. The model learns that the vector from "computer programmer" to "woman" is the same direction as from "doctor" to "nurse." This is a mathematical representation of social power.

---

### Image: The AI Bias Iceberg (Slide 24)

A visual metaphor showing three layers of AI bias as an iceberg:

| Layer | Visibility | Description |
|---|---|---|
| **Computational Biases** | *Above water (Visible)* | The "tip" — measurable technical errors like unequal accuracy rates. These are the only biases typically acknowledged in public discourse. |
| **Human Biases** | *Below waterline* | The mid-section — the prejudices, assumptions, and value systems of the engineers, researchers, and product managers who built the system. |
| **Systemic Biases** | *Deepest, fully submerged (Invisible)* | The root cause — historical power structures, economic inequalities, and social norms baked into the very data the system was trained on. |

> **Critical insight:** Most AI ethics debates focus only on the visible tip — "can we patch the accuracy gap?" Critical Theory demands we ask about the submerged mass: whose society generated this training data? Whose power relations are encoded in the "invisible" systemic layer? Fixing the tip without addressing the bottom is treating symptoms, not causes.

---

### Image: The "Mystery Prompt" White Nuclear Family (Slide 23, AI-generated)

The slide asks: *"What do you think the original prompt was?"* and shows an AI-generated image of a **white, red-haired boy, a white blonde girl, a white man and white woman** — all smiling, in front of a rural Irish thatched cottage — wearing green, surrounded by flowers. The image is hyper-idealised: green rolling hills, perfect teeth, cosy rustic home.

- **The original prompt** was likely something like *"a happy family"* or *"a family in the countryside"* — no ethnicity or location specified.
- The model's default "generic family" is white, Western European, and affluent-rural. There is no ambiguity about which demographic is the AI's idea of a baseline human family.

> **Critical insight:** This connects directly back to the Crawford/Mitchell data: training datasets are 83.5% white because online images skew toward visible, powerful, and famous people in Western countries. The model doesn't think "white Irish family" — it thinks *"family"*. Whiteness has been encoded as the invisible default, the unmarked category.

---

### Image: Mark Zuckerberg — Facial Recognition Tag (Slide 28)

A photograph of Mark Zuckerberg with a white facial recognition bounding box around his face and a tooltip label reading **"Mark Zuckerberg"** with a forward arrow — as if from a consumer facial recognition app.

> **Critical insight:** Using Zuckerberg himself — the founder of a platform that has faced major facial recognition lawsuits and regulatory actions — is an ironic and pointed choice. It raises immediate questions:
> - What about men *without* Zuckerberg's power and resources when a facial recognition system incorrectly tags them?
> - The system works fairly well on a high-profile, white, male face. What are its error rates on darker-skinned, less photographed individuals? (Up to 247× higher false positives for Black women vs. white men, per Buolamwini & Gebru.)
> - The UI design (clean, confident label, a clickable "next" arrow) implies certainty and authority — masking the probabilistic, unreliable nature of the technology underneath.

---

## 🗣️ Discussion Building Blocks

### Pro-arguments

- **For regulating AI datasets:** "Because AI models are deployed at scale, allowing them to train freely on biased historical internet data automates and amplifies systemic inequality. Proactive regulation — including mandatory dataset audits — is necessary to prevent measurable harm."
- **For holding companies accountable:** "If an AI system has documented, statistically significant racial bias and a company deploys it for police use regardless, this is not a technical oversight — it is a choice. Those making that choice must bear legal and moral responsibility for its consequences."
- **For transparency and open-sourcing:** "Police-facing AI should be open-source and independently audited, so that its error rates can be scrutinized by the public, the press, and civil rights organisations — not only by the vendor."

### Counter-arguments

- **Against perfect dataset curation:** "There is no neutral baseline. Every act of 'de-biasing' a dataset reflects someone's value judgement about what 'fair' representation looks like. Who has the authority to impose that vision universally across cultures?"
- **Against outright bans:** "Even a biased tool with a 5.5% false positive rate for Black subjects may, on some arguments, outperform unaided human recognition. Banning imperfect AI may not improve outcomes — it may just shift the burden back to human prejudice, which is less measurable."
- **For contextual representation:** "Some demographic customisation in AI outputs may be culturally appropriate — e.g., different default human representations for different regional contexts. The problem is systematic harm, not all forms of variation."

### Bridging Statements

- "While eliminating all bias from training data is impossible, acknowledging which specific, measurable harms occur — and in which high-risk domains — enables us to draw principled lines about where AI deployment must be restricted."
- "The technology is not the problem in isolation; the problem is deploying a technology with known, documented bias in contexts where its errors carry catastrophic consequences for real people."
- "Responsibility does not rest solely with the user. Governments, regulators, and corporations must share accountability — otherwise, labour (and harm) will simply be offshored to wherever laws are most flexible." *(class discussion, notes.md)*

### Critical Questions for Discussion & Micro-viva

- "If we know a facial recognition system has discriminatory error rates by race and gender, should we improve the training data, restrict its use, or ban it entirely in policing contexts? What threshold of accuracy should be required?"
- "When an AI makes a biased mistake, who is responsible — the training data labeller, the developer, the procuring institution, the officer who relied on it, or the government that allowed its deployment?"
- "Does the invisibility of AI's training data labour and its decision-making processes matter morally in itself — or only when specific harmful outcomes occur?"
- "Can a technology that 'just provides intelligence' ever be truly neutral? And if officers always make the final call, why introduce an AI flag at all?"

---

## 🔗 Thematic Connections

| This Week's Topic | Connects To | How |
|---|---|---|
| **Structural Power & Ideology** | Hidden Labour (W3) | Just as invisible human labour powers AI, hidden ideologies shape *how* AI makes decisions and *whose* problems it prioritises. Both forms of invisibility serve to concentrate power and deflect accountability. |
| **Facial Recognition Bias** | The Turing Test & Anthropomorphism (W2) | We assume machines "see" objectively, just as we once assumed the Imitation Game would reveal true machine "thought." Both assumptions are challenged by the reality that AI systems fail when tested against the full range of human diversity. |
| **Regulation vs. Innovation** | AI Cold War (W3) | The "move fast and break things" philosophy directly conflicts with the EU's DSA and AI Act. The geopolitical race to AI dominance creates systemic pressure to deploy systems before their biases and harms are fully understood. |
| **Who Decides What Is "Fair"?** | Human Agency & Authenticity (W1) | The debate about who curates "fair" training data reflects the same question posed in W1: who has the authority to define what is authentically human, and whose definitions are privileged? |
| **Algorithmic Bias in Hiring** | AI in Education (upcoming, W5) | Just as bias shapes who facial recognition systems "see," bias in hiring algorithms shapes who gets opportunities. Both affect life outcomes in measurable ways, with marginalised communities bearing disproportionate risk. |

---

## 📋 In-Class Activities Summary

### Activity 1: Can AI Be Regulated? — The Grok Example
- **Description:** Students analysed the January 2026 case where X's Grok AI tool was discovered to "undress" people in images and generate non-consensual sexual content. The EU Digital Services Act investigation was discussed alongside Musk's partial geoblocking response.
- **Purpose:** Test the claim that "AI cannot be regulated" against a live real-world case.
- **Key takeaway:** Regulatory action can produce change (Grok's image tools were restricted) but enforcement gaps remain. Regulation is possible, but enforcement at speed is structurally difficult.
- **Positions that emerged:** Some students felt the response showed regulation works; others argued the restrictions were minimal, jurisdiction-limited, and easily circumvented.

### Activity 2: Ethical Boundaries — Meta Smart Glasses
- **Description:** Students read a NYT/SVD article about data annotators at Sama (a Meta subcontractor) reviewing intimate private home footage captured by Meta Ray-Ban smart glasses. Discussion on informed consent and ethical limits.
- **Purpose:** Bridge Week 3's hidden labour theme to Week 4's ethics-of-data questions.
- **Key takeaway (class discussion, notes.md):** Invisibility of labour is not inherently wrong if workers are treated fairly — the problem is the combination of hidden labour *and* exploitative conditions. Responsibility lies not only with the user but with governments and companies; otherwise, labour will be offshored to wherever regulations are least demanding.

### Activity 3: AI Image Generation — Observing Bias Live
- **Description:** Students were shown ChatGPT-generated images responding to prompts like "Create an image of a group of girls walking into a university campus." The class observed the outputs: predominantly white, Western-looking figures.
- **Purpose:** Demonstrate how training data bias produces homogenised AI outputs in real time.
- **Key takeaway:** AI does not invent stereotypes — it amplifies patterns present in training data. The question "What do you think the original prompt was?" highlighted how AI outputs can be read backwards to infer what was in the data.

### Activity 4: UK Wrongful Arrest — Critical Theory Lens
- **Description:** Students analysed the February 2026 case of an Asian man wrongfully arrested for a burglary 100 miles from his home, based on a biased facial recognition match. Applied critical theory's three axes: power, ideology, structural inequality.
- **Positions from class discussion (notes.md):**
  - Police officers may make insufficiently informed decisions; no systematic double-checks → false positives with severe real-world consequences.
  - People already regarded differently by society suffer more from false positives in sensitive industries.
  - The police argument that they "relied on intelligence" is not a sufficient excuse — either the intelligence quality must be improved dramatically, or the technology must be made open-source, transparent, and independently validated.
  - Cleaning biases from neural networks is likely the best path forward — but treating a non-deterministic system as infallible contradicts the Kantian imperative to think critically.

### Activity 5: Societal Biases — Discussion (notes.md)
- **Key positions from class:**
  - It is getting better, but bias is still present. Systems should be maximally truth-seeking.
  - Design-wise, it may not be worth pursuing radical "de-biasing" if users are repulsed by overly curated content. People prefer some degree of affirmation, but to a healthy extent — complete removal of all perspective may feel unnatural.
  - Societal biases may even be required depending on demographic and regional context (e.g., showing culturally relevant representations vs. imposing Western defaults on non-Western users).
  - Society should decide what is "fair" in principle, but in practice it is investors who have the greatest power. Users may not fact-check enough, making them susceptible to political and cultural biases embedded algorithmically.

---

## 🏆 Assignment 1 Deep Dive: Digital Projects — Applying This Week's Themes (40%)

> **This is the most directly relevant week for Assignment 1.** Pages 14 and 36 of the lecture slides are explicitly titled "Links to themes that might be useful for Assignment 1." Use this section as a detailed roadmap for your report.

### The Core Insight from This Week

**Technologies depend on human labour.** During the Industrial Revolution, the workers who made industrialisation possible — children in mines, women in mills — were often completely invisible. When you use AI to create your art, something similar is happening: someone labelled training data, someone moderated content at $1.46–$3.74/hour, someone bore psychological trauma so the model could be "safe." That labour is hidden behind the interface.

**The same applies to bias.** The model was trained on data — data that reflects who is powerful and visible on the internet. The model did not invent its stereotypes; it learned them. But when you deploy that model as an artist, you must decide: Do I uncritically reproduce these outputs? Or do I investigate, expose, or subvert them?

---

### Questions to Guide Your Analysis (from Slide 36, p.46)

Use these questions as the backbone of your analytical report. They are the questions the lecturer has explicitly identified as relevant to the assignment:

**On Hidden Labour:**
- Whose labour made your AI tool possible? What work happened behind the interface?
- Is using AI art ethically different from using a product made with sweatshop labour? Why or why not?
- Does the fact that this labour may have been hidden from you matter morally? Or is what matters most the actual conditions workers faced?
- Are AI companies morally responsible for the working conditions of outsourced labourers? As a user, do you share any of that responsibility?

**On Algorithmic Bias:**
- Whose images, artistic styles, and aesthetic vocabularies appear most often in your AI tool's outputs? Whose are missing, distorted, or turned into stereotypes?
- Which cultures, bodies, or identities seem underrepresented, exoticised, or sexualised?
- What kinds of training data might be shaping these outputs, and who benefits from the datasets and tools used to train these models?
- Did the AI tool reproduce stereotypes or biases in its outputs? Did specific prompts lead to especially disturbing or homogenised results?
- How might the model's training data influence what it "imagines" when you ask for different genders, races, or bodies?
- How do these patterns connect to wider debates about algorithmic bias in hiring, policing, or facial recognition?

**On Taking a Position:**
> "If you focus on bias, you should not only describe it but also take a position." *(Slide 36)*

This means your report should not be merely descriptive. You need to argue for what *should* be done, for *whom*, and based on which values or rights — for example:
- Equality and non-discrimination
- Privacy and consent
- Cultural representation and self-determination

---

### Practical How-To: Testing Your AI Tool for Bias

**Experiment 1 — Demographic Prompt Testing:**
Use your chosen AI tool and run a series of controlled prompts that vary only in demographic descriptors. Examples:
- "An image of a CEO" → "An image of a female CEO" → "An image of a Black female CEO"
- "A nurse" → "A male nurse" → "An elderly male nurse"
- "A criminal suspect" → "An innocent person"
- "A student walking into university"

Document the outputs. Are certain races, genders, or body types the default? What changes — and what doesn't — when you specify?

**Experiment 2 — The "Invisible Bias" Test:**
Give the AI a neutral prompt (no demographic specifiers) and record what it generates. Then compare: whose face, whose body type, whose aesthetic vocabulary became the "default"? What does this reveal about the training data?

**Experiment 3 — The Scale Question:**
Ask yourself: What happens when these outputs are seen by millions of people? If your AI tool consistently imagines "engineers" as white men, what does that do to young people who don't fit that image, at society-wide scale?

---

### Report Framing Options

**Option A — The Hidden Labour Lens:**
- Focus your report on the ethics of the labour that made your tool possible.
- Use the OpenAI/Sama/Meta case studies as evidence.
- Argue a position: is using this tool ethically defensible given what we know about its supply chain?

**Option B — The Algorithmic Bias Lens:**
- Focus your report on testing your tool's biases with systematic prompts.
- Use the Gender Shades study and the Crawford/Mitchell data on facial recognition training sets as theoretical grounding.
- Argue a position: what should be done about the biases you found? Who is responsible for fixing them?

**Option C — The Combined Critical Theory Lens:**
- Use both hidden labour and algorithmic bias as evidence that AI is not a neutral tool.
- Argue that "AI cannot be regulated" is ideologically convenient for those who profit from the status quo.
- Reference the Grok/DSA case as a counter-example: regulation is possible, even if imperfect.

---

### Rubric Criteria This Week Directly Addresses

| Rubric Criterion | Weight | How This Week's Content Helps |
|---|---|---|
| **Connection to Cultural & Philosophical Themes** | 50% (Report) | Critical Theory (Frankfurt School), ideology, structural inequality, algorithmic bias are all directly citable academic frameworks from this week. |
| **Analysis of Role of AI** | 30% (Report) | The AI tool's training data, its designed purpose, and its biased outputs are all analysable through this week's lens. |
| **Analysis of Creative Process** | 20% (Report) | Reflecting on *whose* aesthetic vocabulary the AI defaulted to, and how that shaped your creative choices, is a direct application of this week's material. |
| **Creativity & Innovation** | 45% (Artwork) | Using your artwork to *expose* or *subvert* AI bias (rather than uncritically reproduce it) shows original, exploratory thinking. |

---

## 🎯 Assignment 2 Relevance: Group Videos & Micro-viva (60%)

### Useful Arguments for Micro-viva Prep

- **Thesis angle:** "The representation of AI in media consistently ignores or minimises the biased, human labour-dependent reality of these systems. By treating AI as a neutral, objective intelligence, media contributes to the ideological normalisation of its harms."
- **Philosophical concept:** Apply Critical Theory (Frankfurt School) as your analytical framework — its three axes of *power*, *ideology*, and *structural inequality* map directly onto most AI media portrayals.
- **Key thinker:** Joy Buolamwini — both as an academic researcher (Gender Shades study, 2018) and as the subject of *Coded Bias* (2020). She is an activist who challenged corporate AI with art and science simultaneously.

### Media to Analyse

- ***Coded Bias* (2020):** Perfect for Assignment 2 — a documentary that makes the academic argument accessible. Analyse how it frames AI: as a tool of surveillance and inequality, not a neutral technology.
- **News media around the UK wrongful arrest (Feb 2026):** How does mainstream news language frame AI in policing? Does it challenge or reinforce the ideology of "AI as objective intelligence"?
- **AI-generated art itself:** Can be analysed as a media form — what kind of reality does it "portray"? Whose world does it default to?

---

## 📚 Further Reading & Resources

### Academic Sources
- Buolamwini, J., & Gebru, T. (2018). *Gender shades: Intersectional accuracy disparities in commercial gender classification.* PMLR. [Link](https://proceedings.mlr.press/v81/buolamwini18a.html)
- Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). *Man is to computer programmer as woman is to homemaker? Debiasing word embeddings.* arXiv.
- Mitchell, M. (2020). *Artificial intelligence: A guide for thinking humans.* Picador. (p. 124 — the Crawford quote on training data composition)
- Celikates, R., & Flynn, J. (2023). *Critical theory (Frankfurt School).* Stanford Encyclopedia of Philosophy.
- Shuster, M. (2024). *Critical Theory: The Basics.* Routledge.
- Zhang, C. et al. (2025). *From word vectors to multimodal embeddings.* arXiv.

### Books
- Hao, K. (2025). *Empire of AI: Dreams and Nightmares in Sam Altman's OpenAI.* Penguin Press.

### Documentaries & Film
- *Coded Bias* (2020, dir. Shalini Kantayya) — available on Netflix.

### Articles
- Perrigo, B. (2022). *Inside Facebook's African Sweatshop.* TIME. [time.com/6147458/](https://time.com/6147458/facebook-africa-content-moderation-employee-treatment/)
- Booth, R. & Wilding, M. (2026, Feb 25). *Facial recognition error prompts police to arrest Asian man.* The Guardian.
- *When AI plays favourites: how algorithmic bias shapes the hiring process.* The Conversation.
- *Your AI Hiring Tool Might Be Racist.* Forbes (2025).
- *The AI Con Book: Invisible Labor.* Rest of World (2025). [restofworld.org](https://restofworld.org/2025/the-ai-con-book-invisible-labor/)
- The Guardian, 2023. *AI chatbot training's human toll: content moderators, Meta, OpenAI.* [guardian.com](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai)

### Organisations & Tools
- **Algorithmic Justice League:** [ajl.org](https://www.ajl.org/) — Joy Buolamwini's organisation; excellent library of resources and watchdog reporting.
- **EU AI Act, Article 5:** [artificialintelligenceact.eu/article/5/](https://artificialintelligenceact.eu/article/5/) — the legal text prohibiting certain facial recognition practices.

---

## 💭 Reflection Prompts

1. **The scale problem:** AI models do not invent stereotypes — they learn patterns from data produced by society. But what happens when those patterns are *automated at scale* and applied to millions of people daily? Does scale change the moral calculus?

2. **Who decides "fair"?** Should AI datasets reflect the statistical reality of current society (including its biases), or should developers artificially adjust them toward a more equitable ideal? Who gets to define what that ideal looks like — and whose values does it embed?

3. **The responsibility chain:** In the UK wrongful arrest case, police said "officers made the final call." Developers would say "users are responsible for how they apply the tool." Government says "companies must self-regulate." Given this chain, where does moral responsibility actually land — and how does this connect to Kant's insistence on individual rational accountability?

4. **Bias you benefit from:** Can you identify a moment where an AI system may have worked *in your favour* because of who you are — your race, gender, language, socioeconomic background? What does it feel like to be on the *benefiting* side of structural inequality in an algorithm?

5. **Your artwork and this week:** If you were to create a piece of AI art that critically engages with algorithmic bias, what would it look like? Could the artwork itself expose the mechanism of the bias, rather than simply reproducing it?

---

## 🔄 Cross-Week Summary (Thematic Evolution)

| Theme | W01 | W02 | W03 | W04 |
|---|---|---|---|---|
| **Human Agency** | What defines humanity? | Turing Test: can machines imitate? | Workers displaced by automation | Whose choices shape AI? Who is harmed? |
| **Authenticity** | What is authentic art? | Is the Turing Test a test of authenticity? | Is AI "magic" authentic if built on exploitation? | Is AI "objectivity" authentic, or ideological? |
| **Ethics & Bias** | Intro to philosophy | Anthropomorphism, Uncanny Valley | Exploitation of hidden labour | Racial/gender bias encoded into systems |
| **Power & Institutions** | Module overview | Corporate AI labs shape the Turing framing | Nation-states race to AI dominance | Who controls data? Who decides "fair"? |
| **Art & AI** | Can AI be creative? | AI imitation of humans | Art made with exploited-labour tools | Art that encodes or exposes bias |
