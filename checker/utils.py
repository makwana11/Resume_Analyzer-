"""
Core logic of the ATS checker.
Simple ane samjva jevu rakhyu che - interview ma explain karva mate easy.
"""
import re
import pdfplumber

# Common words je skip karva na che (skills/keywords nathi hota)
STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'is', 'are', 'was', 'were', 'to', 'of',
    'in', 'on', 'for', 'with', 'as', 'by', 'at', 'this', 'that', 'be',
    'will', 'we', 'you', 'your', 'our', 'it', 'their', 'from', 'have',
    'has', 'not', 'but', 'can', 'must', 'should', 'able', 'etc', 'job',
    'work', 'role', 'team', 'using', 'use', 'per', 'all', 'any', 'who',
    'knowledge', 'experience', 'looking', 'good', 'strong', 'excellent',
    'years', 'year', 'skills', 'skill', 'candidate', 'looking', 'need',
    'needed', 'required', 'requirements', 'about', 'into', 'more',
}


def extract_text_from_pdf(file_path):
    """PDF file ma thi plain text kadhe che (pdfplumber use kari)."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text


def extract_keywords(text):
    """
    Text ma thi meaningful keywords (words) kadhe che.
    - Lowercase kare
    - Only alphabets vadi words rakhe (numbers/symbols hatavi de)
    - Stopwords hatavi de
    - 2 character thi nana words hatavi de
    """
    words = re.findall(r'\b[a-zA-Z][a-zA-Z+#.]*\b', text.lower())
    keywords = {w for w in words if w not in STOPWORDS and len(w) > 2}
    return keywords


def calculate_match_score(resume_text, jd_text):
    """
    Resume ane Job Description na keywords compare kare che.
    Match score = (matched keywords / total JD keywords) * 100
    """
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    if not jd_keywords:
        return 0, set(), set()

    matched = resume_keywords & jd_keywords          # common keywords
    missing = jd_keywords - resume_keywords           # JD ma che pan resume ma nathi

    score = round((len(matched) / len(jd_keywords)) * 100, 2)
    return score, matched, missing
