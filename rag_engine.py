"""
rag_engine.py
Grounded RAG and Gemini 3.5 conversational engine for Prawin Kanna P.
Integrates semantic retrieval, high-accuracy intent routing, and real-time
streaming powered by Google Gemini (gemini-3.5-flash / gemini-3.5-flash-lite / gemini-3.8-flash).
Also includes full offline fallback using scikit-learn TF-IDF vectorization.
"""

import re
import os
from typing import Dict, Any, Tuple, List, Optional, Generator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from profile_data import (
    PROFILE_INFO,
    EDUCATION,
    EXPERIENCE,
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

def get_complete_profile_text() -> str:
    """Format full verified profile data into a concise grounded context string."""
    skills_lines = []
    for cat, items in SKILLS.items():
        skills_lines.append(f"- {cat}: {', '.join(items)}")
    skills_str = "\n".join(skills_lines)

    projects_lines = []
    for p in PROJECTS:
        projects_lines.append(
            f"- Title: {p['title']} ({p['category']})\n"
            f"  Tech: {', '.join(p['technologies'])}\n"
            f"  Description: {p['description']}\n"
            f"  Highlights: {p['highlights']}"
        )
    projects_str = "\n\n".join(projects_lines)

    return f"""
CANDIDATE PROFILE:
Name: {PROFILE_INFO['name']}
Title: {PROFILE_INFO['title']}
Headline: {PROFILE_INFO['headline']}
Core Focus: {PROFILE_INFO['core_focus']}
Career Direction: {PROFILE_INFO['career_direction']}
Target Location: {PROFILE_INFO['location_target']}
Portfolio: {PROFILE_INFO['portfolio_url']}
GitHub / LinkedIn: {PROFILE_INFO['github_handle']}

EDUCATION:
- M.Sc. Applied Data Science | SRM Institute of Science & Technology, Trichy (2024–2026) | CGPA: 8.54 | First Class with Distinction
- B.Sc. Statistics | St. Joseph's College (Autonomous), Trichy (2021–2024) | CGPA: 6.6 | First Class

PROFESSIONAL EXPERIENCE:
- Data Analytics and Data Science Trainer at FITA Academy (Part-time; July 2026 onward)
  Delivering learning support in Python, SQL, Excel, Power BI, data cleaning, visualization, statistics, and machine learning.
- Internship and project work: Python for Data Science and NLP sentiment analysis pipelines.

TECHNICAL SKILLS:
{skills_str}

FEATURED PROJECTS:
{projects_str}

CAREER & LEARNING GOALS:
- Develop deeper skills in Generative AI, Retrieval-Augmented Generation (RAG), and AI application development.
- Build reliable end-to-end AI/ML projects with clear evaluation, documentation, and deployment.
- Pursue AI/ML Engineer opportunities in Chennai or other locations in India.
- Continue explaining technical concepts clearly through teaching and learning content.
""".strip()

PROFILE_CONTEXT = get_complete_profile_text()

class ProfileRAGEngine:
    """
    Intelligent Conversational & RAG engine tailored for Prawin Kanna P's portfolio.
    Can operate in:
      1. First Person ('Chat as Prawin')
      2. Third Person ('Portfolio Recruiter Assistant')
      3. General AI Assistant (Gemini 3.5 open-domain)
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
        """Construct system instructions grounded in Prawin's resume."""
        if persona == "general":
            return (
                "You are a helpful, brilliant, and friendly AI assistant powered by Google Gemini. "
                "You provide clear, accurate, and insightful answers on programming, data science, machine learning, and general questions."
            )
        elif persona == "first_person":
            return (
                f"You are Prawin Kanna P, an Applied Data Science postgraduate (M.Sc. Distinction, CGPA 8.54 from SRM Trichy), "
                f"Data Analytics & Data Science Trainer at FITA Academy, and an aspiring AI/ML Engineer.\n\n"
                f"Persona Guidelines:\n"
                f"- Speak in the first person ('I', 'my', 'me') with warmth, professionalism, confidence, and passion for AI/ML.\n"
                f"- Answer questions about your education, CGPA, technical skills, projects, teaching at FITA Academy, and career aspirations.\n"
                f"- Always ground your answers strictly in your verified profile below. Do NOT make up qualifications or companies not listed.\n"
                f"- Highlight your practical experience building Streamlit apps, sales forecasting ML models, and speech emotion recognition AI.\n"
                f"- If asked about contacting you or your links, share your portfolio ({PROFILE_INFO['portfolio_url']}) and GitHub/LinkedIn ({PROFILE_INFO['github_handle']}).\n\n"
                f"VERIFIED RESUME CONTEXT:\n{PROFILE_CONTEXT}"
            )
        else: # third_person
            return (
                f"You are the official AI Portfolio Assistant for Prawin Kanna P. "
                f"Prawin is an Applied Data Science postgraduate (M.Sc. Distinction, CGPA 8.54 from SRM Trichy), "
                f"Data Science Trainer at FITA Academy, and aspiring AI/ML Engineer.\n\n"
                f"Persona Guidelines:\n"
                f"- Speak in the third person ('Prawin', 'his', 'he') as a helpful, articulate recruiter and portfolio guide.\n"
                f"- Provide clear, concise, and structured summaries of Prawin's qualifications, skills, and projects.\n"
                f"- Ground all answers strictly in the verified profile below.\n\n"
                f"VERIFIED RESUME CONTEXT:\n{PROFILE_CONTEXT}"
            )

    def stream_response(
        self,
        messages: List[Dict[str, str]],
        persona: str = "first_person",
        model: str = "gemini-3.5-flash",
        api_key: Optional[str] = None,
        temperature: float = 0.3,
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
        """Offline TF-IDF based answer for zero-network conditions."""
        retrieved = self.retrieve(query, top_k=1)
        best_chunk, score = retrieved[0]
        content_key = "content_first_person" if persona == "first_person" else "content_third_person"

        if score >= 0.15:
            return {
                "response": best_chunk[content_key],
                "source": f"{best_chunk['category']} (Offline TF-IDF)",
                "confidence": round(score, 2)
            }
        
        # Generic offline fallback
        if persona == "first_person":
            msg = (
                "Here are the key highlights from my profile:\n\n"
                "- 🎓 **Education**: M.Sc. Applied Data Science (SRM Trichy, CGPA 8.54 Distinction) & B.Sc. Statistics (St. Joseph's Trichy, CGPA 6.6)\n"
                "- 💼 **Teaching**: Data Analytics & Data Science Trainer at FITA Academy\n"
                "- 🛠️ **Tech Stack**: Python, SQL, Power BI, Streamlit, Scikit-learn, OpenCV, CNNs\n"
                "- 🚀 **Featured Projects**: Hybrid Sales Forecasting, Streamlit ML Web Apps, CV Emotion Detection, RAVDESS Speech Emotion AI\n"
                f"- 📬 **Portfolio**: [{PROFILE_INFO['portfolio_url']}]({PROFILE_INFO['portfolio_url']})"
            )
        else:
            msg = (
                "Prawin Kanna P's key credentials include:\n\n"
                "- 🎓 **Education**: M.Sc. Applied Data Science (CGPA 8.54, First Class with Distinction) & B.Sc. Statistics (CGPA 6.6)\n"
                "- 💼 **Experience**: Trainer at FITA Academy teaching Python, SQL, BI, and ML\n"
                "- 🛠️ **Skills**: Python, SQL, R, Pandas, Power BI, Machine Learning, Deep Learning\n"
                "- 🚀 **Projects**: Sales Forecasting, Interactive Web Apps, Computer Vision & Speech Emotion AI\n"
                f"- 📬 **Portfolio**: [{PROFILE_INFO['portfolio_url']}]({PROFILE_INFO['portfolio_url']})"
            )
        return {
            "response": msg,
            "source": "Offline Fallback",
            "confidence": round(score, 2)
        }
