"""
profile_data.py
Comprehensive Structured Knowledge Base for Prawin Kanna P
Data Analytics | Data Science | AI/ML Engineer
Updated October 2026 with full 14 profile sections.
"""

PROFILE_INFO = {
    "name": "Prawin Kanna P",
    "short_name": "Prawin",
    "title": "Data Analytics & Data Science Trainer | Applied Data Science Postgraduate | Aspiring AI/ML Engineer",
    "headline": "Applied Data Science postgraduate with an undergraduate foundation in Statistics. Passionate about data analytics, machine learning, predictive modelling, computer vision, and Generative AI application development.",
    "core_focus": "Python, SQL, R, Machine Learning, Power BI, Generative AI, Computer Vision",
    "career_direction": "AI/ML Engineer / Data Scientist / Generative AI Application Developer",
    "location": "Trichy, Tamil Nadu, India",
    "location_target": "Chennai and other cities across India (open to remote/relocation)",
    "email": "p.prawinkanna@gmail.com",
    "alternative_email": "prawinkannathiru@gmail.com",
    "phone": "+91 6383297328",
    "portfolio_url": "https://prawinkanna.github.io/prawin-portfolio/",
    "github_handle": "prawinkanna",
    "github_url": "https://github.com/prawinkanna",
    "linkedin_handle": "prawinkannapalaniyappan",
    "linkedin_url": "https://www.linkedin.com/in/prawinkannapalaniyappan/",
}

PROFESSIONAL_SUMMARY = (
    "Postgraduate in Applied Data Science with an undergraduate background in Statistics. "
    "Technical interests span data analytics, business intelligence, machine learning, predictive modelling, "
    "computer vision, and Generative AI application development. Experienced in building sales forecasting models, "
    "model comparisons, end-to-end ML workflows, OpenCV image preprocessing, emotion detection, personal profile chatbots, "
    "and AI-powered data analytics tools. Alongside hands-on technical development, experienced in teaching and mentoring "
    "learners in data analytics and data science at FITA Academy."
)

EDUCATION = [
    {
        "qualification": "M.Sc. Applied Data Science",
        "institution": "SRM Institute of Science & Technology, Trichy",
        "period": "2024–2026",
        "result": "CGPA: 8.54",
        "honors": "First Class with Distinction",
        "details": "Postgraduate specialization focusing on Applied Data Science, machine learning, predictive modeling, statistical learning, and applied AI."
    },
    {
        "qualification": "B.Sc. Statistics",
        "institution": "St. Joseph’s College (Autonomous), Trichy",
        "period": "2021–2024",
        "result": "CGPA: 6.6",
        "honors": "First Class",
        "details": "Undergraduate degree providing a rigorous mathematical and statistical foundation in probability distributions, regression theory, hypothesis testing, and exploratory data analysis."
    }
]

SKILLS = {
    "Programming Languages": ["Python", "SQL", "R"],
    "Data Analysis & Statistics": [
        "Pandas", "NumPy", "Matplotlib", "Data Cleaning", "Exploratory Data Analysis (EDA)",
        "Feature Engineering", "Statistical Analysis", "Data Preprocessing", "Descriptive Statistics"
    ],
    "Business Intelligence & Data Visualization": [
        "Microsoft Power BI", "DAX", "Tableau", "Advanced Excel", "KPI Reporting",
        "Dashboard Development", "Business Reporting", "Data Visualization"
    ],
    "Machine Learning": [
        "Regression", "Classification", "Clustering", "Predictive Modelling",
        "Model Evaluation", "Sales Forecasting", "Scikit-learn"
    ],
    "Computer Vision": [
        "OpenCV", "Image Processing", "Image Preprocessing", "Edge Detection",
        "Grayscale Conversion", "Noise Reduction", "Emotion Detection"
    ],
    "Generative AI & LLM Development": [
        "Gemini API", "LangChain", "LangGraph", "Model Context Protocol (MCP)",
        "Retrieval-Augmented Generation (RAG)", "FAISS", "Prompt Engineering",
        "AI-Powered Chatbots", "Natural-Language-Based Data Analysis"
    ],
    "Development Tools": [
        "Streamlit", "Jupyter Notebook", "Google Colab", "Visual Studio Code", "Git", "GitHub"
    ],
    "AI-Assisted Tools": [
        "ChatGPT", "Claude", "GitHub Copilot", "Cursor", "Antigravity"
    ]
}

