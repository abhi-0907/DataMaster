import google.generativeai as genai
import markdown
from dotenv import load_dotenv
import os
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3600)  # Cache up to 100 results for 1 hour
load_dotenv()

@cached(cache)

def generate_insights(course, budget, country):
    genai.configure(api_key=os.getenv("GEMINI_API"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (
    f"Generate detailed information for a student planning to study {course} in {country}. "
    "Include: \n"
    f"- Top {budget} Budget universities for this course\n"
    "- Admission requirements and deadlines\n"
    "- Tuition fees and living expenses\n"
    "- Scholarships available\n"
    "- Rankings and job opportunities post-graduation\n"
    "- Any other relevant information for a student planning to study in this country"
)
    response = model.generate_content(prompt)   
    html_response = markdown.markdown(response.text)
    return html_response

