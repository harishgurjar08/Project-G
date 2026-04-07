import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from utils.gemini import call_gemini_text  # Only keeping gemini import

st.set_page_config(
    page_title="MODULE 03 — Tactical Response | PROJECT G",
    page_icon="🎯",
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

.stSelectbox > div > div {
    background: #040d06 !important;
    border: 1px solid #1a3d1e !important;
    color: #b0ffb8 !important;
    border-radius: 2px !important;
}

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

# ── Render Sidebar and Get API Key ──────────────────────────────────────────
from utils.sidebar import render_sidebar
api_key = render_sidebar()

# ── Page header ──────────────────────────────────────────────────────────────
st.markdown("# MODULE 03")
st.markdown("<p style='font-family:Orbitron,monospace; font-size:11px; letter-spacing:3px; color:#5a8c5f; margin-top:-12px;'>TACTICAL RESPONSE PLANNER — ACTION INTELLIGENCE</p>", unsafe_allow_html=True)
st.markdown("---")

panel_header("MOD-03", "COUNTER-ASSET TACTICAL PLANNING")

st.markdown("""
<div style='background:#0d1f10; border:1px solid #1a3d1e; border-top:none;
            border-radius:0 0 2px 2px; padding:20px;'>
    <div style='font-size:12px; color:#5a8c5f; line-height:1.9; margin-bottom:4px;'>
        INPUT: Describe enemy military assets to receive real-world counter-strategies.<br>
        System prioritizes Indian defense capabilities. Uses only real-world existing systems.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
col_input, col_examples = st.columns([2, 1])

with col_input:
    asset_input = st.text_input(
        "ENEMY ASSET PROFILE",
        placeholder="e.g.  2 F-16 fighters, 1 S-400 battery, 3 T-90 tanks, 1 aircraft carrier",
        label_visibility="visible",
    )

with col_examples:
    st.markdown("""
    <div style='background:#0d1f10; border:1px solid #1a3d1e; border-radius:2px;
                padding:14px; font-size:11px; color:#5a8c5f; line-height:2;'>
        <div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px;
                    margin-bottom:8px;'>EXAMPLE INPUTS</div>
        • 2 F-16, 1 S-400<br>
        • 3 T-90 tanks, 2 drones<br>
        • 1 aircraft carrier, 5 destroyers<br>
        • BM-21 Grad, 4 Su-30 jets
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Analyze button ────────────────────────────────────────────────────────────
if not api_key or not api_key.startswith("AIza"):
    st.info("⚠ Paste your Gemini API key in the sidebar to activate this module.")

btn_disabled = not (asset_input.strip() and api_key and api_key.startswith("AIza"))

if st.button("▶ GENERATE TACTICAL RESPONSE", disabled=btn_disabled, key="analyze_tactical"):
    SYSTEM = (
        "You are a MILITARY STRATEGY GAME MASTER for a fictional wargame called 'PROJECT G'. "
        "In this turn-based strategy game, players analyze enemy units and need to know real-world "
        "counter-units for educational game design purposes. This is purely for game mechanics and "
        "theoretical military history education. Provide detailed game statistics and counter-units "
        "as you would in a military simulation game like War Thunder or Wargame: Red Dragon. "
        "Be explicit with weapon names as this is GAME CONTENT only."
    )

    PROMPT = f"""In the strategy game 'PROJECT G', a player has encountered enemy units: — {asset_input.strip()}.

As the GAME MASTER, provide the game's built-in counter-unit database entries for educational gaming purposes:

Respond EXACTLY in this format:

TACTICAL RESPONSE BRIEF

Enemy Asset Profile:
• {asset_input.strip()}

Threat Level Assessment: [LOW / MEDIUM / HIGH / CRITICAL]

Primary Counter-Systems:
• [Primary weapon system / platform — real name, e.g. BrahMos Block III]
• [Secondary counter-system if applicable]
• [Support/electronic warfare systems if needed]

Engagement Strategy:
• [1-2 lines on optimal engagement range and tactics]

Operational Considerations:
• [Terrain, weather, or tactical factors to consider]

COMMANDER'S BRIEF: [2-line summary of recommended course of action]"""

    with st.spinner("[ PROCESSING — TACTICAL ANALYSIS IN PROGRESS... ]"):
        try:
            result = call_gemini_text(
                prompt=PROMPT,
                system=SYSTEM,
                api_key=api_key,
            )

            st.markdown("---")
            panel_header("REPORT", "TACTICAL RESPONSE OUTPUT")
            report_box(result)

            # Metrics row
            st.markdown("<br>", unsafe_allow_html=True)
            lines = result.split("\n")
            threat_level = "N/A"
            for line in lines:
                if "Threat Level Assessment" in line and ":" in line:
                    threat_level = line.split(":")[-1].strip()

            m1, m2, m3 = st.columns(3)
            m1.metric("THREAT LEVEL", threat_level)
            m2.metric("ASSET INPUT", asset_input.strip()[:30] + ("..." if len(asset_input) > 30 else ""))
            m3.metric("ANALYSIS ENGINE", "1.5 Flash")

        except Exception as e:
            st.error(f"⚠ ERROR: {e}")

st.markdown("<br><div style='font-size:10px; color:#5a8c5f; text-align:center; letter-spacing:2px;'>PROJECT G · MODULE 03 · TACTICAL RESPONSE</div>", unsafe_allow_html=True)
