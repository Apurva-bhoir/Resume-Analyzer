import streamlit as st
from resume_parser import extract_text_from_pdf
from nlp_utils import extract_skills
from job_recommender import recommend_jobs
from resume_scorer import suggest_improvements

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer & Job Matcher")

# --- Upload PDF ---
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
resume_text = ""

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    # --- Styled Extracted Resume Text ---
    st.subheader("📄 Resume Text")
    st.markdown("Here's what we found in your resume:")

    st.markdown(
        f"""
        <div style='height: 300px; overflow-y: auto; padding: 1rem;
                    background-color: #1e1e1e; color: #f1f1f1; 
                    border-radius: 10px; border: 1px solid #444;'>
            <pre style="white-space: pre-wrap; font-size: 0.9rem;">{resume_text}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Skills Extraction ---
    skills = extract_skills(resume_text)
    st.subheader("🛠️ Detected Skills")
    st.write(skills)

    # --- Job Recommendations ---
    job_matches = recommend_jobs(skills)
    st.subheader("💼 Recommended Jobs")
    for job in job_matches:
        st.write(f"🔹 {job['title']} - {job['company']}")

    # --- AI Suggestions ---
    if st.button("📌 Get AI Suggestions to Improve Resume"):
        with st.spinner("Analyzing resume..."):
            suggestions = suggest_improvements(resume_text)
            st.subheader("✅ AI Suggestions")
            st.write(suggestions)
else:
    st.info("👆 Please upload a PDF resume to begin.")
