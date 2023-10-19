class Item:
    discount_level = 0.85
    instances = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.instances.append(self)

    def get_total_cost(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.__class__.discount_level
