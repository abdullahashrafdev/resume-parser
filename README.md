# Resume Parser API

A Flask REST API that extracts structured information from PDF resumes using Natural Language Processing (NLP). Upload a PDF resume and get back a clean JSON response with the candidate's name, email, phone number, and skills.

---

## Features

- Extracts name using spaCy NLP (Named Entity Recognition)
- Extracts email and phone number using regex
- Detects skills from a predefined skills list
- Accepts PDF file uploads via REST API
- Containerized with Docker for easy deployment
- Automated testing and CI/CD pipeline via GitHub Actions

---

## Tech Stack

- **Python** — Core language
- **Flask** — REST API framework
- **spaCy** — NLP library for named entity recognition
- **pdfplumber** — PDF text extraction
- **Docker** — Containerization
- **GitHub Actions** — CI/CD pipeline
- **pytest** — Automated testing

---

## Project Structure

```
resume-parser/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── test_app.py             # Automated tests
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## How to Run

### Option 1: Run with Docker (Recommended)

Make sure Docker Desktop is installed and running.

```bash
git clone https://github.com/abdullahashrafdev/resume-parser.git
cd resume-parser
docker-compose up
```

The API will be live at `http://localhost:5001`

### Option 2: Run Locally

```bash
git clone https://github.com/abdullahashrafdev/resume-parser.git
cd resume-parser
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

---

## API Usage

### Endpoint

```
POST /parse
```

### Request

Send a PDF file as form-data with the key `file`.

**Using curl:**
```bash
curl -X POST http://localhost:5001/parse -F "file=@your_resume.pdf"
```

**Using Postman:**
1. Set method to POST
2. URL: `http://localhost:5001/parse`
3. Body → form-data → Key: `file`, Type: File
4. Select your PDF and click Send

### Response

```json
{
  "name": "Muhammad Abdullah",
  "email": "abdullahhashraf@gmail.com",
  "phone": "+923341470836",
  "skills": [
    "python",
    "flask",
    "docker",
    "aws",
    "opencv",
    "git",
    "n8n",
    "ci/cd",
    "github actions"
  ]
}
```

### Error Response

If no file is uploaded:
```json
{
  "error": "No file uploaded"
}
```

---

## Running Tests

```bash
pytest test_app.py
```

---

## CI/CD Pipeline

Every push to the repository automatically:
1. Builds the Docker image
2. Runs all tests inside the container

Pipeline status is visible under the **Actions** tab on GitHub.

---

## Author

**Muhammad Abdullah**  
[github.com/abdullahashrafdev](https://github.com/abdullahashrafdev)  
[linkedin.com/in/muhammad-abdullah-a4b59328b](https://www.linkedin.com/in/muhammad-abdullah-a4b59328b)
