""" controller """
import csv

from scrap_categories import all_categories_details


# init data and header of csv file
data = [['product_page_url', 'universal_ product_code (upc)', 'title', 
'price_including_tax', 'number_available', 'product_description',
'category', 'review_rating', 'image_url']]

info = all_categories_details('https://books.toscrape.com/index.html')

# Pour chacune de ces catégories, recup leur nom et appeler category_details
# Mettre tout en forme dans un csv 
# with csv lib
with open('data.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    # write data
    for line in info:
        writer.writerow(data)
        writer.writerow(line)
