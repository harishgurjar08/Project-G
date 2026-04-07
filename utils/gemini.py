"""
utils/gemini.py
Shared Gemini API helpers for all Project G modules.
"""

import base64
import requests


GEMINI_MODEL    = "gemini-2.5-flash"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def call_gemini_text(prompt: str, system: str, api_key: str) -> str:
    """Call Gemini with text-only input."""
    url  = f"{GEMINI_BASE_URL}/{GEMINI_MODEL}:generateContent?key={api_key}"
    body = {
        "system_instruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 1024},
    }

    resp = requests.post(url, json=body, timeout=60)
    data = resp.json()

    if "error" in data:
        code = data["error"].get("code", "?")
        msg  = data["error"].get("message", "Unknown error")
        raise RuntimeError(f"GEMINI API ERROR [{code}]: {msg}")

    parts = data["candidates"][0]["content"]["parts"]
    return "".join(p.get("text", "") for p in parts)


def call_gemini_vision(
    prompt: str,
    system: str,
    api_key: str,
    image_bytes: bytes,
    mime_type: str,
) -> str:
    """Call Gemini with image + text input."""
    url        = f"{GEMINI_BASE_URL}/{GEMINI_MODEL}:generateContent?key={api_key}"
    image_b64  = base64.b64encode(image_bytes).decode("utf-8")

    body = {
        "system_instruction": {"parts": [{"text": system}]},
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"inline_data": {"mime_type": mime_type, "data": image_b64}},
                    {"text": prompt},
                ],
            }
        ],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 1024},
    }

    resp = requests.post(url, json=body, timeout=60)
    data = resp.json()

    if "error" in data:
        code = data["error"].get("code", "?")
        msg  = data["error"].get("message", "Unknown error")
        raise RuntimeError(f"GEMINI API ERROR [{code}]: {msg}")

    parts = data["candidates"][0]["content"]["parts"]
    return "".join(p.get("text", "") for p in parts)
