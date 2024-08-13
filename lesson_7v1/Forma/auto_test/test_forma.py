from lesson_7.Forma.Pages.MainPage import MainPage
from lesson_7.Forma.Pages.DataPole import DataPole

def TEST_FORMA(chrome_browser):#
    main = MainPage(chrome_browser)
    main.field()
    main.field_full()
    main.click_button()

    dat = DataPole(chrome_browser)
    dat.field
    dat.get_att_first_name
    dat.get_att_last_name
    dat.get_att_address
    dat.get_att_email
    dat.get_att_phone
    dat.get_att_zip_code
    dat.get_att_city
    dat.get_att_country
    dat.get_att_job_position
    dat.get_att_company
    
    assert 'alert-danger' in dat.get_att_zip_code
    assert 'success' in dat.get_att_first_name
    assert 'success' in dat.get_att_last_name
    assert 'success' in dat.get_att_phone
    assert 'success' in dat.get_att_email
    assert 'success' in dat.get_att_address
    assert 'success' in dat.get_att_city
    assert 'success' in dat.get_att_country
    assert 'success' in dat.get_att_job_position
    assert 'success' in dat.get_att_company

