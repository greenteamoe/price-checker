import requests
from bs4 import BeautifulSoup
import html5lib
import lxml
import urllib.request
from plyer import notification
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import sys
from urllib.request import urlopen
from plyer.utils import platform
from datetime import datetime
from colorama import init
from colorama import Fore, Back, Style

init()

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
}


count = 0
current_time = datetime.now().strftime('%d/%m/%Y at %H:%M')
print("made by " + Fore.LIGHTGREEN_EX + "@greenteamoe\n" + Style.RESET_ALL + "https://github.com/greenteamoe\n")
print("\nInitializing price checker bot..." "\n")
print(Style.BRIGHT + "OBS: Requests using SELENIUM, e.g, Terabyte, may take some time." + Style.RESET_ALL)
print("")
time.sleep(1.2)
print("Cycle started at: " + Fore.LIGHTRED_EX + current_time + Style.RESET_ALL)
print("")


def page_request_terabyte(url):
    CHROMEDRIVER = './chromedriver'

    URLterabyte = url

    title_class = 'tit-prod'
    price_a_vista_id = 'valVista'
    #price_parcelado_id = 'valParc'
    
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    options.headless = True
    options.add_argument('window-size=1920x1080')
    options.add_argument('--log-level=0')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(CHROMEDRIVER, options=options)
    driver.get(URLterabyte)


    try:
        title = driver.find_element_by_class_name(title_class).text
        converted_title = str(title[0:47])
        price_a_vista = driver.find_element_by_id(price_a_vista_id).text
        txtstrip_a_vista = price_a_vista.strip()
        converted_price_a_vista = float(txtstrip_a_vista[3:8])
        #price_parcelado = driver.find_element_by_class_name(price_parcelado_id).text
        #converted_price_parcelado = float(price_parcelado[3:8])
        if converted_price_a_vista < 1.400:
            notification.notify(
                title=converted_title,
                message="R${0} à vista\n\n{1}".format(converted_price_a_vista, URLterabyte),
                app_icon="images\lojaterabyteICO.ico",
                app_name="Terabyte",
                timeout=7
            )
            print(Fore.LIGHTGREEN_EX + "{0} [from terabyte] is available!".format(converted_title) + Style.RESET_ALL)
        elif converted_price_a_vista > 1.400:
            print(Fore.LIGHTRED_EX + converted_title, "[from terabyte] is unavailable (price is not matching)")

    except:
        title = driver.find_element_by_class_name(title_class).text
        converted_title = str(title[0:47])
        print(Fore.LIGHTRED_EX + converted_title, "[from terabyte] is unavailable (out of stock)" + Style.RESET_ALL)
        driver.quit()
        pass


