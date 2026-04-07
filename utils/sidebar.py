"""
utils/sidebar.py
Renders the shared sidebar across all pages.
"""

import streamlit as st


def render_sidebar() -> str:
    """Render sidebar, return API key string (empty if not set)."""
    with st.sidebar:
        st.markdown("""
        <div style='text-align:center; padding: 20px 0 10px;'>
            <div style='font-family:Orbitron,monospace; font-size:22px; font-weight:900;
                        color:#00ff41; letter-spacing:6px;
                        text-shadow: 0 0 20px rgba(0,255,65,0.5);'>PROJECT G</div>
            <div style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:3px;
                        color:#5a8c5f; margin-top:4px;'>DEFENSE INTELLIGENCE SYSTEM</div>
        </div>
        <hr style='border-color:#1a3d1e; margin:10px 0 20px;'>
        """, unsafe_allow_html=True)

        st.markdown(
            "<div style='font-family:Orbitron,monospace; font-size:9px; "
            "letter-spacing:2px; color:#5a8c5f; margin-bottom:8px;'>API CONFIGURATION</div>",
            unsafe_allow_html=True,
        )

        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            placeholder="AIzaSy... (free at aistudio.google.com)",
            key="gemini_api_key",
            label_visibility="collapsed",
        )

        if api_key:
            if api_key.startswith("AIza"):
                st.success("✓  KEY SET — GEMINI FREE TIER")
            else:
                st.error("✗  INVALID KEY FORMAT")
        else:
            st.warning("⚠  NO KEY — MODULES OFFLINE")

        st.markdown("<hr style='border-color:#1a3d1e; margin:16px 0;'>", unsafe_allow_html=True)
        st.markdown(
            "<div style='font-family:Orbitron,monospace; font-size:9px; "
            "letter-spacing:2px; color:#5a8c5f; margin-bottom:12px;'>NAVIGATION</div>",
            unsafe_allow_html=True,
        )

        st.page_link("app.py",              label="◉  OVERVIEW",           icon="🛡️")
        st.page_link("pages/1_module01.py", label="01  IMAGE INTEL",        icon="🔍")
        st.page_link("pages/2_module02.py", label="02  TEXT INTEL",         icon="📡")
        st.page_link("pages/3_module03.py", label="03  TACTICAL RESPONSE",  icon="🎯")

        st.markdown("<hr style='border-color:#1a3d1e; margin:16px 0;'>", unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size:10px; color:#5a8c5f; line-height:2.2;'>
        ► ENGINE &nbsp;&nbsp; <span style='color:#00ffe1;'>GEMINI 1.5 FLASH</span><br>
        ► COST &nbsp;&nbsp;&nbsp;&nbsp; <span style='color:#00ff41;'>FREE TIER</span><br>
        ► LIMIT &nbsp;&nbsp;&nbsp; <span style='color:#ffb800;'>15 REQ/MIN</span><br>
        ► STATUS &nbsp;&nbsp; <span style='color:#00ff41;'>ACTIVE</span>
        </div>
        """, unsafe_allow_html=True)

    return api_key or ""


def inject_global_css():
    """Inject shared dashboard CSS."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

    .stApp { background-color: #040d06 !important; font-family: 'Share Tech Mono', monospace !important; }

    [data-testid="stSidebar"] { background-color: #071209 !important; border-right: 1px solid #1a3d1e !important; }
    [data-testid="stSidebar"] * { font-family: 'Share Tech Mono', monospace !important; color: #b0ffb8 !important; }

    h1, h2, h3 { font-family: 'Orbitron', monospace !important; color: #00ff41 !important; letter-spacing: 4px !important; }
    h1 { font-size: 22px !important; text-shadow: 0 0 20px rgba(0,255,65,0.4); }
    h2 { font-size: 15px !important; color: #00cc33 !important; }
    h3 { font-size: 12px !important; color: #009922 !important; }

    p, li, span, label, div { color: #b0ffb8 !important; font-family: 'Share Tech Mono', monospace !important; }

    .stTextInput > div > div > input,
    .stTextArea  > div > div > textarea {
        background-color: #040d06 !important;
        border: 1px solid #1a3d1e !important;
        color: #b0ffb8 !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 13px !important;
        border-radius: 2px !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea  > div > div > textarea:focus {
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
    }
    .stButton > button:hover { background: rgba(0,255,65,0.1) !important; border-color: #00ff41 !important; }

    [data-testid="stFileUploader"] {
        background: #040d06 !important;
        border: 1px dashed #2a6b30 !important;
        border-radius: 2px !important;
    }

    .stSuccess { background: rgba(0,255,65,0.08)  !important; border: 1px solid #009922 !important; border-radius: 2px !important; }
    .stInfo    { background: rgba(0,255,225,0.06) !important; border: 1px solid rgba(0,255,225,0.3) !important; border-radius: 2px !important; }
    .stWarning { background: rgba(255,184,0,0.08) !important; border: 1px solid rgba(255,184,0,0.3) !important; border-radius: 2px !important; }
    .stError   { background: rgba(255,59,59,0.08) !important; border: 1px solid rgba(255,59,59,0.3)  !important; border-radius: 2px !important; }

    [data-testid="stMetric"] { background: #0d1f10 !important; border: 1px solid #1a3d1e !important; border-radius: 2px !important; padding: 12px !important; }
    [data-testid="stMetricLabel"] { color: #5a8c5f !important; font-size: 11px !important; }
    [data-testid="stMetricValue"] { color: #00ff41 !important; font-family: 'Orbitron', monospace !important; }

    hr { border-color: #1a3d1e !important; }
    [data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }

    .stApp::before {
        content: '';
        position: fixed; inset: 0;
        background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px);
        pointer-events: none;
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)


def panel_header(tag: str, title: str):
    """Render a panel header bar."""
    st.markdown(f"""
    <div style='background:rgba(0,255,65,0.025); border:1px solid #1a3d1e;
                border-radius:2px; padding:12px 20px; margin-bottom:0;
                display:flex; align-items:center; gap:12px;'>
        <span style='font-family:Orbitron,monospace; font-size:9px; letter-spacing:2px;
                     color:#040d06; background:#009922; padding:3px 8px; border-radius:1px;'>{tag}</span>
        <span style='font-family:Orbitron,monospace; font-size:11px; letter-spacing:3px;
                     color:#00cc33;'>{title}</span>
    </div>
    """, unsafe_allow_html=True)


def report_box(content: str, border_color: str = "#2a6b30"):
    """Render an intelligence report output box."""
    st.markdown(f"""
    <div style='background:#040d06; border:1px solid {border_color}; border-radius:2px;
                padding:20px; margin-top:16px; font-size:13px; line-height:1.9;
                white-space:pre-wrap; word-break:break-word;
                font-family:"Share Tech Mono",monospace; color:#b0ffb8;'>{content}</div>
    """, unsafe_allow_html=True)
