import allure
import pytest

from api.courier_api import CourierApi
from data import ResponseMessages, TestData
from helpers import build_courier_data, build_credentials, generate_random_string, without_field


@allure.feature('Курьеры')
@allure.story('Авторизация курьера')
class TestCourierLogin:

    @allure.title('Курьер может авторизоваться, успешный ответ содержит id')
    def test_login_with_valid_credentials_returns_200_and_courier_id(self, registered_courier):
        response = CourierApi.login(build_credentials(registered_courier.payload))

        assert response.status_code == 200
        assert isinstance(response.json().get('id'), int)
        assert response.json()['id'] == registered_courier.courier_id

    @allure.title('Нельзя авторизоваться без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', TestData.REQUIRED_LOGIN_FIELDS)
    def test_login_without_required_field_returns_400_and_message(
        self,
        registered_courier,
        missing_field,
    ):
        credentials = without_field(build_credentials(registered_courier.payload), missing_field)

        response = CourierApi.login(credentials)

        assert response.status_code == 400
        assert response.json() == ResponseMessages.LOGIN_MISSING_DATA

    @allure.title('Нельзя авторизоваться с неверным логином')
    def test_login_with_incorrect_login_returns_404_and_message(self, registered_courier):
        credentials = build_credentials(registered_courier.payload)
        credentials['login'] = generate_random_string(16)

        response = CourierApi.login(credentials)

        assert response.status_code == 404
        assert response.json() == ResponseMessages.ACCOUNT_NOT_FOUND

    @allure.title('Нельзя авторизоваться с неверным паролем')
    def test_login_with_incorrect_password_returns_404_and_message(self, registered_courier):
        credentials = build_credentials(registered_courier.payload)
        credentials['password'] = generate_random_string(16)

        response = CourierApi.login(credentials)

        assert response.status_code == 404
        assert response.json() == ResponseMessages.ACCOUNT_NOT_FOUND

    @allure.title('Нельзя авторизоваться под несуществующим курьером')
    def test_login_with_nonexistent_courier_returns_404_and_message(self):
        response = CourierApi.login(build_credentials(build_courier_data()))

        assert response.status_code == 404
        assert response.json() == ResponseMessages.ACCOUNT_NOT_FOUND
