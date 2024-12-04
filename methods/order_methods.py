import requests
from data import Data

class OrderMethods:

    def create_order_with_authorization(params, token):
        response = requests.post(f"{Data.BASE_URL}{Data.CREATE_ORDER_URL}", headers=token, json=params)
        return response.status_code, response.text

    def create_order_without_authorization(params):
        response = requests.post(f"{Data.BASE_URL}{Data.CREATE_ORDER_URL}", json=params)
        return response.status_code, response.text

    def get_all_orders_without_authorization ():
        response = requests.get(f"{Data.BASE_URL}{Data.CREATE_ORDER_URL}")
        return response.status_code, response.text

    def get_all_orders_with_authorization(token):
        response = requests.get(f"{Data.BASE_URL}{Data.CREATE_ORDER_URL}", headers=token)
        return response.status_code, response.text
