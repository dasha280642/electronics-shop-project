class InstantiateCSVError(Exception):
    pass

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
        try:
            with open('../homework-6/items.csv', 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    cls(name, float(price), int(quantity))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except ValueError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string):
        return float(string)
