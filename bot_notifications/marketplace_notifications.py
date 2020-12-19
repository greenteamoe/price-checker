import requests
from bs4 import BeautifulSoup
import html5lib
import lxml
from plyer import notification
import re
import json
import time


# Example below:

def page_request_pichau():
    URLpichau = 'https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-1660-6gb-gddr5-1-click-oc-192-bit-60srh7dsy91c'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }

    page = requests.get(URLpichau, headers=headers)  # pichau

    soup = BeautifulSoup(page.content, "lxml")  # pichau

    title = soup.find(id=None, attrs={'product title'}).get_text()  # pichau
    converted_title = str(title[0:48])
    price_a_vista = soup.find(id=None, attrs={'price-boleto'}).get_text()  # pichau
    converted_price_a_vista = float(price_a_vista[11:16])
    price_parcelado = soup.find(id=None, attrs={'price'}).get_text()
    converted_price_parcelado = float(price_parcelado[2:7])
    # title_price_parcelado = soup.find(id=None, attrs={'price-installments'}).get_text()

    if converted_price_a_vista > 1.400 or converted_price_parcelado < 1.700:
        notification.notify(
            title=converted_title,
            message="R${0} à vista\nR${1} parcelado\n\n{2}".format(converted_price_a_vista, converted_price_parcelado,
                                                                   URLpichau),
            timeout=7
        )
    elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
        print(converted_title, converted_price_parcelado, converted_price_a_vista)
        

    while True:
        time.sleep(60 * 60 * 24)
        page_request_pichau()

time.sleep(60 * 60 * 24)
page_request_pichau()
