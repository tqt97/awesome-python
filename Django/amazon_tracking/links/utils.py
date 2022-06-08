import requests
import lxml
from bs4 import BeautifulSoup


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup.prettify().encode('cp1252', errors='ignore'))

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price
