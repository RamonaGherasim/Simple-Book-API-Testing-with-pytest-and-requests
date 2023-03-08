from requests_folder.get_all_books import get_all_books


class TestBooks:
    # Toate numele metodelor trebuie sa iceapa cu test_
    def test_get_all_books_no_type_no_limit_status_code(self):
        r = get_all_books("", "")
        assert r.status_code == 200, f"Error: status code is not correct. " \
                                     f"Expected: 200, Actual: {r.status_code}"

    def test_get_all_books_no_type_no_limit_check_no_res(self):
        r = get_all_books("", "")
        assert len(r.json()) == 6, f"Error: length is not correct." \
                                   f"Expected: 6, Actual: {len(r.json())}"

    def test_get_all_books_type_fiction(self):
        r = get_all_books("fiction", "").json()
        status = get_all_books("fiction", "").status_code
        assert status == 200, f"Error: status code is not correct. " \
                              f"Expected: 200, Actual: {status}"
        assert len(r) == 4, f"ERROR! Expected: 4, Actual: {len(r)}"
        for i in r:
            assert i["type"] == "fiction", f"Error: Book {i['name']} has an invalid type"

    def test_get_all_books_type_non_fiction(self):
        r = get_all_books("non-fiction", "").json()
        status = get_all_books("non-fiction", "").status_code
        assert status == 200, f"Error: status code is not correct. " \
                              f"Expected: 200, Actual: {status}"
        assert len(r) == 2, f"ERROR! Expected: 2, Actual: {len(r)}"
        for i in r:
            assert i[
                       "type"] == "non-fiction", f"Error: Book {i['name']} has an invalid type"

    def test_get_all_books_type_invalid(self):
        r = get_all_books("pepelepe", "")
        assert r.status_code == 400
        assert r.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must " \
                               "be one of: fiction, non-fiction.", f"Error is not correct"

    def test_get_all_books_limit_invalid(self):
        r = get_all_books("", "22")
        assert r.status_code == 400
        assert r.json()[
                   "error"] == "Invalid value for query parameter 'limit'. " \
                               "Cannot be greater than 20.", f"Error is not correct"

    def test_get_all_books_type_fiction_limit_2(self):
        r = get_all_books("fiction", 2)
        status = r.status_code
        assert status == 200, f"Error: status code is not correct. " \
                              f"Expected: 200, Actual: {status}"
        assert len(r.json()) == 2, f"Error: invalid number of results for type 'fiction' and limit '2'. Expected 2, actual {len(r.json())}"
        for i in r.json():
            assert i["type"] == "fiction", f"Error: Book {i['name']} has an invalid type"

    def test_get_all_books_type_non_fiction_limit_1(self):
        r = get_all_books("non-fiction", 1)
        status = r.status_code
        assert status == 200, f"Error: status code is not correct. " \
                              f"Expected: 200, Actual: {status}"
        assert len(r.json()) == 1, f"Error: invalid number of results for type 'non-fiction' and limit '1'. Expected 1, actual {len(r.json())}"
        for i in r.json():
            assert i["type"] == "non-fiction", f"Error: Book {i['name']} has an invalid type"

    # Positive testing
    def test_get_all_books_limit_3(self):
        r = get_all_books("", 3)
        status = r.status_code
        assert status == 200, f"Error: status code is not correct. " \
                              f"Expected: 200, Actual: {status}"
        assert len(r.json()) == 3, f"Error: invalid number of results for limit '3'. Expected 3, actual {len(r.json())}"

    # Negative testing
    def test_all_books_limit_minus_7(self):
        r = get_all_books("", -7)
        status = r.status_code
        assert status == 400, "Status is not correct"
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0.", f"Error is not correct"