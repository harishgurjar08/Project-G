import streamlit as st

st.set_page_config(
    page_title="PROJECT G — Defense Intelligence System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

/* Root theme */
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

/* App background */
.stApp {
    background-color: #040d06 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Sidebar */
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

/* Main headers */
h1, h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #00ff41 !important;
    letter-spacing: 4px !important;
}
h1 { font-size: 24px !important; text-shadow: 0 0 20px rgba(0,255,65,0.4); }
h2 { font-size: 16px !important; color: #00cc33 !important; }
h3 { font-size: 13px !important; color: #009922 !important; }

/* All text */
p, li, span, label, div {
    color: #b0ffb8 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Inputs */
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

/* Buttons */
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

/* File uploader */
[data-testid="stFileUploader"] {
    background: #040d06 !important;
    border: 1px dashed #2a6b30 !important;
    border-radius: 2px !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #009922 !important;
}
[data-testid="stFileUploader"] * { color: #5a8c5f !important; }

/* Selectbox */
.stSelectbox > div > div {
    background: #040d06 !important;
    border: 1px solid #1a3d1e !important;
    color: #b0ffb8 !important;
    border-radius: 2px !important;
}

/* Success / info / warning / error boxes */
.stSuccess { background: rgba(0,255,65,0.08) !important; border: 1px solid #009922 !important; border-radius: 2px !important; }
.stInfo    { background: rgba(0,255,225,0.06) !important; border: 1px solid rgba(0,255,225,0.3) !important; border-radius: 2px !important; }
.stWarning { background: rgba(255,184,0,0.08) !important; border: 1px solid rgba(255,184,0,0.3) !important; border-radius: 2px !important; }
.stError   { background: rgba(255,59,59,0.08) !important; border: 1px solid rgba(255,59,59,0.3) !important; border-radius: 2px !important; }

/* Code blocks / report output */
.stCodeBlock, code, pre {
    background: #071209 !important;
    border: 1px solid #1a3d1e !important;
    color: #b0ffb8 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 13px !important;
    border-radius: 2px !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #0d1f10 !important;
    border: 1px solid #1a3d1e !important;
    border-radius: 2px !important;
    padding: 12px !important;
}
[data-testid="stMetricLabel"] { color: #5a8c5f !important; font-size: 11px !important; letter-spacing: 1px !important; }
[data-testid="stMetricValue"] { color: #00ff41 !important; font-family: 'Orbitron', monospace !important; }

/* Divider */
hr { border-color: #1a3d1e !important; }

/* Scanline overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px);
    pointer-events: none;
    z-index: 9999;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px;'>
        <div style='font-family: Orbitron, monospace; font-size: 22px; font-weight: 900;
                    color: #00ff41; letter-spacing: 6px;
                    text-shadow: 0 0 20px rgba(0,255,65,0.5);'>PROJECT G</div>
        <div style='font-family: Orbitron, monospace; font-size: 9px; letter-spacing: 3px;
                    color: #5a8c5f; margin-top: 4px;'>DEFENSE INTELLIGENCE SYSTEM</div>
    </div>
    <hr style='border-color:#1a3d1e; margin: 10px 0 20px;'>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px; color:#5a8c5f; margin-bottom:8px;'>API CONFIGURATION</div>", unsafe_allow_html=True)

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="AIzaSy... (free at aistudio.google.com)",
        key="gemini_api_key",
        label_visibility="collapsed",
    )

    if api_key:
        if api_key.startswith("AIza"):
            st.success("✓ KEY SET — GEMINI FREE TIER")
        else:
            st.error("✗ INVALID KEY FORMAT")
    else:
        st.warning("⚠ NO KEY — MODULES OFFLINE")

    st.markdown("<hr style='border-color:#1a3d1e; margin: 16px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px; color:#5a8c5f; margin-bottom:12px;'>NAVIGATION</div>
    """, unsafe_allow_html=True)

    st.page_link("app.py",            label="◉  OVERVIEW",              icon="🛡️")
    st.page_link("pages/1_module01.py", label="01  IMAGE INTEL",          icon="🔍")
    st.page_link("pages/2_module02.py", label="02  TEXT INTEL",           icon="📡")
    st.page_link("pages/3_module03.py", label="03  TACTICAL RESPONSE",    icon="🎯")

    st.markdown("<hr style='border-color:#1a3d1e; margin: 16px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:10px; color:#5a8c5f; line-height:2;'>
    ► ENGINE &nbsp;&nbsp; <span style='color:#00ffe1'>1.5 FLASH</span><br>
    ► COST &nbsp;&nbsp;&nbsp;&nbsp; <span style='color:#00ff41'>FREE TIER</span><br>
    ► LIMIT &nbsp;&nbsp;&nbsp; <span style='color:#ffb800'>15 REQ/MIN</span><br>
    ► STATUS &nbsp;&nbsp; <span style='color:#00ff41'>ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)

# ── Home page content ────────────────────────────────────────────────────────
st.markdown("# PROJECT G")
st.markdown("<p style='color:#5a8c5f; font-family:Orbitron,monospace; font-size:11px; letter-spacing:3px; margin-top:-12px;'>DEFENSE INTELLIGENCE SYSTEM — OVERVIEW</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px;
                padding:22px 20px; position:relative; overflow:hidden;
                border-bottom: 2px solid #009922;'>
        <div style='font-family:Orbitron,monospace; font-size:34px; font-weight:900;
                    color:#004d14; line-height:1; margin-bottom:10px;'>01</div>
        <div style='font-family:Orbitron,monospace; font-size:10px; letter-spacing:2px;
                    color:#00cc33; margin-bottom:8px;'>VISUAL INTELLIGENCE</div>
        <div style='font-size:11px; color:#5a8c5f; line-height:1.6;'>
            Forensic deepfake detection. Identifies AI-generated image manipulation
            patterns for battlefield intel validation.
        </div>
        <span style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:1px;
                     padding:3px 8px; border:1px solid #00ffe1; color:#00ffe1;
                     display:inline-block; margin-top:14px; border-radius:1px;'>IMAGE ANALYSIS</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px;
                padding:22px 20px; border-bottom: 2px solid #009922;'>
        <div style='font-family:Orbitron,monospace; font-size:34px; font-weight:900;
                    color:#004d14; line-height:1; margin-bottom:10px;'>02</div>
        <div style='font-family:Orbitron,monospace; font-size:10px; letter-spacing:2px;
                    color:#00cc33; margin-bottom:8px;'>TEXTUAL INTELLIGENCE</div>
        <div style='font-size:11px; color:#5a8c5f; line-height:1.6;'>
            Fake news and propaganda detection. Evaluates misinformation,
            psychological operations, and narrative manipulation.
        </div>
        <span style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:1px;
                     padding:3px 8px; border:1px solid #ffb800; color:#ffb800;
                     display:inline-block; margin-top:14px; border-radius:1px;'>NEWS / ARTICLE</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px;
                padding:22px 20px; border-bottom: 2px solid #009922;'>
        <div style='font-family:Orbitron,monospace; font-size:34px; font-weight:900;
                    color:#004d14; line-height:1; margin-bottom:10px;'>03</div>
        <div style='font-family:Orbitron,monospace; font-size:10px; letter-spacing:2px;
                    color:#00cc33; margin-bottom:8px;'>TACTICAL RESPONSE</div>
        <div style='font-size:11px; color:#5a8c5f; line-height:1.6;'>
            Counter-asset planning. Input enemy military assets to receive
            real-world counter-systems and engagement strategies.
        </div>
        <span style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:1px;
                     padding:3px 8px; border:1px solid #ff3b3b; color:#ff3b3b;
                     display:inline-block; margin-top:14px; border-radius:1px;'>ASSETS / STRATEGY</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Status panel
st.markdown("""
<div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px; padding:20px;'>
    <div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px;
                color:#5a8c5f; margin-bottom:16px;'>SYSTEM OPERATIONAL STATUS</div>
    <div style='line-height:2.4; font-size:12px;'>
        <span style='color:#5a8c5f;'>► AI ENGINE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span style='color:#00ffe1;'>ONLINE</span>
        <span style='color:#5a8c5f;'> — 1.5 Flash (can be upgraded further)</span><br>
        <span style='color:#5a8c5f;'>► MODULE 01 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span style='color:#00ff41;'>READY</span>
        <span style='color:#5a8c5f;'> — Deepfake Visual Analysis</span><br>
        <span style='color:#5a8c5f;'>► MODULE 02 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span style='color:#00ff41;'>READY</span>
        <span style='color:#5a8c5f;'> — Misinformation Detection</span><br>
        <span style='color:#5a8c5f;'>► MODULE 03 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span style='color:#00ff41;'>READY</span>
        <span style='color:#5a8c5f;'> — Tactical Counter Planning</span><br>
        <span style='color:#5a8c5f;'>► CLASSIFICATION &nbsp;</span>
        <span style='color:#ffb800;'>RESTRICTED — AUTHORIZED USE ONLY (api key can be limited to authorized user)</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='font-size:10px; color:#5a8c5f; text-align:center; letter-spacing:2px;'>
PROJECT G v2.0 &nbsp;|&nbsp; CLEARANCE: AUTHORIZED &nbsp;|&nbsp; ENGINE: GEMINI 1.5 FLASH (FREE)
</div>
""", unsafe_allow_html=True)
