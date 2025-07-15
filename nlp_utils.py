def extract_skills(text):
    keywords = ["Python", "Java", "C++", "Machine Learning", "Deep Learning", "NLP", "SQL", "HTML", "CSS", "JavaScript"]
    return [kw for kw in keywords if kw.lower() in text.lower()]
