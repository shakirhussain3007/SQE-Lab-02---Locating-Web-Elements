from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open W3Schools HTML tables page
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)

# Locate 2nd td inside 3rd tr
cell = driver.find_element(
    By.XPATH,
    "//table[@id='customers']//tr[3]/td[2]"
)

# Print cell text
print("Table Cell Text:", cell.text)

time.sleep(2)

# Close browser
driver.quit()