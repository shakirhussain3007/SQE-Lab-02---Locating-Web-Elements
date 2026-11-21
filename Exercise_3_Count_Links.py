from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org")
time.sleep(2)

# Find all links using Tag Name
links = driver.find_elements(By.TAG_NAME, "a")

# Print total links
print("Total links on Wikipedia:", len(links))

time.sleep(2)

# Close browser
driver.quit()