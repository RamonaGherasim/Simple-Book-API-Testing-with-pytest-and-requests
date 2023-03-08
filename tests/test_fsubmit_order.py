from requests_folder.submit_order import submit_order


class TestSubmitOrder:
    orders_ids = []

    # Positive testing
    def test_submit_order(self):
        r = submit_order(1, "John")
        self.orders_ids.append(r.json()["orderId"])
        assert r.status_code == 201, f"Error: status code is not valid. Expected: 201, Actual: {r.status_code}"
        assert r.json()["created"], f"Error: Order creation status is not correct. Expected: True, Actual: {r.json()['created']}"
        assert len(r.json()["orderId"]) > 0, f"Error: Order id is invalid. Expected length must be greater than 0. Actual length: {len(r.json())}"

    # Positive testing
    def test_submit_order1(self):
        r = submit_order(3, "Ramona")
        self.orders_ids.append(r.json()["orderId"])
        assert r.status_code == 201, f"Error: status code is not valid. Expected: 201, Actual: {r.status_code}"
        assert r.json()["created"], f"Error: Order creation status is not correct. Expected: True, Actual: {r.json()['created']}"
        assert len(r.json()["orderId"]) > 0, f"Error: Order id is invalid. Expected length must be greater than 0. Actual length: {len(r.json())}"

    # Positive testing
    def test_submit_order2(self):
        r = submit_order(6, "John")
        self.orders_ids.append(r.json()["orderId"])
        assert r.status_code == 201, f"Error: status code is not valid. Expected: 201, Actual: {r.status_code}"
        assert r.json()["created"], f"Error: Order creation status is not correct. Expected: True, Actual: {r.json()['created']}"
        assert len(r.json()["orderId"]) > 0, f"Error: Order id is invalid. Expected length must be greater than 0. Actual length: {len(r.json())}"

    # Negative testing
    def test_submit_order_invalid_id(self):
        r = submit_order(1003, "John")
        assert r.status_code == 400, f"Error: status code is not valid. Expected: 201, Actual: {r.status_code}"
        assert r.json()["error"] == "Invalid or missing bookId.", f"Error is not correct!"