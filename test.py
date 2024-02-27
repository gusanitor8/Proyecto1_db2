import pytest
from Connection.DBConnection import get_books, get_book_by_name, get_book_image


def test_get_books():
    print()
    res = get_books(0, 10)
    print(res)
    assert res is not None


def test_get_book_by_name():
    name = "Kid I especially benefit recognize."
    print()
    res = get_book_by_name(name)
    print(res)
    assert res is not None


def test_get_book_image():
    book_tite = "Add perhaps including commercial cover."
    decoded_image = get_book_image(book_tite)
    print("")