from src.item import Item
class Phone(Item):
    def __init__(self, name, price, quantity, sim_cards):
        super().__init__(name, price, quantity)
        self.sim_cards = sim_cards

    def __add__(self, other):
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Cannot add Phone or Item with instances of other classes.")