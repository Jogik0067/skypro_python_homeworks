from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def LOGIN (driver):
    driver.get("http://the-internet.herokuapp.com/login")
    sleep(3)
    driver.find_element(By.ID,'username').send_keys("tomsmith")
    sleep(3)
    driver.find_element(By.ID,'password').send_keys("SuperSecretPassword!")
    sleep(3)
    driver.find_element(By.TAG_NAME, 'button').click()
    sleep(3)
    driver.quit()

LOGIN (webdriver.Chrome())
LOGIN (webdriver.Firefox())