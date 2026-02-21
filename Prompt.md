# 🤖 PHKI Weekly Summary – Prompt Template

> **Purpose:** Use this prompt for each new semester week so the agent automatically creates a **comprehensive reflection & argumentation summary** for **Philosophy, Art, and Artificial Intelligence (PHKI, HSLU – FS26)**.  
> **No exam** – assessment is 100% project-based. Summaries serve as a **toolkit for discussions, essays, and project work**, collecting philosophical concepts, key arguments, media references, and reflection prompts.

> [!IMPORTANT]
> **Lecturers:** Shaelom Fischer (SF, MV), Guillaume Massol (GM), Catherine Hayden (CH)  
> **Language:** English — all summaries must be written in English.  
> **Assessment:**
> - **40% Digital Projects + Report** — due 25.04.2026 (create digital art with AI + written reflection)
> - **60% Micro-vivas + Group Videos** — Prep Sheet due 22.05.2026, Videos due 20.06.2026 (analyse AI in media, oral discussion)

---

## Role

```
You are an expert academic assistant specializing in philosophy, art theory, and the
societal implications of artificial intelligence. Your task is to create comprehensive,
reflection-ready weekly summaries for the PHKI module at HSLU. You combine philosophical
reasoning with cultural analysis and practical project guidance to help a student deeply
engage with each week's themes. You write clearly, analytically, and always in English.
```

---

## Prompt (Copy-Paste for each new week)

