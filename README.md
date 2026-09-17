99Bookstores Web Scraper

A Python web scraper that extracts book/product information from 99Bookstores and stores the collected data in a CSV file.
Features
Scrapes book/product information from 99Bookstores.
Extracts book name, price, rating, availability, and product URL.
Removes duplicate products using unique product URLs.
Handles missing product fields with fallback values.
Uses request timeouts and retry logic for failed HTTP requests.
Skips individual products when all request attempts fail instead of stopping the entire scraper.
Saves the collected data to book.csv.

Technologies Used

Python 3
Requests
BeautifulSoup
lxml
CSV

Data Collected

The scraper stores the following fields:
Field	Description
Book name	Name of the book/product
Price	Product price
Rating	Product rating
Availability	Availability status
link	Product page URL

How It Works

The scraper follows these steps:
Sends an HTTP request to the 99Bookstores page.
Parses the HTML using BeautifulSoup with the lxml parser.
Identifies product cards on the page.
Extracts the book name, price, rating, and product URL.
Uses a set to prevent duplicate product URLs.
Requests each individual product page to determine availability.
Retries failed HTTP requests up to three times.
Skips a product if its page cannot be retrieved after all retry attempts.
Writes the successfully processed records to book.csv.
Error Handling
The scraper uses a reusable request function with:
A 10-second request timeout.
Up to 3 attempts for a failed request.
A 2-second delay between retry attempts.
HTTP status validation using raise_for_status().
Handling of requests.RequestException.
If an individual product request continues to fail after all retries, that product is skipped and the scraper continues processing the remaining products.

Project Structure

Web Scrapping/
├── scrapping.py
├── book.csv
├── README.md
└── .gitignore

How to Run
Clone the repository and navigate to the project directory.
Install the required Python packages:
pip install requests beautifulsoup4 lxml
Run the scraper:
python3 scrapping.py
The extracted data will be saved to:
book.csv
Data Verification
The current verified dataset contains:
100 product records
100 unique product URLs
0 duplicate URLs
0 empty fields
0 failed product requests during the verification run
These results were obtained from the current scraper run and CSV validation.

Limitations

The scraper depends on the current HTML structure and CSS classes used by 99Bookstores.
Changes to the website structure may require updates to the selectors.
Availability is determined from the product page's current HTML.
The scraper is intended as a learning and portfolio project rather than a general-purpose scraping framework.
