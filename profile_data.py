"""
profile_data.py
Structured Knowledge Base for Prawin Kanna P
Extracted from official PDF profile.
"""

PROFILE_INFO = {
    "name": "Prawin Kanna P",
    "short_name": "Prawin",
    "title": "Applied Data Science | Data Analytics & Data Science Trainer | Aspiring AI/ML Engineer",
    "headline": "Applied Data Science postgraduate with an undergraduate foundation in Statistics. Enthusiastic about turning data into useful insights and building practical, interactive applications with Python and Streamlit.",
    "core_focus": "Python, SQL, BI, ML, visualization",
    "career_direction": "AI/ML Engineering and applied AI projects",
    "location_target": "Chennai or other locations in India",
    "portfolio_url": "https://prawinkanna.github.io/prawin-portfolio",
    "github_handle": "prawinkanna / prawinkannapalaniyappan",
    "linkedin_handle": "prawinkanna / prawinkannapalaniyappan",
}

EDUCATION = [
    {
        "qualification": "M.Sc. Applied Data Science",
        "institution": "SRM Institute of Science & Technology, Trichy",
        "period": "2024–2026",
        "result": "CGPA: 8.54",
        "honors": "First Class with Distinction",
        "details": "Postgraduate specialization focusing on Applied Data Science, machine learning, predictive modeling, and applied AI."
    },
    {
        "qualification": "B.Sc. Statistics",
        "institution": "St. Joseph’s College (Autonomous), Trichy",
        "period": "2021–2024",
        "result": "CGPA: 6.6",
        "honors": "First Class",
        "details": "Undergraduate degree providing a rigorous mathematical and statistical foundation for hypothesis testing, probability, regression, and data analytics."
    }
]

EXPERIENCE = [
    {
        "role": "Data Analytics and Data Science Trainer",
        "company": "FITA Academy",
        "type": "Part-time",
        "period": "July 2026 onward (based on profile record)",
        "summary": "Delivering learning support in data analytics and data science topics, with a focus on making technical concepts accessible to learners.",
        "skills_taught": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Data Cleaning",
            "Data Visualization",
            "Statistics",
            "Machine Learning"
        ],
        "highlights": "Passionate about explaining complex technical concepts with clarity, building hands-on exercises, and mentoring learners through end-to-end analytics workflows."
    },
    {
        "role": "Internship & Project Experience",
        "company": "Data Science & NLP Projects",
        "type": "Prior experience",
        "period": "Completed / Previous",
        "summary": "Internship and project work covering Python for Data Science and NLP sentiment analysis pipelines.",
        "skills_taught": ["Python", "NLP", "Sentiment Analysis", "Data Science"],
        "highlights": "Hands-on implementation of NLP pipelines, text preprocessing, and feature engineering for sentiment classification."
    }
]

SKILLS = {
    "Programming": ["Python", "SQL", "R"],
    "Data Analysis & BI": [
        "Pandas", "NumPy", "Excel", "Power BI", "Tableau", 
        "SPSS", "Data Cleaning", "KPI Reporting", "Interactive Dashboards"
    ],
    "Machine Learning": [
        "Regression", "Classification", "Clustering", "Feature Engineering",
        "Model Evaluation", "Sales Forecasting", "Predictive Modeling"
    ],
    "Deep Learning & Computer Vision": [
        "CNN Fundamentals", "OpenCV", "Image Preprocessing", "Emotion Detection"
    ],
    "App Development & Tools": [
        "Streamlit", "Scikit-learn", "Matplotlib", "Jupyter Notebook",
        "Google Colab", "VS Code", "GitHub"
    ]
}

