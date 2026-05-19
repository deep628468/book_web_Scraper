from bs4 import BeautifulSoup
import requests
import csv

url = "https://99bookstores.com/"

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

books = soup.find_all('div', class_='card-wrapper product-card-wrapper underline-links-hover')

file = open("books.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["Book name", "Price", "Rating", "Publisher", "Link"])

for book in books[:5]:

    # Book name
    name = book.find('h3')
    book_name = name.text.strip() if name else "Not available"

    # Price
    price = book.find('span', class_='price-item')
    book_price = price.text.strip() if price else "Not available"

    # Rating
    rating = book.find('span', class_='rating')
    book_rating = rating.text.strip() if rating else "No rating"

    # Book link
    link_tag = book.find('a', href=True)
    book_link = "https://99bookstores.com" + link_tag['href'] if link_tag else "No link"

    # Publisher
    if link_tag:
        book_page = requests.get(book_link).text
        book_soup = BeautifulSoup(book_page, "lxml")

        publisher = book_soup.find('div', class_='product_vendor')
        book_publisher = publisher.text.strip() if publisher else "Not available"
    else:
        book_publisher = "Not available"

    # Write row
    writer.writerow([
        book_name,
        book_price,
        book_rating,
        book_publisher,
        book_link
    ])

    print("Saved:", book_name)

file.close()
print("Data saved to books.csv")