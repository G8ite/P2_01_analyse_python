""" controller """
import csv

from scrap_categories import all_categories_details


# init data and header of csv file
data = ['product_page_url', 'universal_ product_code (upc)', 'title', 
'price_including_tax', 'number_available', 'product_description',
'category', 'review_rating', 'image_url']

info, names = all_categories_details('https://books.toscrape.com/index.html')

# with csv lib


for name in names :
    with open(f"{name}'.csv'", "w", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        for category in info :
            print(len(category))
            for book in category:
                print(len(book))
                writer.writerow(book)

