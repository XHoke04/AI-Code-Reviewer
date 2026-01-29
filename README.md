# AI Code Review Assistant

An automated code review tool powered by AI that analyzes pull requests and provides intelligent feedback.

## Setup

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone the repository
2. Create virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create `.env` file:
```bash
   cp backend/.env.example backend/.env
```

### Running Locally
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

Visit: http://localhost:8000

### API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Status

- [x] Task 1: Basic FastAPI setup
- [ ] Task 2: Database setup
- [ ] Task 3: GitHub webhook endpoint
- [ ] Task 4: GitHub API integration
- [ ] Task 5: OpenAI integration