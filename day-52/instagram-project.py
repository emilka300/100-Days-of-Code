import os
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
# to install with success use python-dotenv in settings/project day-x/pythoninterpreter
load_dotenv()

url = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        # keeping browser active
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)

        # to approach website
        self.driver = webdriver.Edge(options=self.edge_options)

    def login(self):
        self.driver.get(url)

        time.sleep(2)
        cookies = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Odrzuć opcjonalne pliki cookie")]')
        cookies.click()

        time.sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, value='[name="username"]')
        username.send_keys(os.environ["NAME"])

        password = self.driver.find_element(By.CSS_SELECTOR, value='[name="password"]')
        password.send_keys(os.environ["PASSWORD"], Keys.ENTER)

        time.sleep(6)
        not_save = self.driver.find_element(By.XPATH, value='//div[contains(text(), "Nie teraz")]')
        not_save.click()

        try:
            time.sleep(2)
            cookies = self.driver.find_element(By.XPATH,
                                               value='//div[contains(text(), "Odrzuć opcjonalne pliki cookie")]')
            cookies.click()
            time.sleep(5)
        except:
            pass

    def find_followers(self):
        boxer_url = f"{url}/{os.environ['SIMILAR_ACCOUNT']}"
        self.driver.get(boxer_url)

        time.sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, value='[href="/boxer.lover/followers/"]')
        followers.click()

        time.sleep(3)
        # Scrolling through follower list. Since the popup is dynamic, nothing will be shown if not scroll down.
        # After scrolling our list will expand and we will have more people to follow.
        xpath_follower_list_1 = '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        xpath_follower_list_2 = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        try:
            scrollable_popup = self.driver.find_element(By.XPATH, xpath_follower_list_1)
        except NoSuchElementException:
            scrollable_popup = self.driver.find_element(By.XPATH, xpath_follower_list_2)
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(4)

    def follow(self):
        dialog = self.driver.find_element(By.XPATH,
                                          value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
        follow_buttons = dialog.find_elements(By.TAG_NAME, value='button')
        for button in follow_buttons:
            try:
                time.sleep(2)
                button.click()
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Anuluj")]')
                cancel.click()
                time.sleep(1)
                button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
