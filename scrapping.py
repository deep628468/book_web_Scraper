from bs4 import BeautifulSoup
import requests
import csv
import time
from urllib.parse import urljoin

url = "https://99bookstores.com/"

def get_page(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text

        except requests.RequestException as error:
            print(f"Request failed (attempt {attempt}/{retries}): {error}")

            if attempt < retries:
                time.sleep(2)

    print(f"Skipping URL after {retries} failed attempts: {url}")
    return None


html_text = get_page(url)

if html_text is None:
    print("Failed to load the main page.")
    exit()


soup = BeautifulSoup(html_text, "lxml")
books = soup.find_all(
    "div",
    class_="card-wrapper product-card-wrapper underline-links-hover"
)

seen_urls = set()
failed_requests = 0
successful_records = 0


with open("book.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Book name",
        "Price",
        "Rating",
        "Availability",
        "link"
    ])

    for book in books:
        # Book name
        name = book.find("h3")
        book_name = name.text.strip() if name else "Not available"

        # Price
        price = book.find("span", class_="price-item")
        book_price = price.text.strip() if price else "Not available"

        # Rating
        rating = book.find("span", class_="rating star")
        book_rating = rating.text.strip() if rating else "No rating"

        # Book link
        link_tag = book.find("a", href=True)

        if not link_tag:
            continue

        book_link = urljoin(url, link_tag["href"])

        if book_link in seen_urls:
            continue

        seen_urls.add(book_link)

        # Open individual book page
        book_page = get_page(book_link)

        if book_page is None:
            failed_requests += 1
            continue

        book_soup = BeautifulSoup(book_page, "lxml")

        # Availability
        availability = book_soup.find(
            "span",
            class_="price__badge-sold-out"
        )

        book_availability = (
            availability.text.strip()
            if availability
            else "Available"
        )

        writer.writerow([
            book_name,
            book_price,
            book_rating,
            book_availability,
            book_link
        ])

        successful_records += 1
        print("Saved:", book_name)


print("Data saved to book.csv")
print("Failed product requests:", failed_requests)
print("Successfully saved:", successful_records)
