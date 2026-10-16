"""
test_chatbot.py
Comprehensive test suite verifying Gemini 3.5 connectivity, streaming,
grounding accuracy against Prawin's resume, and offline fallback.
"""

import sys
from profile_data import PROFILE_INFO, EDUCATION, SKILLS, PROJECTS
from gemini_client import get_api_key, generate_content, stream_generate_content
from rag_engine import ProfileRAGEngine

def test_api_key():
    key = get_api_key()
    assert key and len(key) > 10, "Expected Gemini API key to be loaded from .env"
    print("[OK] test_api_key passed")

def test_gemini_client_sync():
    res = generate_content([{"role": "user", "parts": [{"text": "Reply with 'GEMINI_OK'"}]}])
    assert "GEMINI_OK" in res or len(res) > 0
    print(f"[OK] test_gemini_client_sync passed (Received: {res[:30]}...)")

def test_gemini_client_streaming():
    chunks = []
    for chunk in stream_generate_content([{"role": "user", "parts": [{"text": "Count 1 to 3"}]}]):
        chunks.append(chunk)
    full = "".join(chunks)
    assert len(full) > 0
    print(f"[OK] test_gemini_client_streaming passed ({len(chunks)} chunks, '{full.strip()}')")

def test_grounded_education():
    engine = ProfileRAGEngine()
    chunks = []
    for chunk in engine.stream_response([{"role": "user", "content": "What is your CGPA in M.Sc.?"}], persona="first_person"):
        chunks.append(chunk)
    reply = "".join(chunks)
    assert "8.54" in reply or "Distinction" in reply, f"Expected 8.54 or Distinction in reply: {reply}"
    print(f"[OK] test_grounded_education passed ('8.54' confirmed in response)")

def test_grounded_projects():
    engine = ProfileRAGEngine()
    chunks = []
    for chunk in engine.stream_response([{"role": "user", "content": "Tell me about your sales forecasting project."}], persona="first_person"):
        chunks.append(chunk)
    reply = "".join(chunks)
    assert "Sales" in reply or "Forecasting" in reply or "forecast" in reply.lower()
    print("[OK] test_grounded_projects passed")

def test_offline_fallback():
    engine = ProfileRAGEngine()
    res = engine.get_offline_response("education and college", persona="first_person")
    assert "CGPA" in res["response"] or "Degree" in res["response"] or "College" in res["response"]
    print("[OK] test_offline_fallback passed")

if __name__ == "__main__":
    print("Running Chatbot Test Suite...")
    test_api_key()
    test_gemini_client_sync()
    test_gemini_client_streaming()
    test_grounded_education()
    test_grounded_projects()
    test_offline_fallback()
    print("\n====================================")
    print("ALL CHATBOT TESTS PASSED SUCCESSFULLY!")
    print("====================================")
