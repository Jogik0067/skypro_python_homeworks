import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_10.lesson_7_N.urllinks import link_calc


class CalcPage:
    def __init__(self, browser):
        with allure.step("Установка выборанного браузера"):
            self.browser = browser
        with allure.step("Установка адреса для открытия страницы"):
            self.browser.get(link_calc)
    
    @allure.step('Задержка расчета')
    def wait_rel(self):
        with allure.step('Поиск элемента "Delay"'):
            stroka_v = self.browser.find_element(By.ID, "delay")
        with allure.step('Очищение элемента "Delay"'):
            stroka_v.clear()
        with allure.step('Ввод занчения 45 в элемент "Delay"'):
            stroka_v.send_keys(45)
    
    @allure.step('Вычисления')
    def click_act(self):
        with allure.step("Нажатие цифры 7"):
            self.browser.find_element(By.XPATH, '//span[text()="7"]').click()
        with allure.step('Нажатие кнопки "+"'):
            self.browser.find_element(By.XPATH, '//span[text()="+"]').click()
        with allure.step("Нажатие цифры 8"):
            self.browser.find_element(By.XPATH, '//span[text()="8"]').click()
        with allure.step('Нажатие кнопки "="'):
            self.browser.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step('Результат вычисления')
    def result_w(self):
        with allure.step("Ожидание ответа за указанное ранее время"):
            WebDriverWait(self.browser, 47).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        with allure.step("Передача значения поля Screen"):
            return self.browser.find_element(By.CLASS_NAME, 'screen').text