PROJECTS = [
    {
        "id": "proj_analytics_bot",
        "title": "AI-Powered Data Analytics Chatbot",
        "category": "Generative AI / Data Analytics",
        "objective": "Develop an AI-powered application that helps users analyze structured datasets using natural-language questions and controlled analytical tools.",
        "description": "Enables users to upload structured datasets and interact through a conversational chat interface to inspect columns, perform data quality checks, generate missing/duplicate value analysis, run descriptive statistics, execute automated data filtering/aggregations, and visualize results with interactive charts.",
        "technologies": ["Python", "Streamlit", "Pandas", "NumPy", "Gemini API", "LangChain", "LangGraph", "MCP", "FAISS", "RAG", "Plotly", "Pytest"],
        "highlights": "Combined conversational LLM interaction with programmatic Pandas tools via a Python MCP server architecture for reliable, controlled analytical execution."
    },
    {
        "id": "proj_profile_bot",
        "title": "Personal Profile AI Chatbot",
        "category": "Generative AI / Information Retrieval",
        "objective": "Create an interactive chatbot that answers questions about Prawin's professional profile using grounded information.",
        "description": "Assists recruiters and visitors in exploring education, technical skills, machine learning projects, professional experience, and career aspirations. Integrates TF-IDF vectorization, cosine similarity retrieval, Google Gemini API for generative responses, and strict guardrails to decline irrelevant/unwanted questions.",
        "technologies": ["Python", "Streamlit", "Google Gemini API", "Scikit-learn", "TF-IDF", "Cosine Similarity"],
        "highlights": "Real-time streaming responses, multi-persona selection, and robust safety guardrails against off-topic queries."
    },
    {
        "id": "proj_ml_webapp",
        "title": "End-to-End Machine Learning Web Application",
        "category": "Machine Learning / Application Development",
        "objective": "Build an interactive web application that helps users experiment with end-to-end machine learning workflows.",
        "description": "Allows users to upload custom datasets, choose a target variable, select either a regression or classification task, automatically train and compare 4 regression models and 4 classification models, and view comparative evaluation metrics and performance charts.",
        "technologies": ["Python", "Streamlit", "Pandas", "NumPy", "Scikit-learn"],
        "highlights": "Presented at Dhanalakshmi Srinivasan Engineering College conference; simplifies ML model experimentation for aspiring practitioners."
    },
    {
        "id": "proj_sales_comp",
        "title": "Comparative Analysis of ML Models for Sales Forecasting",
        "category": "Machine Learning / Predictive Analytics",
        "objective": "Compare multiple machine learning algorithms for sales prediction.",
        "description": "Prepared historical sales datasets, engineered temporal and product features, and trained Linear Regression, Decision Tree, and Random Forest models to evaluate sales forecasting performance.",
        "technologies": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
        "highlights": "Rigorous data preprocessing, model benchmarking, and graphical interpretation of predicted vs actual sales trends."
    },
    {
        "id": "proj_hybrid_sales",
        "title": "Hybrid Machine Learning Model for Sales Forecasting",
        "category": "Time-Series Forecasting / Machine Learning",
        "objective": "Explore a hybrid sales forecasting approach combining time-series forecasting with machine learning.",
        "description": "Blends Prophet for temporal time-series trend and seasonality decomposition with Gradient Boosting for non-linear residual feature learning, enhancing sales prediction precision.",
        "technologies": ["Python", "Prophet", "Scikit-learn", "Pandas", "NumPy"],
        "highlights": "Innovative dual-model approach capturing macro seasonality alongside localized granular feature dynamics."
    },
    {
        "id": "proj_cv_preprocessing",
        "title": "Computer Vision Image Preprocessing Web Application",
        "category": "Computer Vision",
        "objective": "Build an interactive web application for applying and understanding core image-processing techniques.",
        "description": "Features user image upload, real-time grayscale conversion, edge detection (Canny/Sobel), noise reduction filters (Gaussian, Median), and side-by-side preview comparisons.",
        "technologies": ["Python", "OpenCV", "Streamlit"],
        "highlights": "Accessible, visual interface for understanding computer vision transformation pipelines."
    },
    {
        "id": "proj_cv_emotion",
        "title": "Computer Vision Emotion Detection Web Application",
        "category": "Computer Vision / AI",
        "objective": "Develop an application for detecting human facial emotions using image-processing and neural vision methods.",
        "description": "Implements face localization, bounding box normalization, image enhancement, and facial expression analysis to detect human emotions from input visuals.",
        "technologies": ["Python", "OpenCV", "CNN fundamentals", "NumPy"],
        "highlights": "Hands-on implementation of computer vision pipelines tailored for affective computing."
    },
    {
        "id": "proj_bi_analytics",
        "title": "Data Analytics and Business Intelligence Projects",
        "category": "Data Analytics / Business Intelligence",
        "objective": "Transform raw datasets into actionable business insights through rigorous analytics, KPI dashboards, and visual reporting.",
        "description": "A comprehensive portfolio of business analytics workflows involving data cleaning, exploratory data analysis, DAX KPI calculations, interactive Power BI and Tableau dashboards, and Advanced Excel financial reporting.",
        "technologies": ["Python", "Pandas", "Matplotlib", "Microsoft Power BI", "DAX", "Tableau", "Advanced Excel"],
        "highlights": "Practical dashboard solutions designed for executive decision-making and operational tracking."
    }
]

