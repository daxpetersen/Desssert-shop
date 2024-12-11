from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent / 100)


class Candy(DessertItem):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.weight = weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.weight * self.price_per_pound


class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_dozen


class IceCream(DessertItem):
    def __init__(self, name, scoops, price_per_scoop):
        super().__init__(name)
        self.scoops = scoops
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoops * self.price_per_scoop


class Sundae(IceCream):
    def __init__(self, name, scoops, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoops, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price


class Order:
    def __init__(self):
        self.order = []

    def add(self, dessert_item):
        self.order.append(dessert_item)

    def order_cost(self):
        return sum(item.calculate_cost() for item in self.order)

    def order_tax(self):
        return sum(item.calculate_tax() for item in self.order)

    def __len__(self):
        return len(self.order)