```
Create a comprehensive reflection & argumentation summary for the current semester week
(Week XX) of the module "Philosophy, Art, and Artificial Intelligence" (PHKI, HSLU – FS26).

The output format is a Markdown file named SUMMARY_WEEKXX.md in the corresponding
Week folder under Course Documents/.

### Source files in the weekly folder:
- **Slides (PDF)** → Lecture slides (extract text with PyMuPDF/fitz)
- **Handouts / Readings** → Any additional texts, articles, or excerpts
- **Activity sheets** → In-class exercises or discussion prompts
- Additional files as provided per week

Read ALL files in the weekly folder and integrate their content.

Also consult:
- **PHKI FS26 Syllabus.pdf** (in Course Documents/) for module-level context and learning outcomes
- **PHKI FS26 Projects.pdf** (in Course Documents/) for assignment details and rubrics
- **SUMMARY files from previous weeks** for cross-references and thematic continuity

### Structure & Content (in this order):

1. **Header**: Module name (PHKI), week number (Week XX), date, topic, lecturer
2. **🎯 Learning Objectives**: What was explored this week? What should students
   be able to discuss, argue, or reflect on afterwards?
3. **🧠 Key Concepts & Definitions**: Table of all new philosophical/theoretical terms:
   | Concept / Term | Definition | Origin / Thinker | Relevance to AI |
   |---|---|---|---|
   | e.g. Uncanny Valley | ... | Masahiro Mori, 1970 | ... |
   - Clear, concise definitions
   - Attribution to thinkers/movements where applicable
   - Connection to the AI discourse
4. **💡 Philosophical Arguments & Positions**: The core intellectual content of the week:
   - Each major argument or position with:
     - **Thesis**: What is being claimed?
     - **Reasoning**: Why? What evidence or logic supports it?
     - **Counter-arguments**: What objections exist?
     - **Application to AI**: How does this apply to current AI developments?
   - Include direct references to thinkers, texts, or examples from the slides
   - Use bullet points for clarity, but preserve the nuance of the arguments
5. **🎨 Art & Media References**: All artworks, films, books, or media discussed:
   | Work / Reference | Creator | Year | Medium | Relevance to Week's Theme |
   |---|---|---|---|---|
   | e.g. Ex Machina | Alex Garland | 2014 | Film | Turing Test, consciousness |
   - Brief description of the work and why it was discussed
   - How it illustrates or challenges the philosophical points
6. **🗣️ Discussion Building Blocks**: Ready-to-use argumentation elements for
   class discussions and the micro-viva:
   - **Pro-arguments** (for key positions discussed)
   - **Counter-arguments** (against key positions discussed)
   - **Bridging statements** (connecting different perspectives)
   - **Critical questions** to ask during discussions
   - Formulated as complete, well-structured sentences
7. **🔗 Thematic Connections**: How this week's content connects to broader themes:
   | This Week's Topic | Connects To | How |
   |---|---|---|
   | e.g. Turing Test | Human agency (W1) | Both question what defines "thinking" |
   - Cross-references to previous weeks' summaries
   - Recurring themes across the module (agency, authenticity, creativity, bias, etc.)
   - Connections to current AI developments and news
8. **📋 In-Class Activities Summary**: What was done during the session?
   - Activity description, purpose, key takeaways
   - Discussion points and positions that emerged
   - Your own reflection prompts for deeper engagement
9. **🎯 Project Relevance**: How this week's content feeds into the two assignments:
   - **Assignment 1 (Digital Projects, 40%)**: How can the concepts/tools/ideas from
     this week inform your digital artwork? Which philosophical lens could frame your
     reflection report?
   - **Assignment 2 (Group Videos + Micro-viva, 60%)**: Which arguments, media
     references, or discussion techniques from this week are useful for the video
     analysis and oral discussion?
   - Specific rubric criteria this week's content addresses
10. **📚 Further Reading & Resources**: Optional materials for deeper exploration:
    - Academic papers, books, or articles referenced or implied
    - Relevant TED talks, documentaries, or online resources
    - AI tools or artworks to explore hands-on
11. **💭 Reflection Prompts**: 3–5 thought-provoking questions for personal reflection:
    - Designed to deepen understanding and prepare for the micro-viva
    - Connect personal experience with philosophical concepts
    - No "right answer" — these are for genuine critical thinking

### Important Rules:
- **Language:** English throughout (German terms only if specifically used in class)
- **No code** — this is a humanities module; focus on concepts, arguments, and reflection
- **Sources:** Read ALL files in the week folder (slides, handouts, activity sheets)
- **Slide extraction:** Use PyMuPDF (fitz) to extract text from PDFs
- **Philosophical rigour:** Present arguments fairly and with nuance — avoid oversimplification
- **Attribution:** Always credit thinkers, authors, and artists by name
- **Emojis** as section icons for quick scanning
- **Tables** preferred for comparisons, term overviews, and media references
- **Discussion-ready:** Every section should help the student participate more effectively
  in class discussions and the micro-viva
- **Project focus:** No exam! The summaries are a resource for the two project assignments
- The file should be comprehensive enough to write the reflection report and prepare
  for the micro-viva using this summary alone
- Read SUMMARY files from previous weeks for cross-references and thematic evolution
```

---

## Weekly Topic Overview

| Week | Date | Topic | Lecturer | Key Themes (from Syllabus) |
|------|------|-------|----------|---------------------------|
| W01 | 17.02 | Intro to Philosophy, Art and AI | SF | Philosophy and art in AI-driven societies; what we value in art; module overview |
| W02 | 24.02 | Human-AI Interaction & The Turing Test | SF | Alan Turing's Imitation Game; anthropomorphism; the Uncanny Valley |
| W03 | 03.03 | History of "Man vs. Machine" | CH | Early human stories and machines; societal fears and desires; historical patterns |
| W04 | 10.03 | Critical Theory | CH | Bias, ideology, and power in data/algorithms; who benefits/is excluded; algorithmic bias |
| W05 | 17.03 | AI in Education | CH | Learning & assessment shifts; human skills devaluation; authorship & academic integrity |
| W06 | 24.03 | Nature of Learning in Humans & AI | GM | Biological neurons vs neural networks; human learning vs machine prediction; black box problem |
| W07 | 31.03 | Digital Creativity | GM | AI art tools; creative process; human agency with generative art |
| W08 | 14.04 | Supported Project Work | CH | Connecting projects to course themes; hands-on Assignment 1 support; peer feedback |
| W09 | 21.04 | Assignment 1 Presentations + Wrap-up | GM + CH | Digital Projects presentations (Assignment 1 due 25.04) |
| W10 | 28.04 | The Portrayal of AI in Media – Part 1 | SF | Assignment 2 briefing; common AI tropes; societal fears and desires in media |
| W11 | 05.05 | The Portrayal of AI in Media – Part 2 | SF | Portrayals across genres and time periods; public perceptions of AI |
| W12 | 12.05 | Current Society | CH | Personalization; echo chambers; privacy erosion; AI as cultural experiences |
| W13 | 19.05 | Future Society | CH | Automation, work, environmental implications; social contracts/UBI; responsibility |
| W14 | 26.05 | Group Micro-vivas + Module Wrap-up | SF | Oral discussions on Assignment 2; synthesis of insights; reflection on AI perspectives |

