""" controller """
import csv
import math

from bs4 import BeautifulSoup
import requests

from scrap_books_for_catogory import category_details


# init data and header of csv file
data = [['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']]

print(len(category_details("http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html")))

# Récupérer toutes les catégories depuis le menu de navigation
# Pour chacune de ces catégories, récupérer leur nom et appeler category_details
# Mettre tout en forme dans un csv 
# call the function who add book details of book page

# with csv lib
# with open('data.csv', mode='w+') as file:
#     writer = csv.writer(file, delimiter=';')
#     # write data
#     for line in data:
#         writer.writerow(line)