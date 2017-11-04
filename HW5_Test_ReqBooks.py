import unittest
import requests
from HW5_ReqBooks import ReqBooks

class Test_Req_Books(unittest.TestCase):

    base_url = 'http://pulse-rest-testing.herokuapp.com/'

    def setUp(self):
        self.b1 = ReqBooks('War and Peace', 'Lev Tolstoy')
        self.book_data = {'title': self.b1.title, 'author': self.b1.author}

    def test_add_book(self):
        book = self.b1.add_book(self.base_url + 'books/', self.book_data)
        self.book_data['id'] = book
        self.assertEqual(requests.get(self.base_url + 'books/' + str(book) + '/').json()['title'],'War and Peace')
        self.assertEqual(requests.get(self.base_url + 'books/' + str(book) + '/').json()['author'], 'Lev Tolstoy')

    def test_change_book(self):
        book = self.b1.add_book(self.base_url + 'books/', self.book_data)
        self.book_data['id'] = book
        ch_book_data = {'title': 'Delirium', 'author': 'Loren Oliver'}
        ch_book = self.b1.change_book(self.base_url + 'books/' + str(book) + '/', ch_book_data)
        if 200 <= ch_book < 300:
            res = True
        self.assertTrue(res)
        self.assertEqual(requests.get(self.base_url + 'books/' + str(book) + '/').json()['title'],'Delirium')
        self.assertEqual(requests.get(self.base_url + 'books/' + str(book) + '/').json()['author'], 'Loren Oliver')

    def tearDown(self):
        d = self.b1.delete_book(str(self.base_url) + 'books/', str(self.book_data['id']))




