
from bs4 import BeautifulSoup as bs
import requests
import re
from pathlib import Path

def save_images(url: str):
    """ Function that creates an images folder that retrieves all images from the Books to Scrap catalog

    Args:
        url (str):
    """

    page_url = [f'http://books.toscrape.com/catalogue/page-{i}.html' for i in range(1, 51)]

    folder = Path("data/images/")
    folder.mkdir(parents=True, exist_ok=True)

    for links in page_url:
        result = requests.get(links)
        content = result.text
        content_page = bs(content, 'html.parser')
        images = content_page.find_all('img')     

        for image in images:
            name = image['alt']
            href =(url + image['src'])
            name = re.sub(r"['\"[\]{}()?\-\+*&é;:./!,$=#]*","",name)
            with open((f"data\images\{name}.jpg"), 'wb') as f:
                f.write(requests.get(href).content)
