# Product Market Insight

## Overview

This project collects product data using web scraping techniques.

The scraped data includes:

* Product Name
* Price
* Rating
* Availability

The data is exported into CSV format for market analysis purposes.

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* CSV

## Project Structure

product-market-insight/
│
├── data/
│   └── products.csv
│
├── screenshots/
│
├── scraper.py
├── requirements.txt
├── README.md
└── .gitignore

## Output Example

| Product   | Price  | Rating |
| --------- | ------ | ------ |
| Product A | $29.99 | 4.5    |
| Product B | $15.99 | 4.2    |

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
