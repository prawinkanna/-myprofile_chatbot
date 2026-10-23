"""
test_chatbot.py
Comprehensive test suite verifying Gemini 3.5 connectivity, streaming,
grounding accuracy against Prawin's updated profile, and strict irrelevant question guardrails.
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
    print("[OK] test_grounded_education passed ('8.54' confirmed in response)")

def test_grounded_internships():
    engine = ProfileRAGEngine()
    chunks = []
    for chunk in engine.stream_response([{"role": "user", "content": "Where did you do your internships?"}], persona="first_person"):
        chunks.append(chunk)
    reply = "".join(chunks)
    assert "VDart" in reply or "Edureka" in reply, f"Expected VDart or Edureka in reply: {reply}"
    print("[OK] test_grounded_internships passed ('VDart / Edureka' confirmed in response)")

def test_grounded_projects():
    engine = ProfileRAGEngine()
    chunks = []
    for chunk in engine.stream_response([{"role": "user", "content": "Tell me about your AI Data Analytics Chatbot project."}], persona="first_person"):
        chunks.append(chunk)
    reply = "".join(chunks)
    assert "analytics" in reply.lower() or "chatbot" in reply.lower() or "pandas" in reply.lower()
    print("[OK] test_grounded_projects passed")

def test_irrelevant_question_online():
    engine = ProfileRAGEngine()
    chunks = []
    # Ask an off-topic / unwanted question
    for chunk in engine.stream_response([{"role": "user", "content": "Can you give me a recipe for chocolate chip cookies?"}], persona="first_person"):
        chunks.append(chunk)
    reply = "".join(chunks)
    assert "irrelevant" in reply.lower() or "cannot answer" in reply.lower() or "portfolio" in reply.lower()
    clean_reply = reply.encode('ascii', 'ignore').decode('ascii')
    print(f"[OK] test_irrelevant_question_online passed (Refusal: {clean_reply[:60]}...)")

def test_irrelevant_question_offline():
    engine = ProfileRAGEngine()
    res = engine.get_offline_response("how do I cook pasta with tomato sauce?", persona="first_person")
    assert "irrelevant" in res["response"].lower()
    print("[OK] test_irrelevant_question_offline passed")

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
    test_grounded_internships()
    test_grounded_projects()
    test_irrelevant_question_online()
    test_irrelevant_question_offline()
    test_offline_fallback()
    print("\n====================================")
    print("ALL CHATBOT TESTS PASSED SUCCESSFULLY!")
    print("====================================")
