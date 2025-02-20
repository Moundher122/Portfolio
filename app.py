import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv

# Page title
st.set_page_config(page_title="Moundher Bouroumana - Portfolio", layout="wide")
load_dotenv()
GA_TRACKING_ID = os.getenv("ID")
if GA_TRACKING_ID:
    GA_SCRIPT = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_TRACKING_ID}');
    </script>
    """
    st.markdown(GA_SCRIPT, unsafe_allow_html=True)
# Profile Picture and Name in the same line
profile_pic = "profile.jpg"  # Ensure this image exists in your working directory
image = Image.open(profile_pic)

col1, col2 = st.columns([1,15])
with col1:
    st.image(image, width=300)
    
with col2:
    st.markdown("# Bouroumana Moundher")



# Social links
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-moundher122-black?logo=github)](https://github.com/moundher122)")
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-moundherbourouma-blue?logo=linkedin)](https://linkedin.com/in/moundherbourouma)")
st.write("****")
with open("cv.pdf", "rb") as file:
    cv_data = file.read()

st.markdown(
    """
    <div style="text-align: center; font-size: 18px; font-weight: bold; color: #FFFAFA; margin-top: 10px;">
        ✨ Hi! I'm Moundher Bouroumana, a Backend Engineer, ML Developer, and Python Developer. ✨
    </div>
    <div style="text-align: center; margin-top: 20px;">
    """,
    unsafe_allow_html=True,
)

st.download_button(
    label="Download My CV",
    data=cv_data,
    file_name="Moundher_Bouroumana_CV.pdf",
    mime="application/pdf",
)

st.markdown(
    """
        <a href="mailto:bouroumanamoundher@gmail.com">
            <button style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Hire Me</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)




# Education
st.header("Education")
st.write("**Higher School of Computer Science SBA**")
st.write("B.S. Computer Science ")


# Skills
st.header("Skills")
skills = {
    "Python": "https://img.shields.io/badge/Python-blue?logo=python",
    "Dart": "https://img.shields.io/badge/Dart-blue?logo=dart",
    "SQL": "https://img.shields.io/badge/SQL-orange?logo=mysql",
    "Java": "https://img.shields.io/badge/Java-red?logo=java",
    "Django": "https://img.shields.io/badge/Django-green?logo=django",
    "Django Rest Framework": "https://img.shields.io/badge/DRF-red?logo=django",
    "TensorFlow": "https://img.shields.io/badge/TensorFlow-orange?logo=tensorflow",
    "PyTorch": "https://img.shields.io/badge/PyTorch-red?logo=pytorch",
    "Scikit-Learn": "https://img.shields.io/badge/Scikit--Learn-yellow?logo=scikit-learn",
    "NumPy": "https://img.shields.io/badge/NumPy-blue?logo=numpy",
    "Pandas": "https://img.shields.io/badge/Pandas-blue?logo=pandas",
    "PostgreSQL": "https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql",
    "Docker": "https://img.shields.io/badge/Docker-blue?logo=docker",
    "RabbitMQ": "https://img.shields.io/badge/RabbitMQ-orange?logo=rabbitmq",
    "Celery": "https://img.shields.io/badge/Celery-green?logo=celery",
    "Redis": "https://img.shields.io/badge/Redis-red?logo=redis",
    "Git": "https://img.shields.io/badge/Git-black?logo=git",
}

for skill, icon in skills.items():
    st.markdown(f"![{skill}]({icon}) **{skill}**")
st.header("Projects")

projects = [
    {"name": "AI-Powered Logistics Optimization", "overview": "Developed an AI-powered logistics system for optimizing truck space and suggest drivers.", "skills": "Django, RabbitMQ, Pyb3, TensorFlow, PostgreSQL", "github": "https://github.com/Moundher122/tatweer"},
    {"name": "Hackathon Logistics Platform", "overview": "Developed a logistics platform for efficient truck-sharing and route optimization.", "skills": "Django, Flutter, Firebase, RabbitMQ, PostgreSQL", "github": "https://github.com/Moundher122/tatweer"},
    {"name": "Career Bridge Platform", "overview": "Developed a platform connecting students with internships and companies posting real-world problems to solve.", "skills": "Web, App, Redis, RabbitMQ, Celery, JWT", "github": "https://github.com/Moundher122/CP2Project"},
    {"name": "Neural Network from Scratch", "overview": "Built a fully connected neural network from scratch using only NumPy.", "skills": "Python, NumPy", "github": "https://github.com/Moundher122/number-classfier"},
    {"name": "Hotel Management and Reservation App", "overview": "Developed a Flutter app for managing hotel bookings with real-time data.", "skills": "Flutter, Firebase, API Integration", "github": "https://github.com/Moundher122/bsc_app"},
    {"name": "Library Management System", "overview": "Built a library management system with role-based access control.", "skills": "Django, flutter, PostgreSQL", "github": "https://github.com/Moundher122/library"},
]

for project in projects:
    with st.container():
        st.markdown(
            f"""
            <div style="border: 2px solid rgba(221, 221, 221, 0.5); padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: rgb(14, 17, 23);">
                <h3>{project["name"]}</h3>
                <p>{project["overview"]}</p>
                <strong>Skills:</strong> {project["skills"]}
                <br>
                <a href="{project['github']}" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-Repo-black?logo=github" alt="GitHub">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

st.header("Blog & Open Source Packages")
st.write("Check out my latest blog posts and Python packages!")
st.markdown("[Understanding the N+1 Problem in Django (And How to Fix It)](https://medium.com/@bouroumanamoundher/understanding-the-n-1-problem-in-django-and-how-to-fix-it-d8dcc7573bd3)")
st.markdown("[Setting Up a task Queue using Celery and RabbitMQ WITH DJANGO](https://medium.com/@bouroumanamoundher/setting-up-a-task-queue-using-celery-and-rabbitmq-with-django-1f96dd8b885e)")
st.markdown("[django-schema-history](https://github.com/moundher122/django-schema-history)")

# Certifications
st.header("Certifications")
st.write("- Data Science from HP")
st.write("- Problem Solving from Hackrank")
st.write("- Participant in BSc Hackathon by Dev Up")
st.write("- Participant in Tatweer Hackathon by Micro Club")
st.write("- Basics AI to Gen AI by NVIDIA")
