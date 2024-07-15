from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def Klikni (driver):
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    
    for i in range(0,3):
        driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        print(f'Жмак{i}, {str(driver)}')
    driver.quit()

Klikni(webdriver.Chrome())
Klikni(webdriver.Firefox())