EXPERIENCE = [
    {
        "role": "Data Analytics and Data Science Trainer",
        "company": "FITA Academy, Anna Nagar, Chennai",
        "type": "Part-time / Training Role",
        "period": "July 2026 onward",
        "summary": "Delivering learning support and interactive training in data analytics and data science, focusing on making complex concepts intuitive and accessible.",
        "skills_taught": [
            "Python", "SQL", "Excel", "Power BI", "Data Cleaning",
            "Data Visualization", "Statistics", "Machine Learning"
        ],
        "highlights": "Teaches technical topics using hands-on practical examples, mentors learners through end-to-end data pipelines, and explains ML algorithms and workflows."
    },
    {
        "role": "Property Manager",
        "company": "RS Residency",
        "type": "Operational Management",
        "period": "Professional Experience",
        "summary": "Maintained residential operations and tenant management using structured Excel systems.",
        "skills_taught": ["Excel Record Keeping", "Rent Collection Tracking", "Accounting Support", "Tenant Communication"],
        "highlights": "Supported basic financial accounting, tracked rent payments, and managed day-to-day property operations."
    },
    {
        "role": "Delivery Partner",
        "company": "Swiggy",
        "type": "Logistics & Operations",
        "period": "Operational Experience",
        "summary": "Hands-on frontline customer service and operational logistics management.",
        "skills_taught": ["Customer Service", "Time Management", "Communication & Coordination", "Operational Discipline"],
        "highlights": "Built strong real-world discipline, independent problem-solving, and efficient time management under dynamic conditions."
    },
    {
        "role": "Client Management / Telecalling",
        "company": "Indian Post Payments Bank (IPPB) Sector",
        "type": "Customer Relations",
        "period": "Client Services",
        "summary": "Supported client communications and financial services onboarding.",
        "skills_taught": ["Client Communication", "Banking Procedures", "Customer Onboarding Support"],
        "highlights": "Communicated with potential customers, explained account-opening procedures, and provided foundational support."
    }
]

