from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys("Emilia")

last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys("Wach")

email = driver.find_element(By.NAME, value='email')
email.send_keys("emilka300@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# closing browser - preferable
# driver.quit()

# closing tab in browser
# driver.close()