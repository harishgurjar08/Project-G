import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from utils.gemini import call_gemini_vision  # Only keeping gemini import

st.set_page_config(
    page_title="MODULE 01 — Image Intel | PROJECT G",
    page_icon="🔍",
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

/* FIXED: Hide Streamlit branding WITHOUT hiding sidebar */
[data-testid="stHeader"] { visibility: hidden !important; }
footer { visibility: hidden !important; }
#MainMenu { visibility: hidden !important; }
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
        
        # Navigation using st.page_link
        st.markdown("""
        <div style='font-family: Orbitron, monospace; font-size: 10px; letter-spacing: 2px; 
                    color: #5a8c5f; margin-bottom: 10px;'>
            NAVIGATION
        </div>
        """, unsafe_allow_html=True)
        
        st.page_link("app.py", label="🏠 OVERVIEW", icon="🛡️")
        st.page_link("pages/1_module01.py", label="🖼️ VISUAL INTEL", icon="🔍")
        st.page_link("pages/2_module02.py", label="📰 TEXT INTEL", icon="📡")
        st.page_link("pages/3_module03.py", label="⚔️ TACTICAL", icon="🎯")
        
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
            <div style='font-size: 11px; color: #00ffe1;'>VISUAL INTEL</div>
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
st.markdown("# MODULE 01")
st.markdown("<p style='font-family:Orbitron,monospace; font-size:11px; letter-spacing:3px; color:#5a8c5f; margin-top:-12px;'>DEEPFAKE IMAGE ANALYSIS — VISUAL INTELLIGENCE</p>", unsafe_allow_html=True)
st.markdown("---")

panel_header("MOD-01", "FORENSIC IMAGE ANALYSIS")

st.markdown("""
<div style='background:#0d1f10; border:1px solid #1a3d1e; border-top:none;
            border-radius:0 0 2px 2px; padding:20px;'>
    <div style='font-size:12px; color:#5a8c5f; line-height:1.9; margin-bottom:16px;'>
        OBJECTIVE: Forensic analysis to determine if an image is real or AI-generated.<br>
        Assesses operational risk for intelligence usage in the field.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Upload ────────────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "UPLOAD IMAGE FOR ANALYSIS",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="visible",
)

if uploaded_file:
    col_img, col_info = st.columns([1, 1])
    with col_img:
        st.image(uploaded_file, caption="UPLOADED — AWAITING ANALYSIS", use_container_width=True)
    with col_info:
        st.markdown(f"""
        <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px; padding:16px; font-size:12px; line-height:2.2;'>
            <div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px; color:#5a8c5f; margin-bottom:12px;'>FILE METADATA</div>
            <span style='color:#5a8c5f;'>► FILENAME &nbsp;</span><span style='color:#b0ffb8;'>{uploaded_file.name}</span><br>
            <span style='color:#5a8c5f;'>► TYPE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style='color:#b0ffb8;'>{uploaded_file.type}</span><br>
            <span style='color:#5a8c5f;'>► SIZE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style='color:#b0ffb8;'>{uploaded_file.size / 1024:.1f} KB</span><br>
            <span style='color:#5a8c5f;'>► STATUS &nbsp;&nbsp;&nbsp;</span><span style='color:#ffb800;'>READY FOR ANALYSIS</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Analyze button ────────────────────────────────────────────────────────────
btn_disabled = not (uploaded_file and api_key and api_key.startswith("AIza"))

if not api_key or not api_key.startswith("AIza"):
    st.info("⚠ Paste your Gemini API key in the sidebar to activate this module.")

if st.button("▶ INITIATE FORENSIC ANALYSIS", disabled=btn_disabled, key="analyze_img"):
    SYSTEM = (
        "You are PROJECT G, a Defense Intelligence AI specializing in forensic visual analysis. "
        "Analyze images to determine if they are real or AI-generated/deepfake. "
        "Respond in strict format. Be factual and analytical. "
        "No casual language, no emojis."
    )

    PROMPT = """Analyze this image for signs of deepfake or AI generation. Cover: facial deformation, lighting/shadow inconsistencies, edge blending artifacts, texture anomalies, background distortion, compression artifacts.

Respond EXACTLY in this format:

DEEPFAKE ANALYSIS REPORT


Deepfake Probability     : XX%
AI Generation Likelihood : XX%
Likely Subject           : [describe main object/person/scene]

Threat Assessment        : [LOW RISK / MEDIUM RISK / HIGH RISK]

Key Indicators Detected:
• [Specific visual indicator 1]
• [Specific visual indicator 2]
• [Specific visual indicator 3]
• [Specific visual indicator 4]

Metadata Analysis:
• [Observation about compression, artifacts, or digital fingerprints]

Operational Note:
• [1-line implication]

ANALYST VERDICT: [1 sentence final assessment]"""

    with st.spinner("[ PROCESSING — FORENSIC ANALYSIS IN PROGRESS... ]"):
        try:
            image_bytes = uploaded_file.read()
            result = call_gemini_vision(
                prompt=PROMPT,
                system=SYSTEM,
                api_key=api_key,
                image_bytes=image_bytes,
                mime_type=uploaded_file.type,
            )

            st.markdown("---")
            panel_header("REPORT", "DEEPFAKE ANALYSIS OUTPUT")
            report_box(result)

            # Metrics row
            st.markdown("<br>", unsafe_allow_html=True)
            lines = result.split("\n")
            deepfake_pct, ai_pct, threat = "N/A", "N/A", "N/A"
            for line in lines:
                if "Deepfake Probability" in line and ":" in line:
                    deepfake_pct = line.split(":")[-1].strip()
                if "AI Generation Likelihood" in line and ":" in line:
                    ai_pct = line.split(":")[-1].strip()
                if "Threat Assessment" in line and ":" in line:
                    threat = line.split(":")[-1].strip()

            m1, m2, m3 = st.columns(3)
            m1.metric("DEEPFAKE PROBABILITY", deepfake_pct)
            m2.metric("AI GENERATION LIKELIHOOD", ai_pct)
            m3.metric("THREAT ASSESSMENT", threat)

        except Exception as e:
            st.error(f"⚠ ERROR: {e}")

st.markdown("<br><div style='font-size:10px; color:#5a8c5f; text-align:center; letter-spacing:2px;'>PROJECT G · MODULE 01 · VISUAL INTELLIGENCE</div>", unsafe_allow_html=True)
