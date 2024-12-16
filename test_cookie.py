from Dessert import DessertItem
class Cookie(DessertItem):
    def __init__(self, name, number, price_per_dozen):
        super().__init__(name)
        self.number = number
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
