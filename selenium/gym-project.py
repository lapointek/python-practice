ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/login/")

wait = WebDriverWait(driver, 10)

email = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password = wait.until(EC.presence_of_element_located((By.ID, "password-input")))

email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)

button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".Login_submitButton__tJFna"))
)

button.click()
