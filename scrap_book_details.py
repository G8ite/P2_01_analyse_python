import re

import requests
from bs4 import BeautifulSoup


def book_details(url:str)->list:
    """_This is a function who retrieve information of a book page

    Args:
        url (str): url of the page of a book

    Returns:
        detail (array): array that contains information about a book
    """
    # Stock the request response
    response = requests.get(url)

    # init an array
    details = []

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
        number = re.findall('\d+', information[5])

        # the description of the book
        article = soup.find('article', class_='product_page')
        if article.find('p', class_="") is None:
            description = "no description"
        else :
            # Used of "get_text" function because some description have simple quotes in double quotes
            # So We can't use ".text"
            description =  article.find('p', class_="").get_text()

        # the category of the book
        ul = soup.find('ul', class_='breadcrumb')
        categorys = ul.find_all('li')
        category = categorys[2].text.strip()

        # review rating
        p_icone = soup.find('p', class_='star-rating')
        tab_icone = p_icone.attrs.get('class')
        dico = {"One": "1", "Two": "2", "Three":"3", "Four":"4", "Five":"5"}
        rating = dico[tab_icone[1]]

        # image url
        div_img = soup.find('div', class_='item active')
        img = div_img.find('img')
        img_src = img['src']

        details.append(url)
        details.append(information[0])
        # print(title)
        details.append(title)
        details.append(information[3])
        details.append(number[0])
        details.append(description)
        details.append(category)
        details.append(rating)
        details.append(img_src)
        return details
