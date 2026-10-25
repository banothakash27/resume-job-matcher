import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

st.set_page_config(page_title="Resume Job Matcher", page_icon="🧭")
st.title("🧭 Resume–Job Description Matcher")
st.write("Compare the text of a resume with a job description and inspect shared and missing keywords. This is a decision-support demo, not a hiring decision tool.")
resume_file = st.file_uploader("Upload resume PDF (text-based)", type=["pdf"])
job_text = st.text_area("Paste the job description", height=200)
def extract_pdf(upload):
    reader = PdfReader(upload)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
def words(text):
    return set(re.findall(r"[a-zA-Z][a-zA-Z+#.-]{1,}", text.lower()))
if st.button("Compare documents", type="primary", disabled=resume_file is None or not job_text.strip()):
    try:
        resume_text = extract_pdf(resume_file)
        if not resume_text.strip():
            st.error("No text could be extracted. The PDF may be scanned; OCR is not included.")
        else:
            vectorizer = TfidfVectorizer(stop_words="english")
            matrix = vectorizer.fit_transform([resume_text, job_text])
            score = float(cosine_similarity(matrix[0], matrix[1])[0, 0])
            r_words, j_words = words(resume_text), words(job_text)
            shared = sorted(r_words & j_words)
            missing = sorted(j_words - r_words)
            a, b = st.columns(2)
            a.metric("Text similarity", f"{score:.0%}")
            b.metric("Shared keywords", len(shared))
            st.caption("Similarity is based on TF-IDF text overlap. It is not a probability of being hired or a measure of candidate quality.")
            st.subheader("Keywords found in both")
            st.write(", ".join(shared) if shared else "No shared keywords found.")
            st.subheader("Job-description keywords not found in resume")
            st.write(", ".join(missing[:100]) if missing else "No unmatched keywords found.")
            st.info("Review the missing terms manually. Only add skills or experience to a resume if they are accurate.")
    except Exception as exc:
        st.error(f"Could not process the resume: {exc}")
