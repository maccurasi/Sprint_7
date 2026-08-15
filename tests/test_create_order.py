import allure
import pytest

from data import TestData
from helpers import build_order_data


@allure.feature('Заказы')
@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ создаётся с вариантом цвета: {case_name}')
    @pytest.mark.parametrize(
        ('case_name', 'colour_payload'),
        TestData.ORDER_COLOURS,
        ids=[case[0] for case in TestData.ORDER_COLOURS],
    )
    def test_create_order_with_colour_options_returns_201_and_track(
        self,
        order_factory,
        case_name,
        colour_payload,
    ):
        order = order_factory({**build_order_data(), **colour_payload})

        assert order.response.status_code == 201
        assert isinstance(order.response.json().get('track'), int)