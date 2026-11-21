from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open login page
driver.get("https://www.saucedemo.com")
time.sleep(2)

# Locate username using ID
username1 = driver.find_element(By.ID, "user-name")
print("Username found using ID")

# Locate username using Name
username2 = driver.find_element(By.NAME, "user-name")
print("Username found using Name")

# Locate username using CSS Selector
username3 = driver.find_element(By.CSS_SELECTOR, "input#user-name")
print("Username found using CSS Selector")

time.sleep(2)

# Close browser
driver.quit()