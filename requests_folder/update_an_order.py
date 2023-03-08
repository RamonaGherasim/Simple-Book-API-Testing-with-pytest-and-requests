import requests
from requests_folder.get_token import access_token


def update_an_order(customer_name, order_id):
    requests_body = {"customerName": customer_name}
    header_params = {'Authorization': access_token}
    r = requests.patch(f"https://simple-books-api.glitch.me/orders/{order_id}",
                     headers=header_params)
    return r