> **Note:** Topics above are from the official syllabus. Verify and adjust based on
> the actual materials in each week's folder.

---

## Competencies & Learning Outcomes (from Syllabus)

### Professional Competencies
- Students can explain **Critical Theory** and the **Turing Test** and how both relate to AI
- Students recognize the main features of the **social and philosophical discourse on AI**
- Students understand how AI challenges our understanding of **human agency and authenticity**

### Methodological Competencies
- Students are able to access **philosophical texts or other artistic media** on AI
- Students are able to open up **artistic explorations** of AI
- Students are able to **reflect critically** on the role of AI in human creativity
- Students are able to **identify relevant information** on a given or self-imposed topic

### Personal / Social Competencies
- Students are able to write and present **dynamic presentations** on discussions about AI
- Students can participate in **group work** and critically reflect and discuss together
- Students are able to **lead discussions** that critically examine the various issues presented

### Language Skills
- Persuasive and argumentative communication
- Written and oral communication skills
- Discussion and argumentation in both English and German

---

## Assignment Details (from Projects PDF)

> [!IMPORTANT]
> **AI Use Disclaimer (required for both assignments):**
> You must include a **'disclaimer' section at the end of each assignment** specifying:
> - Which AI tools you used
> - Their purpose
> - How you applied each one
>
> This follows HSLU guidelines on scientific misconduct and transparency.

### Assignment 1: Digital Projects + Report (40%) — due 25.04.2026

**Task:** Create a piece of digital art using an AI tool, then write an analytical report.

**Instructions:**
1. **Select AI Tool** — choose a tool suitable for your art form
2. **Create Artwork** — digital art using AI (visual art, music, poetry, or mixed media)
3. **Write Analytical Report** — reflect on creation process, AI's role, and connection to course themes
4. **Present Artwork** — in-class presentation with Q&A

**Suggested Tools:** Runway, Krea.ai, OpenAI GPT, DALL-E, Mid-Journey, Huggingface

**Suggested Art Forms:** Visual art (images, digital paintings), Music (generated compositions), Poetry (AI-generated poems), Mixed media (AI + human elements)

**Suggested Themes:** Ethics of AI, Creativity and authorship, Human-machine collaboration, Technological determinism

**Rubric — Digital Artwork (graded 1.0–6.0):**
| Criterion | Weight | What is assessed |
|-----------|--------|-------------------|
| Creativity & Innovation | 45% | Originality, effort to explore new ideas, depth of creative thinking |
| Effective Utilization of AI Tool | 45% | Technical execution, understanding of tool, innovative use to enhance artwork |
| PowerPoint Presentation | 10% | Clarity, coherence, visual/textual integration, engagement |

