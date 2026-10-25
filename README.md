# Resume–Job Description Matcher

A lightweight tool that compares a text-based resume PDF with a pasted job description using TF-IDF similarity and keyword overlap.

## Features
- Extract text from a PDF resume
- Compare resume and job description text
- Display a similarity score and shared keywords
- List job-description terms absent from the resume
- Include a caution that results require human review

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Privacy
This app processes files locally when run on your own computer. Do not upload real resumes to a public hosted demo without consent and suitable privacy protections.

## Limitations
Keyword overlap misses context and synonyms. The similarity score is not a hiring probability, ranking, or recommendation. It must not be used as the sole basis for hiring decisions.

## Skills demonstrated
Python, PDF text extraction, TF-IDF, cosine similarity, keyword analysis, and Streamlit.
