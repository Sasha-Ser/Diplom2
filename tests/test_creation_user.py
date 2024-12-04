from data import Data
import allure
import pytest
from methods.user_methods import UserMethods

class TestCreationUser:

    @allure.title('Проверка успешного создания пользователя')
    def test_creation_user_success(self, user_authorization):
        status_code, response_context = UserMethods.create_user(Data.USER_REGISTER)
        assert status_code == 200
        assert Data.RESPONSE_TEXT_CREATE_USER_SUCCESS in response_context

    @allure.title('Проверка не создания пользователя с существующими данными')
    def test_creation_clone_user_success(self, user_authorization):
        UserMethods.create_user(Data.USER_REGISTER)
        status_code, response_context = UserMethods.create_user(Data.USER_REGISTER)
        assert status_code == 403
        assert Data.RESPONSE_TEXT_EXISTING_USER == response_context

    @allure.title('Проверка не создания пользователя без обязательных полей')
    @pytest.mark.parametrize("user_data", [
        Data.USER_REGISTER_WITHOUT_EMAIL,
        Data.USER_REGISTER_WITHOUT_PASS,
        Data.USER_REGISTER_WITHOUT_NAME
    ])
    def test_creation_user_success(self, user_data):
        status_code, response_context = UserMethods.create_user(user_data)
        assert status_code == 403
        assert Data.RESPONSE_TEXT_WITHOUT_REQUIRED_FIELD == response_context

        