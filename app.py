"""
app.py
Prawin Kanna P | AI Portfolio & Profile Assistant
Interactive Streamlit Application powered by Google Gemini 3.5 Flash and Grounded Semantic RAG.
"""

import os
import datetime
import streamlit as st
from profile_data import (
    PROFILE_INFO,
    EDUCATION,
    EXPERIENCE,
    SKILLS,
    PROJECTS,
    CAREER_GOALS
)
from rag_engine import ProfileRAGEngine
from gemini_client import get_api_key

# Page Configuration
st.set_page_config(
    page_title="Prawin Kanna P | AI Portfolio Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    /* Gradient Main Header */
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1E88E5 0%, #7E57C2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #555;
        margin-bottom: 1.2rem;
    }
    /* Badges */
    .badge-pill {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 600;
        background-color: #E3F2FD;
        color: #1565C0;
        border: 1px solid #BBDEFB;
    }
    .badge-pill-green {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 600;
        background-color: #E8F5E9;
        color: #2E7D32;
        border: 1px solid #C8E6C9;
    }
    .badge-pill-purple {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 600;
        background-color: #F3E5F5;
        color: #6A1B9A;
        border: 1px solid #E1BEE7;
    }
    .profile-card {
        background-color: #F8F9FA;
        border-radius: 12px;
        padding: 1.2rem;
        border: 1px solid #E0E0E0;
        margin-bottom: 1.2rem;
    }
    .avatar-circle {
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1E88E5 0%, #9C27B0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.7rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .source-tag {
        font-size: 0.75rem;
        color: #888;
        font-style: italic;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "rag_engine" not in st.session_state:
    st.session_state.rag_engine = ProfileRAGEngine()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm **Prawin Kanna P**'s interactive AI assistant, powered by **Google Gemini 3.5**.\n\n"
                "I can answer any questions regarding my **academic qualifications** (M.Sc. Applied Data Science with Distinction), "
                "**technical skills** in Python, SQL & ML, **teaching experience at FITA Academy**, "
                "**featured projects** (Sales forecasting, Streamlit apps, Speech emotion AI), and **career aspirations**.\n\n"
                "Feel free to ask a question below or click any of the suggested prompt buttons!"
            ),
            "source": "System Welcome"
        }
    ]

