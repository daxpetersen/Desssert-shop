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

    def __str__(self):
        return self.name


class Candy(DessertItem):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.weight = weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.weight * self.price_per_pound

    def __str__(self):
        return f"{self.name}, {self.weight:.2f}lbs, ${self.price_per_pound:.2f}/lb, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"


class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_dozen

    def __str__(self):
        return f"{self.name}, {self.quantity} cookies, ${self.price_per_dozen:.2f}/dozen, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"


class IceCream(DessertItem):
    def __init__(self, name, scoops, price_per_scoop):
        super().__init__(name)
        self.scoops = scoops
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoops * self.price_per_scoop

    def __str__(self):
        return f"{self.name}, {self.scoops} scoops, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"


class Sundae(IceCream):
    def __init__(self, name, scoops, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoops, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

    def __str__(self):
        return f"{self.name} Sundae with {self.topping_name}, {self.scoops} scoops, ${self.price_per_scoop:.2f}/scoop, topping: ${self.topping_price:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"


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

    def __str__(self):
        receipt = [str(item) for item in self.order]
        subtotal = self.order_cost()
        tax = self.order_tax()
        total = subtotal + tax
        receipt.append(f"Order Subtotals, ${subtotal:.2f}, ${tax:.2f}")
        receipt.append(f"Order Total, ${total:.2f}")
        receipt.append(f"Total items in the order, {len(self.order)}")
        return "\n".join(receipt)
