from List import *
import pytest
from typing import List

tests_first = [([Product('banana', 50.0), Product('lemon', 20.0), Product('cake', 100.0)], [Product('banana', 50.0), Product('lemon', 20.0), Product('cake', 100.0)]),\
    ([Product('banana', 50.0)], [Product('banana', 50.0)])]
@pytest.mark.parametrize('basket, ideal', tests_first)
def test_add(basket: List[Product], ideal : List[Product]):
    basket1 = Basket()
    for p in basket:
        basket1.add(p)
    is_equal = True
    for p1, p2 in zip(ideal, basket1.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            is_equal = False
            break
    assert is_equal

tests_second = [([Product('banana', 50.0), Product('lemon', 20.0), Product('cake', 100.0)], [Product('banana', 50.0), Product('lemon', 20.0), Product('cake', 100.0)]),\
    ([Product('banana', 50.0)], [Product('banana', 50.0)])]

@pytest.mark.parametrize('basket, ideal', tests_second)
def test_remove(basket: List[Product], ideal : List[Product]):
    basket2 = Basket()
    for p in basket:
        basket2.add(p)
        basket2.remove(p)
    is_equal = True
    for p1, p2 in zip(ideal, basket2.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            is_equal = False
            break
    assert is_equal

test_third = [([Product('banana', 50.0), Product('lemon', 20.0), Product('cake', 100.0)], 170.0)]
@pytest.mark.parametrize('product, s', test_third)
def test_summ(product: Product, s: float):
    basket3 = Basket()
    for p in product:
        basket3.add(p)
    assert s == basket3.count_sum()

test_fourth = [('banana', 50.0), ('lemon', 20.0)]
def test_field():
    bread = Product('banana', 50.0)
    assert bread.name == 'banana'


@pytest.mark.parametrize('name, price', test_fourth)
def test_name(name: str, price: float):
    field_name = Product(name, price)
    assert field_name.name == name


@pytest.mark.parametrize('name, price', test_fourth)
def test_price(name: str, price: float):
    field_price = Product(name, price)
    assert field_price.price == price
