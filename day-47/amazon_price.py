from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

url = "https://www.amazon.pl/adapter-ZESKRIS-Multiport-czytnikiem-urz%C4%85dze%C5%84/dp/B09MJYT2LN/ref=sr_1_1_sspa?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=YC62A4C3RT42&dib=eyJ2IjoiMSJ9.opYAn-hw9lDKz_6maPZdnI56cyaH6mk2kVmSlZ0o8GV3bjqSIUOlzpqnPl8GSKgr2t2CxTGcgYAxT_69dcRLl-hAH0nyZNTvAPL4749SjYML0AVrveZi9ZNa413sUIggMyG8KkTJTa4IeL3gj8BZA-IrbXt5k5tj8bkEDyFg7qogItGdTh5bpUvmmFPe1wLcV-ePiHjW2_s5An5-7J5yRbcyiMSVqFF_1cN1rvV2b_X_lcW6FFZGITOCsVpnpT6QYaqF5YG6J-wL6fO3UZEdRMsWQ0N-nV8JlUP7CBu7Bkc.pmeH_FvGcQLCwlZeNyd8ucvWNNRPQM2Gbz3CqMRk6SI&dib_tag=se&keywords=adapter%2Busb%2Bc%2Bdo%2Bmacbook%2Bhdmi&qid=1730240717&sprefix=adapter%2Busb%2Bc%2Bdo%2Bmacbook%2Bhdmi%2Caps%2C109&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
load_dotenv()
header = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
          "Accept-Language":"pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"}


response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.select_one("#productTitle").getText().strip()
print(title)
# print(soup.prettify())
price_whole = soup.select_one(".a-price-whole").getText().strip(",")
# print(price_whole)
price_fraction = soup.select_one(".a-price-fraction").getText().strip()
# print(price_fraction)

price = float(f"{price_whole}.{price_fraction}")
# print(price)

if price <= 40:
    # Then send me an email to tell me to look up.
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs="emilka300@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\nPrice of {title} is now {price}!".encode('utf-8')
        )

