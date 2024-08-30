import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_10.lesson_7_N.urllinks import link_mag
from lesson_10.lesson_7_N.Mag.mag_sells import *


class MainMag:
    
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(link_mag)
    with allure.step("Авторизация пользователя"):
        def auto_vhod(self):
            self._name = (By.ID, 'user-name')
            self._pass = (By.ID, 'password')
            self._button_l = (By.ID, 'login-button')
            self.browser.find_element(*self._name).send_keys(user_name)
            self.browser.find_element(*self._pass).send_keys(pass_user)
            self.browser.find_element(*self._button_l).click()
    with allure.step("Подбор вещей в корзину"):
        def sell_item(self):
            self.browser.find_element(By.ID, buy_1).click()
            self.browser.find_element(By.ID, buy_2).click()
            self.browser.find_element(By.ID, buy_3).click()
            with allure.step("Перемещение в корзину"):
                self.browser.find_element(By.ID, 'shopping_cart_container').click()
    with allure.step("Переход к оплате"):
        def pay_item(self):
            self.browser.find_element(By.ID, 'checkout').click()
            with allure.step("Ввод информации о покупателе и карте"):
                self.browser.find_element(By.ID, 'first-name').send_keys(f_name)
                self.browser.find_element(By.ID, 'last-name').send_keys(l_name)
                self.browser.find_element(By.ID, 'postal-code').send_keys(post_ind)
            with allure.step("Оплата и переход на страницу с информацией о операции"):
                self.browser.find_element(By.ID, 'continue').click()
    with allure.step("Ожидание загрузки информации об оплате"):
        def total_buy(self):
            WebDriverWait(self.browser, 15, 0.1).until(EC.element_to_be_clickable((By.ID, 'finish')))
            with allure.step("Сохранение суммы оплаты"):
                All_buy = self.browser.find_element(By.CLASS_NAME, text_buy).text
            with allure.step("Вывод на печать суммы оплаты"):
                print(All_buy)
            return All_buy
