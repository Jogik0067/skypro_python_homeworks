import allure
from lesson_10.lesson_7_N.Mag.MainModul import MainMag
from lesson_10.lesson_7_N.Mag.mag_sells import all_sells

@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Подбор и покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_mag(chrome_browser):
    with allure.step("Открытие страницы веб-браузера"):
        mag = MainMag(chrome_browser)
    mag.auto_vhod()
    mag.sell_item()
    mag.pay_item()
    with allure.step("Проверить,что ожидаемая и фактическая стоимость равны"):
        assert mag.total_buy() == all_sells