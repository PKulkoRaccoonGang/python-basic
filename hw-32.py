class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.name}, price: {self.price}'


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt
        self.total = sum(product.price * quantity for product, quantity in self.products.items())

    def __str__(self):
        items_str = '\n'.join(f'{product.name}: {quantity} pcs.' for product, quantity in self.products.items())
        return f'User: {self.user}\nItems:\n{items_str}\n'

    def get_total(self):
        return self.total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
# New product
tomato = Item('tomato', 3, "red", "small", )
print(lemon)  # lemon, price: 5
print(tomato)  # tomato, price: 3

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

# New user
buyer_2 = User("Peter", "Kulko", "03625271")
print(buyer_2)  # Peter Kulko

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

# New user

cart_2 = Purchase(buyer_2)
cart_2.add_item(apple, 20)
cart_2.add_item(tomato, 10)
print(cart_2)

"""
User: Peter Kulko
Items:
apple: 20 pcs.
tomato: 10 pcs.
"""

print(cart_2.get_total())

assert isinstance(cart_2.user, User) is True, 'Екземпляр класу User'
assert cart_2.get_total() == 70, "Всього 70"
cart_2.add_item(lemon, 4)
assert cart_2.get_total() == 90, "Всього 90"

print(cart_2)

"""
User: Peter Kulko
Items:
apple: 20 pcs.
tomato: 10 pcs.
lemon: 4 pcs.
"""
