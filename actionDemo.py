from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action =ActionChains(driver)
# action.double_click(driver.find_element(By))
# action.context_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()