PROJECTS = [
    {
        "title": "Hybrid Machine Learning Model for Sales Forecasting",
        "category": "Machine Learning & Forecasting",
        "description": "Explores combining complementary forecasting approaches to estimate future sales and compare predictive performance against baseline models.",
        "technologies": ["Python", "Scikit-learn", "Pandas", "Time Series / Forecasting"],
        "highlights": "Analyzed historical trends, engineered temporal features, and blended multiple algorithmic approaches to enhance sales predictions."
    },
    {
        "title": "End-to-End Machine Learning Web App",
        "category": "Full-Stack ML App",
        "description": "A Streamlit-based workflow that brings together model input, prediction inference, and performance visualization into an intuitive, interactive application.",
        "technologies": ["Python", "Streamlit", "Scikit-learn", "Pandas"],
        "highlights": "Allowed non-technical users to input real-time feature variables and immediately see model predictions with interactive charts."
    },
    {
        "title": "Data Analysis and Visualization Web App",
        "category": "BI & Analytics Web App",
        "description": "An interactive web application designed for exploring diverse datasets, generating KPI summaries, and presenting dynamic visual insights.",
        "technologies": ["Python", "Streamlit", "Pandas", "Matplotlib / Plotly"],
        "highlights": "Enabled automated exploratory data analysis (EDA), trend identification, and exportable business intelligence charts."
    },
    {
        "title": "Computer Vision Emotion Detection / Image Preprocessing Apps",
        "category": "Computer Vision",
        "description": "Computer vision applications focused on image preprocessing pipelines and facial emotion detection using convolutional neural network principles.",
        "technologies": ["Python", "OpenCV", "CNN fundamentals", "NumPy"],
        "highlights": "Implemented grayscale filtering, face localization, bounding box normalization, and emotion feature classification."
    },
    {
        "title": "Speech Emotion Recognition (In Progress)",
        "category": "Deep Learning & Audio Signal Processing",
        "description": "A deep-learning project extracting audio acoustic features from the RAVDESS dataset to classify speech emotions. Ongoing model evaluation and fine-tuning.",
        "technologies": ["Python", "Deep Learning", "Audio Feature Extraction (MFCC)", "RAVDESS Dataset"],
        "highlights": "Processes speech spectrograms and acoustic pitch features to classify human emotional states with continuous model iteration."
    }
]

CAREER_GOALS = [
    "Develop deeper expertise in Generative AI, Retrieval-Augmented Generation (RAG), and modern AI application engineering.",
    "Build reliable, production-ready end-to-end AI/ML systems with rigorous evaluation, clean documentation, and seamless deployment.",
    "Secure an AI/ML Engineer position in Chennai or other key tech hubs across India.",
    "Continue teaching and simplifying technical data science concepts to make technology accessible to students and developers."
]

