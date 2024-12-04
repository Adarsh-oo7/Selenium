from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google
driver.get('https://www.google.com/')

# Locate the search box element using its ID
my = driver.find_element(By.ID, 'APjFqb')

# Print the element to confirm it's found
my.send_keys("adarshbs.com")
my.send_keys(Keys.RETURN)
time.sleep(4)
first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
first_result.click()
time.sleep(19)
# Close the browser (optional)
# driver.quit()