# Sidebar Configuration
with st.sidebar:
    st.markdown("""
    <div class="avatar-circle">PK</div>
    <h3 style="margin-bottom:0;">Prawin Kanna P</h3>
    <p style="color:#666; font-size:0.85rem; margin-top:2px;">
        Applied Data Science | Data Science Trainer | Aspiring AI/ML Engineer
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Chat Settings")
    
    persona_option = st.radio(
        "Chatbot Persona",
        options=[
            "Chat as Prawin (1st Person)",
            "Portfolio Assistant (3rd Person)",
            "General AI Assistant (Gemini 3.5)"
        ],
        index=0
    )
    if "1st Person" in persona_option:
        persona = "first_person"
    elif "3rd Person" in persona_option:
        persona = "third_person"
    else:
        persona = "general"

    # Model Selection
    model_choice = st.selectbox(
        "Gemini Model",
        options=[
            "gemini-3.5-flash (Fast & Accurate)",
            "gemini-3.5-flash-lite (Ultra Lightweight)",
            "gemini-3.8-flash (Latest Preview)",
            "Offline Semantic Engine (No API)"
        ],
        index=0
    )
    
    if "gemini-3.5-flash-lite" in model_choice:
        selected_model = "gemini-3.5-flash-lite"
    elif "gemini-3.8-flash" in model_choice:
        selected_model = "gemini-3.8-flash"
    elif "Offline" in model_choice:
        selected_model = "offline"
    else:
        selected_model = "gemini-3.5-flash"

    # Backend API Key (Loaded securely from .env, completely hidden from UI)
    active_api_key = get_api_key()
    if active_api_key:
        st.caption("🟢 AI Assistant Online (Connected)")
    else:
        st.caption("🟡 Running in Offline Fallback Mode")

    with st.expander("🎛️ Model Parameters"):
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.3, step=0.05)
        max_tokens = st.slider("Max Tokens", min_value=256, max_value=2048, value=1200, step=128)

    st.markdown("---")
    st.markdown("### 📌 Key Highlights")
    st.markdown("""
    - 🎓 **M.Sc. Applied Data Science**  
      *SRM Trichy (2024–2026)* — **CGPA 8.54** (Distinction)
    - 🎓 **B.Sc. Statistics**  
      *St. Joseph's Trichy (2021–2024)* — **CGPA 6.6** (First Class)
    - 💼 **Trainer @ FITA Academy**  
      *Teaching Python, SQL, Power BI, ML, Statistics*
    - 🚀 **5+ ML & AI Projects**  
      *Sales Forecasting, Streamlit Apps, Speech Emotion AI*
    """)

    st.markdown("---")
    st.markdown("### 🌐 Connect with Prawin")
    st.markdown(f"🔗 [Portfolio Website]({PROFILE_INFO['portfolio_url']})")
    st.markdown("🐙 [GitHub: prawinkanna](https://github.com/prawinkanna)")
    st.markdown("💼 [LinkedIn: prawinkanna](https://linkedin.com/in/prawinkanna)")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": f"Chat reset! Ask me anything about {PROFILE_INFO['name']}'s qualifications, projects, or background.",
                    "source": "Reset"
                }
            ]
            st.rerun()
    with col2:
        chat_text = "\n\n".join([f"**{m['role'].capitalize()}**: {m['content']}" for m in st.session_state.messages])
        st.download_button(
            "💾 Export Chat",
            data=chat_text,
            file_name=f"prawin_chat_{datetime.date.today()}.md",
            mime="text/markdown",
            use_container_width=True
        )

# Main Title & Subtitle
st.markdown('<div class="main-title">Prawin Kanna P — AI Portfolio Chatbot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Explore my background, academic credentials, teaching experience, and machine learning projects powered by Google Gemini 3.5.</div>',
    unsafe_allow_html=True
)

# Badges
st.markdown("""
<div>
    <span class="badge-pill">🎓 M.Sc. Distinction (8.54 CGPA)</span>
    <span class="badge-pill-green">💼 FITA Academy Trainer</span>
    <span class="badge-pill-purple">🤖 Streamlit & ML Developer</span>
    <span class="badge-pill">⚡ Powered by Gemini 3.5 Flash</span>
</div>
""", unsafe_allow_html=True)

tab_chat, tab_explorer, tab_resume = st.tabs(["💬 AI Chat Assistant", "🚀 Projects & Experience Explorer", "📄 Full Resume Summary"])

# ==========================================
# TAB 1: AI CHAT ASSISTANT
# ==========================================
with tab_chat:
    st.markdown("##### 💡 Suggested Questions (Click any to ask immediately):")
    
    chip_cols_1 = st.columns(4)
    with chip_cols_1[0]:
        btn_edu = st.button("🎓 Education & Grades", key="chip_edu", use_container_width=True)
    with chip_cols_1[1]:
        btn_skills = st.button("🛠️ Technical Skills", key="chip_skills", use_container_width=True)
    with chip_cols_1[2]:
        btn_fita = st.button("💼 Experience @ FITA", key="chip_fita", use_container_width=True)
    with chip_cols_1[3]:
        btn_sales = st.button("📈 Sales Forecasting ML", key="chip_sales", use_container_width=True)

    chip_cols_2 = st.columns(4)
    with chip_cols_2[0]:
        btn_st = st.button("💻 Streamlit Apps", key="chip_st", use_container_width=True)
    with chip_cols_2[1]:
        btn_speech = st.button("🎙️ Speech Emotion AI", key="chip_speech", use_container_width=True)
    with chip_cols_2[2]:
        btn_goals = st.button("🎯 Career Goals & Jobs", key="chip_goals", use_container_width=True)
    with chip_cols_2[3]:
        btn_contact = st.button("📬 Contact & Portfolio", key="chip_contact", use_container_width=True)

    # Map clicked button to prompt
    chip_prompt = None
    if btn_edu:
        chip_prompt = "What is your educational background, institutions, and CGPA?"
    elif btn_skills:
        chip_prompt = "What technical skills, programming languages, and data science tools do you know?"
    elif btn_fita:
        chip_prompt = "Tell me about your experience as a trainer at FITA Academy."
    elif btn_sales:
        chip_prompt = "Tell me about your Hybrid Machine Learning Sales Forecasting project."
    elif btn_st:
        chip_prompt = "What Streamlit web applications have you built?"
    elif btn_speech:
        chip_prompt = "Tell me about your Speech Emotion Recognition project using the RAVDESS dataset."
    elif btn_goals:
        chip_prompt = "What are your career aspirations and are you open to AI/ML Engineer jobs in Chennai?"
    elif btn_contact:
        chip_prompt = "Where can I view your portfolio and how can I connect with you?"

    st.markdown("---")

    # Render Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("source"):
                st.markdown(f"<div class='source-tag'>Source: {message['source']}</div>", unsafe_allow_html=True)

    # Chat Input Box
    chat_input = st.chat_input("Ask about education, ML projects, skills, or career goals...")
    active_prompt = chip_prompt or chat_input

    if active_prompt:
        st.session_state.messages.append({"role": "user", "content": active_prompt})
        with st.chat_message("user"):
            st.markdown(active_prompt)

        # Generate Assistant Response
        with st.chat_message("assistant"):
            if selected_model == "offline" or not active_api_key:
                # Use offline TF-IDF engine
                offline_res = st.session_state.rag_engine.get_offline_response(active_prompt, persona=persona)
                st.markdown(offline_res["response"])
                source_label = offline_res["source"]
                full_reply = offline_res["response"]
            else:
                # Stream response from Gemini 3.5 API
                try:
                    stream_gen = st.session_state.rag_engine.stream_response(
                        messages=st.session_state.messages,
                        persona=persona,
                        model=selected_model,
                        api_key=active_api_key,
                        temperature=temperature,
                        max_output_tokens=max_tokens
                    )
                    full_reply = st.write_stream(stream_gen)
                    source_label = f"Google {selected_model} (Grounded)"
                except Exception as e:
                    # Graceful fallback to offline engine if network issue
                    offline_res = st.session_state.rag_engine.get_offline_response(active_prompt, persona=persona)
                    full_reply = f"[Offline Fallback due to connection issue: {e}]\n\n" + offline_res["response"]
                    st.markdown(full_reply)
                    source_label = "Offline Fallback"

            st.markdown(f"<div class='source-tag'>Source: {source_label}</div>", unsafe_allow_html=True)

        st.session_state.messages.append({
            "role": "assistant",
            "content": full_reply,
            "source": source_label
        })
        st.rerun()

# ==========================================
# TAB 2: PROJECTS & EXPERIENCE EXPLORER
# ==========================================
with tab_explorer:
    st.markdown("### 🚀 Featured Machine Learning & AI Projects")
    for proj in PROJECTS:
        with st.expander(f"📌 {proj['title']} — {proj['category']}", expanded=True):
            st.markdown(f"**Description**: {proj['description']}")
            st.markdown(f"**Key Highlights**: {proj['highlights']}")
            st.markdown("**Tech Stack**: " + " ".join([f"`{t}`" for t in proj['technologies']]))

    st.markdown("---")
    st.markdown("### 🎓 Academic Qualifications")
    col_edu1, col_edu2 = st.columns(2)
    with col_edu1:
        st.markdown("""
        <div class="profile-card">
            <h4>M.Sc. Applied Data Science</h4>
            <p><strong>Institution</strong>: SRM Institute of Science & Technology, Trichy</p>
            <p><strong>Period</strong>: 2024–2026</p>
            <p><strong>Result</strong>: <span style="color:#2E7D32; font-weight:700;">CGPA: 8.54 — First Class with Distinction</span></p>
            <p>Advanced focus on statistical modeling, machine learning algorithms, deep learning fundamentals, and data science pipelines.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_edu2:
        st.markdown("""
        <div class="profile-card">
            <h4>B.Sc. Statistics</h4>
            <p><strong>Institution</strong>: St. Joseph’s College (Autonomous), Trichy</p>
            <p><strong>Period</strong>: 2021–2024</p>
            <p><strong>Result</strong>: <span style="color:#1565C0; font-weight:700;">CGPA: 6.6 — First Class</span></p>
            <p>Strong mathematical foundation in probability distributions, regression theory, hypothesis testing, and exploratory data analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💼 Professional Experience")
    for exp in EXPERIENCE:
        with st.container():
            st.markdown(f"#### {exp['role']} — {exp['company']} ({exp['type']})")
            st.markdown(f"**Timeline**: *{exp['period']}*")
            st.markdown(f"{exp['summary']}")
            st.markdown(f"**Training / Skill Areas**: " + ", ".join(exp['skills_taught']))
            st.markdown(f"*{exp['highlights']}*")
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🛠️ Technical Skills Matrix")
    for category, skills_list in SKILLS.items():
        st.markdown(f"**{category}**")
        st.markdown(" ".join([f"`{s}`" for s in skills_list]))
        st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# TAB 3: FULL RESUME SUMMARY
# ==========================================
with tab_resume:
    st.markdown("### 📄 Complete Resume & Profile Breakdown")
    resume_md = f"""
# {PROFILE_INFO['name']}
**{PROFILE_INFO['title']}**

{PROFILE_INFO['headline']}

---

### 🎓 Education
- **M.Sc. Applied Data Science** | SRM Institute of Science & Technology, Trichy (2024–2026)  
  *Result*: **CGPA 8.54 (First Class with Distinction)**
- **B.Sc. Statistics** | St. Joseph’s College (Autonomous), Trichy (2021–2024)  
  *Result*: **CGPA 6.6 (First Class)**

---

### 💼 Professional Experience
- **Data Analytics and Data Science Trainer** — FITA Academy (Part-time, July 2026 onward)  
  *Delivering structured training in Python, SQL, Excel, Power BI, data cleaning, visualization, statistics, and machine learning.*
- **Internship & Project Experience** — Python for Data Science and NLP sentiment analysis workflows.

---

### 🛠️ Technical Skills
- **Programming**: Python, SQL, R
- **Data Analysis & BI**: Pandas, NumPy, Excel, Power BI, Tableau, SPSS, Data Cleaning, KPI Reporting, Interactive Dashboards
- **Machine Learning**: Regression, Classification, Clustering, Feature Engineering, Model Evaluation, Sales Forecasting
- **Deep Learning & CV**: CNN Fundamentals, OpenCV, Image Preprocessing, Emotion Detection
- **App Development & Tools**: Streamlit, Scikit-learn, Matplotlib, Jupyter Notebook, Google Colab, VS Code, GitHub

---

### 🚀 Selected Projects
1. **Hybrid Machine Learning Model for Sales Forecasting**: Blending multiple forecasting algorithms to estimate future sales.
2. **End-to-End Machine Learning Web App**: Streamlit-based workflow bringing model inference into an interactive UI.
3. **Data Analysis and Visualization Web App**: Dynamic web app for exploratory data analysis and visual KPI charts.
4. **Computer Vision Emotion Detection**: Image preprocessing and emotion recognition using OpenCV and CNN principles.
5. **Speech Emotion Recognition (In Progress)**: Audio acoustic classification from the RAVDESS dataset.

---

### 🎯 Career Goals
- Develop deeper skills in Generative AI, Retrieval-Augmented Generation (RAG), and AI application development.
- Build reliable end-to-end AI/ML projects with clear evaluation, documentation, and deployment.
- Pursue AI/ML Engineer opportunities in Chennai and across India.

---

### 🌐 Links & Contact
- **Portfolio**: [{PROFILE_INFO['portfolio_url']}]({PROFILE_INFO['portfolio_url']})
- **GitHub**: [{PROFILE_INFO['github_handle']}](https://github.com/prawinkanna)
- **LinkedIn**: [{PROFILE_INFO['linkedin_handle']}](https://linkedin.com/in/prawinkanna)
"""
    st.markdown(resume_md)
    
    st.download_button(
        label="📥 Download Full Resume Markdown",
        data=resume_md,
        file_name="Prawin_Kanna_P_Resume.md",
        mime="text/markdown",
        use_container_width=True
    )
