import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from utils.gemini import call_gemini_text  # Only keeping gemini import

st.set_page_config(
    page_title="MODULE 02 — Text Intel | PROJECT G",
    page_icon="📡",
    layout="wide",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

:root {
    --green:   #00ff41;
    --green2:  #00cc33;
    --green3:  #009922;
    --green4:  #004d14;
    --bg:      #040d06;
    --bg2:     #071209;
    --panel:   #0d1f10;
    --border:  #1a3d1e;
    --text:    #b0ffb8;
    --dim:     #5a8c5f;
    --amber:   #ffb800;
    --red:     #ff3b3b;
    --cyan:    #00ffe1;
}

.stApp {
    background-color: #040d06 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

[data-testid="stSidebar"] {
    background-color: #071209 !important;
    border-right: 1px solid #1a3d1e !important;
}
[data-testid="stSidebar"] * {
    font-family: 'Share Tech Mono', monospace !important;
    color: #b0ffb8 !important;
}
[data-testid="stSidebarNav"] a {
    font-family: 'Orbitron', monospace !important;
    font-size: 11px !important;
    letter-spacing: 2px !important;
    color: #5a8c5f !important;
    padding: 10px 16px !important;
    border-radius: 2px !important;
    transition: all 0.2s !important;
}
[data-testid="stSidebarNav"] a:hover,
[data-testid="stSidebarNav"] a[aria-current="page"] {
    color: #00ff41 !important;
    background: rgba(0,255,65,0.07) !important;
    border-left: 2px solid #00ff41 !important;
}

h1, h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #00ff41 !important;
    letter-spacing: 4px !important;
}
h1 { font-size: 24px !important; text-shadow: 0 0 20px rgba(0,255,65,0.4); }
h2 { font-size: 16px !important; color: #00cc33 !important; }
h3 { font-size: 13px !important; color: #009922 !important; }

p, li, span, label, div {
    color: #b0ffb8 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background-color: #040d06 !important;
    border: 1px solid #1a3d1e !important;
    color: #b0ffb8 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 13px !important;
    border-radius: 2px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #009922 !important;
    box-shadow: 0 0 0 1px #009922 !important;
}
.stTextArea > div > div > textarea {
    min-height: 220px !important;
}

.stButton > button {
    background: transparent !important;
    border: 1px solid #009922 !important;
    color: #00ff41 !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    letter-spacing: 2px !important;
    border-radius: 2px !important;
    padding: 10px 24px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(0,255,65,0.1) !important;
    border-color: #00ff41 !important;
}
.stButton > button:disabled {
    opacity: 0.4 !important;
    border-color: #1a3d1e !important;
    color: #5a8c5f !important;
}

[data-testid="stFileUploader"] {
    background: #040d06 !important;
    border: 1px dashed #2a6b30 !important;
    border-radius: 2px !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #009922 !important;
}
[data-testid="stFileUploader"] * { color: #5a8c5f !important; }

.stSuccess { background: rgba(0,255,65,0.08) !important; border: 1px solid #009922 !important; border-radius: 2px !important; }
.stInfo    { background: rgba(0,255,225,0.06) !important; border: 1px solid rgba(0,255,225,0.3) !important; border-radius: 2px !important; }
.stWarning { background: rgba(255,184,0,0.08) !important; border: 1px solid rgba(255,184,0,0.3) !important; border-radius: 2px !important; }
.stError   { background: rgba(255,59,59,0.08) !important; border: 1px solid rgba(255,59,59,0.3) !important; border-radius: 2px !important; }

.stCodeBlock, code, pre {
    background: #071209 !important;
    border: 1px solid #1a3d1e !important;
    color: #b0ffb8 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 13px !important;
    border-radius: 2px !important;
}

[data-testid="stMetric"] {
    background: #0d1f10 !important;
    border: 1px solid #1a3d1e !important;
    border-radius: 2px !important;
    padding: 12px !important;
}
[data-testid="stMetricLabel"] { color: #5a8c5f !important; font-size: 11px !important; letter-spacing: 1px !important; }
[data-testid="stMetricValue"] { color: #00ff41 !important; font-family: 'Orbitron', monospace !important; }

hr { border-color: #1a3d1e !important; }

.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px);
    pointer-events: none;
    z-index: 9999;
}

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Helper Functions ─────────────────────────────────────────────────────────
def panel_header(code, title):
    st.markdown(f"""
    <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px 2px 0 0; 
                padding:16px 20px; margin-top:20px;'>
        <div style='display:flex; align-items:center; gap:12px;'>
            <span style='font-family:Orbitron,monospace; font-size:9px; color:#009922; 
                         border:1px solid #1a3d1e; padding:4px 8px;'>{code}</span>
            <span style='font-family:Orbitron,monospace; font-size:11px; letter-spacing:2px; 
                         color:#00ff41;'>{title}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def report_box(content):
    st.markdown(f"""
    <div style='background:#040d06; border:1px solid #1a3d1e; border-top:none;
                border-radius:0 0 2px 2px; padding:24px;'>
        <pre style='background:transparent; border:none; color:#b0ffb8; 
                   font-family:Share Tech Mono,monospace; font-size:13px; 
                   line-height:1.8; margin:0; white-space:pre-wrap;'>{content}</pre>
    </div>
    """, unsafe_allow_html=True)

# ── Sidebar Render Function ─────────────────────────────────────────────────
def render_sidebar():
    """Render the sidebar and return the API key"""
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <div style='font-family: Orbitron, monospace; font-size: 24px; font-weight: 900; 
                        color: #00ff41; letter-spacing: 6px; text-shadow: 0 0 20px rgba(0,255,65,0.4);'>
                PROJECT G
            </div>
            <div style='font-family: Share Tech Mono, monospace; font-size: 9px; 
                        color: #5a8c5f; letter-spacing: 3px; margin-top: 5px;'>
                DEFENSE INTELLIGENCE
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation
        st.markdown("""
        <div style='font-family: Orbitron, monospace; font-size: 10px; letter-spacing: 2px; 
                    color: #5a8c5f; margin-bottom: 10px;'>
            NAVIGATION
        </div>
        """, unsafe_allow_html=True)
        
        # Page navigation buttons
        if st.button("🏠 OVERVIEW", use_container_width=True, key="nav_home"):
            st.switch_page("app.py")
        
        if st.button("🖼️ VISUAL INTEL", use_container_width=True, key="nav_visual"):
            st.switch_page("pages/1_🔍_Visual_Intel.py")
        
        if st.button("📰 TEXT INTEL", use_container_width=True, key="nav_text"):
            st.rerun()  # Already on this page
        
        if st.button("⚔️ TACTICAL", use_container_width=True, key="nav_tactical"):
            st.info("Module 03 - Coming Soon")
        
        st.markdown("---")
        
        # API Key Section
        st.markdown("""
        <div style='font-family: Orbitron, monospace; font-size: 10px; letter-spacing: 2px; 
                    color: #5a8c5f; margin-bottom: 15px;'>
            API CONFIGURATION
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize session state if not exists
        if 'api_key' not in st.session_state:
            st.session_state.api_key = ""
        
        api_key = st.text_input(
            "Google Gemini API Key",
            type="password",
            value=st.session_state.api_key,
            placeholder="Enter your API key...",
            help="Required for AI-powered analysis modules",
            key="api_key_input"
        )
        
        if api_key:
            st.session_state.api_key = api_key
            if api_key.startswith("AIza"):
                st.markdown("""
                <div style='font-size: 10px; color: #00ff41; margin-top: 5px;'>
                    ⚡ API Key Valid
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='font-size: 10px; color: #ffb800; margin-top: 5px;'>
                    ⚠️ Invalid Key Format
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # System Info
        st.markdown("""
        <div style='font-family: Orbitron, monospace; font-size: 10px; letter-spacing: 2px; 
                    color: #5a8c5f; margin-bottom: 10px;'>
            SYSTEM STATUS
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style='font-size: 9px; color: #5a8c5f;'>MODULE</div>
            <div style='font-size: 11px; color: #00ffe1;'>TEXT INTEL</div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='font-size: 9px; color: #5a8c5f;'>STATUS</div>
            <div style='font-size: 11px; color: #00ff41;'>ACTIVE</div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Footer
        st.markdown("""
        <div style='margin-top: 20px;'>
            <div style='font-size: 9px; color: #004d14; text-align: center; letter-spacing: 1px;'>
                v1.5.0 | DEFENSE INTEL
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        return st.session_state.api_key

# ── Render Sidebar and Get API Key ──────────────────────────────────────────
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
