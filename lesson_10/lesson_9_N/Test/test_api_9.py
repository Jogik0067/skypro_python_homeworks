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


def test_create_employee(token_work):
    # создать новую компанию в DB
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
    # создать нового сотрудника с помощью API
    new_employee = api.new_sotr(token_work, body_employer)
    new_employee_id = new_employee["id"]

    # получить сотрудника из DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(com_id)

    assert len(employee) == 1, "Employee was not created"


def test_get_employee():
    # создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # получите информацию о сотруднике с помощью API
    employee = api.get_employee(new_employee_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee["id"] == new_employee_id
    assert employee["firstName"] == first_name
    assert len(employee) == 12


def test_get_employee_list():
    # создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # получить список сотрудников с помощью API
    employee_list_api = api.get_employee_list(new_company_id)

    # получить список сотрудников в DB
    employee_list_db = employee_table.get_company_employees(new_company_id)

    # удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee_list_api[0]["id"] == new_employee_id, \
        "Employee's ID is not equal"
    assert len(employee_list_api) == len(employee_list_db)


def test_change_employee_by_db():
    # создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # изменить сотрудника с помощью DB
    employee_table.update(new_employee_id, new_email, new_is_active)

    # получите информацию о сотруднике с помощью API
    employee = api.get_employee(new_employee_id)

    assert employee["id"] == new_employee_id
    assert employee["email"] == new_email
    assert employee["isActive"] == new_is_active


def test_change_employee_by_api(token_work):
    # создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()
    body_patch_employer = {
        'companyId': new_company_id,
        'email': new_email,
        'isActive': new_is_active
    }
    # изменить сотрудника с помощью API
    patched_employee = api.patch_inf(token_work, new_employee_id, body_patch_employer)
    assert patched_employee["id"] == new_employee_id
    assert patched_employee["email"] == new_email
    assert patched_employee["isActive"] == new_is_active

    # получите исправленную информацию о сотруднике из DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee[0][0] == new_employee_id
    assert employee[0][8] == new_email
    assert employee[0][1] == new_is_active