def page_request_combatinfo(url):
    URLcombatinfo = url

    page = requests.get(URLcombatinfo, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    
    try:
        title = soup.find(id=None, attrs={'col-lg-8'}).get_text()
        converted_title = str(title[0:59])
        price_a_vista = soup.find('h4').get_text()  # search for the <h4> html tag
        txtstrip_a_vista = price_a_vista.strip()
        converted_price_a_vista = float(txtstrip_a_vista[3:8])
        if converted_price_a_vista < 1.400:
            notification.notify(
                title=converted_title,
                message="R${0} à vista\n\n{1}".format(converted_price_a_vista,
                                                                       URLcombatinfo),
                app_icon="images\combatinfoICO.ico",
                app_name="CombatInfo",
                timeout=7
            )
            print(Fore.LIGHTGREEN_EX + "{0} [from combatinfo] is available!".format(converted_title) + Style.RESET_ALL)
        elif converted_price_a_vista > 1.400:
            print(Fore.LIGHTRED_EX + converted_title, "[from combatinfo] is unavailable (price is not matching)")
    except:
        print(Fore.LIGHTRED_EX + "{0} [from combatinfo] is unavailable (out of stock)".format(converted_title))
        pass


def page_request_kabum(url):
    URLkabum = url

    page = requests.get(URLkabum, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    try:
        title = soup.find(id=None, attrs={'titulo_det'}).get_text()
        converted_title = str(title[0:59])
        price_a_vista = soup.find(id=None, attrs={'preco_desconto'}).get_text()
        txtstrip_a_vista = price_a_vista.strip()
        converted_price_a_vista = float(txtstrip_a_vista[3:8])
        price_parcelado = soup.find(id=None, attrs={'preco_normal'}).get_text()
        txtstrip_parcelado = price_parcelado.strip()
        converted_price_parcelado = float(txtstrip_parcelado[3:8])
        # juros = soup.find(id=None, attrs={'12x'}).get_text()
        # txtstrip_juros = juros.strip()
        # converted_juros = str(txtstrip_juros[0:41])
        if converted_price_a_vista < 1.400 or converted_price_parcelado < 1.700:
            notification.notify(
                title=converted_title,
                message="R${0} à vista\nR${1} parcelado\n\n{2}".format(converted_price_a_vista,
                                                                       converted_price_parcelado,
                                                                       URLkabum),
                app_icon="images\kabumICO.ico",
                app_name="Kabum",
                timeout=7
            )
            print(Fore.LIGHTGREEN_EX + "{0} [from kabum] is available!".format(converted_title) + Style.RESET_ALL)
        elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
            print(Fore.LIGHTRED_EX + converted_title, "[from kabum] is unavailable (price is not matching)")
    except:
        print(Fore.LIGHTRED_EX + "{0} [from kabum] is unavailable (out of stock)".format(converted_title))
        pass


def page_request_pichau(url):
    URLpichau = url

    page = requests.get(URLpichau, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")
    try:
        title = soup.find(id=None, attrs={'product title'}).get_text()
        converted_title = str(title[1:48])
        price_a_vista = soup.find(id=None, attrs={'price-boleto'}).get_text()
        converted_price_a_vista = float(price_a_vista[11:16])
        price_parcelado = soup.find(id=None, attrs={'price'}).get_text()
        converted_price_parcelado = float(price_parcelado[2:7])
        out_of_stock = soup.find(id=None, attrs={'stock unavailable'}).get_text()
        txtstrip_stock = out_of_stock.strip()
        

        if converted_price_a_vista < 1.400 or converted_price_parcelado < 1.700:
            if txtstrip_stock != 'Produto indisponível':
              notification.notify(
                  title=converted_title,
                  message="R${0} à vista\nR${1} parcelado\n\n{2}".format(converted_price_a_vista,
                                                                        converted_price_parcelado,
                                                                        URLpichau),
                  app_icon="images\pichauICO.ico",
                  app_name="Pichau",
                  timeout=7

              )
              print(Fore.LIGHTGREEN_EX + "{0} [from pichau] is available!".format(converted_title) + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + '{0} [from pichau] is unavailable (out of stock)'.format(converted_title))
        elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
            if txtstrip_stock == 'Produto indisponível':
                print(Fore.LIGHTRED_EX + "{0} [from pichau] is unavailable (out of stock)".format(converted_title))
        elif converted_price_a_vista > 1.400 or converted_price_parcelado > 1.700:
            print(Fore.LIGHTRED_EX + "{0} [from pichau] price is not matching")
    except:
        pass


count = 1

while True:
    # GTX 1660 - PCYES - combatinfo
    page_request_combatinfo(
    'https://www.combatinfo.com.br/placa-de-video-pcyes-geforce-gtx-1660-dual-oc-gddr5-6gb-pp1660oc19206g5/783/pr')
    # RX 580 - XFX - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/7611/placa-de-video-xfx-radeon-rx-580-8gb-oc-gts-xxx-edition-rx-580p8dfd6-gddr5')
    # RX 580 BIOSTAR - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/13987/placa-de-video-biostar-radeon-rx-580-8gb-gddr5-256-bit-va5805rv82-tbsrh-bs2')
    # RX 580 - GIGABYTE - terabyte
    #page_request_terabyte(
    #'https://www.terabyteshop.com.br/produto/7626/placa-de-video-gigabyte-radeon-rx-580-gaming-4g-gv-rx580gaming-4gd-4gb-gddr5')
    # RX 580 - ASUS - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/7926/placa-de-video-asus-radeon-rx-580-dual-oc-dual-rx580-o8g-8gb-gddr5')
    # RX 580 - SAPPHIRE - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/7862/placa-de-video-sapphire-radeon-rx-580-pulse-8gb-11265-05-20g-256bit-gddr5-chdmi-pci-exp')
    # RX 580 - AFOX - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/13050/placa-de-video-radeon-rx-580-8gb-gddr5-256bit-dual-fan-afrx580-8192d5h5')
    # RX 580 - GIGABYTE - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/7543/placa-de-video-gigabyte-radeon-rx-580-gaming-8g-gv-rx580gaming-8gd-8gb-gddr5')
    # GTX 1660 - ZOTAC - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/11237/placa-de-video-zotac-geforce-gtx-1660-dual-6gb-gddr5-192bit-zt-t16600f-10l')
    # GTX 1660 - GALAX - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/12759/placa-de-video-galax-geforce-gtx-1660-super-ex-1-click-oc-dual-6gb-gddr6-192bit-60srl7ds03es')
    #GTX 1660 - BIOSTAR - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/14471/placa-de-video-biostar-geforce-gtx-1660-dual-6gb-gddr5-192bit-vn1665xf69')
    #GTX 1660 - COLORFUL - terabyte
    page_request_terabyte(
    'https://www.terabyteshop.com.br/produto/12797/placa-de-video-colorful-geforce-gtx-1660-nb-6g-v-dual-6gb-gddr5-192bit')
    #GTX 1660 - GIGABYTE - terabyte
    page_request_terabyte(      
    'https://www.terabyteshop.com.br/produto/10984/placa-de-video-gigabyte-geforce-gtx-1660-oc-6gb-gddr5-pci-exp-gv-n1660oc-6gd')
    # GTX 1660 - PCYES - terabyte
    page_request_terabyte(
        'https://www.terabyteshop.com.br/produto/11852/placa-de-video-pcyes-geforce-gtx-1660-dual-6gb-gddr5-192bit-pa166019206g5')
    # GTX 1660 - GALAX - terabyte
    page_request_terabyte(
        'https://www.terabyteshop.com.br/produto/10905/placa-de-video-galax-geforce-gtx-1660-6gb-1-click-oc-60srh7dsy91c-gddr5-pci-exp')
    # GTX 1660 - GALAX - pichau
    page_request_pichau(
        'https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-1660-6gb-gddr5-1-click-oc-192-bit-60srh7dsy91c')
    # GTX 1660 - GIGABYTE - pichau
    page_request_pichau(
        'https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-gigabyte-geforce-gtz-1660-6gb-gddr5-oc-192-bit-gv-n1660oc-6gd')
    # RX 580 - GIGABYTE - pichau
    page_request_pichau(
        'https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-gigabyte-radeon-rx-580-8gb-gddr5-windforce-256-bit-gv-rx580gaming-8gd')
    # GTX 1660 - PCyes - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/130938/placa-de-v-deo-pcyes-nvidia-geforce-gtx-1660-oc-dual-fan-6gb-gddr5-192-bits-graffiti-series-ppoc166019206g5')
    # GTX 1660 - Zotac - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/100947/placa-de-v-deo-zotac-nvidia-geforce-gtx-1660-twin-fan-6gb-gddr5-zt-t16600f-10l')
    # GTX 1660 - EVGA - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/100930/placa-de-v-deo-evga-nvidia-geforce-gtx-1660-xc-ultra-gaming-6gb-gddr5-06g-p4-1167-kr')
    # GTX 1660 - Gigabyte - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/101039/placa-de-v-deo-gigabyte-nvidia-geforce-gtx-1660-oc-6g-gddr5-gv-n1660oc-6gd')
    # GTX 1660 - Galax - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/101268/placa-de-v-deo-galax-nvidia-geforce-gtx-1660-1-click-oc-6gb-gddr5-60srh7dsy91c')
    # GTX 1660 - EVGA - kabum
    #page_request_kabum(
    #    'https://www.kabum.com.br/produto/102130/placa-de-v-deo-evga-nvidia-geforce-gtx-1660-sc-ultra-gaming-6gb-gddr5-06g-p4-1067-kr')

    print()
    print(Style.RESET_ALL + "Next cycle starting in 14 hours.")
    print()
    time.sleep(60 * 60 * 14)
    count = count + 1
    print()
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M')
    print("Cycle restarted at: " + Fore.LIGHTRED_EX + current_time + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "Total price-check cycles: {0}\n".format(count) + Style.RESET_ALL)
