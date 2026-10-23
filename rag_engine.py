"""
rag_engine.py
Grounded RAG and Gemini 3.5 conversational engine for Prawin Kanna P.
Integrates semantic retrieval, high-accuracy intent routing, strict off-topic guardrails,
and real-time streaming powered by Google Gemini (gemini-3.5-flash / gemini-3.5-flash-lite / gemini-3.8-flash).
Includes full offline fallback with TF-IDF vectorization.
"""

import re
import os
from typing import Dict, Any, Tuple, List, Optional, Generator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from profile_data import (
    PROFILE_INFO,
    PROFESSIONAL_SUMMARY,
    EDUCATION,
    EXPERIENCE,
    INTERNSHIPS,
    CERTIFICATIONS,
    CONFERENCE_PRESENTATIONS,
    WORKSHOPS,
    EXTRACURRICULARS,
    SKILLS,
    PROJECTS,
    CAREER_GOALS,
    KNOWLEDGE_CHUNKS
)
from gemini_client import (
    stream_generate_content,
    generate_content,
    get_api_key
)

IRRELEVANT_RESPONSE = (
    "⚠️ Irrelevant question. I am Prawin Kanna P's dedicated AI Portfolio Assistant. "
    "I can only answer questions related to Prawin's professional profile, education, "
    "machine learning projects, technical skills, certifications, work experience, and career aspirations. "
    "Please feel free to ask anything about Prawin's background!"
)

def get_complete_profile_text() -> str:
    """Format full verified profile data into a concise grounded context string."""
    skills_lines = []
    for cat, items in SKILLS.items():
        skills_lines.append(f"- {cat}: {', '.join(items)}")
    skills_str = "\n".join(skills_lines)

    projects_lines = []
    for p in PROJECTS:
        projects_lines.append(
            f"- Project: {p['title']} ({p['category']})\n"
            f"  Objective: {p['objective']}\n"
            f"  Tech Stack: {', '.join(p['technologies'])}\n"
            f"  Description: {p['description']}\n"
            f"  Highlights: {p['highlights']}"
        )
    projects_str = "\n\n".join(projects_lines)

    exp_lines = []
    for e in EXPERIENCE:
        exp_lines.append(
            f"- {e['role']} at {e['company']} ({e['period']})\n"
            f"  Summary: {e['summary']}\n"
            f"  Skills: {', '.join(e['skills_taught'])}\n"
            f"  Highlights: {e['highlights']}"
        )
    exp_str = "\n\n".join(exp_lines)

    intern_lines = []
    for i in INTERNSHIPS:
        intern_lines.append(
            f"- {i['role']} at {i['organization']} ({i['duration']})\n"
            f"  Focus: {', '.join(i['focus_areas'])}\n"
            f"  Tech: {', '.join(i['technologies'])}\n"
            f"  Summary: {i['summary']}"
        )
    intern_str = "\n\n".join(intern_lines)

    cert_lines = [f"- {c['title']} ({c['domain']})" for c in CERTIFICATIONS]
    cert_str = "\n".join(cert_lines)

    conf_lines = [f"- {c['title']} at {c['institution']} ({c['topic']})" for c in CONFERENCE_PRESENTATIONS]
    conf_str = "\n".join(conf_lines)

    return f"""
CANDIDATE PROFILE:
Name: {PROFILE_INFO['name']}
Title: {PROFILE_INFO['title']}
Headline: {PROFILE_INFO['headline']}
Current Location: {PROFILE_INFO['location']}
Target Job Locations: {PROFILE_INFO['location_target']}
Email: {PROFILE_INFO['email']} (Alt: {PROFILE_INFO['alternative_email']})
Phone: {PROFILE_INFO['phone']}
Portfolio Website: {PROFILE_INFO['portfolio_url']}
GitHub: {PROFILE_INFO['github_url']}
LinkedIn: {PROFILE_INFO['linkedin_url']}

PROFESSIONAL SUMMARY:
{PROFESSIONAL_SUMMARY}

EDUCATION:
- M.Sc. Applied Data Science | SRM Institute of Science & Technology, Trichy (2024–2026) | CGPA: 8.54 | First Class with Distinction
- B.Sc. Statistics | St. Joseph's College (Autonomous), Trichy (2021–2024) | CGPA: 6.6 | First Class

TECHNICAL SKILLS:
{skills_str}

FEATURED PROJECTS:
{projects_str}

PROFESSIONAL EXPERIENCE:
{exp_str}

INTERNSHIPS:
{intern_str}

CERTIFICATIONS:
{cert_str}

CONFERENCE PRESENTATIONS:
{conf_str}

WORKSHOPS & LEARNING:
- One-Day Agentic AI Workshop (Mission AI Initiative & FITA Academy)

EXTRACURRICULARS:
- Filmmaking & Storytelling: Short film making, screenplays, visual storytelling, team coordination, people & budget management.

CAREER OBJECTIVE & GOALS:
- Target Roles: AI/ML Engineer / Data Scientist / Generative AI Application Developer
- Target Locations: Chennai and other cities across India (open to remote/relocation).
- Goals: Developing practical GenAI (LangChain, MCP, RAG) and machine learning applications; continuing to teach data science.
""".strip()

