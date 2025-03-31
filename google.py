from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")



driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()



time.sleep(5)