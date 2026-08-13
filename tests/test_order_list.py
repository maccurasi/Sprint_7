import allure

from api.order_api import OrderApi
from data import TestData


@allure.feature('Заказы')
@allure.story('Получение списка заказов')
class TestOrderList:

    @allure.title('В теле ответа возвращается список заказов')
    def test_get_orders_returns_200_and_orders_list(self):
        response = OrderApi.get_list(TestData.ORDERS_LIST_PARAMS)

        assert response.status_code == 200
        assert isinstance(response.json().get('orders'), list)

    @allure.title('Элементы списка заказов содержат трек-номер')
    def test_orders_in_list_contain_track(self, order_factory):
        order_factory()

        response = OrderApi.get_list(TestData.ORDERS_LIST_PARAMS)
        orders = response.json()['orders']

        assert response.status_code == 200
        assert len(orders) > 0
        assert all('track' in item for item in orders)
