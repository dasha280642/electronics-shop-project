from src.item import Item

def test_get_total_cost():
    item = Item("Телефон", 10000, 5)
    assert item.get_total_cost() == 50000

def test_apply_discount():
    item = Item("Телефон", 10000, 5)
    item.apply_discount()
    assert item.price == 8500