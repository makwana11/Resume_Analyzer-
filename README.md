# Resume_Analyzer-
# Resume ATS Score Checker

Django-based web app je resume (PDF) ne job description sathe match kari ne
ATS (Applicant Tracking System) score aape che, ane missing keywords batave che.

## Features
- Resume (PDF) upload
- Job description paste karo
- Automatic keyword extraction & matching
- ATS match score (%) with color-coded result
- Matched vs Missing keywords list
- History of all previous checks

## Tech Stack
- Python, Django
- PostgreSQL (SQLite for quick local testing)
- pdfplumber (PDF text extraction)
- Bootstrap 5 (frontend)

## How it works (Logic)
1. User PDF resume upload kare -> `pdfplumber` thi text extract thay
2. Resume text ane Job Description, banne ma thi keywords kadhay
   (stopwords jeva ke "the", "and", "with" hatavi devay)
3. Keywords set operations vapari matched/missing keywords kadhay:
   - `matched = resume_keywords & jd_keywords`
   - `missing = jd_keywords - resume_keywords`
4. Score = (matched keywords / total JD keywords) * 100

## Setup

```bash
pip install django pdfplumber psycopg2-binary

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Browser ma kholo: http://127.0.0.1:8000/

## PostgreSQL vaparva mate
`resume_analyzer/settings.py` ma `USE_POSTGRES = True` karo ane
tamara database credentials (NAME, USER, PASSWORD) update karo.

## Project Structure
```
resume_analyzer/
├── checker/
│   ├── models.py      # Resume model
│   ├── forms.py       # Upload form
│   ├── utils.py        # ATS matching logic (core)
│   ├── views.py        # upload / result / history views
│   ├── urls.py
│   └── templates/checker/
│       ├── base.html
│       ├── upload.html
│       ├── result.html
│       └── history.html
└── resume_analyzer/
    ├── settings.py
    └── urls.py
```
