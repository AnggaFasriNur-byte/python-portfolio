# E-Commerce Books Scraper

## Overview
An automated web scraping pipeline built to extract 1,000 product records across a 50-page e-commerce catalog. It handles multi-page pagination, parses nested HTML/CSS attributes, converts categorical text ratings into numerical values, and exports clean data into an Excel spreadsheet.

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- Pandas
- openpyxl
- Jupyter Notebook

## Key Features
- **Pagination Automation:** Loops programmatically across 50 target pages.
- **Robust Error Handling:** Implements `try-except` blocks to prevent script crashes on missing attributes.
- **Data Transformation:** Maps text-based star ratings ('One', 'Two', 'Three') directly to integers (1-5).

## Project Structure
```text
Web_Scraping_BeautifulSoup_Ecommerce_Books/
│
├── data/
│   └── book_scrape.xlsx    # The final extracted dataset
│
├── scraper.ipynb           # Main Jupyter Notebook containing the scraper logic
└── README.md
```

## Author
**Angga Fasri Nur**
