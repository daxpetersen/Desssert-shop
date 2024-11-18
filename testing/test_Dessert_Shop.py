from Dessert import Candy, Cookie, IceCream, Sundae

def test_candy():
    candy_item = Candy("Chocolate", 2.5, 3.00)
    assert candy_item.calculate_cost() == 7.5
    assert candy_item.name == "Chocolate"
    assert candy_item.weight == 2.5

def test_cookie():
    cookie_item = Cookie("Oatmeal Raisin", 24, 5.00)
    assert cookie_item.calculate_cost() == 10.0
    assert cookie_item.name == "Oatmeal Raisin"
    assert cookie_item.quantity == 24

def test_ice_cream():
    ice_cream_item = IceCream("Vanilla", 3, 2.50)
    assert ice_cream_item.calculate_cost() == 7.5
    assert ice_cream_item.name == "Vanilla"
    assert ice_cream_item.scoops == 3

def test_sundae():
    sundae_item = Sundae("Strawberry", 2, 2.50, "Whipped Cream", 1.00)
    assert sundae_item.calculate_cost() == 6.0 
    assert sundae_item.name == "Strawberry"
    assert sundae_item.topping_name == "Whipped Cream"
