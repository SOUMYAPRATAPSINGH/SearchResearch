
# 🧬 PubMed Paper Fetcher

A full-stack application that fetches research papers from **PubMed** based on user queries, specifically filtering for **pharmaceutical** or **biotech** affiliations. Built with **FastAPI** for the backend and a lightweight **React + Tailwind CSS** frontend.

---

## 🔍 Features

- ✅ FastAPI-based backend using Biopython Entrez to query PubMed
- ✅ Filters results based on pharma/biotech affiliations
- ✅ Returns JSON data with PMID, title, date, emails, and affiliations
- ✅ React frontend with:
  - Dynamic query form
  - Sortable results table
  - CSV download
  - Dark mode toggle
  - Error/loading indicators

---

## ⚙️ Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) (for backend dependency management)
- Node.js (optional, for frontend development)
- Git

---

## 📁 Project Structure



pubmed-fetcher/
├── backend/
│   ├── main.py            # FastAPI app
│   ├── pyproject.toml     # Poetry dependencies
│   └── README.md          # Optional: backend-specific info
├── frontend/
│   └── index.html         # Single-page React frontend
└── README.md              # Project root documentation (this file)

````



## 🚀 Setup Instructions

### 🔧 Backend Setup

```bash
# Clone the repo
git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher/backend

# Install Poetry dependencies
poetry install

# Activate the environment
poetry shell

# Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
````

Access the backend at: [http://localhost:8000](http://localhost:8000)
API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🌐 Frontend Setup

```bash
# Navigate to frontend folder
cd ../frontend

# Serve using Python HTTP server
python -m http.server 3000
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🧪 Usage

1. Enter a PubMed search query (e.g., `biotech cancer`)
2. Provide your **email** (required by NCBI)
3. Optionally enter your **NCBI API key** for higher request limits
4. Set max results (default 20)
5. Click **Search**
6. View results, download CSV, or toggle dark mode

---

## 🔐 Configuration

| Setting            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| Email (required)   | Used for NCBI API compliance                               |
| API Key (optional) | Boosts PubMed rate limits                                  |
| CORS               | Development: `*` (open); update for production deployments |

---

## ☁️ Deployment

### 🚀 Backend (Render.com or similar)

1. **Push your code** to a Git repo
2. On Render:

   * Create a **Web Service**
   * **Build Command**: `poetry install --no-dev`
   * **Start Command**: `poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`
   * **Environment Variables**:

     * `PYTHON_VERSION=3.12`

### 🌍 Frontend (Render or GitHub Pages)

1. Push `index.html` to the `frontend/` directory
2. On Render:

   * Create a **Static Site**
   * **Publish Directory**: `frontend/`

---

## 🤝 Contributing

```bash
# Fork the repo and clone it
git checkout -b feature-branch
# Make your changes
git commit -m "Add awesome feature"
git push origin feature-branch
# Open a pull request!
```

---

## 📄 License

\[Add your preferred license here, e.g., MIT, Apache 2.0]

---

## 📬 Contact

For questions, suggestions, or feedback, please reach out to the project maintainer.

```

---

### ✅ Next Steps:
- Replace `https://github.com/your-username/pubmed-fetcher.git` with your actual GitHub repo URL.
- Specify your **license** in the relevant section (and add a `LICENSE` file).
- (Optional) Add project screenshots or badges at the top for flair.

Let me know if you want a version with badges, GIF demo, Docker support, or anything else!
```
