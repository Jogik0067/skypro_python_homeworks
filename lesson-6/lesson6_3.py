from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
jdun = WebDriverWait(browser, 40, 0.1)

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

jdun.until(
    EC.visibility_of_element_located((By.ID, "landscape"))
)

print(browser.find_element(By.ID, "award").get_attribute('src'))

browser.quit()
