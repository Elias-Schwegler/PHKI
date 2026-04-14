"""
Generate PHKI Assignment 1 PowerPoint Presentation
Elias Schwegler - HSLU FS26
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "PHKI_Assignment1_Presentation.pptx")

DARK_BG = RGBColor(0x1A, 0x2A, 0x1A)       # deep forest green background
WHITE = RGBColor(0xF5, 0xF5, 0xF0)         # warm off-white
LIGHT_GREY = RGBColor(0xD4, 0xD9, 0xCE)    # sage-tinted grey for body text
ACCENT = RGBColor(0x6B, 0xB5, 0x6A)        # fresh leaf green for highlights
SUBTLE = RGBColor(0x7A, 0x8A, 0x72)        # muted olive for small text
AMBER = RGBColor(0xE8, 0xA8, 0x3E)         # warm amber for warnings/refusals

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)


def add_bg(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BG


def tb(slide, left, top, width, height, text, size=18,
       color=WHITE, bold=False, italic=False, align=PP_ALIGN.LEFT):
    """Add a simple text box."""
    box = slide.shapes.add_textbox(Inches(left), Inches(top),
                                    Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = "Calibri"
    p.line_spacing = Pt(int(size * 1.4))
    return tf


def bullets(slide, left, top, width, height, items, size=16, color=LIGHT_GREY):
    """Add bulleted items."""
    box = slide.shapes.add_textbox(Inches(left), Inches(top),
                                    Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10)
        p.line_spacing = Pt(int(size * 1.5))
        run = p.add_run()
        run.text = "\u2022  " + item
        run.font.size = Pt(size)
        run.font.color.rgb = color
        run.font.name = "Calibri"
    return tf


def line(slide, left, top, width):
    shape = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(width), Pt(2))
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT
    shape.line.fill.background()


def img(slide, filename, left, top, height):
    path = os.path.join(SCRIPT_DIR, filename)
    if os.path.exists(path):
        slide.shapes.add_picture(path, Inches(left), Inches(top), height=Inches(height))


# ══════════════════════════════════════════════════════════
#  SLIDE 1 - TITLE
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 1.5, 1.8, 10.3, 1.2, "Synthetic Pine & Heavy Air",
   size=44, bold=True, align=PP_ALIGN.CENTER)
line(s, 4.5, 3.3, 4.3)
tb(s, 1.5, 3.6, 10.3, 0.8, "Can AI copy the soul of a song?",
   size=24, color=ACCENT, italic=True, align=PP_ALIGN.CENTER)
tb(s, 1.5, 5.5, 10.3, 0.5,
   "Elias Schwegler  |  PHKI FS26  |  HSLU  |  April 2026",
   size=14, color=SUBTLE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════
#  SLIDE 2 - WHAT I TESTED
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.8, 11.7, 0.8, "What I tested", size=36, bold=True)
line(s, 0.8, 1.7, 3.0)

tb(s, 0.8, 2.2, 11.7, 1.0,
   '"Let Her Go" by Passenger - ~5 billion YouTube views, a song from my childhood.',
   size=20, color=LIGHT_GREY)

tb(s, 0.8, 3.5, 11.7, 0.5, "Two tests with Google Gemini:",
   size=18, color=ACCENT, bold=True)

bullets(s, 0.8, 4.2, 11.7, 2.0, [
    "Test 1: Copy the melody, but write new lyrics about a car and a pine air freshener",
    "Test 2: Keep the original lyrics, but write a new melody",
], size=18)

tb(s, 0.8, 6.0, 11.7, 0.8,
   "Goal: see if Gemini can copy, and what happens when it refuses.",
   size=16, color=SUBTLE, italic=True)

# ══════════════════════════════════════════════════════════
#  SLIDE 3 - TEST 1 + SCREENSHOT
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.8, 6.0, 0.8, "Test 1: Same melody, different text", size=30, bold=True)
line(s, 0.8, 1.7, 3.0)

tb(s, 0.8, 2.0, 6.0, 0.4, "MY PROMPT", size=12, color=ACCENT, bold=True)
tb(s, 0.8, 2.5, 6.0, 1.5,
   '"Make a similar song to Let Her Go, same melody, '
   'but about a car, tires, and a pine air freshener."',
   size=15, color=LIGHT_GREY, italic=True)

tb(s, 0.8, 4.0, 6.0, 0.4, "GEMINI REFUSED THE MELODY", size=12, color=AMBER, bold=True)
tb(s, 0.8, 4.5, 6.0, 0.5, "But created:", size=14, color=LIGHT_GREY)

tb(s, 0.8, 5.2, 6.0, 0.5, '"Synthetic Pine & Heavy Air"', size=22, bold=True)
tb(s, 0.8, 5.9, 6.0, 0.8, "Bedroom Pop / 80 BPM / breathy vocals",
   size=14, color=SUBTLE)

img(s, "Chat_1_01.png", 7.3, 0.8, 6.2)

# ══════════════════════════════════════════════════════════
#  SLIDE 4 - TEST 2 + SCREENSHOT
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.8, 6.0, 0.8, "Test 2: New melody, same lyrics", size=30, bold=True)
line(s, 0.8, 1.7, 3.0)

tb(s, 0.8, 2.0, 6.0, 0.4, "MY PROMPT", size=12, color=ACCENT, bold=True)
tb(s, 0.8, 2.5, 6.0, 1.0,
   '"Can you do a new melody for the Let Her Go lyrics?"',
   size=15, color=LIGHT_GREY, italic=True)

tb(s, 0.8, 3.5, 6.0, 0.4, "GEMINI REFUSED THE LYRICS", size=12, color=AMBER, bold=True)
tb(s, 0.8, 4.0, 6.0, 0.5, "But created:", size=14, color=LIGHT_GREY)

tb(s, 0.8, 4.7, 6.0, 0.5, '"The Physics of the Thing"', size=22, bold=True)
tb(s, 0.8, 5.4, 6.0, 0.8, "Indie-Folk / Chamber Pop / nylon guitar, cello",
   size=14, color=SUBTLE)

img(s, "Chat_1_03_follow_up.png", 7.3, 0.8, 6.2)

# ══════════════════════════════════════════════════════════
#  SLIDE 5 - WHAT I FOUND
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.8, 11.7, 0.8, "What I found", size=36, bold=True)
line(s, 0.8, 1.7, 3.0)

bullets(s, 0.8, 2.3, 11.7, 4.5, [
    "Two copyright guardrails: melody protected + lyrics protected",
    "Both held firm under direct pressure",
    "Yet both tracks captured the emotional vibe of the original",
    "Gemini uses DeepMind Lyria 3 - trained on massive audio datasets (SynthID watermarked)",
    "The vocals sound human - but whose voice trained the model?",
    "AI treats absurd subject matter (pine air freshener) with complete sincerity",
], size=17)

# ══════════════════════════════════════════════════════════
#  SLIDE 6 - WHY IT MATTERS (brief themes)
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.8, 11.7, 0.8, "Why it matters", size=36, bold=True)
line(s, 0.8, 1.7, 3.0)

# Left column
tb(s, 0.8, 2.2, 5.5, 0.4, "PROCESS VS. RESULT (W1)", size=12, color=ACCENT, bold=True)
tb(s, 0.8, 2.7, 5.5, 1.0,
   "30-second prompt vs. years of learning guitar.\nThe result sounds great - but was anything created?",
   size=15, color=LIGHT_GREY)

tb(s, 0.8, 3.9, 5.5, 0.4, "HIDDEN LABOUR (W3, W4)", size=12, color=ACCENT, bold=True)
tb(s, 0.8, 4.4, 5.5, 1.0,
   "Real singers' voices absorbed into the model.\nNo credit, no compensation. Same pattern as Sama/OpenAI.",
   size=15, color=LIGHT_GREY)

# Right column
tb(s, 7.0, 2.2, 5.5, 0.4, "EMBODIED PERCEPTION (W6)", size=12, color=ACCENT, bold=True)
tb(s, 7.0, 2.7, 5.5, 1.0,
   "Merleau-Ponty: music is embodied.\nGemini simulates the sound of a body singing - without having one.",
   size=15, color=LIGHT_GREY)

tb(s, 7.0, 3.9, 5.5, 0.4, "SLOT-MACHINE EFFECT (W7)", size=12, color=ACCENT, bold=True)
tb(s, 7.0, 4.4, 5.5, 1.0,
   'Doctorow: AI tools keep you pulling the lever.\nAfter track 1, my instinct was "what if I try again?"',
   size=15, color=LIGHT_GREY)

# Bottom takeaway
tb(s, 0.8, 5.8, 11.7, 1.0,
   "AI can make good music. The question is: does authenticity of process still matter?",
   size=20, color=WHITE, italic=True, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════
#  SLIDE 7 - DISCUSSION QUESTIONS
# ══════════════════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s)

tb(s, 0.8, 0.6, 11.7, 0.8, "Discussion", size=40, bold=True, align=PP_ALIGN.CENTER)
line(s, 4.5, 1.5, 4.3)

tb(s, 0.8, 1.8, 11.7, 0.4, "Let's listen to the tracks first, then discuss:",
   size=15, color=SUBTLE, italic=True, align=PP_ALIGN.CENTER)

questions = [
    "If you can't tell whether a song was made by a human or AI,\n"
    "does the answer change how it makes you feel?",

    "Should artists be able to opt out of AI training datasets?\n"
    "What would that mean for tools like Gemini?",

    "Is there a difference between copying a melody\n"
    "and copying an emotional style? Where do you draw the line?",

    "Would you pay the same for an AI-generated song\n"
    "as for a human-composed one? Why or why not?",

    "Did the AI collaborate with me,\n"
    "or did I just press a button?",
]

y = 2.5
for i, q in enumerate(questions):
    num_color = ACCENT
    tb(s, 1.2, y, 0.5, 0.5, f"{i+1}.", size=18, color=num_color, bold=True)
    tb(s, 1.8, y, 10.0, 0.8, q, size=16, color=LIGHT_GREY)
    y += 1.0

tb(s, 0.8, 7.0, 11.7, 0.4,
   "Elias Schwegler  |  PHKI FS26  |  HSLU",
   size=12, color=SUBTLE, align=PP_ALIGN.CENTER)

# ── Save ───────────────────────────────────────────────
prs.save(OUTPUT_PATH)
print(f"Presentation saved to: {OUTPUT_PATH}")
