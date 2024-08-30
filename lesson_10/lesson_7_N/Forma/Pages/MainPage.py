import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_10.lesson_7_N.urllinks import link_data
from lesson_10.lesson_7_N.Forma.vvod import *


class MainPage:
    def __init__(self, browser):
        with allure.step("Установка выборанного браузера"):
            self.browser = browser
        with allure.step("Установка адреса для открытия страницы"):
            self.browser.get(link_data)
    
    @allure.step("Поиск и сохранение маркеров")
    def fields(self):
        self._first_name = (By.NAME, 'first-name')
        self._last_name = (By.NAME, 'last-name')
        self._address = (By.NAME, 'address')
        self._email = (By.NAME, 'e-mail')
        self._phone = (By.NAME, 'phone')
        self._zip_code = (By.NAME, 'zip-code')
        self._city = (By.NAME, 'city')
        self._country = (By.NAME, 'country')
        self._job_position = (By.NAME, 'job-position')
        self._company = (By.NAME, 'company')
        self._button = (By.TAG_NAME, 'button')

    @allure.step("Заполнение формы с персональными данными")
    def field_full(self):
        self.browser.find_element(*self._first_name).send_keys(first_name)
        self.browser.find_element(*self._last_name).send_keys(last_name)
        self.browser.find_element(*self._address).send_keys(address)
        self.browser.find_element(*self._email).send_keys(email)
        self.browser.find_element(*self._phone).send_keys(phone)
        self.browser.find_element(*self._zip_code).send_keys(zip_code)
        self.browser.find_element(*self._city).send_keys(city)
        self.browser.find_element(*self._country).send_keys(country)
        self.browser.find_element(*self._job_position).send_keys(job_position)
        self.browser.find_element(*self._company).send_keys(company)
        
    @allure.step('Ожидание доступности и последующее нажатие кнопки "Submit"')
    def click_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()

