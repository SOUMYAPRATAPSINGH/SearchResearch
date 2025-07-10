from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import pandas as pd
from Bio import Entrez
import time
import re
from typing import Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production to specific frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PaperRequest(BaseModel):
    query: str
    email: str
    api_key: Optional[str] = None
    max_results: int = 100
    debug: bool = False

def setup_logging(debug: bool):
    """Configure logging based on debug flag."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_papers(query: str, email: str, api_key: Optional[str], max_results: int):
    """Fetch papers from PubMed using the provided query."""
    Entrez.email = email
    if api_key:
        Entrez.api_key = api_key
    try:
        logging.debug(f"Executing search with query: {query}")
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()
        return record["IdList"]
    except Exception as e:
        logging.error(f"Error fetching papers: {e}")
        return []

def get_paper_details(pmid: str):
    """Retrieve details for a specific PubMed ID."""
    time.sleep(0.34)  # Rate limit: ~3 requests/second without API key
    try:
        logging.debug(f"Fetching details for PMID: {pmid}")
        handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
        record = Entrez.read(handle)
        handle.close()
        
        article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
        title = article.get("ArticleTitle", "N/A")
        
        pub_date = "N/A"
        if article.get("Journal", {}).get("JournalIssue", {}).get("PubDate"):
            date_dict = article["Journal"]["JournalIssue"]["PubDate"]
            pub_date = f"{date_dict.get('Year', 'N/A')}-{date_dict.get('Month', 'N/A')}-{date_dict.get('Day', 'N/A')}"
        
        authors = article.get("AuthorList", [])
        email = "N/A"
        affiliation = "N/A"
        for author in authors:
            if author.get("AffiliationInfo"):
                aff = author["AffiliationInfo"][0].get("Affiliation", "N/A")
                if is_pharma_biotech(aff):
                    affiliation = aff
                    email = author["AffiliationInfo"][0].get("Email", "N/A") if "Email" in author["AffiliationInfo"][0] else "N/A"
                    if email == "N/A":
                        logging.debug(f"No email found for PMID {pmid}")
                    break
        
        return {
            "PMID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Corresponding Author Email": email,
            "Affiliation": affiliation
        }
    except Exception as e:
        logging.error(f"Error fetching details for PMID {pmid}: {e}")
        return None

def is_pharma_biotech(affiliation: str):
    """Check if affiliation indicates a pharmaceutical or biotech company."""
    pharma_keywords = [r"\bInc\b", r"\bLtd\b", r"\bPharma\b", r"\bBiotech\b", r"\bLaboratories\b", r"\bPharmaceuticals\b"]
    return any(re.search(keyword, affiliation, re.IGNORECASE) for keyword in pharma_keywords)

@app.post("/api/fetch-papers")
async def fetch_papers_endpoint(request: PaperRequest):
    """API endpoint to fetch papers from PubMed."""
    setup_logging(request.debug)
    logging.info("Starting paper fetch process")
    
    pmids = fetch_papers(request.query, request.email, request.api_key, request.max_results)
    
    if not pmids:
        raise HTTPException(status_code=404, detail="No papers found for the query.")
    
    papers = []
    for pmid in pmids:
        paper = get_paper_details(pmid)
        if paper and paper["Affiliation"] != "N/A":
            papers.append(paper)
        else:
            logging.debug(f"Skipping PMID {pmid} due to no pharma/biotech affiliation")
    
    if not papers:
        raise HTTPException(status_code=404, detail="No papers with pharmaceutical/biotech affiliations found.")
    
    return {"papers": papers}