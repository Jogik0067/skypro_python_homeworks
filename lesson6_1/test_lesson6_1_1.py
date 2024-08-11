from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from lesson6_1_1_vvod import *

def test_vvod():
    driver = webdriver.Chrome()
    driver.get(link_1)
    driver.find_element(By.NAME, 'first-name').send_keys(first_name)
    driver.find_element(By.NAME, 'last-name').send_keys(last_name)
    driver.find_element(By.NAME, 'address').send_keys(address)
    driver.find_element(By.NAME, 'e-mail').send_keys(e_mail)
    driver.find_element(By.NAME, 'phone').send_keys(phone)
    driver.find_element(By.NAME, 'zip-code').send_keys('')
    driver.find_element(By.NAME, 'city').send_keys(city)
    driver.find_element(By.NAME, 'country').send_keys(country)
    driver.find_element(By.NAME, 'job-position').send_keys(job_position)
    driver.find_element(By.NAME, 'company').send_keys(company)
    WebDriverWait(driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()  
    assert 'alert-danger' in driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#address').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#city').get_attribute("class")
    driver.quit