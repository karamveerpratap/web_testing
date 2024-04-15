from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Creating an instance of the webdriver
browser = webdriver.Chrome()
browser.get('https://www.f.com')

# Letting the page load
time.sleep(2)

# Clicking on the login link
login = browser.find_element(By.XPATH, '//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
login.click()
print("Login to Twitter")

# Entering username
user = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
user.send_keys('USER-NAME')

# Reading password from a text file
with open('test.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')

# Entering password
password_field = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
password_field.send_keys(password)

# Clicking the login button
login_button = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
login_button.click()
print("Login Successful")

# Waiting for page to load
time.sleep(5)

# Finding the search input element
search_input = browser.find_element(By.NAME, "q")

# Clearing the search input
search_input.clear()

# Entering search query
search_input.send_keys("Geeks for geeks ")

# Pressing Enter
search_input.send_keys(Keys.RETURN)
print("Search Successful")

# Closing the browser
browser.close()
