# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element after explicitly waiting for 5 seconds
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Courses"))
)
# click the element
element.click()
driver.quit()
