from requests_folder.get_an_order import get_an_order
from tests.test_fsubmit_order import TestSubmitOrder


class TestGetAnOrder:
    def test_get_an_order_valid_order_id(self):
        orders = TestSubmitOrder.orders_ids
        for order_id in orders:
            r = get_an_order(order_id)
            assert r.status_code == 200
            assert r.json()['id'] == order_id, f"Error, order id's do not match. Expected {order_id}, actual {r.json()['id']}"

    def test_get_an_order_invalid_order_id(self):
        r = get_an_order("adlsfeslefdsl")
        assert r.status_code == 404, "Error, invalid status code."
        assert r.json()['error'] == "No order with id adlsfeslefdsl.", f"Error, invalid error message."