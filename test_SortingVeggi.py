from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggis = []
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    veggiWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

    for elements in veggiWebElements:
        browserSortedVeggis.append(elements.text)

    originalSortedBrowserList = browserSortedVeggis.copy()
    browserSortedVeggis.sort()
    assert browserSortedVeggis == originalSortedBrowserList

