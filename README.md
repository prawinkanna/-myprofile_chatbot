# 🤖 Prawin Kanna P — AI Portfolio & Profile Chatbot

An intelligent, interactive AI conversational assistant powered by **Google Gemini 3.5 Flash** and grounded in the comprehensive academic, project, and professional profile of **Prawin Kanna P** (Applied Data Science postgraduate, Data Science Trainer at FITA Academy, and aspiring AI/ML Engineer).

---
## 🚀 Live Demo

Try my AI Profile Chatbot here:
👉 [Open My Chatbot](https://dxgbpzwxfjuwdvy7j8rg3n.streamlit.app/)


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


# 🤖 Prawin Kanna P — AI Portfolio & Profile Chatbot

An intelligent, interactive AI conversational assistant powered by **Google Gemini 3.5 Flash** and grounded in the complete professional profile of **Prawin Kanna P** (Applied Data Science postgraduate, Data Science Trainer at FITA Academy, and aspiring AI/ML Engineer).

---

## 🌟 Key Features

1. **⚡ Powered by Google Gemini 3.5 Flash**:
   - Integrated with Google AI Studio's latest authorization key specification.
   - Real-time Server-Sent Events (SSE) token streaming via `st.write_stream` in the web UI and live console stream in the CLI.
   - Automatic model fallback hierarchy: `gemini-3.5-flash` → `gemini-3.5-flash-lite` → `gemini-3.8-flash`.

2. **🛡️ Strict Guardrails Against Irrelevant Questions**:
   - The chatbot strictly answers questions related to Prawin's professional profile, education, 8 projects, skills, certifications, internships, and work experience.
   - When asked unwanted, off-topic, or irrelevant questions (e.g., cooking recipes, general trivia, weather, unrelated coding tasks), it politely declines with:
     > *"⚠️ Irrelevant question. I am Prawin Kanna P's dedicated AI Portfolio Assistant. I can only answer questions related to Prawin's professional profile, education, machine learning projects, technical skills, certifications, work experience, and career aspirations. Please feel free to ask anything about Prawin's background!"*

3. **🧠 Comprehensive Grounded Profile Knowledge Base (14 Sections)**:
   - **Academic Credentials**:
     - M.Sc. Applied Data Science | SRM Institute of Science & Technology, Trichy (2024–2026, **CGPA 8.54 First Class with Distinction**).
     - B.Sc. Statistics | St. Joseph's College (Autonomous), Trichy (2021–2024, **CGPA 6.6 First Class**).
   - **8 Featured Projects**:
     1. AI-Powered Data Analytics Chatbot (Gemini API, LangChain, LangGraph, Python MCP server, FAISS, Plotly, Streamlit).
     2. Personal Profile AI Chatbot (TF-IDF, Cosine Similarity, Gemini 3.5 streaming, Guardrails).
     3. End-to-End Machine Learning Web Application (Streamlit, Scikit-learn, 4 regression & 4 classification models).
     4. Comparative Analysis of ML Models for Sales Forecasting.
     5. Hybrid Machine Learning Model for Sales Forecasting (Prophet + Gradient Boosting).
     6. Computer Vision Image Preprocessing Web Application (OpenCV, Streamlit).
     7. Computer Vision Emotion Detection Web Application.
     8. Data Analytics & Business Intelligence Projects (Power BI, Tableau, Advanced Excel, DAX KPI dashboards).
   - **Professional Experience**:
     - Data Analytics & Data Science Trainer — FITA Academy, Anna Nagar, Chennai.
     - Property Manager — RS Residency.
     - Delivery Partner — Swiggy.
     - Client Management / Telecalling — IPPB Sector.
   - **Technical Internships**:
     - AI & ML Intern — VDart, Trichy (3 months).
     - Data Science & ML Intern — Edureka (6 months).
   - **Certifications & Conferences**:
     - Certifications: Python Analytics, Power BI, Advanced Excel, R.
     - Conference presentations at Dhanalakshmi Srinivasan Engineering College and SRM Institute.
     - Workshop: Agentic AI with Mission AI Initiative & FITA Academy.

4. **💡 1-Click Suggested Questions**:
   - Instant prompt chips for Education, Skills, FITA Academy, AI Data Analytics Bot, Sales Forecasting ML, Internships (VDart & Edureka), Career Goals, and Contact details.

5. **🖥️ Dual Interfaces**:
   - **Streamlit Web Application** (`app.py`): Full-featured visual UI with tabs for AI Chat, Project Explorer, and Resume Breakdown.
   - **Terminal CLI Chatbot** (`cli_chat.py`): Fast, lightweight command-line chat session with live streaming.

6. **🔒 Complete Privacy & Offline Fallback**:
   - API key isolated in `.env` and completely hidden from the UI.
   - Includes full offline fallback using scikit-learn TF-IDF semantic vectorization if network is unavailable.

---

## 📁 Project Architecture

```
prawin_profile_chatbot/
├── .env                # Stores GEMINI_API_KEY securely (git-ignored)
├── .env.example        # Environment template file
├── .gitignore          # Prevents committing API keys
├── app.py              # Streamlit Web Application (UI, streaming, tabs)
├── cli_chat.py         # Terminal CLI chatbot with streaming output
├── gemini_client.py    # Gemini 3.5 API client (SSE streaming & sync fallback)
├── profile_data.py     # Structured knowledge base extracted from resume
├── rag_engine.py       # Grounded RAG, prompt formatting & irrelevant question guardrail
├── test_chatbot.py     # Automated test suite
├── requirements.txt    # Python dependencies
└── README.md           # Documentation and run instructions
```

---

## 🚀 How to Run

### 1. Launch the Streamlit Web Application:
```powershell
cd C:\Users\Admin\.gemini\antigravity\scratch\prawin_profile_chatbot
streamlit run app.py
```
The application will open in your browser at `http://localhost:8501`.

### 2. Run the Terminal CLI Chatbot:
```powershell
cd C:\Users\Admin\.gemini\antigravity\scratch\prawin_profile_chatbot
python cli_chat.py
```

### 3. Run Automated Tests:
```powershell
cd C:\Users\Admin\.gemini\antigravity\scratch\prawin_profile_chatbot
python test_chatbot.py
```

---

## 📬 Contact Information

- **Full Name**: PRAWIN KANNA P
- **Location**: Trichy, Tamil Nadu, India (Target: Chennai / India)
- **Email**: p.prawinkanna@gmail.com | prawinkannathiru@gmail.com
- **Phone**: +91 6383297328
- **Portfolio**: [prawinkanna.github.io/prawin-portfolio](https://prawinkanna.github.io/prawin-portfolio/)
- **GitHub**: [github.com/prawinkanna](https://github.com/prawinkanna)
- **LinkedIn**: [linkedin.com/in/prawinkannapalaniyappan](https://www.linkedin.com/in/prawinkannapalaniyappan/)

