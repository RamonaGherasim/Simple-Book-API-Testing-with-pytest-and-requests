from requests_folder.get_status import get_status


class TestGetStatus:
    def test_get_api_status(self):
        r = get_status().status_code
        assert r == 200, f"API status error. Expected 200, actual {r}"
