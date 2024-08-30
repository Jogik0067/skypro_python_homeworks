import pytest
import json
import requests
import allure
from lesson_10.lesson_9_N.Pages.API import Employer
from lesson_10.lesson_9_N.Pages.DB_employee import DBEmployee
from lesson_10.lesson_9_N.Pages.DB_comp import DBComp
from lesson_10.lesson_9_N.const import *


api = Employer('https://x-clients-be.onrender.com')

db_con = ("postgresql+psycopg2://x_clients_user:" +
          "95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa" +
          "@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com" +
          "/x_clients_db_fxd0")

company_table = DBComp(db_con)
employee_table = DBEmployee(db_con)


@allure.title('Создать сотрудника')
@allure.description('Тест создания сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee(token_work):
    with allure.step('Создание новой компании в DB'):
        company_table.create(name, description)
        com_id = company_table.get_max_id()
        body_employer = {
            'id': 0,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': 'string',
            'companyId': com_id,
            'email': email,
            'url': 'string',
            'phone': phone,
            'birthdate': '2000-06-07T08:06:30.137Z',
            'isActive': is_active
        }

    with allure.step('Создание нового сотрудника с помощью API'):
        new_employee = api.new_sotr(token_work, body_employer)
        new_employee_id = new_employee["id"]

    with allure.step('Получение сотрудника из DB'):
        employee = employee_table.get_employee_by_id(new_employee_id)

    with allure.step('Удаление нового сотрудника и новой компанию из DB'):
        employee_table.delete(new_employee_id)
        company_table.delete(com_id)
    with allure.step('Проверка был ли создан новый сотрудник в DB'):
        assert len(employee) == 1, "Employee was not created"


@allure.title('Получить сотрудника')
@allure.description('Протестируйте сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee():
    with allure.step('Создание новой компании в DB'):
        company_table.create(name, description)
        new_company_id = company_table.get_max_id()

    with allure.step('Создание нового сотрудника в DB'):
        employee_table.create(first_name, last_name, phone, new_company_id,
                              is_active)
        new_employee_id = employee_table.get_max_id()

    with allure.step('Получение информации о сотруднике с помощью API'):
        employee = api.get_employee(new_employee_id)

    with allure.step('Удаление нового сотрудника и компании из DB'):
        employee_table.delete(new_employee_id)
        company_table.delete(new_company_id)
    with allure.step('Проверка полученного через API нового ID'):
        assert employee["id"] == new_employee_id
    with allure.step('Проверка полученного через API имени нового сотрудника'):
        assert employee["firstName"] == first_name
    with allure.step('Проверьте длину тела срабатывания'):
        assert len(employee) == 12


@allure.title('Получить список сотрудников')
@allure.description('Тест получения списка сотрудников с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list():
    with allure.step('Cоздание новой компании в DB'):
        company_table.create(name, description)
        new_company_id = company_table.get_max_id()

    with allure.step('Создание нового сотрудника в DB'):
        employee_table.create(first_name, last_name, phone, new_company_id,
                            is_active)
        new_employee_id = employee_table.get_max_id()

    with allure.step('Получение списока сотрудников с помощью API'):
        employee_list_api = api.get_employee_list(new_company_id)

    with allure.step('Получение списока сотрудников в DB'):
        employee_list_db = employee_table.get_company_employees(new_company_id)

    with allure.step('Удаление нового сотрудника и новой компании из DB'):
        employee_table.delete(new_employee_id)
        company_table.delete(new_company_id)
    with allure.step('Сравнение id сотрудника из DB и полученного через API '):
        assert employee_list_api[0]["id"] == new_employee_id, \
                "Employee's ID is not equal"
    with allure.step('Сравнение размеров списков API и DB'):
        assert len(employee_list_api) == len(employee_list_db)


@allure.title('Изменить сотрудника по DB')
@allure.description('Тестовое изменение сотрудника по DB')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_db():
    with allure.step('Создание новой компании в DB'):
        company_table.create(name, description)
        new_company_id = company_table.get_max_id()

    with allure.step('Создание нового сотрудника в DB'):
        employee_table.create(first_name, last_name, phone, new_company_id,
                            is_active)
        new_employee_id = employee_table.get_max_id()

    with allure.step('Изменение сотрудника с помощью DB'):
        employee_table.update(new_employee_id, new_email, new_is_active)

    with allure.step('Получение информации о сотруднике с помощью API'):
        employee = api.get_employee(new_employee_id)
    with allure.step('Проверка исправленной информации о сотруднике из API'):
        assert employee["id"] == new_employee_id
        assert employee["email"] == new_email
        assert employee["isActive"] == new_is_active


@allure.title('Сменить сотрудника с помощью API')
@allure.description('Протестируйте смену сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_api(token_work):
    with allure.step('Создание новой компании в DB'):
        company_table.create(name, description)
        new_company_id = company_table.get_max_id()

    with allure.step('Создание нового сотрудника в DB'):
        employee_table.create(first_name, last_name, phone, new_company_id,
                            is_active)
        new_employee_id = employee_table.get_max_id()
        body_patch_employer = {
            'companyId': new_company_id,
            'email': new_email,
            'isActive': new_is_active
        }
    with allure.step('Изменение сотрудника с помощью API'):
        patched_employee = api.patch_inf(token_work, new_employee_id, body_patch_employer)
    with allure.step('Проверка исправленной информации о сотруднике из API'):
        assert patched_employee["id"] == new_employee_id
        assert patched_employee["email"] == new_email
        assert patched_employee["isActive"] == new_is_active

    with allure.step('Получение исправленной информации о сотруднике из DB'):
        employee = employee_table.get_employee_by_id(new_employee_id)

    with allure.step('Удаление нового сотрудника и новой компании из DB'):
        employee_table.delete(new_employee_id)
        company_table.delete(new_company_id)

    with allure.step('Проверка исправленной информации о сотруднике из DB'):
        assert employee[0][0] == new_employee_id
        assert employee[0][8] == new_email
        assert employee[0][1] == new_is_active