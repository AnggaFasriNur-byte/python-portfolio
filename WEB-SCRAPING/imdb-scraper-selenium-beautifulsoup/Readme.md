# IMDb Advanced Search Scraper

A robust and automated web scraping pipeline built with Python to extract movie metadata from IMDb's Advanced Search platform.

This project demonstrates the ability to bypass strict anti-bot protections, handle dynamic React-based UI elements, and overcome lazy-loading pagination to extract large-scale datasets cleanly.

## Key Features

- Anti-Bot Bypass: Utilizes undetected-chromedriver to navigate IMDb's security blocks seamlessly.
- Dynamic Interaction: Automates human-like browser interactions (dropdown selection, keyboard simulation, and custom JavaScript clicks) to configure complex search filters.
- Lazy Loading Handling: Programmatically scrolls and clicks the Load More pagination buttons to reveal hidden elements, successfully scraping 1,000+ records in a single run.
- Automated Data Cleaning: Cleans and formats raw HTML text like removing ranking numbers from titles before structuring the data.
- Ready-to-Use Output: Exports the final, clean dataset into a structured Excel format.

## Tech Stack

- Python 3
- Selenium and Undetected-Chromedriver for browser automation and JavaScript execution
- BeautifulSoup4 for HTML parsing and element extraction
- Pandas for data manipulation and Excel export

## Extracted Data Points

## 📂 Project Structure

```text
imdb-scraper-selenium-beautifulsoup/
│
├── data/
│   └── imdb_advanced_search_results.xlsx   # The final extracted dataset
│
├── imdb_scraper.ipynb                      # Main Jupyter Notebook containing the scraper logic
└── README.md
```

For each movie or TV series, the scraper extracts:

1. Movie Title
2. Release Year
3. Duration
4. IMDb Rating
