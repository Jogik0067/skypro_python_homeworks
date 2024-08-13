from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from lesson6_1_1_vvod import *

def test_vvod():
    driver = webdriver.Chrome()
    driver.get(link_3)
    driver.find_element(By.ID, 'user-name').send_keys(user_name)
    driver.find_element(By.ID, 'password').send_keys(pass_user)
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, buy_1).click()
    driver.find_element(By.ID, buy_2).click()
    driver.find_element(By.ID, buy_3).click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys(f_name)
    driver.find_element(By.ID, 'last-name').send_keys(l_name)
    driver.find_element(By.ID, 'postal-code').send_keys(post_ind)
    driver.find_element(By.ID, 'continue').click()
    All_buy = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    print(All_buy)
    assert All_buy == 'Total: $'+ all_sells
    driver.quit