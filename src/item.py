class Item:
    discount_level = 0.85
    instances = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.__quantity = quantity
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

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self.__quantity = value
        else:
            raise ValueError('Количество должно быть больше или равно 1.')

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


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value >= 1:
            self.__number_of_sim = value
        else:
            raise ValueError('Количество сим-карт должно быть больше или равно 1.')

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Number of SIM: {self.number_of_sim}"



#Доп класс
class LanguageMixin:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self, lang):
        if lang == "EN" or lang == "RU":
            self.__language = lang
        else:
            raise ValueError("Invalid language. Only EN and RU are supported.")



class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Language: {self.language}"


