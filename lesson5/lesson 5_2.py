from selenium import webdriver
from selenium.webdriver.common.by import By


def Klikni(driver):
    for i in range(0, 3):
        driver.get("http://uitestingplayground.com/dynamicid")
        driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        print(f'Жмак{i}, {str(driver)}')
    driver.quit()


Klikni(webdriver.Chrome())
Klikni(webdriver.Firefox())
