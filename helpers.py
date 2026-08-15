from copy import deepcopy
from datetime import date, timedelta
from uuid import uuid4


def generate_random_string(length=10):
    """Возвращает случайную строку заданной длины."""
    return uuid4().hex[:length]


def build_courier_data():
    """Собирает уникальный набор данных для регистрации курьера."""
    suffix = generate_random_string()
    return {
        "login": f"courier_{suffix}",
        "password": generate_random_string(12),
        "firstName": f"name_{suffix}",
    }


def build_credentials(courier_data):
    """Оставляет от данных курьера только логин и пароль."""
    return {
        "login": courier_data["login"],
        "password": courier_data["password"],
    }


def build_order_data():
    """Собирает тело заказа без указания цвета."""
    suffix = generate_random_string(8)
    return {
        "firstName": f"Test{suffix}",
        "lastName": "Autotest",
        "address": "Москва, Тестовая улица, 1",
        "metroStation": 4,
        "phone": "+7 999 000 00 00",
        "rentTime": 2,
        "deliveryDate": (date.today() + timedelta(days=2)).isoformat(),
        "comment": f"autotest-{suffix}",
    }


def without_field(payload, field):
    """Возвращает копию тела запроса без указанного поля."""
    changed_payload = deepcopy(payload)
    changed_payload.pop(field, None)
    return changed_payload
