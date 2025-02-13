from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.amazon.pl/adapter-ZESKRIS-Multiport-czytnikiem-urz%C4%85dze%C5%84/dp/B09MJYT2LN/ref=sr_1_1_sspa?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=YC62A4C3RT42&dib=eyJ2IjoiMSJ9.opYAn-hw9lDKz_6maPZdnI56cyaH6mk2kVmSlZ0o8GV3bjqSIUOlzpqnPl8GSKgr2t2CxTGcgYAxT_69dcRLl-hAH0nyZNTvAPL4749SjYML0AVrveZi9ZNa413sUIggMyG8KkTJTa4IeL3gj8BZA-IrbXt5k5tj8bkEDyFg7qogItGdTh5bpUvmmFPe1wLcV-ePiHjW2_s5An5-7J5yRbcyiMSVqFF_1cN1rvV2b_X_lcW6FFZGITOCsVpnpT6QYaqF5YG6J-wL6fO3UZEdRMsWQ0N-nV8JlUP7CBu7Bkc.pmeH_FvGcQLCwlZeNyd8ucvWNNRPQM2Gbz3CqMRk6SI&dib_tag=se&keywords=adapter%2Busb%2Bc%2Bdo%2Bmacbook%2Bhdmi&qid=1730240717&sprefix=adapter%2Busb%2Bc%2Bdo%2Bmacbook%2Bhdmi%2Caps%2C109&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

price_zl = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_gr = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_zl.text}.{price_gr.text}")

# closing browser - preferable
driver.quit()

# closing tab in browser
# driver.close()