KNOWLEDGE_CHUNKS = [
    {
        "id": "summary",
        "category": "About",
        "keywords": "who is prawin kanna background bio summary about profile introduction who are you tell me about yourself",
        "content_first_person": (
            "Hi there! I'm **Prawin Kanna P**, an Applied Data Science postgraduate with an undergraduate foundation in Statistics.\n\n"
            "My core expertise spans **data analytics, machine learning, data visualization, and applied AI**. "
            "I enjoy converting raw data into actionable insights and building practical, interactive web applications using **Python and Streamlit**.\n\n"
            "My long-term career ambition is to excel as an **AI/ML Engineer** while continuing to advance both my technical capabilities and teaching/mentoring skills."
        ),
        "content_third_person": (
            "**Prawin Kanna P** is an Applied Data Science postgraduate with a strong academic foundation in Statistics.\n\n"
            "His expertise spans **data analytics, machine learning, data visualization, and applied AI**. "
            "He specializes in transforming complex data into actionable business insights and creating interactive web applications with **Python and Streamlit**.\n\n"
            "His career goal is to work as an **AI/ML Engineer** while continually advancing his technical and educational skills."
        )
    },
    {
        "id": "education_msc",
        "category": "Education",
        "keywords": "msc masters postgraduate srm institute trichy applied data science degree cgpa grade marks distinction college",
        "content_first_person": (
            "### 🎓 Postgraduate Education\n"
            "- **Degree**: M.Sc. in Applied Data Science\n"
            "- **Institution**: SRM Institute of Science & Technology, Trichy\n"
            "- **Period**: 2024 – 2026\n"
            "- **Academic Performance**: **CGPA 8.54** (Graduated with **First Class with Distinction**)\n\n"
            "My coursework focused heavily on modern data science, statistical modeling, machine learning algorithms, and real-world data pipelines."
        ),
        "content_third_person": (
            "### 🎓 Postgraduate Education\n"
            "- **Degree**: M.Sc. in Applied Data Science\n"
            "- **Institution**: SRM Institute of Science & Technology, Trichy\n"
            "- **Period**: 2024 – 2026\n"
            "- **Result**: **CGPA 8.54** (**First Class with Distinction**)\n\n"
            "This postgraduate degree provided advanced training in machine learning, statistical modeling, and applied AI architectures."
        )
    },
    {
        "id": "education_bsc",
        "category": "Education",
        "keywords": "bsc bachelors undergraduate st joseph college autonomous trichy statistics college degree cgpa grade marks score",
        "content_first_person": (
            "### 🎓 Undergraduate Education\n"
            "- **Degree**: B.Sc. in Statistics\n"
            "- **Institution**: St. Joseph’s College (Autonomous), Trichy\n"
            "- **Period**: 2021 – 2024\n"
            "- **Academic Performance**: **CGPA 6.6** (**First Class**)\n\n"
            "My undergraduate degree gave me a deep mathematical and statistical grounding in hypothesis testing, regression analysis, probability theory, and data distributions."
        ),
        "content_third_person": (
            "### 🎓 Undergraduate Education\n"
            "- **Degree**: B.Sc. in Statistics\n"
            "- **Institution**: St. Joseph’s College (Autonomous), Trichy\n"
            "- **Period**: 2021 – 2024\n"
            "- **Result**: **CGPA 6.6** (**First Class**)\n\n"
            "Prawin's undergraduate degree in Statistics forms the mathematical backbone of his machine learning and data modeling competencies."
        )
    },
    {
        "id": "experience_fita",
        "category": "Experience",
        "keywords": "fita academy trainer teaching experience job work part-time instructor training mentoring data analytics teacher",
        "content_first_person": (
            "### 💼 Professional Experience — FITA Academy\n"
            "- **Role**: Data Analytics and Data Science Trainer (Part-time)\n"
            "- **Timeline**: July 2026 onward\n\n"
            "**Key Responsibilities & Training Areas**:\n"
            "- Delivering interactive learning support in data analytics and data science, focusing on making complex concepts accessible.\n"
            "- Mentoring students across **Python, SQL, Excel, Power BI, data cleaning, visualization, statistics, and machine learning**.\n"
            "- Designing hands-on exercises and real-world case studies for practical skill development."
        ),
        "content_third_person": (
            "### 💼 Professional Experience — FITA Academy\n"
            "- **Role**: Data Analytics and Data Science Trainer (Part-time)\n"
            "- **Timeline**: July 2026 onward\n\n"
            "**Core Impact**:\n"
            "- Provides structured training in data science and analytics with an emphasis on practical application.\n"
            "- Covers Python, SQL, Excel, Power BI, data cleaning, statistical analysis, and machine learning algorithms.\n"
            "- Known for making challenging technical ideas intuitive for aspiring data professionals."
        )
    },
    {
        "id": "experience_internship",
        "category": "Experience",
        "keywords": "internship nlp sentiment analysis natural language processing previous experience python for data science prior project",
        "content_first_person": (
            "### 💼 Additional Experience & Internships\n"
            "- Prior project and internship experience includes **Python for Data Science** and **NLP Sentiment Analysis**.\n"
            "- Built text preprocessing and classification workflows to analyze sentiment trends from textual data.\n"
            "*(Note: Formal certificate verification and specific duration records can be furnished upon request.)*"
        ),
        "content_third_person": (
            "### 💼 Additional Experience & Internships\n"
            "- Prior internship and project work includes **Python for Data Science** and **NLP sentiment analysis**.\n"
            "- Experience handling natural language preprocessing, tokenization, feature extraction, and sentiment classification."
        )
    },
    {
        "id": "skills_overview",
        "category": "Skills",
        "keywords": "skills tech stack programming languages tools libraries technologies python sql r power bi tableau machine learning deep learning excel pandas numpy opencv streamlit",
        "content_first_person": (
            "### 🛠️ Technical Skills Overview\n\n"
            "| Domain | Technologies & Competencies |\n"
            "| :--- | :--- |\n"
            "| **Programming** | Python, SQL, R |\n"
            "| **Data Analysis & BI** | Pandas, NumPy, Excel, Power BI, Tableau, SPSS, Data Cleaning, KPI Reporting, Dashboards |\n"
            "| **Machine Learning** | Regression, Classification, Clustering, Feature Engineering, Model Evaluation, Sales Forecasting |\n"
            "| **Deep Learning & CV** | CNN Fundamentals, OpenCV, Image Preprocessing, Emotion Detection |\n"
            "| **App Dev & Tools** | Streamlit, Scikit-learn, Matplotlib, Jupyter Notebook, Google Colab, VS Code, GitHub |"
        ),
        "content_third_person": (
            "### 🛠️ Technical Skills Overview\n\n"
            "| Domain | Technologies & Competencies |\n"
            "| :--- | :--- |\n"
            "| **Programming** | Python, SQL, R |\n"
            "| **Data Analysis & BI** | Pandas, NumPy, Excel, Power BI, Tableau, SPSS, Data Cleaning, KPI Reporting, Dashboards |\n"
            "| **Machine Learning** | Regression, Classification, Clustering, Feature Engineering, Model Evaluation, Sales Forecasting |\n"
            "| **Deep Learning & CV** | CNN Fundamentals, OpenCV, Image Preprocessing, Emotion Detection |\n"
            "| **App Dev & Tools** | Streamlit, Scikit-learn, Matplotlib, Jupyter Notebook, Google Colab, VS Code, GitHub |"
        )
    },
    {
        "id": "projects_sales_forecasting",
        "category": "Projects",
        "keywords": "sales forecasting hybrid machine learning model time series predictive models future sales estimate",
        "content_first_person": (
            "### 📈 Hybrid Machine Learning Model for Sales Forecasting\n"
            "- **Focus**: Combining diverse forecasting models to estimate future sales and benchmark predictive accuracy.\n"
            "- **Tech Stack**: Python, Scikit-learn, Pandas, Statistical forecasting.\n"
            "- **Key Contribution**: Engineered time-based features, tested baseline models against ensemble/hybrid approaches, and evaluated error metrics (RMSE/MAE) to optimize sales prediction accuracy."
        ),
        "content_third_person": (
            "### 📈 Hybrid Machine Learning Model for Sales Forecasting\n"
            "- **Focus**: Combines complementary forecasting approaches to estimate future sales and compare predictive performance.\n"
            "- **Tech Stack**: Python, Scikit-learn, Pandas, Predictive Modeling.\n"
            "- **Value**: Improves forecasting reliability by combining algorithmic strengths to capture trends and seasonality."
        )
    },
    {
        "id": "projects_streamlit_apps",
        "category": "Projects",
        "keywords": "streamlit web app end to end machine learning web app data analysis visualization interactive dashboard apps",
        "content_first_person": (
            "### 💻 Streamlit Web Applications\n"
            "I have built multiple interactive web applications using Streamlit:\n\n"
            "1. **End-to-End Machine Learning Web App**:\n"
            "   - Built a complete interactive pipeline connecting user inputs directly with trained Scikit-learn models to generate instantaneous inference results and visualizations.\n\n"
            "2. **Data Analysis and Visualization Web App**:\n"
            "   - Developed an exploratory data application for loading datasets, slicing dimensions, computing metrics, and plotting real-time charts."
        ),
        "content_third_person": (
            "### 💻 Streamlit Web Applications\n"
            "Prawin has built interactive web apps using Streamlit:\n\n"
            "1. **End-to-End Machine Learning Web App**: Streamlit-based workflow that interfaces user inputs, inference models, and real-time visualization.\n"
            "2. **Data Analysis and Visualization Web App**: Interactive platform enabling dataset exploration, automated visual graphs, and business KPI tracking."
        )
    },
    {
        "id": "projects_cv_emotion",
        "category": "Projects",
        "keywords": "computer vision opencv emotion detection image preprocessing cnn convolutional neural network face",
        "content_first_person": (
            "### 👁️ Computer Vision Emotion Detection / Image Preprocessing Apps\n"
            "- **Focus**: Image processing pipelines and emotion classification from visual cues.\n"
            "- **Tech Stack**: Python, OpenCV, CNN fundamentals, NumPy.\n"
            "- **Details**: Developed face and feature localization pipelines, implemented image transformation/normalization techniques, and applied CNN models for emotion classification."
        ),
        "content_third_person": (
            "### 👁️ Computer Vision Emotion Detection / Image Preprocessing Apps\n"
            "- **Focus**: Image preprocessing workflows and facial emotion detection using computer vision.\n"
            "- **Tech Stack**: Python, OpenCV, CNN fundamentals, NumPy.\n"
            "- **Capabilities**: Handles face detection, image scaling/normalization, and neural feature extraction."
        )
    },
    {
        "id": "projects_speech_emotion",
        "category": "Projects",
        "keywords": "speech emotion recognition ravdess audio deep learning audio features ongoing in progress sound classification acoustic",
        "content_first_person": (
            "### 🎙️ Speech Emotion Recognition (In Progress)\n"
            "- **Focus**: Classifying human emotional states from spoken audio utterances.\n"
            "- **Dataset**: RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song).\n"
            "- **Tech Stack**: Python, Deep Learning, Audio signal processing (MFCC / Mel-Spectrogram features).\n"
            "- **Current Status**: Active experimentation with feature extraction, model architecture improvements, and performance evaluation."
        ),
        "content_third_person": (
            "### 🎙️ Speech Emotion Recognition (In Progress)\n"
            "- **Focus**: Deep-learning project using audio features from the RAVDESS dataset to classify speech emotions.\n"
            "- **Tech Stack**: Python, Audio Feature Extraction, Deep Learning.\n"
            "- **Status**: Ongoing model evaluation, acoustic feature optimization, and validation."
        )
    },
    {
        "id": "goals_and_aspirations",
        "category": "Career Goals",
        "keywords": "career goals future aspirations rag generative ai llm chennai job opportunity machine learning engineer where do you see yourself target role",
        "content_first_person": (
            "### 🎯 Learning & Career Goals\n"
            "- **Generative AI & RAG**: Deepening practical skills in Generative AI, Retrieval-Augmented Generation (RAG), and intelligent agent workflows.\n"
            "- **End-to-End Delivery**: Building robust, production-grade AI/ML projects with comprehensive testing, evaluation, and CI/CD deployment.\n"
            "- **Career Aspirations**: Seeking **AI/ML Engineer** opportunities in **Chennai** or other major tech hubs across India.\n"
            "- **Knowledge Sharing**: Continuing to mentor, teach, and create clear learning content in data science."
        ),
        "content_third_person": (
            "### 🎯 Learning & Career Goals\n"
            "- Deepening capabilities in Generative AI, Retrieval-Augmented Generation (RAG), and modern AI application engineering.\n"
            "- Engineering reliable end-to-end AI/ML solutions with strong evaluation metrics and documentation.\n"
            "- Actively pursuing **AI/ML Engineer** opportunities in **Chennai** and across India.\n"
            "- Passionate about pedagogical clarity and mentoring future data professionals."
        )
    },
    {
        "id": "contact_and_links",
        "category": "Contact",
        "keywords": "contact email github portfolio linkedin social profile website reach hire phone connect location link",
        "content_first_person": (
            "### 📬 Get in Touch & Online Profiles\n"
            "- **Portfolio Website**: [prawinkanna.github.io/prawin-portfolio](https://prawinkanna.github.io/prawin-portfolio)\n"
            "- **GitHub**: Search `prawinkanna` or `prawinkannapalaniyappan`\n"
            "- **LinkedIn**: Search `prawinkanna` or `prawinkannapalaniyappan`\n"
            "- **Preferred Location**: Chennai, Tamil Nadu, India (open to relocation / remote across India)\n\n"
            "Feel free to connect regarding AI/ML roles, data analytics collaborations, or speaking/mentorship opportunities!"
        ),
        "content_third_person": (
            "### 📬 Contact & Online Profiles\n"
            "- **Portfolio Website**: [prawinkanna.github.io/prawin-portfolio](https://prawinkanna.github.io/prawin-portfolio)\n"
            "- **GitHub**: Search `prawinkanna` / `prawinkannapalaniyappan`\n"
            "- **LinkedIn**: Search `prawinkanna` / `prawinkannapalaniyappan`\n"
            "- **Target Location**: Chennai, Tamil Nadu, India (open across India)\n\n"
            "Prawin is open to discussing AI/ML engineering roles, data science consulting, and training initiatives."
        )
    }
]

FAQ_QUESTIONS = [
    {
        "q": "🎓 What is Prawin's educational background and CGPA?",
        "intent": "education_msc",
        "prompt": "What is your education and academic performance?"
    },
    {
        "q": "🛠️ What are Prawin's core technical skills?",
        "intent": "skills_overview",
        "prompt": "What technical skills and tools do you know?"
    },
    {
        "q": "💼 Tell me about Prawin's experience at FITA Academy.",
        "intent": "experience_fita",
        "prompt": "Tell me about your role at FITA Academy and what you teach."
    },
    {
        "q": "🚀 What projects has Prawin built?",
        "intent": "projects_sales_forecasting",
        "prompt": "What machine learning and web projects have you developed?"
    },
    {
        "q": "🎯 What are Prawin's career goals and target locations?",
        "intent": "goals_and_aspirations",
        "prompt": "What are your career goals and what job roles are you looking for?"
    },
    {
        "q": "📬 How can I contact Prawin and view his portfolio?",
        "intent": "contact_and_links",
        "prompt": "Where can I find your portfolio, GitHub, and contact links?"
    }
]
