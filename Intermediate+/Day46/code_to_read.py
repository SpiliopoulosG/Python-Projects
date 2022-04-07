
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("E:\GitHub\Python-Projects\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.python.org/")
#
# events = {}
#
# css_selector = ".event-widget time"
# events_times = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
#
# css_selector = ".event-widget li a"
# events_names = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
#
# for n in range(len(events_times)):
#     events[n] = {
#         "time": events_times[n].text,
#         "name": events_names[n].text
#     }
#
# print(events)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# css_selector = "#articlecount a"

# article_count = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
# print(article_count.text)

# article_count.click()

# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python Rocks")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value='fName')
first_name.send_keys("George")

last_name = driver.find_element(by=By.NAME, value='lName')
last_name.send_keys("Spilio")

email = driver.find_element(by=By.NAME, value='email')
email.send_keys("example@example.com")

button = driver.find_element(by=By.CLASS_NAME, value="btn")
button.click()

# driver.quit()