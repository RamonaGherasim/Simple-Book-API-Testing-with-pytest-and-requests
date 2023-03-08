import requests


def get_all_books(type="", limit=""):
    if type == "" and limit == "":
        r = requests.get("https://simple-books-api.glitch.me/books")
        # requests e o metoda built-in din cadrul librariei requests.
    elif type != "" and limit == "":
        r = requests.get(f"https://simple-books-api.glitch.me/books?type={type}")
    elif type == "" and limit != "":
        r = requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}")
    else:
        r = requests.get(f"https://simple-books-api.glitch.me/books?type={type}&limit={limit}")
    return r