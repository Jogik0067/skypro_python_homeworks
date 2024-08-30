import allure
from lesson_10.lesson_7_N.Forma.Pages.MainPage import MainPage
from lesson_10.lesson_7_N.Forma.Pages.DataPole import DataPole

@allure.id("PersonalData")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.story("Заполнение персональных данных и проверка цвета полей ввода после подтверждения")
@allure.feature("CREATE")
@allure.title("Заполнить персональные данные")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
def test_forma(chrome_browser): 
    with allure.step("Открыть страницу веб-браузера"):
        main = MainPage(chrome_browser)
    with allure.step("Сбор данных о полях ввода"):
        main.fields()
    with allure.step("Заполнение данных в поля ввода"):
        main.field_full()
    with allure.step("Подтверждение введеных данных"):
        main.click_button()

    with allure.step("Сбор данных о значениях атрибутов полей"):
        data_fild = DataPole(chrome_browser)
        data_fild.fields()
        data_fild.get_class_first_name()
        data_fild.get_class_last_name()
        data_fild.get_class_address()
        data_fild.get_class_email()
        data_fild.get_class_phone()
        data_fild.get_class_zip_code()
        data_fild.get_class_city()
        data_fild.get_class_country()
        data_fild.get_class_job_position()
        data_fild.get_class_company()
    
    with allure.step("Проверка предупреждения о пустом Zip-коде"):
        assert 'alert py-2 alert-danger' in data_fild.get_class_zip_code()
    with allure.step("Проверка корректности заполения поля Имя"):
        assert 'alert py-2 alert-success' in data_fild.get_class_first_name()
    with allure.step("Проверка корректности заполения поля Фамилия"):
        assert 'alert py-2 alert-success' in data_fild.get_class_last_name()
    with allure.step("Проверка корректности заполения поля Телефон"):
        assert 'alert py-2 alert-success' in data_fild.get_class_phone()
    with allure.step("Проверка корректности заполения поля E-mail"):
        assert 'alert py-2 alert-success' in data_fild.get_class_email()
    with allure.step("Проверка корректности заполения поля Адрес"):
        assert 'alert py-2 alert-success' in data_fild.get_class_address()
    with allure.step("Проверка корректности заполения поля Город"):
        assert 'alert py-2 alert-success' in data_fild.get_class_city()
    with allure.step("Проверка корректности заполения поля Страна"):
        assert 'alert py-2 alert-success' in data_fild.get_class_country()
    with allure.step("Проверка корректности заполения поля Должность"):
        assert 'alert py-2 alert-success' in data_fild.get_class_job_position()
    with allure.step("Проверка корректности заполения поля Компания"):
        assert 'alert py-2 alert-success' in data_fild.get_class_company()

