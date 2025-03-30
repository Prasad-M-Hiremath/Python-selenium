from selenium import webdriver
import time

from selenium.webdriver.common.by import By
browserSortedVeggis = []
driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)







time.sleep(10)