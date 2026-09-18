# 99Bookstores Web Scraper

A Python web scraper that collects book/product information from 99Bookstores and stores the extracted data in a CSV file.

## Features

- Scrapes book/product information from 99Bookstores.
- Extracts book name, price, rating, availability, and product URL.
- Prevents duplicate products using unique product URLs.
- Handles missing product fields with fallback values.
- Uses request timeouts and retry logic for failed HTTP requests.
- Validates HTTP responses using `raise_for_status()`.
- Skips individual products when all request attempts fail instead of stopping the entire scraper.
- Saves successfully processed records to `book.csv`.
- Uses a `main()` entry point to organize the scraper workflow.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- lxml
- CSV

## Data Collected

| Field | Description |
|---|---|
| Book name | Name of the book/product |
| Price | Product price |
| Rating | Product rating |
| Availability | Availability status detected from the product page |
| link | Product page URL |

## How It Works

The scraper follows these steps:

1. Sends an HTTP request to the 99Bookstores website.
2. Parses the HTML using BeautifulSoup with the `lxml` parser.
3. Identifies product cards on the page.
4. Extracts the book name, price, rating, and product URL.
5. Uses a `set` to prevent duplicate product URLs.
6. Requests each individual product page to determine availability.
7. Retries failed HTTP requests up to three times with a delay between attempts.
8. Skips a product if its page cannot be retrieved after all retry attempts.
9. Writes successfully processed records to `book.csv`.

## Error Handling

The scraper uses a reusable `get_page()` function that provides:

- A 10-second request timeout.
- Up to 3 attempts for a failed request.
- A 2-second delay between retry attempts.
- HTTP status validation using `raise_for_status()`.
- Handling of `requests.RequestException`.

If an individual product request continues to fail after all retries, that product is skipped and the scraper continues processing the remaining products.

## Project Structure

```text
Web_Scraper/
├── scrapping.py
├── book.csv
├── README.md
└── .gitignore
