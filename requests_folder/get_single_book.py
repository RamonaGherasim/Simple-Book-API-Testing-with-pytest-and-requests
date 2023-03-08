import requests


def get_single_book(book_id):
    r = requests.get(f"https://simple-books-api.glitch.me/books/{book_id}")
    return r