import pytest
from Connection.DBConnection import get_books

def test_get_books():
    print()
    res = get_books(0, 10)
    print(res)
    assert res is not None
