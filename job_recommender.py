def recommend_jobs(skills):
    jobs = [
        {"title": "Machine Learning Engineer", "company": "TechCorp", "skills": ["Python", "Machine Learning"]},
        {"title": "Frontend Developer", "company": "Webify", "skills": ["JavaScript", "HTML", "CSS"]},
        {"title": "Data Analyst", "company": "DataDive", "skills": ["Python", "SQL"]},
    ]
    matched = []
    for job in jobs:
        match_count = len(set(job["skills"]) & set(skills))
        if match_count > 0:
            matched.append(job)
    return matched
