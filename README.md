PubMed Paper Fetcher
A FastAPI-based backend application that fetches research papers from PubMed based on user queries, filtering for pharmaceutical or biotech affiliations. Paired with a React-based frontend for an interactive user interface.
Overview

Backend: Written in Python using FastAPI, the backend queries the PubMed API (via Biopython) to retrieve paper details (e.g., PMID, title, publication date, author email, affiliation) and returns results in JSON format.
Frontend: A single-page React application with Tailwind CSS styling, offering a form to input search parameters and a table to display results with sorting, CSV download, and dark mode toggle.

Prerequisites

Python 3.12 or higher
Poetry for dependency management
Node.js (optional, for serving the frontend locally)
Git (for version control)

Project Structure
pubmed-fetcher/
├── backend/
│   ├── main.py          # FastAPI backend code
│   ├── pyproject.toml   # Poetry configuration and dependencies
│   └── README.md        # This file
├── frontend/
│   └── index.html       # React frontend code
└── README.md            # Project root README

Installation
Backend Setup

Clone the Repository:
git clone <your-repo-url>
cd pubmed-fetcher/backend


Install Dependencies:

Ensure Poetry is installed (poetry --version).
Install dependencies:poetry install




Verify Python Version:

Check your Python version:python3 --version


If Python 3.12 isn’t installed, use pyenv to install it:pyenv install 3.12.0
pyenv local 3.12.0
poetry install





Frontend Setup

Navigate to Frontend Directory:
cd ../frontend


No Additional Installation Needed:

The frontend is a single index.html file with CDN-hosted React and Tailwind CSS. Serve it using a simple HTTP server (see Usage below).



Usage
Running the Backend

Activate the Poetry Environment:
cd backend
poetry shell


Start the FastAPI Server:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


Access the API at http://localhost:8000.
Test the /api/fetch-papers endpoint via http://localhost:8000/docs.



Running the Frontend

Serve the Frontend:
cd frontend
python -m http.server 3000


Access the Interface:

Open http://localhost:3000 in a browser.
Enter a query (e.g., biotech cancer), email, optional NCBI API key, max results, and toggle debug mode, then submit to fetch papers.



Features

Backend: Fetches PubMed papers, filters for pharma/biotech affiliations, and returns JSON data.
Frontend: Interactive form, sortable table, CSV download, dark mode, and loading/error handling.

Configuration

NCBI API Key: Optional, improves PubMed rate limits (set in the frontend form).
Email: Required for PubMed API access (set in the frontend form or main.py).
CORS: Enabled with allow_origins=["*"] (update to your frontend domain in production).

Deployment
Backend Deployment (e.g., Render.com)

Push to Git Repository:

Commit pyproject.toml, poetry.lock, and main.py.


Configure Render:

Create a Web Service.
Build Command: poetry install --no-dev
Start Command: poetry run uvicorn main:app --host 0.0.0.0 --port $PORT
Environment: Set PYTHON_VERSION=3.12.
Deploy and note the URL (e.g., https://your-backend.onrender.com).



Frontend Deployment (e.g., Render.com)

Push Frontend Files:

Commit index.html to a frontend/ directory.


Configure Render:

Create a Static Site.
Publish Directory: frontend/
Environment: Set REACT_APP_API_URL=https://your-backend.onrender.com.
Deploy and note the URL (e.g., https://your-frontend.onrender.com).



Contributing

Fork the repository.
Create a branch (git checkout -b feature-branch).
Commit changes (git commit -m "Add new feature").
Push and open a pull request.

License
[MIT License] - See LICENSE file for details (add a LICENSE file if not present).
Contact
For questions or support, contact Your Name at you@example.com.