INTERNSHIPS = [
    {
        "role": "AI and Machine Learning Intern",
        "organization": "VDart, Trichy",
        "duration": "3 months",
        "focus_areas": [
            "Data Preprocessing", "Exploratory Data Analysis (EDA)",
            "Feature Engineering", "Python-based Data Analysis", "Machine Learning Workflows"
        ],
        "technologies": ["Python", "Pandas", "NumPy", "Scikit-learn"],
        "summary": "Gained practical industry exposure in data cleaning, engineering feature matrices, and developing machine learning model pipelines."
    },
    {
        "role": "Data Science and Machine Learning Intern",
        "organization": "Edureka",
        "duration": "6 months",
        "focus_areas": [
            "Python Programming", "SQL Database Querying", "Machine Learning Algorithms",
            "Deep Learning Fundamentals", "Natural Language Processing (NLP)", "Predictive Modelling"
        ],
        "technologies": ["Python", "SQL", "Scikit-learn", "NLP", "Deep Learning"],
        "summary": "Completed intensive 6-month hands-on internship spanning end-to-end data science, NLP sentiment workflows, and predictive analytics."
    }
]

CERTIFICATIONS = [
    {"title": "Data Analytics Using Python", "domain": "Data Analytics"},
    {"title": "Data Visualization in Power BI", "domain": "Business Intelligence"},
    {"title": "Advanced Excel for Data Analysis", "domain": "Spreadsheet Modeling & Reporting"},
    {"title": "R Programming for Data Science", "domain": "Statistical Computing"}
]

CONFERENCE_PRESENTATIONS = [
    {
        "title": "An End-to-End Interactive Machine Learning Web Application for Freshers Using Streamlit",
        "institution": "Dhanalakshmi Srinivasan Engineering College, Perambalur",
        "topic": "Machine Learning Application Deployment & Interactive UI"
    },
    {
        "title": "Sentiment Analysis of Customer Reviews Using NLP",
        "institution": "SRM Institute of Science & Technology",
        "topic": "Natural Language Processing & Text Sentiment Classification"
    }
]

WORKSHOPS = [
    {
        "name": "One-Day Agentic AI Workshop",
        "organizers": "Mission AI Initiative & FITA Academy",
        "topic": "Autonomous AI Agents, Tool-Calling, and Multi-Agent Workflows"
    }
]

EXTRACURRICULARS = [
    {
        "area": "Filmmaking & Storytelling",
        "skills": [
            "Short film making", "Story writing", "Screenplay development",
            "Dialogue writing", "Camera angles and visual storytelling",
            "Content creation", "Team coordination", "People management", "Budget management"
        ],
        "summary": "Extracurricular creative leadership showcasing high-level communication, teamwork, storytelling, visual planning, and budget management."
    }
]

CAREER_GOALS = [
    "Secure an AI/ML Engineer, Data Scientist, or Generative AI Application Developer position in Chennai or across India.",
    "Develop cutting-edge Generative AI applications integrating LLMs, LangChain/LangGraph, and Model Context Protocol (MCP).",
    "Build practical, reliable solutions transforming raw structured and unstructured data into actionable insights.",
    "Continue teaching and simplifying data science concepts to empower students and developer communities."
]

