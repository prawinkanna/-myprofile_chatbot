"""
app.py
Prawin Kanna P | AI Portfolio & Profile Assistant
Interactive Streamlit Application powered by Google Gemini 3.5 Flash and Grounded Semantic RAG.
Features strict guardrails against unwanted/irrelevant questions.
"""

import os
import datetime
import streamlit as st
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
        font-size: 1.02rem;
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
    .badge-pill-orange {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 600;
        background-color: #FFF3E0;
        color: #E65100;
        border: 1px solid #FFE0B2;
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
                "Hello! 👋 I'm **Prawin Kanna P**'s interactive AI Portfolio Assistant, powered by **Google Gemini 3.5**.\n\n"
                "I can answer questions regarding my **education** (M.Sc. Distinction, SRM Trichy & B.Sc. Statistics), "
                "**8 technical projects** (AI Data Analytics Chatbot, Sales Forecasting, Streamlit Apps, OpenCV Vision), "
                "**training experience at FITA Academy**, **internships at VDart & Edureka**, **certifications**, and **career goals**.\n\n"
                "*(Note: I strictly answer questions related to Prawin's professional profile and reject off-topic questions.)*\n\n"
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
        Data Analytics & Data Science Trainer | Applied Data Science Postgraduate | Aspiring AI/ML Engineer
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Chat Settings")
    
    persona_option = st.radio(
        "Chatbot Persona",
        options=[
            "Chat as Prawin (1st Person)",
            "Portfolio Assistant (3rd Person)"
        ],
        index=0
    )
    persona = "first_person" if "1st Person" in persona_option else "third_person"

    # Model Selection
    model_choice = st.selectbox(
        "AI Mode",
        options=[
            "Online: gemini-3.5-flash (Fast & Accurate)",
            "Online: gemini-3.5-flash-lite (Ultra Lightweight)",
            "Online: gemini-3.8-flash (Latest Preview)",
            "Offline: Local TF-IDF Semantic Engine"
        ],
        index=0
    )
    
    if "flash-lite" in model_choice:
        selected_model = "gemini-3.5-flash-lite"
    elif "gemini-3.8-flash" in model_choice:
        selected_model = "gemini-3.8-flash"
    elif "Offline" in model_choice:
        selected_model = "offline"
    else:
        selected_model = "gemini-3.5-flash"

    # Backend API Key (Loaded securely from .env, completely hidden from UI)
    active_api_key = get_api_key()
    if active_api_key and selected_model != "offline":
        st.caption("🟢 AI Assistant Online (Connected)")
    else:
        st.caption("🟡 Running in Offline Fallback Mode")

    with st.expander("🎛️ Model Parameters"):
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.05,
                                help="Lower temperature maintains strict factual grounding and guardrail adherence.")
        max_tokens = st.slider("Max Tokens", min_value=256, max_value=2048, value=1200, step=128)

    st.markdown("---")
    st.markdown("### 📌 Key Highlights")
    st.markdown("""
    - 🎓 **M.Sc. Applied Data Science**  
      *SRM Trichy (2024–2026)* — **CGPA 8.54** (Distinction)
    - 🎓 **B.Sc. Statistics**  
      *St. Joseph's Trichy (2021–2024)* — **CGPA 6.6** (First Class)
    - 💼 **Trainer @ FITA Academy** (Chennai)  
      *Python, SQL, Power BI, Statistics, ML*
    - 🏢 **Internships**: VDart (3 mos) & Edureka (6 mos)
    - 🚀 **8 Featured AI/ML Projects**
    - 📍 **Location**: Trichy, TN (Target: Chennai / India)
    """)

    st.markdown("---")
    st.markdown("### 📬 Contact & Links")
    st.markdown(f"📧 **Email**: [{PROFILE_INFO['email']}](mailto:{PROFILE_INFO['email']})")
    st.markdown(f"📞 **Phone**: [{PROFILE_INFO['phone']}](tel:{PROFILE_INFO['phone']})")
    st.markdown(f"🔗 [Portfolio Website]({PROFILE_INFO['portfolio_url']})")
    st.markdown(f"🐙 [GitHub: {PROFILE_INFO['github_handle']}]({PROFILE_INFO['github_url']})")
    st.markdown(f"💼 [LinkedIn: {PROFILE_INFO['linkedin_handle']}]({PROFILE_INFO['linkedin_url']})")

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
    '<div class="sub-title">Explore my background, education, FITA Academy training experience, and 8 machine learning / GenAI projects powered by Google Gemini 3.5.</div>',
    unsafe_allow_html=True
)

