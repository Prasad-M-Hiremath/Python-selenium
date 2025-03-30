import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

driver.maximize_window()
#SYNTAX for (XPATH)====>  tagname[@attribute='value'] -> //input[@type="submit"]

#SYNTAX for (CSS)====>  tagname[attribute='value'] -> input[@type="submit"]   #id, .classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()



#DROPDOWN
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()




driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Prasad")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "success" in message



time.sleep(3)