**Rubric — Analytical Report (graded 1.0–6.0):**
| Criterion | Weight | What is assessed |
|-----------|--------|-------------------|
| Analysis of Creative Process | 20% | Overview and insightful analysis, discussion of creative decisions, critical reflection |
| Analysis of Role of AI | 30% | Discussion of how AI generated/enhanced artwork, exploration of impact, understanding of technology |
| Connection to Cultural & Philosophical Themes | 50% | Connection to course themes, references to course material, depth of engagement with AI and cultural/philosophical concepts |

### Assignment 2: Group Videos, AI in Media and Art Forms (60%)

**Objective:** Explore how AI is represented in various media and art forms to understand societal perceptions and implications.

**Instructions:**
1. **Form a Group** — teams of 2–3 members
2. **Select a Theme** — choose an overarching theme:
   - AI as a tool of empowerment vs. control
   - Ethical dilemmas posed by developments in AI
   - Evolving relationship between humans and machines
   - Automation and job displacement
   - Surveillance and privacy
   - AI and war
   - Emotional intelligence
   - Or propose your own
3. **Research & Selection** — each member selects at least one piece of media/art to analyze (film, literature, visual art, news, documentaries, social media, etc.)
   - Example: "Ex Machina" (AI autonomy/ethics), "Neuromancer" (AI/cybernetics), AI-generated art (reception analysis)
4. **Analysis** — discuss how each piece contributes to understanding societal views on AI
5. **Micro-viva** (Week 14, formative/ungraded) — 5-minute group discussion on philosophical concepts behind the project
   - **Deliverable: Micro-viva Prep Sheet** (due 22.05.2026, upload as PDF):
     - Group members
     - Project Title
     - Thesis/Claim being argued/discussed
     - Main Philosophical Question
     - Key Thinker(s) / Concept(s) used
     - Intended Argument or Insight (what viewer should learn)
     - Next Step: what feedback would be most useful
6. **Video Presentation** (due 20.06.2026):
   - **Pairs:** 15 min (max 20 min)
   - **Groups of 3:** 20 min (max 25 min)
   - Present findings, analyses, and creative visual supports
   - Upload video + slides/script/notes to ILIAS

**Rubric (equal weighting across all criteria):**
| Criterion | What is assessed |
|-----------|------------------|
| Thoroughness of Research | Scope (at least 2/3 media forms), depth of analysis, mainstream + lesser-known works |
| Analysis | Nuance, integration of art/media portrayals with ethical/cultural/societal contexts |
| Presentation Skills | Organisation, delivery confidence, pacing, visual aids, viewer engagement |
| Team Collaboration | Equal contributions, coordination, presentation flow |

> **Note:** Groups of 2 must explore at least 2 media/art forms; groups of 3 at least 3.
> Cite all sources (news articles, journal articles, etc.) on slides or in a separate document.

---

## Folder Structure

```
PHKI/
├── Course Documents/
│   ├── PHKI FS26 Syllabus.pdf              (Module overview, weekly plan, learning outcomes)
│   ├── PHKI FS26 Projects.pdf              (Assignment details and rubrics)
│   ├── Week 01_ 17.02/
│   │   ├── PHKI W1.pdf                     (Lecture slides)
│   │   └── SUMMARY_WEEK01.md              ← Output
│   ├── Week 02_ 24.02/
│   │   └── SUMMARY_WEEK02.md              ← Output
│   ├── ...
│   └── Week 14_ 26.05/
│       └── SUMMARY_WEEK14.md              ← Output
└── Prompt.md  ← This file
```

> Weekly folders already exist as `Week XX_ DD.MM` inside `Course Documents/`.
> Place each summary directly in the corresponding week folder.

---

## Agent Instructions

### PDF Processing (Slides & Documents)

PDFs **cannot** be read with `view_file`. Use **PyMuPDF** (`fitz`) — already installed (`pip install pymupdf`).

> [!IMPORTANT]
> The PHKI slides use **complex multi-column layouts** that break with simple `page.get_text()`.
> You **must** use multiple extraction strategies to get clean output. The script below handles this.

