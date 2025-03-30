from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")


# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# driver.find_element(By.ID,"APjFqb").send_keys("Prasad")
# #driver.find_element(By.CLASS_NAME,"MV3Tnb").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(5)