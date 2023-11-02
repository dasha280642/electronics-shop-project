from src.item import Item
import unittest
def test_get_total_cost():
    item = Item("Телефон", 10000, 5)
    assert item.get_total_cost() == 50000

def test_apply_discount():
    item = Item("Телефон", 10000, 5)
    item.apply_discount()
    assert item.price == 8500


def test_instantiate_from_csv():
    item1 = Item("Item1", 10.0, 2)
    item2 = Item("Item2", 20.0, 3)
    item3 = Item("Item3", 30.0, 4)

    Item.instantiate_from_csv()

    assert len(Item.instances) == 6
    assert Item.instances[3].name == "Item4"
    assert Item.instances[3].price == 40.0
    assert Item.instances[3].quantity == 5
    assert Item.instances[4].name == "Item5"
    assert Item.instances[4].price == 50.0
    assert Item.instances[4].quantity == 6
    assert Item.instances[5].name == "Item6"
    assert Item.instances[5].price == 60.0
    assert Item.instances[5].quantity == 7
def test_string_to_number():
    assert Item.string_to_number("10.0") == 10.0
    assert Item.string_to_number("20.5") == 20.5
    assert Item.string_to_number("30") == 30.0
    assert Item.string_to_number("-5.5") == -5.5
    assert Item.string_to_number("0") == 0.0

class ItemTests(unittest.TestCase):
    def setUp(self):
        self.item = Item("Test Item", 10.0, 5)

    def test_repr(self):
        expected = "Item('Test Item', 10.0, 5)"
        actual = repr(self.item)
        self.assertEqual(actual, expected)

    def test_str(self):
        expected = "Name: Test Item, Price: 10.0, Quantity: 5"
        actual = str(self.item)
        self.assertEqual(actual, expected)



from src.phone import Phone

class PhoneTests(unittest.TestCase):
    def setUp(self):
        self.phone1 = Phone("iPhone X", 1000, 10, 2)
        self.phone2 = Phone("Samsung Galaxy S10", 900, 5, 1)
        self.item1 = Item("Headphones", 50, 20)

    def test_phone_attributes(self):
        self.assertEqual(self.phone1.name, "iPhone X")
        self.assertEqual(self.phone1.price, 1000)
        self.assertEqual(self.phone1.quantity, 10)
        self.assertEqual(self.phone1.sim_cards, 2)

    def test_add_phone_instances(self):
        result = self.phone1 + self.phone2
        self.assertEqual(result, 15)

    def test_add_phone_and_item_instances(self):
        result = self.phone1 + self.item1
        self.assertEqual(result, 30)

    def test_add_phone_with_other_class_instance(self):
        with self.assertRaises(TypeError):
            result = self.phone1 + "test"