PROFILE_CONTEXT = get_complete_profile_text()

class ProfileRAGEngine:
    """
    Intelligent Conversational & RAG engine tailored for Prawin Kanna P's portfolio.
    Guarantees strict domain bounding: rejects unwanted or off-topic questions.
    """

    def __init__(self):
        self.chunks = KNOWLEDGE_CHUNKS
        self.corpus = []
        for chunk in self.chunks:
            text = f"{chunk['category']} {chunk['keywords']} {chunk['content_third_person']}"
            self.corpus.append(text)
        
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    def retrieve(self, query: str, top_k: int = 2) -> List[Tuple[Dict[str, Any], float]]:
        """Compute cosine similarity between query and indexed chunks."""
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        ranked_indices = similarities.argsort()[::-1]
        results = []
        for idx in ranked_indices[:top_k]:
            results.append((self.chunks[idx], float(similarities[idx])))
        return results

    def build_system_instruction(self, persona: str = "first_person") -> str:
        """Construct system instructions grounded in Prawin's resume with strict relevance policy."""
        if persona == "first_person":
            persona_desc = (
                f"You are Prawin Kanna P himself.\n"
                f"- Speak in the first person ('I', 'my', 'me') with professionalism, warmth, confidence, and enthusiasm for AI/ML.\n"
                f"- Ground every single answer strictly in your verified resume context below.\n"
                f"- Share your actual contact info (Email: {PROFILE_INFO['email']}, Phone: {PROFILE_INFO['phone']}, Portfolio: {PROFILE_INFO['portfolio_url']}) when asked."
            )
        else: # third_person
            persona_desc = (
                f"You are the official AI Portfolio Assistant representing Prawin Kanna P.\n"
                f"- Speak in the third person ('Prawin', 'his', 'he') as a professional, articulate recruiter and portfolio guide.\n"
                f"- Ground every single answer strictly in Prawin's verified profile context below.\n"
                f"- Provide clean, structured, and insightful answers."
            )

        return f"""{persona_desc}

============================================================
CRITICAL POLICY: HANDLING UNWANTED & IRRELEVANT QUESTIONS
============================================================
1. YOU MUST ONLY answer questions directly related to Prawin Kanna P: his education, technical skills, projects (such as the AI Data Analytics Chatbot, Sales Forecasting, Streamlit apps, OpenCV vision, Power BI dashboards), work experience (FITA Academy trainer, RS Residency, Swiggy, IPPB), internships (VDart, Edureka), certifications, conference presentations, career goals, or contact information.
2. IF THE USER ASKS ANY UNWANTED, OFF-TOPIC, OR IRRELEVANT QUESTION that is NOT about Prawin Kanna P or his professional background (for example: general knowledge trivia, recipes/cooking, weather, sports, celebrity news, general non-profile coding tasks, politics, jokes, general philosophy, or unrelated queries):
   YOU MUST POLITELY DECLINE AND RESPOND EXACTLY OR SIMILAR TO:
   "{IRRELEVANT_RESPONSE}"
3. DO NOT answer off-topic questions under any circumstances. Do not write stories or poems about unrelated subjects. Always bring the user back to Prawin's profile.

============================================================
VERIFIED RESUME CONTEXT:
============================================================
{PROFILE_CONTEXT}
"""

    def stream_response(
        self,
        messages: List[Dict[str, str]],
        persona: str = "first_person",
        model: str = "gemini-3.5-flash",
        api_key: Optional[str] = None,
        temperature: float = 0.2,
        max_output_tokens: int = 1500
    ) -> Generator[str, None, None]:
        """
        Stream conversational answer using Gemini API with full chat history
        and grounded persona system instructions.
        """
        system_instruction = self.build_system_instruction(persona)
        
        # Format history for Gemini API
        contents = []
        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })

        # Yield streaming chunks
        yield from stream_generate_content(
            contents=contents,
            system_instruction=system_instruction,
            model=model,
            api_key=api_key,
            temperature=temperature,
            max_output_tokens=max_output_tokens
        )

    def get_offline_response(self, query: str, persona: str = "first_person") -> Dict[str, Any]:
        """Offline TF-IDF based answer for zero-network conditions with guardrail."""
        retrieved = self.retrieve(query, top_k=1)
        best_chunk, score = retrieved[0]
        content_key = "content_first_person" if persona == "first_person" else "content_third_person"

        # If query has very low similarity, treat as irrelevant question
        if score < 0.12:
            return {
                "response": IRRELEVANT_RESPONSE,
                "source": "Irrelevant Question Filter",
                "confidence": round(score, 2)
            }

        return {
            "response": best_chunk[content_key],
            "source": f"{best_chunk['category']} (Offline TF-IDF)",
            "confidence": round(score, 2)
        }
