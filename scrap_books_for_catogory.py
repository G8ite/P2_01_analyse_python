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
        url (_str_): url of the page of a category

    Returns:
        list: information about books pages for a category
    """
    response = requests.get(url)

    if response.ok:
        
        soup = BeautifulSoup(response.text,"html5lib")
        form = soup.find('form', 'form-horizontal')
        # Retrieve the number of books per page
        article_number_info = form.find_all('strong')
        per_page = int(article_number_info[2].text)
        books_number = int(article_number_info[0].text)
        article_number = math.ceil(books_number/per_page)
        # print(books_number)
        # print(per_page)
        # print(article_number)
       
        return article_number
    

def category_details(url:str)->list:
    """Function that returns all books for a category

    Args:
        url (str): url of the category

    Returns:
        list: all books for a category
    """
    pages_number = category_pages(url)
    books_details = books_url(url)
    book_details_category = []
    for n in range(1,pages_number+1):
        print(n)
        print(pages_number)
        url.replace("index.html",f"'page-'{n}'.html'" )

        books_details = books_url(url)
        print(url)
        print(books_details)

        for i in books_details:
            book_details_category.append(book_details(i))

    return book_details_category

        

# Le fait que ça se fasse en 2 fonction est problématique, elles ont 2 fois la même utilité, ça ne va pas, il faut les repenser
# def category_details(url:str)->list:
#     """_This is a function who retrieve information of a book for one page of a category

#     Args:
#         url (_str_): url of the page of a category

#     Returns:
#         category (_str_): array that contains informations about books for a category
#     """
#     response = requests.get(url)

#     if response.ok:
#         soup = BeautifulSoup(response.text,"html5lib")
#         section = soup.find('section')
#         div = section.find_all('div', 'image_container')
#         links_array = []
#         begin_path = "../../../"
#         for i in div :
#             href = i.find('a').attrs.get('href')
#             href = href.replace(begin_path,"")
#             links_array.append(href)

#         href_begin = "http://books.toscrape.com/catalogue/"
#         category = []
#         for item in links_array :
#             category.append(book_details(f"{href_begin}{item}"))
#         return category
#     else:
#         logger.error("Scrapping aborted. Cannot access to the website")
#         return None


        
