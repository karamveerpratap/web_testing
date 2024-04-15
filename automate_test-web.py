# Import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create webdriver object
driver = webdriver.Edge()

# Get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/?ref=next_article")

# Get element
element = driver.find_element(By.ID, "gsc-i-id1")

# Send keys
element.send_keys("Arrays")
time.sleep(5)
driver.quit()