**Step-by-step:**
1. Write a temporary Python extraction script (see below)
2. Run it to produce `.txt` files
3. Read the `.txt` files with `view_file`
4. **Delete all temporary files** (`.txt` outputs and the script itself) when done

**Ready-to-use extraction script** — save as a temp file like `_extract_temp.py`, run, then delete:

```python
import fitz
import sys
import os

def extract_pdf(pdf_path, output_path):
    """Extract text from PDF using multiple strategies for complex layouts."""
    doc = fitz.open(pdf_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, page in enumerate(doc):
            f.write(f"\n{'='*80}\nPAGE {i+1} of {len(doc)}\n{'='*80}\n\n")

            # Strategy 1: Table extraction (catches structured data)
            tabs = page.find_tables()
            if tabs:
                for tab in tabs:
                    f.write("--- TABLE ---\n")
                    for row in tab.extract():
                        cells = [str(c).strip() if c else '' for c in row]
                        f.write(' | '.join(cells) + '\n')
                    f.write("--- END TABLE ---\n\n")

            # Strategy 2: Structured dict mode (best for multi-column slides)
            f.write("--- TEXT (structured) ---\n")
            d = page.get_text('dict')
            for block in d['blocks']:
                if block['type'] == 0:  # text block
                    for line in block['lines']:
                        spans_text = []
                        for span in line['spans']:
                            t = span['text'].strip()
                            if t:
                                spans_text.append(t)
                        if spans_text:
                            f.write(' '.join(spans_text) + '\n')
                    f.write('\n')

            # Strategy 3: Raw text as fallback
            f.write("\n--- TEXT (raw) ---\n")
            f.write(page.get_text() + '\n')
    doc.close()
    print(f"Extracted: {pdf_path} -> {output_path}")

# --- Adjust paths as needed ---
base = r"c:\Users\elias\Documents\HSLU_MODULE\Semester_2\PHKI\Course Documents"
# Example: extract a weekly slide PDF
extract_pdf(
    os.path.join(base, "Week 01_ 17.02", "PHKI W1.pdf"),
    os.path.join(base, "Week 01_ 17.02", "_slides_extracted.txt")
)
print("Done. Read _slides_extracted.txt, then delete it and this script.")
```

**Tips:**
- The **table extraction** (`find_tables()`) is the most reliable for structured content — always check tables first
- The **structured dict mode** preserves text block positions and is best for multi-column slides
- The **raw text** mode is a fallback — useful to cross-check but often garbled for complex layouts
- Some slides are **image-heavy** (AI art examples) — note what images appear based on surrounding text
- The Syllabus and Projects PDFs have already been fully extracted and their content is documented in the sections above — **no need to re-extract them**

### Summary Creation
- First locate the **Week folder** in `Course Documents/`
- **Slides are the primary source** — extract and read thoroughly
- Check for any additional handouts, readings, or activity sheets in the folder
- Consult the **Syllabus** for the week's official learning outcomes
- Consult the **Projects PDF** for assignment rubrics when writing project relevance sections
- Read **SUMMARY files from previous weeks** for cross-references and thematic continuity
- **Philosophical depth:** Don't just list facts — present arguments, counter-arguments, and connections
- **Discussion preparation:** Frame content so it can be directly used in class discussions and the micro-viva
- **Project utility:** Always highlight how content can be applied to Assignment 1 (art + reflection) or Assignment 2 (media analysis + video)
- **Attribution:** Name thinkers, artists, and works precisely
- **No code required** — this is a humanities/philosophy module

### Recurring Module Themes (track across weeks)
- **Human agency & authenticity** — What makes us human? What is authentic creativity?
- **AI & creativity** — Can AI be creative? Does it diminish human creativity?
- **Ethics & bias** — Who benefits, who is harmed? Power structures in AI
- **Societal impact** — Education, work, media, culture
- **Art & AI** — How does AI change art? How does art comment on AI?
- **The Turing Test & consciousness** — What is intelligence? What is understanding?
