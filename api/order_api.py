import allure
import requests

from urls import Urls

TIMEOUT = 30


class OrderApi:
    """Обёртки над ручками заказа."""

    @staticmethod
    @allure.step('Создать заказ')
    def create(payload):
        return requests.post(Urls.ORDERS, json=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step('Получить список заказов')
    def get_list(params=None):
        return requests.get(Urls.ORDERS, params=params, timeout=TIMEOUT)

    @staticmethod
    @allure.step('Отменить заказ с трек-номером {track}')
    def cancel(track):
        return requests.put(Urls.ORDER_CANCEL, json={"track": track}, timeout=TIMEOUT)
