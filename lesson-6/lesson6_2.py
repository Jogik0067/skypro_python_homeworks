from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(4)

browser.get("http://uitestingplayground.com/textinput")

browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
browser.find_element(By.ID, "updatingButton").click()
print(browser.find_element(By.ID, "updatingButton").text)

browser.quit()
