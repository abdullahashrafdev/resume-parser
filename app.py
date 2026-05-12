import pdfplumber
import spacy
import re
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

SKILLS_LIST = [
    "python", "flask", "docker", "aws", "machine learning", "deep learning",
    "opencv", "tensorflow", "pytorch", "sql", "mongodb", "git", "linux",
    "javascript", "react", "node.js", "n8n", "ci/cd", "github actions"
]

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_email(text):
    match = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"[\+\(]?[0-9][0-9\s\-\(\)]{8,}[0-9]", text)
    return match[0] if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    text_lower = text.lower()
    found = [skill for skill in SKILLS_LIST if skill in text_lower]
    return found

@app.route("/parse", methods=["POST"])
def parse():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    text = extract_text(file)
    
    result = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)