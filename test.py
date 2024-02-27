import pytest
from Connection.crud_ops import get_books, get_book_by_name, get_book_image, get_author_by_keyword
from Connection.agregations import get_top_authors
from src.plotting import plot_top_authors


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


def test_get_top_authors():
    res = get_top_authors()
    plot_top_authors(res)
    print(res)



def test_get_author_by_keyword():
    keyword = "Ma"
    res = get_author_by_keyword(keyword)
    print(res)
    assert res is not None
