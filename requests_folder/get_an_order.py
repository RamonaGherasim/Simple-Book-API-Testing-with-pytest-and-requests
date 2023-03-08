import requests
from requests_folder.get_token import access_token


def get_an_order(order_id):
    header_params = {'Authorization': access_token}
    r = requests.get(f"https://simple-books-api.glitch.me/orders/{order_id}",
                     headers=header_params)
    return r
