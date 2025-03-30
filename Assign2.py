from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the login page
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Locate the email input field and enter email
driver.find_element(By.ID, "username").send_keys("mentor@rahulshettyacademy.com")

# Locate the password field and enter password
driver.find_element(By.ID, "password").send_keys("123456")

# Click the login button
driver.find_element(By.ID, "signInBtn").click()

# Wait for the error message to load
time.sleep(3)  # Adding sleep to allow error message to be displayed

# Capture the error message displayed on the webpage
error_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print("Error Message:", error_message)

# Keep the browser open for 10 seconds to view the output
time.sleep(10)

# Close the browser
driver.quit()
