from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org"

# keeping browser active
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# to approach website
driver = webdriver.Edge(options=edge_options)
driver.get(url)

# expected final_dict format: {0: {'time': '2020-08-28', 'name': 'PyCon JP 2020'}, 1: ..}
time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget div ul li time')
event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget div ul li a')

final_dict = {}
semi_dict = {}
for n in range(0, len(time)):
    final_dict[n] = {
        'time': event_name[n].text,
        'name': event_name[n].text
    }

print(final_dict)

# closing browser - preferable
driver.quit()

# closing tab in browser
# driver.close()
