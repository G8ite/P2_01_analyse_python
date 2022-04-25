""" controller """
import csv
import math

from bs4 import BeautifulSoup
import requests

from scrap_books_for_catogory import category_details


# init data and header of csv file
data = [['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']]

# print(len(category_details("http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html")))

# Récupérer toutes les catégories depuis le menu de navigation
def all_categories_details(url):
    href = "http://books.toscrape.com/"
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text,"html5lib")
        ul = soup.find('ul', 'nav nav-list')
        li_array = ul.find_all('li')
        # Supprimer la première catégorie qui contient tous les livres
        li_array.pop(0)
        for i in li_array:
            a = i.find("a")
            print(a.text.strip())
            # print(a.attrs.get('href'))
            print(len(category_details(f"{href}{a.attrs.get('href')}")))

all_categories_details('https://books.toscrape.com/index.html')
# Pour chacune de ces catégories, récupérer leur nom et appeler category_details
# Mettre tout en forme dans un csv 


# with csv lib
# with open('data.csv', mode='w+') as file:
#     writer = csv.writer(file, delimiter=';')
#     # write data
#     for line in data:
#         writer.writerow(line)