""" all categories """
from typing import final
import requests
from bs4 import BeautifulSoup

from scrap_books_for_catogory import category_details


def all_categories_details(url):
    """_summary_

    Args:
        url (_type_): _description_
    """
    href = "http://books.toscrape.com/"
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text,"html5lib")
        ul_nav = soup.find('ul', 'nav nav-list')
        li_ul = ul_nav.find('li')
        li_array = li_ul.find_all('li')
        references_array = []
        category_names=[]
        for category_link in li_array:
            a_link = category_link.find("a")
            category_names.append(a_link.text.strip())
            references_array.append(category_details(f"{href}{a_link.attrs.get('href')}"))
        return (references_array, category_names)