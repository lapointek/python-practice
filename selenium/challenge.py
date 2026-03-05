from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


fname_field = driver.find_element(By.NAME, value="fName")
lname_field = driver.find_element(By.NAME, value="lName")
email_field = driver.find_element(By.NAME, value="email")

fname_field.send_keys("Kevin")
lname_field.send_keys("Lapointe")
email_field.send_keys("test@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
