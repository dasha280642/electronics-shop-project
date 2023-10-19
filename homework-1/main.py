from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 5)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.get_total_cost())  
    print(item2.get_total_cost())  

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)
    print(item2.price)

    print(Item.apply_discount)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
