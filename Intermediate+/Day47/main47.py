
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = "example@example.com" # Your email
password = "password" # Your Password

service = Service("E:\GitHub\Python-Projects\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/uas/login")

email = driver.find_element(by=By.CSS_SELECTOR, value="#username")
email.send_keys(email)

password = driver.find_element(by=By.CSS_SELECTOR, value="#password")
password.send_keys(password)

button = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
button.click()

driver.get("https://www.linkedin.com/my-items/saved-jobs/")
