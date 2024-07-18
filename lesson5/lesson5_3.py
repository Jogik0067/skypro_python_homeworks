from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def KlikniCSS(driver):
    for i in range(0, 3):
        driver.get("http://uitestingplayground.com/classattr")
        driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        sleep(3)
        driver.switch_to.alert.accept()
        sleep(1)
    driver.quit()


KlikniCSS(webdriver.Chrome())
KlikniCSS(webdriver.Firefox())
