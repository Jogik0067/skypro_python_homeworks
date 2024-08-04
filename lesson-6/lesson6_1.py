from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(17)

browser.get("http://uitestingplayground.com/ajax")
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

textbar = browser.find_element(By.CSS_SELECTOR, "#content")

print(textbar.find_element(By.CSS_SELECTOR, "p.bg-success").text)

browser.quit()
