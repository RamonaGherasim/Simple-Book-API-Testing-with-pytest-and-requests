from requests_folder.update_an_order import update_an_order
from tests.test_fsubmit_order import TestSubmitOrder


class TestUpdateAnOrder:
    def test_update_an_order(self):
        orders = TestSubmitOrder.orders_ids
        r = update_an_order("Adela", orders[0])
        assert r.status_code == 204, "Error, invalid status code"
