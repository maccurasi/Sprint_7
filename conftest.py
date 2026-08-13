from dataclasses import dataclass

import allure
import pytest

from api.courier_api import CourierApi
from api.order_api import OrderApi
from helpers import build_courier_data, build_credentials, build_order_data


@dataclass
class Courier:
    """Данные созданного курьера и ответ ручки создания."""

    payload: dict
    courier_id: int
    response: object


@dataclass
class Order:
    """Данные созданного заказа и ответ ручки создания."""

    payload: dict
    track: int
    response: object


@pytest.fixture
def courier_factory():
    """Создаёт курьеров по запросу теста и удаляет их после его выполнения."""
    created_courier_ids = []

    def create_courier(payload=None):
        courier_payload = payload if payload is not None else build_courier_data()
        response = CourierApi.create(courier_payload)

        courier_id = None
        if response.status_code == 201:
            login_response = CourierApi.login(build_credentials(courier_payload))
            if login_response.status_code == 200:
                courier_id = login_response.json()['id']
                created_courier_ids.append(courier_id)

        return Courier(courier_payload, courier_id, response)

    yield create_courier

    for courier_id in reversed(created_courier_ids):
        with allure.step(f'Удалить тестового курьера с id={courier_id}'):
            CourierApi.delete(courier_id)


@pytest.fixture
def registered_courier(courier_factory):
    """Готовый курьер для тестов, которым нужен существующий аккаунт."""
    courier = courier_factory()

    assert courier.response.status_code == 201, (
        f'Не удалось подготовить курьера: '
        f'{courier.response.status_code} {courier.response.text}'
    )
    assert courier.courier_id is not None, 'API не вернул id подготовленного курьера'

    return courier


@pytest.fixture
def order_factory():
    """Создаёт заказы по запросу теста и отменяет их после его выполнения."""
    created_tracks = []

    def create_order(payload=None):
        order_payload = payload if payload is not None else build_order_data()
        response = OrderApi.create(order_payload)

        track = None
        if response.status_code == 201:
            track = response.json()['track']
            created_tracks.append(track)

        return Order(order_payload, track, response)

    yield create_order

    for track in reversed(created_tracks):
        with allure.step(f'Отменить тестовый заказ с трек-номером {track}'):
            OrderApi.cancel(track)
