from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a"
# )
# print(documentation_link.text)

# link = driver.find_element(
#     By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[1]'
# )
# print(link.text)


event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
print(event_times)
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_times[n].text,
    }
    print(events)

driver.quit()
