Here is a cleaned-up and well-structured **full `README.md` file** for your **PubMed Paper Fetcher** project, suitable for placing in the project root or in the `backend/` directory:

---

```markdown
# PubMed Paper Fetcher

A FastAPI-based backend application that fetches research papers from PubMed based on user queries, filtering for pharmaceutical or biotech affiliations. It is paired with a lightweight React-based frontend that provides an intuitive interface to input queries and view results.

---

## 🧠 Overview

- **Backend**: FastAPI (Python) using Biopython's `Entrez` module to query PubMed. Returns JSON data with paper metadata including PMID, title, publication date, author emails, and affiliations.
- **Frontend**: A React single-page app (SPA) styled with Tailwind CSS. Features include a query form, data table, CSV export, loading/error states, and dark mode.

---

## 📦 Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) for Python dependency management
- Node.js (optional, if modifying frontend)
- Git

---

## 📁 Project Structure

```

pubmed-fetcher/
├── backend/
│   ├── main.py            # FastAPI backend code
│   ├── pyproject.toml     # Poetry dependency configuration
│   └── README.md          # Backend-specific documentation
├── frontend/
│   └── index.html         # React + Tailwind single-page frontend
└── README.md              # Project root documentation (this file)

````

---

## 🚀 Installation

### 🔧 Backend Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd pubmed-fetcher/backend
````

2. **Install Dependencies**:
   Make sure Poetry is installed:

   ```bash
   poetry --version
   ```

   Then install:

   ```bash
   poetry install
   ```

3. **Check Python Version**:

   ```bash
   python3 --version
   ```

   If you don't have Python 3.12 installed:

   ```bash
   pyenv install 3.12.0
   pyenv local 3.12.0
   poetry install
   ```

---

### 🌐 Frontend Setup

1. **Navigate to Frontend**:

   ```bash
   cd ../frontend
   ```

2. **No Build Required**:
   The frontend is a simple `index.html` file with React and Tailwind via CDN.

---

## 🧪 Usage

### ▶️ Running the Backend

1. **Activate the Poetry Shell**:

   ```bash
   cd backend
   poetry shell
   ```

2. **Start the FastAPI Server**:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access API Docs**:

   * Base URL: [http://localhost:8000](http://localhost:8000)
   * Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 💻 Running the Frontend

1. **Serve the Page**:
   From `frontend/` directory:

   ```bash
   python -m http.server 3000
   ```

2. **Open in Browser**:

   * [http://localhost:3000](http://localhost:3000)

3. **Use the Interface**:

   * Enter search terms (e.g., `biotech cancer`)
   * Provide email (required)
   * Optional: Add NCBI API key for higher rate limits
   * Set number of results, toggle debug mode
   * Click **Search**

---

## ✨ Features

### Backend

* Queries PubMed using NCBI's Entrez API
* Filters for pharmaceutical or biotech affiliations
* Returns metadata as JSON: `PMID`, `title`, `authors`, `affiliations`, `emails`, etc.
* Supports optional API key for higher rate limits

### Frontend

* React + Tailwind-based single-page interface
* Responsive and mobile-friendly
* CSV download of results
* Dark mode toggle
* Sorting and loading indicators

---

## ⚙️ Configuration

* **Email (Required)**:
  Needed by NCBI API for contact tracking. Enter via frontend or set a default in `main.py`.

* **API Key (Optional)**:
  Improves API rate limits. Can be input in frontend.

* **CORS**:
  CORS is enabled with `allow_origins=["*"]` in development. Change this in production.

---

## ☁️ Deployment

### Backend (Render.com or similar)

1. **Push Your Code**:

   ```bash
   git add .
   git commit -m "Initial deploy"
   git push origin main
   ```

2. **Render Settings**:

   * **Web Service**
   * **Build Command**: `poetry install --no-dev`
   * **Start Command**: `poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`
   * **Environment**:

     * `PYTHON_VERSION=3.12`

---

### Frontend (Render.com or similar)

1. **Push Code**:
   Commit the `index.html` file inside `frontend/` directory.

2. **Render Settings**:

   * **Static Site**
   * **Publish Directory**: `frontend/`

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch:

   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:

   ```bash
   git commit -m "Add feature"
   ```
4. Push to branch and open a Pull Request

---

## 📄 License

\[Add your license here, e.g., MIT, Apache 2.0, etc.]

---

## 📬 Contact

For questions, issues, or contributions, please reach out to the project maintainer.

---

```

Let me know if you want to embed screenshots, add API example payloads, or automate setup with shell scripts or Docker.
```
