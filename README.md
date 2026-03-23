# PROJECT G — Defense Intelligence System
### Streamlit Dashboard · Powered by Google Gemini (Free Tier)

---

## Project Structure

```
project_g/
├── app.py                   ← Main entry point (Overview page)
├── requirements.txt         ← Python dependencies
├── .streamlit/
│   └── config.toml          ← Theme & server config
├── pages/
│   ├── 1_module01.py        ← Module 01: Deepfake Image Analysis
│   ├── 2_module02.py        ← Module 02: Fake News Detection
│   └── 3_module03.py        ← Module 03: Tactical Response Planner
└── utils/
    ├── __init__.py
    ├── gemini.py            ← Gemini API helpers (text + vision)
    └── sidebar.py           ← Shared sidebar, CSS, components
```

---

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a FREE Gemini API key
1. Go to **https://aistudio.google.com**
2. Sign in with any Google account
3. Click **"Get API Key"** → **"Create API key"**
4. Copy the key (starts with `AIzaSy...`)

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

### 5. Paste your API key
Paste your Gemini key into the sidebar input field — all 3 modules activate instantly.

---

## Free Tier Limits (Gemini 1.5 Flash)
| Limit | Value |
|-------|-------|
| Requests per minute | 15 |
| Requests per day | 1,500 |
| Tokens per minute | 1,000,000 |
| Cost | **FREE** |

---

## Modules

| Module | Function | Input |
|--------|----------|-------|
| 01 — IMAGE INTEL | Deepfake detection | Upload JPG/PNG/WEBP |
| 02 — TEXT INTEL | Fake news analysis | Paste article/headline |
| 03 — TACTICAL RESPONSE | Counter-asset planning | Type enemy assets |

---

## Deploy to Streamlit Cloud (Free)
1. Push this folder to a GitHub repo
2. Go to **share.streamlit.io**
3. Connect your repo → set `app.py` as main file
4. Add your Gemini API key as a **Secret** in the app settings:
   - Key: `GEMINI_API_KEY`
5. Deploy — your dashboard is live on a public URL

---

*PROJECT G v2.0 — Authorized Use Only*
