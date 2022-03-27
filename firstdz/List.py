from typing import List

class Product():
     name: str
     value:  float
     def __init__(self, name, value):
         self.name = name
         self.value = value

class Cart():
    def __init__(self):
        self.cart: List[Product] = []
    
    def add(self, product: Product):
        self.cart.append(product)
        return 'add'

    def remove(self, product: Product):
        self.cart.remove(product)
        return 'remove'
    
    def count_sum(self):
        summa = 0
        for i in range(0, len(self.cart)):
            summa += self.cart[i].value
        return summa



