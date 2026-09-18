# Career Market Intelligence

## Overview
This project collects Python job market data directly from Python.org using web scraping techniques. The data is exported into CSV and Excel formats for further market analysis.

**Website Source:** https://www.python.org/jobs/

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- CSV
- Excel

## Extracted Data
- Job Title
- Company Name
- Location
- Posting Date

## Project Structure
```text
career-market-intelligence/
│
├── data/
│   ├── python_jobs_clean.csv
│   └── python_jobs_clean.xlsx
│
├── screenshots/
│   ├── website-source.png
│   ├── terminal-success.png
│   └── excel-result.png
│
├── scraper.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation & Usage
```bash
pip install -r requirements.txt
python scraper.py
```

## Author
**Angga Fasri Nur**
