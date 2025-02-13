import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
# to install with success use python-dotenv in settings/project day-x/pythoninterpreter
load_dotenv()

url = "https://twitter.com/"
url_speed_test = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        # keeping browser active
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)

        # to approach website
        self.driver = webdriver.Edge(options=self.edge_options)
        self.chwd = self.driver.window_handles
        self.old_window = ""
        self.new_window = ""
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url_speed_test)
        self.old_window = self.driver.current_window_handle
        reject_cookie = self.driver.find_element(By.ID, 'onetrust-reject-all-handler')
        reject_cookie.click()
        go = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go.click()
        time.sleep(36)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        #print(f"down: {self.down}\nup:{self.up}")

    def tweet_at_provider(self):
        self.driver.get(url)

        # NOT NEEDED BUT INTERESTING
        # dealing with 2 windows -> closing old one (speed_test)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.number_of_windows_to_be(len(self.chwd) + 1))
        # self.new_window = self.driver.current_window_handle
        # self.driver.switch_to.window(self.old_window)
        # self.driver.close()
        # self.driver.switch_to.window(self.new_window)

        # logging in
        time.sleep(4)
        log_in = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a')
        log_in.click()

        time.sleep(2)
        email = self.driver.find_element(By.CSS_SELECTOR, value='[autocomplete="username"]')
        email.send_keys(os.environ["TWITTER_EMAIL"], Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.CSS_SELECTOR, value='[autocomplete="current-password"]')
        password.send_keys(os.environ["TWITTER_PASSWORD"], Keys.ENTER)

        # writing complaint
        complaint = f'Hey Internet Provider, why is my internet speed\n{self.down}down/{self.up}up ' \
                    f'when I pay for {os.environ["PROMISED_DOWN"]}down/{os.environ["PROMISED_UP"]}up?'
        time.sleep(4)
        post_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_box.send_keys(complaint)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
