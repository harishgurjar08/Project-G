import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from utils.sidebar import inject_global_css, render_sidebar, panel_header, report_box
from utils.gemini import call_gemini_text

st.set_page_config(
    page_title="MODULE 03 — Tactical Response | PROJECT G",
    page_icon="🎯",
    layout="wide",
)

inject_global_css()
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
        "You are PROJECT G, a Defense Intelligence AI specializing in tactical military analysis. "
        "Analyze enemy assets and recommend real-world counter-systems and strategies. "
        "RULES: Use ONLY real-world currently existing military systems. "
        "No fictional or speculative weapons. No political opinions. "
        "Prioritize Indian defense systems (BrahMos, Tejas Mk2, Agni-V, S-400 Triumf, "
        "Akash-NG, DRDO systems, etc.) when relevant. "
        "Be tactical, precise, and concise. Command-center format only."
    )

    PROMPT = f"""As a Defense Intelligence Expert, analyze this threat scenario: Enemy forces are equipped with — {asset_input.strip()}.

In real life, what are the best military systems and strategies currently existing in the world (with focus on Indian Defense capabilities) to counter and neutralize these assets?

Respond EXACTLY in this format:

TACTICAL RESPONSE BRIEF
════════════════════════════════════════

Enemy Asset Profile:
• {asset_input.strip()}

Threat Level Assessment: [LOW / MEDIUM / HIGH / CRITICAL]

Primary Counter-Systems:
• [Primary weapon system / platform — real name, e.g. BrahMos Block III]
• [Secondary counter weapon / platform]
• [Air defense / EW system if applicable]

Indian Defense Priority Systems:
• [Most applicable Indian system(s) — be specific]
• [Capability advantage in this scenario]

Global Best-in-Class Alternatives:
• [Non-Indian world-class system option 1]
• [Non-Indian world-class system option 2]

Engagement Strategy:
• Tactical Advantage     : [key edge to exploit]
• Detection Method       : [radar / satellite / AWACS / SIGINT approach]
• Engagement Principle   : [how to neutralize — standoff / close / EW]
• Recommended Formation  : [brief tactical note on force structure]
• Vulnerability to Exploit: [identified weak point in enemy assets]

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
            m3.metric("ANALYSIS ENGINE", "GEMINI 1.5 FLASH")

        except Exception as e:
            st.error(f"⚠ ERROR: {e}")

st.markdown("<br><div style='font-size:10px; color:#5a8c5f; text-align:center; letter-spacing:2px;'>PROJECT G · MODULE 03 · TACTICAL RESPONSE</div>", unsafe_allow_html=True)
