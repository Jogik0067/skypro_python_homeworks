from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_7v1.urllinks import link_calc


class CalcPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(link_calc)
    
    # Задержка расчета
    def wait_rel(self):
        stroka_v = self.browser.find_element(By.ID, "delay")
        stroka_v.clear()
        stroka_v.send_keys(45)
    
    # Вычисления
    def click_act(self):
        self.browser.find_element(By.XPATH, '//span[text()="7"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="+"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="8"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="="]').click()
    
    # Ожидание ответа за указанное ранее время
    def result_w(self):
        WebDriverWait(self.browser, 47).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.browser.find_element(By.CLASS_NAME, 'screen').text
