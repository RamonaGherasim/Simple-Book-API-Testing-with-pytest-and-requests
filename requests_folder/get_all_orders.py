import requests
from requests_folder.get_token import access_token


def get_all_orders():
    header_params = {'Authorization': access_token}
    r = requests.get("https://simple-books-api.glitch.me/orders", headers=header_params)
    return r


def get_all_orders_invalid_token():
    token = "1dsjfkjdsf232"
    header_params = {'Authorization': token}
    r = requests.get("https://simple-books-api.glitch.me/orders",
                     headers=header_params)
    return r
