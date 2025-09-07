
# resume_analyzer.py
import re

def analyze_resume(text):
    skills = ["Python", "Java", "Machine Learning", "SQL", "AI", "GitHub"]
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return found

if __name__ == "__main__":
    resume = """
    John Doe
    Skills: Python, Machine Learning, GitHub, SQL
    Experience: Data Analyst
    """
    print("✅ Found Skills:", analyze_resume(resume))
