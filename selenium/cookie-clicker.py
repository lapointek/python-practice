from itertools import count
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

button = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")

try:
    language = driver.find_element(by=By.ID, value="#langSelect-EN")
    language.click()
    sleep(3)
except:
    print("Language slection not found")

while True:
    button.click()
