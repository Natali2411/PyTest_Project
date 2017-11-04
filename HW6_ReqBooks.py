import requests

class ReqBooks:
    def __init__(self, domain="localhost"):
        self.base_url = "http://{}/".format(domain)

    def create_book(self, book):
        r = requests.post(self.base_url + "books/", data=book)
        return r

    def change_book(self, b_id, book_new):
        ch_book = requests.put(self.base_url + "books/" + str(b_id) + '/', data=book_new)
        return ch_book

    def delete_books(self):
        books = requests.get(self.base_url + "books/").json()
        if books:
            for book in books:
                # requests.delete(self.base_url+"books/"+ str(book['id'])+ '/')
                r = requests.get(self.base_url + "books/" + str(book['id']) + '/')
                print(r.json())