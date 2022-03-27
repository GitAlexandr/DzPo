import pytest
from List import *

tests = [('potato', 50.0), ('apple', 50.0), ('melon', 100.0)]

def test_field():
    potato = Product('potato', 66.8)
    assert potato.name == 'potato'


@pytest.mark.parametrize('name, value', tests)
def test_field_name(name: str, value: float):
    ex = Product(name, value)
    assert ex.name == name


@pytest.mark.parametrize('name, value', tests)
def test_field_value(name: str, value: float):
    ex = Product(name, value)
    assert ex.value == value


test_1 = [([Product('potato', 50.0), Product('apple', 50.0), Product('melon', 100.0)], 'add')]

@pytest.mark.parametrize('products, s', test_1)
def test_add_cart(products: Product, s: str):
    cart_1 = Cart()
    for p in products:
        cart_1.add(p)
        assert s == cart_1.add(p)


test_2 = [([Product('potato', 50.0), Product('apple', 50.0), Product('melon', 100.0)], 'remove')]

@pytest.mark.parametrize('products, s', test_2)
def test_remove_cart(products: Product, s: str):
    cart_2 = Cart()
    for p in products:
        cart_2.add(p)
        assert s == cart_2.remove(p)


test_3 = [([Product('potato', 50.0), Product('apple', 50.0), Product('melon', 100.0)], 200.0)]

@pytest.mark.parametrize('products, s', test_3)
def test_count_sum_cart(products: Product, s: float):
    cart_3 = Cart()
    for p in products:
        cart_3.add(p)
    assert s == cart_3.count_sum()




