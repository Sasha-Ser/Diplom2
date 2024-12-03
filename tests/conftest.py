import pytest
import requests

from methods.user_methods import UserMethods
from data import Data

@pytest.fixture()
def user_authorization():
    yield
    response = requests.post(f"{Data.BASE_URL}{Data.LOGIN_URL}", json=Data.USER_REGISTER)
    r = response.json()
    access_token = r["accessToken"]
    headers = {'Authorization': f'{access_token}'}
    response = requests.delete(f"{Data.BASE_URL}{Data.USER_URL}", headers=headers)