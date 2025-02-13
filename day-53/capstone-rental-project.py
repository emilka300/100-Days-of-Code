# FINAL RESULTS :
# https://docs.google.com/forms/d/1UM5cjqu1G4I4Ge0vCM4wIp_OGIKb206QQiIxDGNG6Iw/edit#responses
# https://docs.google.com/spreadsheets/d/1RXlmdZenWS62YiT7YUZ_H3d0A1Hk8CHoMTWbrnbCez4/edit?resourcekey=&gid=2138944155#gid=2138944155

import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv

# to install with success use python-dotenv in settings/project day-x/pythoninterpreter
load_dotenv()

url = "https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

links = []
prices = []
addresses = []

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

offers = soup.select("ul.List-c11n-8-84-3-photo-cards li")
for offer in offers:

    # resourcing href
    offer_href = offer.a
    if offer_href is not None:
        links.append(offer_href['href'])
        # print(offer_href['href'])

    # resourcing price
    offer_price = offer.span
    if offer_price is not None:
        price = offer_price.text
        price = price.replace("+", "")
        price = price.replace("/mo", "")
        price = price.replace(" 1bd", "")
        price = price.replace(" 1 bd", "")
        prices.append(price)
        # print(price)

    # resourcing address
    offer_address = offer.address
    if offer_address is not None:
        addresses.append(offer_address.text.strip())
        # print(offer_address.text.strip())

# print(links)
# print(prices)
# print(addresses)

# FILLING THE FORM

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(os.environ["SHEET_ENDPOINT"])

nr_of_offers = len(links)

for _ in range(0, nr_of_offers):
    try:
        input_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_address.send_keys(addresses[_])

        input_price = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_price.send_keys(prices[_])

        input_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_link.send_keys(links[_])

        send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        send_button.click()

        next_offer = driver.find_element(By.LINK_TEXT, "Prześlij kolejną odpowiedź")
        next_offer.click()

    except ElementClickInterceptedException:
        no_logging = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/div[3]/div[1]')
        no_logging.click()

        time.sleep(2)
        send_button = driver.find_element(By.CSS_SELECTOR, value="div [role='button']")
        send_button.click()

driver.quit()
