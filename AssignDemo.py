expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)

    result.find_element(By.XPATH,"div/button").click()


assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#SUM VALIDATION
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)



discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount > discountedAmount


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
#
# # Open the website
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#
# # Search for "ber"
# driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# time.sleep(2)
#
# # Get all products
# results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# assert len(results) > 0  # Ensure products are found
#
# # Add each product to cart
# for result in results:
#     result.find_element(By.XPATH, "div/button").click()
#
# # Go to cart and proceed to checkout
# driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#
# # Apply promo code
# driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#
# # Explicit wait for promo confirmation
# wait = WebDriverWait(driver, 10)  # Fixed casing
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
#
# # Print promo message
# print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
#
# # Close browser
# driver.quit()
