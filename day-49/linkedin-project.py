# HELPFUL LINKS
# 1) https://selenium-python.readthedocs.io/locating-elements.html#locating-by-name
# 2) https://www.selenium.dev/documentation/webdriver/actions_api/wheel/

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
# to install with success use python-dotenv in settings
from dotenv import load_dotenv

load_dotenv()

url = "https://www.linkedin.com/jobs/search/?currentJobId=3959115140&f_AL=true&geoId=105080838&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"


# closing pop-ups, which blocked the view
def footer_search():
    footer_ = driver.find_element(by=By.CSS_SELECTOR, value="div.artdeco-toast-item button.artdeco-toast-item__dismiss")
    if footer_:
        return True
    else:
        return False


# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

# Click Reject Cookies Button
try:
    time.sleep(2)
    reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
    reject_button.click()
except:
    pass

time.sleep(2)

try:
    sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Zaloguj się")
    sign_in_button.click()
except:
    try:
        sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='form p button')
        sign_in_button.click()
    except:
        sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='div.sign-in-modal button')
        driver.execute_script("arguments[0].click();", sign_in_button)


# Sign in
time.sleep(2)
try:
    email = driver.find_element(By.ID, value='username')
    email.send_keys(os.environ["MY_EMAIL"])
    password = driver.find_element(By.ID, value='password')
    password.send_keys(os.environ["PASSWORD"], Keys.ENTER)
except:
    try:
        email = driver.find_element(By.ID, value='session_key')
        email.send_keys(os.environ["MY_EMAIL"])
        password = driver.find_element(By.ID, value='session_password')
        password.send_keys(os.environ["PASSWORD"], Keys.ENTER)
    except:
        email = driver.find_element(By.ID, value='base-sign-in-modal_session_key')
        email.send_keys(os.environ["MY_EMAIL"])
        password = driver.find_element(By.ID, value='base-sign-in-modal_session_password')
        password.send_keys(os.environ["PASSWORD"], Keys.ENTER)


driver.get(url)
time.sleep(2)

nr_offers_ = driver.find_element(by=By.CSS_SELECTOR, value='div.jobs-search-results-list__subtitle span[dir="ltr"]')
pages = driver.find_elements(by=By.CSS_SELECTOR, value='ul.artdeco-pagination__pages li button')
nr_offers = nr_offers_.text
nr_offers = nr_offers.split(" ")[0]
o = 1

for page in pages:
    page.click()
    offers = driver.find_elements(by=By.CSS_SELECTOR, value="li.jobs-search-results__list-item")
    for offer in offers:
        print(f"offers {o}/{nr_offers}")
        try:
            time.sleep(2)
            while footer_search() is True:
                time.sleep(2)
                footer = driver.find_element(by=By.CSS_SELECTOR, value="div.artdeco-toast-item button.artdeco-toast-item__dismiss")
                footer.click()
        except:
            pass

        # idea taken from 2)
        ActionChains(driver) \
            .scroll_to_element(offer) \
            .perform()
        offer.click()
        time.sleep(2)

        save = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        save.click()

        follow = driver.find_element(by=By.CSS_SELECTOR, value='section div div button.follow')
        driver.execute_script("arguments[0].click();", follow)

        o = o+1

print("All offers saved and companies followed")

time.sleep(3)
driver.quit()
