class Item:
    discount_level = 0.85
    instances = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    def get_total_cost(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.__class__.discount_level

    @classmethod
    def instantiate_from_csv(cls):
        with open('src/items.csv', 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(string):
        return float(string)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"