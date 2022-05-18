import logging
import math

import requests
from bs4 import BeautifulSoup

from scrap_book_details import book_details

logger = logging.getLogger()

def books_url(url:str)->list:
    """This is a function who reformat url from books in page of category

    Args:
        url (str): url who need to be reformat

    Returns:
        list: array that contains all url of books in page of category
    """
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text,"html5lib")
        section = soup.find('section')
        div = section.find_all('div', 'image_container')
        links_array = []
        href_begin = "http://books.toscrape.com/catalogue/"
        begin_path = "../../../"
        for i in div :
            href = i.find('a').attrs.get('href')
            href = href.replace(begin_path,"")
            link = f"{href_begin}{href}"
            links_array.append(link)
        return links_array
    else:
        logger.error("Scrapping aborted. Cannot access to the website")
        return None

def category_pages(url:str)->list:
    """_This function checks the number of pages to consult for a category and call another function category_details

    Args:
        url (str): url of the page of a category

    Returns:
        list: information about books pages for a category
    """
    response = requests.get(url)

    if response.ok:
        
        soup = BeautifulSoup(response.text,"html5lib")
        form = soup.find('form', 'form-horizontal')
        # Retrieve the number of books per page
        article_number_info = form.find_all('strong')
        # per_page = int(article_number_info[2].text)
        books_number = int(article_number_info[0].text)
        article_number = math.ceil(books_number/20)
       
        return article_number
    

def category_details(url:str)->list:
    """Function that returns all books for a category

    Args:
        url (str): url of the category

    Returns:
        list: all books for a category
    """
    pages_number = category_pages(url)
    book_details_category = []

    url = url.replace("index.html","")

    for n in range(1,2):

        new_url = f"{url}page-{n}.html"

        # if there is only one page from a category, there is no "page-1" so we keep "index.html"
        if n == 1 :
            new_url = url
        
        books_details = books_url(new_url)
        for i in books_details:
            book_details_category.append(book_details(i))
            
    return book_details_category