# Badges
st.markdown("""
<div>
    <span class="badge-pill">🎓 M.Sc. Distinction (8.54 CGPA)</span>
    <span class="badge-pill-green">💼 FITA Academy Trainer</span>
    <span class="badge-pill-purple">🤖 GenAI & ML Developer</span>
    <span class="badge-pill-orange">🛡️ Strict Profile Guardrails</span>
</div>
""", unsafe_allow_html=True)

tab_chat, tab_explorer, tab_resume = st.tabs(["💬 AI Chat Assistant", "🚀 Projects & Experience Explorer", "📄 Full Resume Breakdown"])

# ==========================================
# TAB 1: AI CHAT ASSISTANT
# ==========================================
with tab_chat:
    st.markdown("##### 💡 Suggested Questions (Click any to ask immediately):")
    
    chip_cols_1 = st.columns(4)
    with chip_cols_1[0]:
        btn_edu = st.button("🎓 Education & CGPA", key="chip_edu", use_container_width=True)
    with chip_cols_1[1]:
        btn_skills = st.button("🛠️ Technical Skills", key="chip_skills", use_container_width=True)
    with chip_cols_1[2]:
        btn_fita = st.button("💼 Experience @ FITA", key="chip_fita", use_container_width=True)
    with chip_cols_1[3]:
        btn_genai = st.button("🤖 AI Data Analytics Bot", key="chip_genai", use_container_width=True)

    chip_cols_2 = st.columns(4)
    with chip_cols_2[0]:
        btn_sales = st.button("📈 Sales Forecasting ML", key="chip_sales", use_container_width=True)
    with chip_cols_2[1]:
        btn_intern = st.button("🏢 Internships (VDart & Edureka)", key="chip_intern", use_container_width=True)
    with chip_cols_2[2]:
        btn_goals = st.button("🎯 Career Goals & Relocation", key="chip_goals", use_container_width=True)
    with chip_cols_2[3]:
        btn_contact = st.button("📬 Contact & Links", key="chip_contact", use_container_width=True)

    # Map clicked button to prompt
    chip_prompt = None
    if btn_edu:
        chip_prompt = "What is your educational background, institutions, and CGPA?"
    elif btn_skills:
        chip_prompt = "What technical skills, programming languages, and tools do you know?"
    elif btn_fita:
        chip_prompt = "Tell me about your experience as a trainer at FITA Academy."
    elif btn_genai:
        chip_prompt = "Tell me about your AI-Powered Data Analytics Chatbot project."
    elif btn_sales:
        chip_prompt = "Tell me about your comparative and hybrid sales forecasting projects."
    elif btn_intern:
        chip_prompt = "Tell me about your internships at VDart and Edureka."
    elif btn_goals:
        chip_prompt = "What are your career aspirations and are you open to AI/ML Engineer jobs in Chennai?"
    elif btn_contact:
        chip_prompt = "Where can I view your portfolio and how can I contact you directly?"

    st.markdown("---")

    # Render Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("source"):
                st.markdown(f"<div class='source-tag'>Source: {message['source']}</div>", unsafe_allow_html=True)

    # Chat Input Box
    chat_input = st.chat_input("Ask about education, ML projects, skills, experience, or career goals...")
    active_prompt = chip_prompt or chat_input

    if active_prompt:
        st.session_state.messages.append({"role": "user", "content": active_prompt})
        with st.chat_message("user"):
            st.markdown(active_prompt)

        # Generate Assistant Response
        with st.chat_message("assistant"):
            if selected_model == "offline" or not active_api_key:
                # Use offline TF-IDF engine with relevance filter
                offline_res = st.session_state.rag_engine.get_offline_response(active_prompt, persona=persona)
                st.markdown(offline_res["response"])
                source_label = offline_res["source"]
                full_reply = offline_res["response"]
            else:
                # Stream response from Gemini 3.5 API with strict domain restriction
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
    st.markdown("### 🚀 Featured Project Portfolio (8 Projects)")
    for proj in PROJECTS:
        with st.expander(f"📌 {proj['title']} — *{proj['category']}*", expanded=False):
            st.markdown(f"**Objective**: {proj['objective']}")
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
            <p>Advanced focus on statistical modeling, machine learning algorithms, predictive modeling, statistical learning, and applied AI.</p>
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
    st.markdown("### 🏢 Technical Internships")
    col_int1, col_int2 = st.columns(2)
    with col_int1:
        st.markdown("""
        <div class="profile-card">
            <h4>AI & Machine Learning Intern</h4>
            <p><strong>Organization</strong>: VDart, Trichy (3 Months)</p>
            <p><strong>Focus Areas</strong>: Data Preprocessing, EDA, Feature Engineering, Python Data Analysis, ML Workflows.</p>
            <p><strong>Technologies</strong>: <code>Python</code> <code>Pandas</code> <code>NumPy</code> <code>Scikit-learn</code></p>
            <p>Gained industry exposure building end-to-end data preparation pipelines and machine learning models.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_int2:
        st.markdown("""
        <div class="profile-card">
            <h4>Data Science & Machine Learning Intern</h4>
            <p><strong>Organization</strong>: Edureka (6 Months)</p>
            <p><strong>Focus Areas</strong>: Python, SQL, Machine Learning, Deep Learning, NLP Sentiment Analysis, Predictive Modelling.</p>
            <p><strong>Technologies</strong>: <code>Python</code> <code>SQL</code> <code>Scikit-learn</code> <code>NLP</code> <code>Deep Learning</code></p>
            <p>Completed intensive training developing NLP text classification and predictive analytics systems.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📜 Certifications & Conference Presentations")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("##### 📜 Certifications")
        for cert in CERTIFICATIONS:
            st.markdown(f"- **{cert['title']}** (*{cert['domain']}*)")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 🛠️ Workshops")
        for ws in WORKSHOPS:
            st.markdown(f"- **{ws['name']}** (*{ws['organizers']}*): {ws['topic']}")
    with col_c2:
        st.markdown("##### 🎤 Conference Presentations")
        for conf in CONFERENCE_PRESENTATIONS:
            st.markdown(f"- **{conf['title']}**  \n  *{conf['institution']}* — {conf['topic']}")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 🎬 Creative & Extracurricular Leadership")
        for extra in EXTRACURRICULARS:
            st.markdown(f"- **{extra['area']}**: {', '.join(extra['skills'][:5])}  \n  *{extra['summary']}*")

    st.markdown("---")
    st.markdown("### 🛠️ Technical Skills Matrix")
    for category, skills_list in SKILLS.items():
        st.markdown(f"**{category}**")
        st.markdown(" ".join([f"`{s}`" for s in skills_list]))
        st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# TAB 3: FULL RESUME BREAKDOWN
# ==========================================
with tab_resume:
    st.markdown("### 📄 Complete Resume & Professional Profile Breakdown")
    resume_md = f"""
# {PROFILE_INFO['name']}
**{PROFILE_INFO['title']}**

📍 **Location**: {PROFILE_INFO['location']} | 🎯 **Target Job Locations**: {PROFILE_INFO['location_target']}  
📧 **Email**: {PROFILE_INFO['email']} | 📧 **Alt Email**: {PROFILE_INFO['alternative_email']}  
📞 **Phone**: {PROFILE_INFO['phone']}  
🔗 **Portfolio**: {PROFILE_INFO['portfolio_url']}  
🐙 **GitHub**: {PROFILE_INFO['github_url']} | 💼 **LinkedIn**: {PROFILE_INFO['linkedin_url']}  

---

### 🌟 Professional Summary
{PROFESSIONAL_SUMMARY}

---

### 🎓 Education
- **M.Sc. Applied Data Science** | SRM Institute of Science & Technology, Trichy (2024–2026)  
  *Result*: **CGPA 8.54 (First Class with Distinction)**
- **B.Sc. Statistics** | St. Joseph’s College (Autonomous), Trichy (2021–2024)  
  *Result*: **CGPA 6.6 (First Class)**

---

### 🛠️ Technical Skills
- **Programming Languages**: {", ".join(SKILLS['Programming Languages'])}
- **Data Analysis & Statistics**: {", ".join(SKILLS['Data Analysis & Statistics'])}
- **Business Intelligence & Data Visualization**: {", ".join(SKILLS['Business Intelligence & Data Visualization'])}
- **Machine Learning**: {", ".join(SKILLS['Machine Learning'])}
- **Computer Vision**: {", ".join(SKILLS['Computer Vision'])}
- **Generative AI & LLMs**: {", ".join(SKILLS['Generative AI & LLM Development'])}
- **Development Tools**: {", ".join(SKILLS['Development Tools'])}
- **AI-Assisted Tools**: {", ".join(SKILLS['AI-Assisted Tools'])}

---

### 🚀 Project Portfolio (8 Projects)
1. **AI-Powered Data Analytics Chatbot** (*Generative AI / Data Analytics*): Natural-language data exploration via Pandas tools, Gemini API, LangChain, LangGraph, Python MCP server, Plotly, Streamlit.
2. **Personal Profile AI Chatbot** (*Generative AI / Information Retrieval*): Interactive profile assistant with TF-IDF/cosine similarity, Gemini 3.5 streaming, and strict guardrails.
3. **End-to-End Machine Learning Web Application** (*ML / Application Development*): Interactive Streamlit app training & comparing 4 regression and 4 classification models.
4. **Comparative Analysis of ML Models for Sales Forecasting** (*Machine Learning / Predictive Analytics*): Benchmarking Linear Regression, Decision Tree, and Random Forest models.
5. **Hybrid Machine Learning Model for Sales Forecasting** (*Time-Series Forecasting / ML*): Prophet time-series forecasting blended with Gradient Boosting.
6. **Computer Vision Image Preprocessing Web App** (*Computer Vision*): OpenCV and Streamlit interface for grayscale, Canny edge detection, and noise filtering.
7. **Computer Vision Emotion Detection Web App** (*Computer Vision / AI*): Image preprocessing and neural vision pipeline for facial emotion detection.
8. **Data Analytics and Business Intelligence Projects** (*Data Analytics / BI*): Power BI & Tableau dashboards, DAX KPI reporting, and Advanced Excel financial reporting.

---

### 💼 Professional Experience
- **Data Analytics and Data Science Trainer** — FITA Academy, Anna Nagar, Chennai (July 2026 onward)  
  *Delivering structured training in Python, SQL, Excel, Power BI, data cleaning, visualization, statistics, and machine learning.*
- **Property Manager** — RS Residency: Operations, Excel record management, rent collections.
- **Delivery Partner** — Swiggy: Customer service, operational discipline, and time management.
- **Client Management / Telecalling** — Indian Post Payments Bank (IPPB) Sector.

---

### 🏢 Internships
- **AI & Machine Learning Intern** — VDart, Trichy (3 months): Data preprocessing, EDA, feature engineering, ML model pipelines.
- **Data Science & Machine Learning Intern** — Edureka (6 months): Python, SQL, ML, Deep Learning, NLP sentiment analysis.

---

### 📜 Certifications & Presentations
- **Certifications**: Data Analytics Using Python, Data Visualization in Power BI, Advanced Excel for Data Analysis, R Programming for Data Science.
- **Conferences**: 
  - *An End-to-End Interactive Machine Learning Web Application for Freshers Using Streamlit* (Dhanalakshmi Srinivasan Engineering College).
  - *Sentiment Analysis of Customer Reviews Using NLP* (SRM Institute of Science & Technology).
- **Workshops**: One-Day Agentic AI Workshop (Mission AI Initiative & FITA Academy).
- **Extracurriculars**: Filmmaking, visual storytelling, team leadership, and budget management.

---

### 🎯 Career Objective
AI/ML Engineer, Data Scientist, or Generative AI Application Developer seeking opportunities in Chennai and across India.
"""
    st.markdown(resume_md)
    
    st.download_button(
        label="📥 Download Full Resume Markdown",
        data=resume_md,
        file_name="Prawin_Kanna_P_Resume.md",
        mime="text/markdown",
        use_container_width=True
    )
