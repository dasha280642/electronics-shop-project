import unittest
from src.item import Item
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

if __name__ == '__main__':
    unittest.main()
