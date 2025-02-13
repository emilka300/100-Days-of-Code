from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

number = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(number.text)

# clicking the anchor tag
# number.click()

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# find the "search" <input> by Name
search = driver.find_element(By.NAME, value='search')

# sending keyboard input to selenium
# Keys library is about all keys you have on keyboard
search.send_keys("Python", Keys.ENTER)

# closing browser - preferable
# driver.quit()

# closing tab in browser
# driver.close()