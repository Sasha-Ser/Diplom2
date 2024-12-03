from data import Data
import allure
import pytest
from methods.user_methods import UserMethods

class TestCreationUser:

    @allure.title('Проверка успешного создания пользователя')
    def test_creation_user_success(self, user_authorization):
        status_code, response_context = UserMethods.create_user(Data.USER_REGISTER)
        expected_response_text = f'"email":"{Data.USER_REGISTER['email']}","name":"{Data.USER_REGISTER['name']}"'
        assert status_code == 200
        assert expected_response_text in response_context

    @allure.title('Проверка не создания пользователя с существующими данными')
    def test_creation_clone_user_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = UserMethods.create_user(Data.USER_REGISTER)
        expected_response_text = '{"success":false,"message":"User already exists"}'
        assert status_code == 403
        assert expected_response_text == response_context

    @allure.title('Проверка не создания пользователя без обязательных полей')
    @pytest.mark.parametrize("user_data", [
        Data.USER_REGISTER_WITHOUT_EMAIL,
        Data.USER_REGISTER_WITHOUT_PASS,
        Data.USER_REGISTER_WITHOUT_NAME
    ])
    def test_creation_user_success(self, user_data):
        status_code, response_context = UserMethods.create_user(user_data)
        expected_response_text = '{"success":false,"message":"Email, password and name are required fields"}'
        assert status_code == 403
        assert expected_response_text == response_context

        