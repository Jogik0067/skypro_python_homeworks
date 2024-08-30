import json
import requests
import allure
from lesson_10.lesson_9_N.const import URL_link


class Employer:
    def __init__(self, url=URL_link):
        self.url = url

    def take_company_id(self):
        response = requests.get(self.url + '/company',
                                params={'active': 'true'})
        return response.json()[-1]['id']

    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    def new_sotr(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()
    
    def get_employee(self, employee_id: int):
        response = requests.get(self.url + '/employee/' + str(employee_id))
        return response.json()

    def patch_inf(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(
            self.url + '/employee/' + str(employee_id),
            headers=headers, json=body)
        return response.json()
    
    def get_employee_list(self, company_id):
        response = requests.get(f'{self.url}/employee?company={company_id}')
        return response.json()
