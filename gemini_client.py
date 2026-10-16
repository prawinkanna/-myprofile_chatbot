"""
gemini_client.py
High-performance, modular Google Gemini API client.
Supports real-time SSE streaming, synchronous calls, multi-turn history,
system instructions, and automatic model fallback.
"""

import os
import json
import requests
from typing import Generator, List, Dict, Any, Optional

DEFAULT_API_KEY = ""
FALLBACK_MODELS = [
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash"
]

def load_env_file(filepath: str = ".env") -> None:
    """Zero-dependency .env loader."""
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        except Exception:
            pass

load_env_file()

def get_api_key(override_key: Optional[str] = None) -> str:
    """Resolve the API key in priority order: override -> env var -> default key."""
    if override_key and override_key.strip():
        return override_key.strip()
    env_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if env_key:
        return env_key
    return DEFAULT_API_KEY

def build_gemini_payload(
    contents: List[Dict[str, Any]],
    system_instruction: Optional[str] = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1500
) -> Dict[str, Any]:
    """Format request body according to Google Gemini v1beta specification."""
    payload: Dict[str, Any] = {
        "contents": contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_output_tokens
        }
    }
    if system_instruction and system_instruction.strip():
        payload["systemInstruction"] = {
            "parts": [{"text": system_instruction.strip()}]
        }
    return payload

def stream_generate_content(
    contents: List[Dict[str, Any]],
    system_instruction: Optional[str] = None,
    model: str = "gemini-3.5-flash",
    api_key: Optional[str] = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1500,
    timeout: int = 60
) -> Generator[str, None, None]:
    """
    Stream generated content from Gemini API using SSE (Server-Sent Events).
    Yields chunks of text as they arrive in real-time.
    """
    resolved_key = get_api_key(api_key)
    if not resolved_key:
        yield "Error: No Gemini API Key provided. Please set GEMINI_API_KEY."
        return

    models_to_try = [model] + [m for m in FALLBACK_MODELS if m != model]
    payload = build_gemini_payload(
        contents=contents,
        system_instruction=system_instruction,
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )

    last_error = None
    for current_model in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{current_model}:streamGenerateContent?alt=sse&key={resolved_key}"
        headers = {"Content-Type": "application/json"}
        try:
            with requests.post(url, headers=headers, json=payload, stream=True, timeout=timeout) as resp:
                if resp.status_code == 200:
                    for line in resp.iter_lines():
                        if line:
                            decoded = line.decode("utf-8")
                            if decoded.startswith("data: "):
                                json_str = decoded[6:].strip()
                                if json_str:
                                    try:
                                        data = json.loads(json_str)
                                        candidates = data.get("candidates", [])
                                        if candidates:
                                            parts = candidates[0].get("content", {}).get("parts", [])
                                            for part in parts:
                                                text = part.get("text", "")
                                                if text:
                                                    yield text
                                    except Exception:
                                        pass
                    return  # Success, exit generator
                else:
                    last_error = f"Model {current_model} returned HTTP {resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            last_error = f"Model {current_model} connection error: {str(e)}"

    yield f"\n\n[Gemini API Error: {last_error}]"

def generate_content(
    contents: List[Dict[str, Any]],
    system_instruction: Optional[str] = None,
    model: str = "gemini-3.5-flash",
    api_key: Optional[str] = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1500,
    timeout: int = 30
) -> str:
    """Synchronous generation returning complete string output."""
    resolved_key = get_api_key(api_key)
    if not resolved_key:
        return "Error: No Gemini API Key provided. Please set GEMINI_API_KEY."

    models_to_try = [model] + [m for m in FALLBACK_MODELS if m != model]
    payload = build_gemini_payload(
        contents=contents,
        system_instruction=system_instruction,
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )

    last_error = None
    for current_model in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{current_model}:generateContent?key={resolved_key}"
        headers = {"Content-Type": "application/json"}
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
            if resp.status_code == 200:
                data = resp.json()
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    return "".join([p.get("text", "") for p in parts]).strip()
            else:
                last_error = f"Model {current_model} returned HTTP {resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            last_error = f"Model {current_model} connection error: {str(e)}"

    return f"[Gemini API Error: {last_error}]"
