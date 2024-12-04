from data import Data
import allure
import pytest
from methods.user_methods import UserMethods

class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_autorization_user_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, token_auth = UserMethods.login_user(Data.USER_REGISTER)
        assert status_code == 200
        assert Data.RESPONSE_TEXT_CREATE_USER_SUCCESS in response_context

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
        assert status_code == 401
        assert Data.RESPONSE_TEXT_INCORRECT_PASS_OR_EMAIL == response_context

        