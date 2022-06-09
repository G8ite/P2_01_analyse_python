""" controller """
import csv

from scrap_categories import all_categories_details
from book_images import save_images


# init data and header of csv file
data = ['product_page_url', 'universal_ product_code (upc)', 'title', 
'price_including_tax', 'number_available', 'product_description',
'category', 'review_rating', 'image_url']
print('The process is launched, it may take several minutes')
info, names = all_categories_details('https://books.toscrape.com/index.html')

# with csv lib
for category in info :
    with open(f"{names[info.index(category)]}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data)
        for book in category:
            writer.writerow(book)

save_images("http://books.toscrape.com/")

