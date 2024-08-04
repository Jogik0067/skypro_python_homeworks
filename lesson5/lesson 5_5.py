from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def EDIT_TEXT(driver):
    driver.get("http://the-internet.herokuapp.com/inputs")
    stroka = driver.find_element(By.TAG_NAME, 'input')
    stroka.send_keys("1000")
    sleep(3)
    stroka.clear()
    sleep(3)
    stroka.send_keys("999")
    sleep(3)
    driver.quit()


EDIT_TEXT(webdriver.Chrome())
EDIT_TEXT(webdriver.Firefox())
