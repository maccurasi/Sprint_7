import allure
import requests

from urls import Urls

TIMEOUT = 30


class CourierApi:
    """Обёртки над ручками курьера."""

    @staticmethod
    @allure.step('Создать курьера')
    def create(payload):
        return requests.post(Urls.COURIER, json=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step('Авторизовать курьера')
    def login(payload):
        return requests.post(Urls.COURIER_LOGIN, json=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step('Удалить курьера с id={courier_id}')
    def delete(courier_id):
        return requests.delete(f'{Urls.COURIER}/{courier_id}', timeout=TIMEOUT)
