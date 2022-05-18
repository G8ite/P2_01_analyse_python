""" controller """
import csv

from scrap_categories import all_categories_details


# init data and header of csv file
data = ['product_page_url', 'universal_ product_code (upc)', 'title', 
'price_including_tax', 'number_available', 'product_description',
'category', 'review_rating', 'image_url']

info, names = all_categories_details('https://books.toscrape.com/index.html')

# Pour chacune de ces catégories, recup leur nom et appeler category_details
# Mettre tout en forme dans un csv 
# with csv lib

for category in info :
    for name in names :
        with open(f"{name}'.csv'", "w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            for book in category:
                writer.writerow(book)

# with open('data.csv', 'w', encoding="utf-8") as file:
#     writer = csv.writer(file, delimiter=',')
#     # write data
#     writer.writerow(data)
#     for line in info:
#         for book in line:
#             writer.writerow(book)
