from data import Data
import allure
import pytest
from methods.user_methods import UserMethods

class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_autorization_user_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, token_auth = UserMethods.login_user(Data.USER_REGISTER)
        expected_response_text = f'"email":"{Data.USER_REGISTER['email']}","name":"{Data.USER_REGISTER['name']}"'
        assert status_code == 200
        assert expected_response_text in response_context

    @allure.title('Проверка неуспешной авторизации с невалидными данными')
    @pytest.mark.parametrize("user_data", [
        Data.USER_REGISTER_WITHOUT_EMAIL,
        Data.USER_REGISTER_WITHOUT_PASS,
        Data.USER_REGISTER_WRONG_EMAIL,
        Data.USER_REGISTER_WRONG_PASS
    ])
    def test_autorization_user_fail(self, user_data, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, token_auth = UserMethods.login_user(user_data)
        expected_response_text = '{"success":false,"message":"email or password are incorrect"}'
        assert status_code == 401
        assert expected_response_text == response_context

        