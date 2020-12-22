import requests
from bs4 import BeautifulSoup
import html5lib
import lxml
from plyer import notification
import re
import json
import time
from plyer.utils import platform

headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }


def page_request_kabum(url):
    URLkabum = url

    page = requests.get(URLkabum, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")
    
    try:
        title = soup.find(id=None, attrs={'titulo_det'}).get_text()
        converted_title = str(title[0:57])
        price_a_vista = soup.find(id=None, attrs={'preco_desconto'}).get_text()
        txtstrip_a_vista = price_a_vista.strip()
        converted_price_a_vista = float(txtstrip_a_vista[3:8])
        price_parcelado = soup.find(id=None, attrs={'preco_normal'}).get_text()
        txtstrip_parcelado = price_parcelado.strip()
        converted_price_parcelado = float(txtstrip_parcelado[3:8])
        juros = soup.find(id=None, attrs={'12x'}).get_text()
        txtstrip_juros = juros.strip()
        converted_juros = str(txtstrip_juros[0:41])
        if converted_price_a_vista > 1.400 or converted_price_parcelado < 1.700:
            notification.notify(
                title=converted_title,
                message="R${0} à vista\nR${1} parcelado\n\n{2}".format(converted_price_a_vista, converted_price_parcelado,
                                                                    URLkabum),
                app_icon= "images\kabumICO.ico",
                app_name= "Kabum",
                timeout=7
            )
        elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
            print(converted_title, converted_price_parcelado, converted_price_a_vista)
    except:
        print("{0} is unavailable.".format(title))
        pass

    


def page_request_pichau(url):
    URLpichau = url

    page = requests.get(URLpichau, headers=headers)  
    soup = BeautifulSoup(page.content, "lxml")  

    title = soup.find(id=None, attrs={'product title'}).get_text()  
    converted_title = str(title[0:48])
    price_a_vista = soup.find(id=None, attrs={'price-boleto'}).get_text()  
    converted_price_a_vista = float(price_a_vista[11:16])
    price_parcelado = soup.find(id=None, attrs={'price'}).get_text()
    converted_price_parcelado = float(price_parcelado[2:7])
    # title_price_parcelado = soup.find(id=None, attrs={'price-installments'}).get_text()

    if converted_price_a_vista > 1.400 or converted_price_parcelado < 1.700:
        notification.notify(
            title=converted_title,
            message="R${0} à vista\nR${1} parcelado\n\n{2}".format(converted_price_a_vista, converted_price_parcelado,
                                                                   URLpichau),
            app_icon= "images\pichauICO.ico",
            app_name= "Pichau",
            timeout=7
        )
    elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
        print(converted_title, converted_price_parcelado, converted_price_a_vista)

while True:
    # GALAX - pichau
  page_request_pichau('https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-1660-6gb-gddr5-1-click-oc-192-bit-60srh7dsy91c')
    # GIGABYTE - pichau
  page_request_pichau('https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-gigabyte-geforce-gtz-1660-6gb-gddr5-oc-192-bit-gv-n1660oc-6gd')
    # PCyes - kabum
  page_request_kabum('https://www.kabum.com.br/produto/130938/placa-de-v-deo-pcyes-nvidia-geforce-gtx-1660-oc-dual-fan-6gb-gddr5-192-bits-graffiti-series-ppoc166019206g5')
    # Zotac - kabum
  page_request_kabum('https://www.kabum.com.br/produto/100947/placa-de-v-deo-zotac-nvidia-geforce-gtx-1660-twin-fan-6gb-gddr5-zt-t16600f-10l')
    # EVGA - kabum
  page_request_kabum('https://www.kabum.com.br/produto/100930/placa-de-v-deo-evga-nvidia-geforce-gtx-1660-xc-ultra-gaming-6gb-gddr5-06g-p4-1167-kr')
    # Gigabyte - kabum
  page_request_kabum('https://www.kabum.com.br/produto/101039/placa-de-v-deo-gigabyte-nvidia-geforce-gtx-1660-oc-6g-gddr5-gv-n1660oc-6gd')
    # Galax - kabum
  page_request_kabum('https://www.kabum.com.br/produto/101268/placa-de-v-deo-galax-nvidia-geforce-gtx-1660-1-click-oc-6gb-gddr5-60srh7dsy91c')
    # EVGA - kabum
  page_request_kabum('https://www.kabum.com.br/produto/102130/placa-de-v-deo-evga-nvidia-geforce-gtx-1660-sc-ultra-gaming-6gb-gddr5-06g-p4-1067-kr')
  time.sleep(60 * 60 * 24)
