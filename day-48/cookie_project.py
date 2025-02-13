from selenium import webdriver
from selenium.common import NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://orteil.dashnet.org/experiments/cookie/"

game_on = True

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

cookie = driver.find_element(By.ID, value="cookie")

start = time.time()
timestamp = time.time()
timeout = time.time() + 60*5
n = 1

try:
    while time.time() < timeout:
        cookie.click()
        if time.time() > start + n:
            options = []
            money = driver.find_element(By.ID, value='money')
            money = money.text.replace(",", "")
            store = driver.find_elements(By.CSS_SELECTOR, "div #store div b")
            store.pop()
            for option in store:
                option_whole = option.text
                option_value = option_whole.split("-")[1]
                option_name = option_whole.split("-")[0]
                option_name = option_name.strip()
                option_value = option_value.replace(",", "")
                option_value = option_value.strip()
                if int(option_value) <= int(money):
                    options.append(option_name)
            option_name_chosen = options[-1]
            option_chosen = driver.find_element(By.ID, value=f"buy{option_name_chosen}")
            option_chosen.click()
            start = time.time()
        if time.time() > timestamp + 3 * n:
            n = 1.1 * n
    print(driver.find_element(By.ID, value='cps').text)
except NoSuchWindowException:
    print("Browser window closed. Exiting...")

driver.quit()