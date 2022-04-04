from List import *
import pytest
from typing import List

tests = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], [Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)]),\
    ([Product('bread', 50.0)], [Product('bread', 50.0)])]
@pytest.mark.parametrize('basket, ideal', tests)
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

tests1 = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], [Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)]),\
    ([Product('bread', 50.0)], [Product('bread', 50.0)])]

@pytest.mark.parametrize('basket, ideal', tests1)
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

test3 = [([Product('bread', 50.0), Product('carrot', 20.0), Product('tea', 100.0)], 170.0)]
@pytest.mark.parametrize('product, s', test3)
def test_summ(product: Product, s: float):
    basket3 = Basket()
    for p in product:
        basket3.add(p)
    assert s == basket3.count_sum()

test4 = [('bread', 50.0), ('carrot', 20.0)]
def test_field():
    bread = Product('bread', 50.0)
    assert bread.name == 'bread'


@pytest.mark.parametrize('name, price', test4)
def test_name(name: str, price: float):
    field_name = Product(name, price)
    assert field_name.name == name


@pytest.mark.parametrize('name, price', test4)
def test_price(name: str, price: float):
    field_price = Product(name, price)
    assert field_price.price == price

