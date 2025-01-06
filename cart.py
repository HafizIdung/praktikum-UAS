from item import Item

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append(Item(name, price, quantity))

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def calculate_total_quantity(self):
        return sum(item.quantity for item in self.items)

