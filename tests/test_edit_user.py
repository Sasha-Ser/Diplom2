from data import Data
import allure
import pytest
from methods.user_methods import UserMethods

class TestEditUser:

    @allure.title('Проверка успешной смены емайла у авторизованного пользователя')
    @pytest.mark.parametrize("user_new_data", [
        Data.USER_NEW_EMAIL,
        Data.USER_NEW_NAME
    ])
    def test_autorization_user_success(self, user_authorization, user_new_data):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = UserMethods.edit_user(Data.USER_REGISTER, user_new_data)
        assert status_code == 200
        assert f'"email":"{user_new_data['email']}","name":"{user_new_data['name']}' in response_context
        UserMethods.edit_user(user_new_data, Data.USER_REGISTER)


    @allure.title('Проверка неуспешной авторизации с невалидными данными')
    @pytest.mark.parametrize("user_data", [
        Data.USER_REGISTER_WITHOUT_EMAIL,
        Data.USER_REGISTER_WITHOUT_PASS,
        Data.USER_REGISTER_WRONG_EMAIL,
        Data.USER_REGISTER_WRONG_PASS
    ])
    def test_autorization_user_fail(self, user_data, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context, auth_token = UserMethods.login_user(user_data)
        assert status_code == 401
        assert Data.RESPONSE_TEXT_INCORRECT_PASS_OR_EMAIL == response_context

        