from data import Data
import allure
import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

class TestCreationOrder:

    @allure.title('Проверка успешного создания заказа после авторизации')
    def test_creation_order_with_auth_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, token_auth = UserMethods.login_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.create_order_with_authorization(Data.FULL_BURGER, token_auth)
        expected_response_text = '"success":true'
        assert status_code == 200
        assert expected_response_text in response_context

    @allure.title('Проверка создания заказа без авторизации')
    def test_creation_order_without_auth_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.create_order_without_authorization(Data.FULL_BURGER)
        expected_response_text = '"success":true'
        assert status_code == 200
        assert expected_response_text in response_context

    @allure.title('Проверка создания заказа с разным набором ингредиентов')
    @pytest.mark.parametrize("burger", [
        Data.FULL_BURGER,
        Data.BURGER_WITHOUT_BRED,
        Data.BURGER_WITHOUT_SOUCE,
        Data.BURGER_WITHOUT_FILLING
    ])
    def test_creation_order_with_ingredients_success(self, user_authorization, burger):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.create_order_without_authorization(burger)
        expected_response_text = '"success":true'
        assert status_code == 200
        assert expected_response_text in response_context

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_creation_order_without_ingredients_succes(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.create_order_without_authorization(Data.EMPTY_BURGER)
        expected_response_text = '{"success":false,"message":"Ingredient ids must be provided"}'
        assert status_code == 400
        assert expected_response_text == response_context

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @pytest.mark.parametrize("burger", [
        Data.BURGER_WRONG_HASH_BREAD,
        Data.BURGER_WRONG_HASH_SOUCE,
        Data.BURGER_WRONG_HASH_FILLING
    ])
    def test_creation_order_with_ingredients_success(self, user_authorization, burger):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = OrderMethods.create_order_without_authorization(burger)
        expected_response_text = 'Internal Server Error'
        assert status_code == 500
        assert expected_response_text in response_context