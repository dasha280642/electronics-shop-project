from src.item import Item

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