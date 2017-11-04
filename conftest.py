import pytest
from HW6_ReqBooks import ReqBooks

@pytest.fixture(scope="session")
def app():
    app = ReqBooks("pulse-rest-testing.herokuapp.com")
    yield app
    app.delete_books()

@pytest.fixture
def book():
    return {"title": "Delirium", "author": "Loren Oliver"}

@pytest.fixture
def book_new(app, book):
    t = app.create_book(book)
    return t.json()

@pytest.fixture()
def book_ch():
    return {"title": "Pandemonium", "author": "Loren Oliver"}

@pytest.fixture
def book_no_name():
    return {"author": "author"}