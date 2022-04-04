from typing import List

class Product():
    name: str
    price:  float
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket:
    def __init__(self):
        self.basket: List[Product] = []
    def add(self, product: Product):
        self.basket.append(product)
        return self.basket

    def remove(self, name: str):
        for product in self.basket:
            if product.name == name:
                self.basket.remove(product)
        return self.basket

    def count_sum(self):
        summ = 0
        for i in range(0, len(self.basket)):
            summ += self.basket[i].price
        return summ