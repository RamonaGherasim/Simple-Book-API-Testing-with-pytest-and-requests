from requests_folder.get_single_book import get_single_book


class TestGetSingleBook:
    def test_get_single_book_id1(self):
        r = get_single_book("1")
        assert r.status_code == 200, f"Error, status code is incorrect"

    def test_get_single_book_id6(self):
        r = get_single_book(6)
        assert r.status_code == 200, f"Error, status code is incorrect"

    def test_get_single_book_id_invalid(self):
        r = get_single_book("10")
        assert r.status_code == 404, f"Error, status code is incorrect"
        assert r.json()['error'] == "No book with id 10"
