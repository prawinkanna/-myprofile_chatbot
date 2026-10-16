# 🤖 Prawin Kanna P — AI Portfolio & Profile Chatbot

An intelligent, interactive AI conversational assistant powered by **Google Gemini 3.5 Flash** and grounded in the comprehensive academic, project, and professional profile of **Prawin Kanna P** (Applied Data Science postgraduate, Data Science Trainer at FITA Academy, and aspiring AI/ML Engineer).

---

## 🌟 Key Features

1. **⚡ Powered by Google Gemini 3.5 Flash**:
   - Integrated with Google AI Studio's latest `AQ.` authorization key specification.
   - Real-time Server-Sent Events (SSE) token streaming via `st.write_stream` in the web UI and live console stream in the CLI.
   - Automatic model fallback hierarchy: `gemini-3.5-flash` → `gemini-3.5-flash-lite` → `gemini-3.8-flash`.

2. **🎭 Dynamic Personas & Modes**:
   - **Chat as Prawin (1st Person)**: Speaks directly as Prawin with technical depth, passion for data science, and enthusiasm.
   - **Portfolio Assistant (3rd Person)**: Objective, recruiter-friendly biographical guide.
   - **General AI Assistant**: Open-domain conversational AI assistant for coding, math, and data science questions.

3. **🧠 Zero-Hallucination Grounded RAG Knowledge Base**:
   - Accurately grounded in all verified records from Prawin's 2-page profile:
     - **M.Sc. Applied Data Science** (SRM Trichy, **CGPA 8.54 First Class with Distinction**).
     - **B.Sc. Statistics** (St. Joseph's College Autonomous Trichy, **CGPA 6.6 First Class**).
     - **Trainer at FITA Academy** teaching Python, SQL, Excel, Power BI, Statistics, and Machine Learning.
     - **Machine Learning Projects**: Hybrid Sales Forecasting, Streamlit ML Web App, Data Analysis & Visualization App, Computer Vision Emotion Detection, and RAVDESS Speech Emotion Recognition.

4. **💡 1-Click Suggested Questions**:
   - Instant prompt buttons for Education, Skills, FITA Academy, ML Projects, Streamlit apps, Speech Emotion AI, Career Goals, and Contact links.

5. **🖥️ Dual Interfaces**:
   - **Streamlit Web Application** (`app.py`): Full-featured visual UI with tabs for AI Chat, Project Explorer, and Resume Breakdown.
   - **Terminal CLI Chatbot** (`cli_chat.py`): Fast, lightweight command-line chat session with live streaming.

6. **🔒 Resilient & Offline Fallback**:
   - Automatically loads API key from `.env`.
   - Includes full offline fallback using scikit-learn TF-IDF semantic vectorization if network is unavailable.

---

## 📁 Project Architecture

```
prawin_profile_chatbot/
├── .env                # Stores GEMINI_API_KEY securely
├── app.py              # Streamlit Web Application (UI, streaming, tabs)
├── cli_chat.py         # Terminal CLI chatbot with streaming output
├── gemini_client.py    # Gemini 3.5 API client (SSE streaming & sync fallback)
├── profile_data.py     # Structured knowledge base extracted from resume
├── rag_engine.py       # Grounded RAG, prompt formatting & offline retrieval
├── test_chatbot.py     # Automated test suite
├── requirements.txt    # Python dependencies
└── README.md           # Documentation and run instructions
```

---



## 🎓 Profile Highlights

- **Master's**: M.Sc. Applied Data Science — SRM Institute of Science & Technology, Trichy (**CGPA 8.54, First Class with Distinction**)
- **Bachelor's**: B.Sc. Statistics — St. Joseph's College (Autonomous), Trichy (**CGPA 6.6, First Class**)
- **Professional Role**: Data Analytics & Data Science Trainer at FITA Academy
- **Core Skills**: Python, SQL, R, Pandas, NumPy, Power BI, Tableau, Scikit-learn, Streamlit, OpenCV, CNNs
- **Target Role**: AI/ML Engineer (Chennai & across India)
- **Portfolio**: [prawinkanna.github.io/prawin-portfolio](https://prawinkanna.github.io/prawin-portfolio)
