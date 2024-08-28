from lesson_7v1.Forma.Pages.MainPage import MainPage
from lesson_7v1.Forma.Pages.DataPole import DataPole


def test_forma(chrome_browser):
    main = MainPage(chrome_browser)
    main.fields()
    main.field_full()
    main.click_button()

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
    
    assert 'alert py-2 alert-danger' in data_fild.get_class_zip_code()
    assert 'alert py-2 alert-success' in data_fild.get_class_first_name()
    assert 'alert py-2 alert-success' in data_fild.get_class_last_name()
    assert 'alert py-2 alert-success' in data_fild.get_class_phone()
    assert 'alert py-2 alert-success' in data_fild.get_class_email()
    assert 'alert py-2 alert-success' in data_fild.get_class_address()
    assert 'alert py-2 alert-success' in data_fild.get_class_city()
    assert 'alert py-2 alert-success' in data_fild.get_class_country()
    assert 'alert py-2 alert-success' in data_fild.get_class_job_position()
    assert 'alert py-2 alert-success' in data_fild.get_class_company()

