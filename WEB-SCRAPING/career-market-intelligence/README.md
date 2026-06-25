# Career Market Intelligence

## Overview

This project collects Python job market data from Python.org using web scraping techniques.

The scraped data includes:

* Job Title
* Company Name
* Location
* Posting Date

The data is exported into CSV and Excel format for further analysis.

## Website Source

https://www.python.org/jobs/

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* CSV
* Excel

## Project Structure

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

## Output Example

| Title                | Company     | Location                    | Date Posted  |
| -------------------- | ----------- | --------------------------- | ------------ |
| Senior Data Engineer | Six Feet Up | 100% Remote, USA            | 18 June 2026 |
| Agentic AI Scientist | AstraZeneca | Durham, North Carolina, USA | 18 June 2026 |

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python scraper.py
```

## Author

Angga Fasri Nur
