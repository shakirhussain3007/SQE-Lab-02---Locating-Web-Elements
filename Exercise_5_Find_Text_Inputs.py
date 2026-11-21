from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open a page containing a form
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

# Find all text inputs using CSS Selector
text_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

# Print total matching elements
print("Total text inputs:", len(text_inputs))

# Print identifying attributes
for element in text_inputs:
    print("Input ID:", element.get_attribute("id"))
    print("Input Name:", element.get_attribute("name"))

time.sleep(2)

# Close browser
driver.quit()