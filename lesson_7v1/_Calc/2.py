from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from lesson_7.url_links import *

def test_vvod():
    driver = webdriver.Chrome()
    driver.get(link_2)
    driver.find_element(By.ID, 'delay').clear()
    driver.find_element(By.ID, 'delay').send_keys(45)
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    WebDriverWait(driver, 47).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert driver.find_element(By.CLASS_NAME, 'screen').text == "15"
    
    driver.quit