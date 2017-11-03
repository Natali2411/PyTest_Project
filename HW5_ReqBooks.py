import requests

class ReqBooks():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add_book(self, url, book_data):
        book = requests.post(url, data=book_data)
        book = book.json()['id']
        return book

    def change_book(self, url, book_data):
        ch_book = requests.put(url, data=book_data)
        return ch_book.status_code

    def delete_book(self, url, id):
        del_book = requests.delete(url + str(id) + '/')
        del_status = del_book.status_code
        return del_status

