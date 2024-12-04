from data import Data
import allure
import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

class TestGetListOrders:


    @allure.title('Проверка получения списка заказов без авторизации')
    def test_get_list_order_without_auth_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.get_all_orders_without_authorization()
        assert status_code == 401
        assert Data.RESPONSE_TEXT_MANDATORY_REGISTRATION in response_context

    @allure.title('Проверка получения списка заказов после авторизации')
    def test_get_list_order_with_auth_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, token_auth = UserMethods.login_user(Data.USER_REGISTER)
        OrderMethods.create_order_with_authorization(Data.FULL_BURGER, token_auth)
        status_code, response_context = OrderMethods.get_all_orders_with_authorization(token_auth)
        assert status_code == 200
        assert Data.RESPONSE_TEXT_SUCCESS in response_context