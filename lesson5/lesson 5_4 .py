from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def KlikniCloseModal(driver):
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(4)
    driver.find_element(By.CSS_SELECTOR, '.modal-footer').click()
    sleep(3)
    driver.quit()


KlikniCloseModal(webdriver.Chrome())
KlikniCloseModal(webdriver.Firefox())
