import allure
from lesson_10.lesson_7_N.Calc.MainModul import CalcPage

def test_calculation(chrome_browser):
    with allure.step("Выбор браузера"):
        calcut = CalcPage(chrome_browser)
    with allure.step("Ввод времени ожидания"):
        calcut.wait_rel()
    with allure.step("Ввод чисел в калькулятор и выполнение сложения"):
        calcut.click_act()
    with allure.step("Сравнение результата сложения с ожидаемым значением 15"):
        assert "15" in calcut.result_w()
