import pytest
import requests
from lesson_10.lesson_9_N.const import URL_link

@pytest.fixture()
def token_work(username='leonardo', password='leads'):
    user_pass = {'username': username, 'password': password}
    log_token = requests.post(URL_link + '/auth/login', json=user_pass)
    token = log_token.json()['userToken']
    return token