KNOWLEDGE_CHUNKS = [
    {
        "id": "summary",
        "category": "About",
        "keywords": "who is prawin kanna background bio summary about profile introduction who are you tell me about yourself overview",
        "content_first_person": (
            "Hi! I'm **Prawin Kanna P**, an Applied Data Science postgraduate (M.Sc. Distinction, CGPA 8.54 from SRM Trichy) "
            "with an undergraduate foundation in Statistics (B.Sc. First Class from St. Joseph's College, Trichy).\n\n"
            "I'm a **Data Analytics & Data Science Trainer at FITA Academy** and an aspiring **AI/ML Engineer & Generative AI Developer**. "
            "My expertise spans **Python, SQL, R, Machine Learning, Power BI, OpenCV Computer Vision, and Generative AI (Gemini API, LangChain, MCP, RAG)**. "
            "I enjoy building practical web applications with Streamlit and teaching complex technical concepts with clarity."
        ),
        "content_third_person": (
            "**Prawin Kanna P** is an Applied Data Science postgraduate (M.Sc. Distinction, CGPA 8.54) with a B.Sc. in Statistics. "
            "He serves as a Data Analytics & Data Science Trainer at FITA Academy and is an aspiring AI/ML Engineer / Generative AI Developer. "
            "His technical toolkit encompasses Python, SQL, R, Machine Learning, Power BI, OpenCV, and Generative AI application development."
        )
    },
    {
        "id": "education",
        "category": "Education",
        "keywords": "education msc bsc masters degree srm institute trichy st joseph college statistics applied data science cgpa grade marks distinction",
        "content_first_person": (
            "### 🎓 Educational Qualifications\n"
            "1. **M.Sc. Applied Data Science**\n"
            "   - **Institution**: SRM Institute of Science & Technology, Trichy (2024–2026)\n"
            "   - **Academic Result**: **CGPA 8.54 — First Class with Distinction**\n"
            "   - Specialized in advanced machine learning, predictive modeling, statistical learning, and applied AI.\n\n"
            "2. **B.Sc. Statistics**\n"
            "   - **Institution**: St. Joseph’s College (Autonomous), Trichy (2021–2024)\n"
            "   - **Academic Result**: **CGPA 6.6 — First Class**\n"
            "   - Rigorous mathematical grounding in probability, hypothesis testing, regression theory, and statistical modeling."
        ),
        "content_third_person": (
            "### 🎓 Educational Qualifications\n"
            "1. **M.Sc. Applied Data Science** — SRM Institute of Science & Technology, Trichy (2024–2026) | **CGPA 8.54 (First Class with Distinction)**.\n"
            "2. **B.Sc. Statistics** — St. Joseph’s College (Autonomous), Trichy (2021–2024) | **CGPA 6.6 (First Class)**."
        )
    },
    {
        "id": "skills",
        "category": "Skills",
        "keywords": "skills technical programming languages python sql r power bi tableau excel machine learning opencv computer vision generative ai langchain rag mcp faiss",
        "content_first_person": (
            "### 🛠️ Technical Skills Overview\n"
            "- **Programming**: Python, SQL, R\n"
            "- **Data Analysis & Stats**: Pandas, NumPy, Matplotlib, Data Cleaning, EDA, Feature Engineering, Preprocessing, Descriptive Stats\n"
            "- **BI & Visualization**: Microsoft Power BI, DAX, Tableau, Advanced Excel, KPI Reporting, Dashboards\n"
            "- **Machine Learning**: Regression, Classification, Clustering, Predictive Modelling, Evaluation, Sales Forecasting, Scikit-learn\n"
            "- **Computer Vision**: OpenCV, Image Preprocessing, Edge Detection, Grayscale Conversion, Noise Reduction, Emotion Detection\n"
            "- **Generative AI & LLMs**: Gemini API, LangChain, LangGraph, Model Context Protocol (MCP), RAG, FAISS, Prompt Engineering\n"
            "- **Tools & Environments**: Streamlit, Jupyter Notebook, Google Colab, VS Code, Git, GitHub\n"
            "- **AI-Assisted Tools**: ChatGPT, Claude, GitHub Copilot, Cursor, Antigravity"
        ),
        "content_third_person": (
            "### 🛠️ Technical Skills Overview\n"
            "- **Programming**: Python, SQL, R\n"
            "- **Data Analysis**: Pandas, NumPy, Matplotlib, EDA, Feature Engineering, Preprocessing\n"
            "- **BI & Reporting**: Microsoft Power BI, DAX, Tableau, Advanced Excel, KPI Dashboards\n"
            "- **Machine Learning**: Scikit-learn, Regression, Classification, Clustering, Forecasting\n"
            "- **Computer Vision**: OpenCV, Preprocessing, Edge Detection, Emotion Detection\n"
            "- **Generative AI**: Gemini API, LangChain, LangGraph, MCP, RAG, FAISS, Chatbots\n"
            "- **Development**: Streamlit, VS Code, Git, GitHub, Colab, Jupyter"
        )
    },
    {
        "id": "projects_all",
        "category": "Projects",
        "keywords": "projects portfolio machine learning ai data analytics chatbot sales forecasting streamlit opencv emotion detection bi power bi",
        "content_first_person": (
            "### 🚀 Featured Project Portfolio (8 Key Projects)\n"
            "1. **AI-Powered Data Analytics Chatbot**: Conversational data analysis of structured datasets using Pandas tools, Gemini API, LangChain, LangGraph, MCP, and Plotly in Streamlit.\n"
            "2. **Personal Profile AI Chatbot**: Interactive profile assistant with TF-IDF/cosine similarity, Gemini 3.5 streaming, and strict guardrails for off-topic queries.\n"
            "3. **End-to-End Machine Learning Web App**: Streamlit web app comparing 4 regression and 4 classification models with automated evaluation.\n"
            "4. **Comparative Analysis of ML Models for Sales Forecasting**: Benchmarking Linear Regression, Decision Trees, and Random Forests on sales data.\n"
            "5. **Hybrid ML Model for Sales Forecasting**: Blending Prophet time-series forecasting with Gradient Boosting machine learning.\n"
            "6. **Computer Vision Image Preprocessing App**: OpenCV & Streamlit app for grayscale, edge detection, and noise filtering.\n"
            "7. **Computer Vision Emotion Detection App**: OpenCV and CNN-based facial emotion detection pipeline.\n"
            "8. **Data Analytics & BI Projects**: Executive Power BI and Tableau dashboards, DAX KPI reporting, and Advanced Excel financial models."
        ),
        "content_third_person": (
            "### 🚀 Prawin's Featured Project Portfolio\n"
            "Prawin has built 8 core projects across Generative AI, Machine Learning, Computer Vision, and Business Intelligence, including conversational data analytics bots (LangChain/MCP), end-to-end ML training web apps, hybrid Prophet/Gradient Boosting forecasting, OpenCV vision tools, and Power BI dashboards."
        )
    },
    {
        "id": "experience_and_internships",
        "category": "Experience",
        "keywords": "experience job work internships fita academy trainer vdart edureka swiggy rs residency ippb teaching",
        "content_first_person": (
            "### 💼 Professional Experience & Internships\n"
            "**Professional Experience**:\n"
            "- **Data Analytics & Data Science Trainer — FITA Academy, Anna Nagar, Chennai**: Teaching Python, SQL, Excel, Power BI, Statistics, and ML with practical real-world exercises.\n"
            "- **Property Manager — RS Residency**: Excel record systems, rent collection tracking, tenant operations.\n"
            "- **Delivery Partner — Swiggy**: Real-world operational discipline, customer communication, and time management.\n"
            "- **Client Management / Telecalling — IPPB Sector**: Customer banking support and onboarding.\n\n"
            "**Internships**:\n"
            "- **AI & ML Intern — VDart, Trichy (3 months)**: Data preprocessing, EDA, feature engineering, and ML model workflows using Python & Scikit-learn.\n"
            "- **Data Science & ML Intern — Edureka (6 months)**: End-to-end curriculum covering Python, SQL, ML, Deep Learning, NLP sentiment analysis, and predictive modeling."
        ),
        "content_third_person": (
            "### 💼 Professional Experience & Internships\n"
            "Prawin serves as a Data Analytics & Data Science Trainer at FITA Academy, Anna Nagar, Chennai. His prior professional background includes operational roles at RS Residency, Swiggy, and IPPB client support. He has completed two technical internships: a 3-month AI/ML internship at VDart, Trichy, and an intensive 6-month Data Science internship at Edureka."
        )
    },
    {
        "id": "certifications_conferences",
        "category": "Certifications & Presentations",
        "keywords": "certifications conference presentations papers workshops dhanalakshmi srinivasan srm perambalur agentic ai mission ai",
        "content_first_person": (
            "### 📜 Certifications & Presentations\n"
            "**Certifications**:\n"
            "- Data Analytics Using Python\n"
            "- Data Visualization in Power BI\n"
            "- Advanced Excel for Data Analysis\n"
            "- R Programming for Data Science\n\n"
            "**Conference Presentations**:\n"
            "- *An End-to-End Interactive Machine Learning Web Application for Freshers Using Streamlit* — Dhanalakshmi Srinivasan Engineering College, Perambalur.\n"
            "- *Sentiment Analysis of Customer Reviews Using NLP* — SRM Institute of Science & Technology.\n\n"
            "**Workshops**:\n"
            "- One-Day Agentic AI Workshop (Mission AI Initiative & FITA Academy)."
        ),
        "content_third_person": (
            "### 📜 Certifications & Presentations\n"
            "Prawin holds certifications in Python Data Analytics, Power BI, Advanced Excel, and R. He presented technical papers on interactive ML web apps using Streamlit at Dhanalakshmi Srinivasan Engineering College, and sentiment analysis via NLP at SRM Institute. He also completed a hands-on Agentic AI workshop with Mission AI & FITA Academy."
        )
    },
    {
        "id": "contact",
        "category": "Contact",
        "keywords": "contact email phone mobile number call reach linkedin github portfolio website location trichy chennai",
        "content_first_person": (
            "### 📬 Contact Information & Links\n"
            "- **Name**: Prawin Kanna P\n"
            "- **Location**: Trichy, Tamil Nadu, India (Preferred Job Locations: Chennai and other cities across India)\n"
            "- **Email**: [p.prawinkanna@gmail.com](mailto:p.prawinkanna@gmail.com)\n"
            "- **Alternative Email**: [prawinkannathiru@gmail.com](mailto:prawinkannathiru@gmail.com)\n"
            "- **Phone**: [+91 6383297328](tel:+916383297328)\n"
            "- **Portfolio Website**: [prawinkanna.github.io/prawin-portfolio](https://prawinkanna.github.io/prawin-portfolio/)\n"
            "- **GitHub**: [github.com/prawinkanna](https://github.com/prawinkanna)\n"
            "- **LinkedIn**: [linkedin.com/in/prawinkannapalaniyappan](https://www.linkedin.com/in/prawinkannapalaniyappan/)"
        ),
        "content_third_person": (
            "### 📬 Contact Information & Links\n"
            "- **Full Name**: Prawin Kanna P\n"
            "- **Location**: Trichy, Tamil Nadu, India (Target: Chennai / India)\n"
            "- **Email**: p.prawinkanna@gmail.com | prawinkannathiru@gmail.com\n"
            "- **Phone**: +91 6383297328\n"
            "- **Portfolio**: https://prawinkanna.github.io/prawin-portfolio/\n"
            "- **GitHub**: https://github.com/prawinkanna\n"
            "- **LinkedIn**: https://www.linkedin.com/in/prawinkannapalaniyappan/"
        )
    }
]

FAQ_QUESTIONS = [
    {
        "q": "🎓 What is your educational background and CGPA?",
        "prompt": "What is your educational background, institutions, and CGPA?"
    },
    {
        "q": "🛠️ What are your core technical skills?",
        "prompt": "What technical skills, programming languages, and tools do you know?"
    },
    {
        "q": "💼 Tell me about your role at FITA Academy.",
        "prompt": "Tell me about your experience as a trainer at FITA Academy."
    },
    {
        "q": "🤖 What Generative AI and ML projects have you built?",
        "prompt": "Tell me about your AI Data Analytics Chatbot and other featured ML projects."
    },
    {
        "q": "🏢 Tell me about your internships at VDart and Edureka.",
        "prompt": "What did you do during your internships at VDart and Edureka?"
    },
    {
        "q": "📜 What certifications and conference presentations do you have?",
        "prompt": "What certifications and conference presentations have you completed?"
    },
    {
        "q": "🎯 What are your career goals and target locations?",
        "prompt": "What are your career goals and preferred job locations?"
    },
    {
        "q": "📬 How can I contact you?",
        "prompt": "What is your email, phone number, and LinkedIn/GitHub links?"
    }
]
