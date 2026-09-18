import requests
from bs4 import BeautifulSoup
import csv

# Target website
URL = "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"

# Page request
page = requests.get(URL)

# Check if the request was successful
if page.status_code == 200:

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.content, "html.parser")

    # List to save all products
    all_products = []

    # Retrieve all products
    products = soup.select("div.thumbnail")

    # Loop through each product
    for product in products:

        # product name
        name = product.select("h4 > a")[0].text.strip()

        # Product description (dibersihkan dari enter/newline agar aman di Excel)
        description = product.select("p.description")[0].text.strip().replace("\n", " ").replace("\r", " ")

        # Product price
        price = product.select("h4.price")[0].text.strip()

        # Product reviews
        reviews = product.select("div.ratings")[0].text.strip()

        # Image URL
        image = product.select("img")[0].get("src")

        # Store in a dictionary
        all_products.append(
            {
                "name": name,
                "description": description,
                "price": price,
                "reviews": reviews,
                "image": image
            }
        )

    # CSV column names
    keys = all_products[0].keys()

    # Save to CSV
    with open(
        "C:/PORTOFOLIO/python-portfolio/WEB-SCRAPING/product-market-insight/data/products.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as output_file:

        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_products)

    print("===================================")
    print("Scraping completed successfully!")
    print(f"Total products saved: {len(all_products)}")
    print("File saved to: data/products.csv")
    print("===================================")

else:
    print("Failed to access website.")
    print("Status code:", page.status_code)