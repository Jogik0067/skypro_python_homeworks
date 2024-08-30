import json
import requests
import allure
from lesson_10.lesson_9_N.const import URL_link


class Employer:
    def __init__(self, url=URL_link):
        self.url = url
        
    @allure.step('Получение ID последней активной компании с помощью API')
    def take_company_id(self):
        response = requests.get(self.url + '/company',
                                params={'active': 'true'})
        return response.json()[-1]['id']
            
    @allure.step('Добавление нового сотрудника с помощью API')
    def new_sotr(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()
    
    @allure.step('Получение сотрудника по идентификатору с помощью API')
    def get_employee(self, employee_id: int):
        response = requests.get(self.url + '/employee/' + str(employee_id))
        return response.json()
    
    @allure.step('Корректировка данных о сотруднике с помощью API')
    def patch_inf(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(
            self.url + '/employee/' + str(employee_id),
            headers=headers, json=body)
        return response.json()
    
    @allure.step('Получение списка сотрудников с помощью API')
    def get_employee_list(self, company_id):
        response = requests.get(f'{self.url}/employee?company={company_id}')
        return response.json()
