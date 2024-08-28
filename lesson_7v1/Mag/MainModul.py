from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_7v1.urllinks import link_mag
from lesson_7v1.Mag.mag_sells import *


class MainMag:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(link_mag)

    def auto_vhod(self):
        self._name = (By.ID, 'user-name')
        self._pass = (By.ID, 'password')
        self._button_l = (By.ID, 'login-button')
        self.browser.find_element(*self._name).send_keys(user_name)
        self.browser.find_element(*self._pass).send_keys(pass_user)
        self.browser.find_element(*self._button_l).click()

    def sell_item(self):
        self.browser.find_element(By.ID, buy_1).click()
        self.browser.find_element(By.ID, buy_2).click()
        self.browser.find_element(By.ID, buy_3).click()
        self.browser.find_element(By.ID, 'shopping_cart_container').click()

    def pay_item(self):
        self.browser.find_element(By.ID, 'checkout').click()
        self.browser.find_element(By.ID, 'first-name').send_keys(f_name)
        self.browser.find_element(By.ID, 'last-name').send_keys(l_name)
        self.browser.find_element(By.ID, 'postal-code').send_keys(post_ind)
        self.browser.find_element(By.ID, 'continue').click()

    def total_buy(self):
        WebDriverWait(self.browser, 15, 0.1).until(EC.element_to_be_clickable((By.ID, 'finish')))
        All_buy = self.browser.find_element(By.CLASS_NAME, text_buy).text
        print(All_buy)
        return All_buy
