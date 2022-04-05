#import libs
import requests
from bs4 import BeautifulSoup
import re

# url to connect
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

# Stock the request response
response = requests.get(url)

# Check if there are not fail
if response.ok : # status = 200

    # html
    soup = BeautifulSoup(response.text, "html5lib")

    # array informations about the book
    table = soup.find('table', class_='table table-striped')

    # informations about the book
    tds = table.find_all('td')

    # table that will contain the information collected
    information = []

    # html table data processing
    for td in tds :
        information.append(td.text)

    # the book's title
    div = soup.find('div', class_='col-sm-6 product_main')
    title = div.find('h1').text
    
    # format number available
    number = re.findall(r'-?\d+\.?\d*', information[5])

    # the description of the book
    article = soup.find('article', class_='product_page')
    description =  article.find('p', class_="").text

    # the category of the book
    ul = soup.find('ul', class_='breadcrumb')
    categorys = ul.find_all('li')
    category = categorys[2].text.strip()

    # review rating
    pIcone = soup.find('p', class_='star-rating')
    tabIcone = pIcone.attrs.get('class')
    if tabIcone[1] == "One" :
        rating = '1'
    elif tabIcone[1] == "Two":
        rating = '2'
    elif tabIcone[1] == "Three":
        rating='3'
    elif tabIcone[1] == "Four":
        rating='4'
    elif tabIcone[1]== "Five":
        rating='5'
        
    # image url
    divImg = soup.find('div', class_='item active')
    img = divImg.find('img')
    imgSrc = img['src']

entetes = ['product_page_url', 'universal_ product_code (upc)', 'title',
  'price_including_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

valeurs = [url, information[0], title, information[3], number[0], description, category, rating, imgSrc]

file = open('monFichier.csv', 'w')
ligneEntete = ";".join(entetes)
file.write(ligneEntete+"\n")
for valeur in valeurs:
    ligne = str(valeur) + ";"
    file.write(ligne)

file.close()