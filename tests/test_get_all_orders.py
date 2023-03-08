from requests_folder.get_all_orders import get_all_orders, get_all_orders_invalid_token


class TestGetAllOrders:
    def test_get_all_orders_valid_token(self):
        r = get_all_orders()
        assert r.status_code == 200
        assert len(r.json()) == 3, f"Invalid number of results. Expected 3, actual {len(r.json())}"

    def test_get_all_orders_invalid_token(self):
        r = get_all_orders_invalid_token()
        assert r.status_code == 401
        assert r.json()['error'] == "Invalid bearer token.", "Invalid error"
