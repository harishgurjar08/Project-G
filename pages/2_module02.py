import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from utils.sidebar import inject_global_css, render_sidebar, panel_header, report_box
from utils.gemini import call_gemini_text

st.set_page_config(
    page_title="MODULE 02 — Text Intel | PROJECT G",
    page_icon="📡",
    layout="wide",
)

inject_global_css()
api_key = render_sidebar()

# ── Page header ──────────────────────────────────────────────────────────────
st.markdown("# MODULE 02")
st.markdown("<p style='font-family:Orbitron,monospace; font-size:11px; letter-spacing:3px; color:#5a8c5f; margin-top:-12px;'>FAKE NEWS DETECTION — TEXTUAL INTELLIGENCE</p>", unsafe_allow_html=True)
st.markdown("---")

panel_header("MOD-02", "CREDIBILITY & MISINFORMATION ANALYSIS")

st.markdown("""
<div style='background:#0d1f10; border:1px solid #1a3d1e; border-top:none;
            border-radius:0 0 2px 2px; padding:20px;'>
    <div style='font-size:12px; color:#5a8c5f; line-height:1.9; margin-bottom:4px;'>
        OBJECTIVE: Evaluate credibility of news articles, headlines, or claims.<br>
        Detect misinformation, propaganda, and psychological operations (PSYOP).
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
news_input = st.text_area(
    "NEWS / ARTICLE / CLAIM INPUT",
    height=220,
    placeholder=(
        "Paste news article, headline, URL content, or claim for analysis...\n\n"
        "Example: 'India launches hypersonic missile capable of reaching Beijing in 4 minutes'"
    ),
)

char_count = len(news_input)
if char_count > 0:
    st.markdown(
        f"<div style='font-size:11px; color:#5a8c5f; text-align:right;'>"
        f"INPUT LENGTH: {char_count} chars"
        f"{'  ·  <span style=\"color:#ffb800;\">TRUNCATED TO 2000</span>' if char_count > 2000 else ''}"
        f"</div>",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── Analyze button ────────────────────────────────────────────────────────────
if not api_key or not api_key.startswith("AIza"):
    st.info("⚠ Paste your Gemini API key in the sidebar to activate this module.")

btn_disabled = not (news_input.strip() and api_key and api_key.startswith("AIza"))

if st.button("▶ RUN CREDIBILITY ANALYSIS", disabled=btn_disabled, key="analyze_news"):
    SYSTEM = (
        "You are PROJECT G, a Defense Intelligence AI specializing in textual intelligence. "
        "Detect misinformation, propaganda, and psychological operations in news content. "
        "Respond in format. Be analytical, factual, and concise. "
        "No casual language."
    )

    content = news_input.strip()[:2000]
    truncated = " [...truncated]" if len(news_input.strip()) > 2000 else ""

    PROMPT = f"""Analyze the following news content for credibility, misinformation, propaganda, and psychological operation indicators.

NEWS CONTENT:
\"\"\"
{content}{truncated}
\"\"\"

Respond EXACTLY in this format:

TEXTUAL INTELLIGENCE REPORT


Credibility Status  : [REAL / LIKELY FAKE / MANIPULATED INFORMATION / UNVERIFIABLE]
Confidence Level    : XX%
Content Type        : [News Article / Headline / Claim / Propaganda / Social Media Post]

Indicators Detected:
• [Emotional or fear-based language — quote if present]
• [Source reliability — named / anonymous / state-affiliated]
• [Timeline consistency — cross-reference with known facts]
• [Strategic exaggeration or omission]
• [Missing corroboration or verifiability]

Propaganda Techniques Identified:
• [List any: appeal to fear, loaded language, bandwagon, false dilemma, etc. — or NONE DETECTED]

Source Reliability Assessment:
• [Rating: High / Medium / Low / Unknown — with 1-line reason]

Strategic Risk Level: [LOW / MEDIUM / HIGH / CRITICAL]
Strategic Risk Note:
• [1-line impact assessment if this information is believed or widely spread]

ANALYST VERDICT: [1 sentence final assessment]"""

    with st.spinner("[ PROCESSING — TEXTUAL ANALYSIS IN PROGRESS... ]"):
        try:
            result = call_gemini_text(
                prompt=PROMPT,
                system=SYSTEM,
                api_key=api_key,
            )

            st.markdown("---")
            panel_header("REPORT", "TEXTUAL INTELLIGENCE OUTPUT")
            report_box(result)

            # Metrics row
            st.markdown("<br>", unsafe_allow_html=True)
            lines = result.split("\n")
            credibility, confidence, risk = "N/A", "N/A", "N/A"
            for line in lines:
                if "Credibility Status" in line and ":" in line:
                    credibility = line.split(":", 1)[-1].strip()
                if "Confidence Level" in line and ":" in line:
                    confidence = line.split(":")[-1].strip()
                if "Strategic Risk Level" in line and ":" in line:
                    risk = line.split(":")[-1].strip()

            m1, m2, m3 = st.columns(3)
            m1.metric("CREDIBILITY STATUS", credibility[:20] if len(credibility) > 20 else credibility)
            m2.metric("CONFIDENCE LEVEL", confidence)
            m3.metric("STRATEGIC RISK", risk)

        except Exception as e:
            st.error(f"⚠ ERROR: {e}")

st.markdown("<br><div style='font-size:10px; color:#5a8c5f; text-align:center; letter-spacing:2px;'>PROJECT G · MODULE 02 · TEXTUAL INTELLIGENCE</div>", unsafe_allow_html=True)
