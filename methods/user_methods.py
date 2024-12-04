import requests
from data import Data

class UserMethods:

    def create_user(params):
        response = requests.post(f"{Data.BASE_URL}{Data.REGISTER_URL}", json=params)
        return response.status_code, response.text

    def login_user(params):
        response = requests.post(f"{Data.BASE_URL}{Data.LOGIN_URL}", json=params)
        r = response.json()
        access_token = r.get("accessToken")
        if access_token is None:
            headers = {'Authorization': f'{access_token}'}
            return response.status_code, response.text, {}

        headers = {'Authorization': f'{access_token}'}
        return response.status_code, response.text, headers

    def edit_user(params, fields):
        response = requests.post(f"{Data.BASE_URL}{Data.LOGIN_URL}", json=params)
        r = response.json()
        access_token = r["accessToken"]
        headers = {'Authorization': f'{access_token}'}
        response = requests.patch(f"{Data.BASE_URL}{Data.USER_URL}", headers=headers, json=fields)
        return response.status_code, response.text

    def delete_user(params):
        response = requests.delete(f"{Data.BASE_URL}{Data.LOGIN_URL}", headers=params)
        return response.status_code, response.text


