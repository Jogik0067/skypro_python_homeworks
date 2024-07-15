from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
firefox=webdriver.Firefox()

chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

for i in range(0,5):
    chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    #___________________________________________
    chrome_del_len = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
    firefox_del_len = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')
    
chrome.quit()
firefox.quit()

print("Размер списка кнопок Delete:")
print(f'В Chrome: {len(chrome_del_len)}')
print(f'В Firefox: {len(firefox_del_len)}')