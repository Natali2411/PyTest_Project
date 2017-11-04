import requests
#from conftest import app, book, book_new, book_ch, book_no_name

def test_book_create(app, book):
    response = app.create_book(book)
    assert response.status_code == 201
    response_body = response.json()
    book['id'] = response_body['id']
    assert response_body == book
    req_get = requests.get(app.base_url + 'books/' + str(response_body['id']))
    assert 200 <= req_get.status_code < 300
    print(req_get.json())
    assert req_get.json() == book

def test_book_change(app, book_new, book_ch):
    # b = book_new.json()
    resp = app.change_book(str(book_new['id']), book_ch)
    assert 200 <= resp.status_code < 300
    book_ch['id'] = resp.json()['id']
    assert book_ch == resp.json()






