from requests_folder.delete_an_order import delete_an_order
from tests.test_fsubmit_order import TestSubmitOrder


class TestDeleteAnOrder:
    def test_delete_an_order_valid_order_id(self):
        order_to_delete = TestSubmitOrder.orders_ids[1]

        r = delete_an_order(order_to_delete)
        assert r.status_code == 204, "Error, invalid status code."

    def test_delete_an_order_invalid_order_id(self):
        r = delete_an_order("fsfdskjjk12124")
        assert r.status_code == 404, "Error, invalid status code."
        assert r.json()['error'] == "No order with id fsfdskjjk12124.", f"Error, invalid error message." \
