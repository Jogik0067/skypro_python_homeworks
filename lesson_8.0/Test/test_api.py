import pytest
import json
import requests
from lesson_8.const import URL_link
from lesson_8.Pages.API import Employer
employer = Employer()

# Проверка не пустой ли token и явлется ли строкой
def test_logon(token_work):
    token = token_work
    assert token is not None
    assert isinstance(token, str)

# Проверка не пустой ли id и состоит ли только из цифр
def test_company_id():
    company_id = employer.take_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

# Добавление нового сотрудника с проверкой
def test_new_sotr(token_work):
    token = str(token_work)
    com_id = employer.take_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Peter',
        'lastName': 'Sidorov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.com',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2001-09-14T10:10:10.021Z',
        'isActive': 'true'
    }

    # Проверка на заполнение id и состав id(только цифры)
    new_sotr_id = (employer.new_sotr(token, body_employer))['id']
    assert new_sotr_id is not None
    assert str(new_sotr_id).isdigit()

# Запрос с пустым токеном(неавторизирован)
def test_no_token():
    token = ""
    com_id = employer.take_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Peter',
        'lastName': 'Sidorov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.com',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2001-09-14T10:10:10.021Z',
        'isActive': 'true'
    }
    new_sotr_id = (employer.new_sotr(token, body_employer))
    assert new_sotr_id['message'] == 'Unauthorized'

# Отправка без тела запроса
def test_no_body(token_work):
    token = str(token_work)
    body_employer = {}
    new_sotr_id = (employer.new_sotr(token, body_employer))
    assert new_sotr_id['message'] == 'Internal server error'

# Проверка является ли списком полученный ответ, а не строкой
def test_get_sotrs():
    com_id = employer.take_company_id()
    assert isinstance(employer.get_list(com_id), list)

# Ошибка с пустым id компании
def test_sotrs_nocomp():
    text_er = ("Employer.get_list() missing 1 required" 
               + " positional argument: 'company_id'")
    try:
        employer.get_list()
    except TypeError as e:
        assert str(e) == text_er

# Невалидным id компании
def test_sotrs_invcomp():
    text_er = ("Employer.get_list() missing 1 required" 
               + " positional argument: 'company_id'")
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == text_er

# Добавление нового сотрудника с последующим редактированием части информации
def test_patch_sotr(token_work):
    token = str(token_work)
    com_id = employer.take_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Peter',
        'lastName': 'Sidorov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.com',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2001-09-14T10:10:10.021Z',
        'isActive': 'true'
    }
    just_employer = employer.new_sotr(token, body_employer)
    id = just_employer['id']
    body_patch_employer = {
        'firstName': 'Kirill01',
        'companyId': com_id,
        'email': 'kirill@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_patch = employer.patch_inf(token, id, body_patch_employer)
    assert employer_patch.status_code == 200
    # проверка совпадения id из базы с id полученным при создании сотрудника
    assert id == employer_patch.json()['id']
    # проверка на изменение почты
    assert (employer_patch.json()['email']
            ) == body_patch_employer.get('email')
