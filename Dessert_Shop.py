from dessert import Candy, Cookie, IceCream, Sundae, Order

def display_candy_menu():
  print("\nAvailable Candies:")
  print("1. Candy Corn")
  print("2. Gummy Bears")
  print("3. Chocolate")

def display_cookie_menu():
  print("\nAvailable Cookies:")
  print("1. Chocolate Chip")
  print("2. Oatmeal Raisin")
  print("3. Peanut Butter")

def display_ice_cream_menu():
  print("\nAvailable Ice Cream Flavors:")
  print("1. Vanilla")
  print("2. Chocolate")
  print("3. Pistachio")
  print("4. Strawberry")

def display_sundae_menu():
  print("\nAvailable Sundae Flavors:")
  print("1. Vanilla")
  print("2. Chocolate")
  print("3. Strawberry")

def get_candy_order():
  display_candy_menu()
  name = input("Enter candy name: ")
  weight = float(input("Enter amount of pounds: "))
  price_per_pound = float(input("Enter price per pound: "))
  return Candy(name, weight, price_per_pound)

def get_cookie_order():
  display_cookie_menu()
  name = input("Enter cookie name: ")
  quantity = int(input("Enter quantity: "))
  price_per_dozen = float(input("Enter price per dozen: "))
  return Cookie(name, quantity, price_per_dozen)

def get_ice_cream_order():
  display_ice_cream_menu()
  name = input("Enter ice cream flavor: ")
  scoops = int(input("Enter number of scoops: "))
  price_per_scoop = float(input("Enter price per scoop: "))
  return IceCream(name, scoops, price_per_scoop)

def get_sundae_order():
  display_sundae_menu()
  name = input("Enter sundae flavor: ")
  scoops = int(input("Enter number of scoops: "))
  price_per_scoop = float(input("Enter price per scoop: "))
  topping_name = input("Enter topping name: ")
  topping_price = float(input("Enter topping price: "))
  return Sundae(name, scoops, price_per_scoop, topping_name, topping_price)

def main():
  order = Order()

  while True:
    print("\nChoose a dessert to add to your order:")
    print("1. Candy")
    print("2. Cookie")
    print("3. Ice Cream")
    print("4. Sundae")
    print("5. Finish")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      order.add(get_candy_order())
    elif choice == '2':
      order.add(get_cookie_order())
    elif choice == '3':
      order.add(get_ice_cream_order())
    elif choice == '4':
      order.add(get_sundae_order())
    elif choice == '5':
      break
    else:
      print("Invalid choice, please try again.")

  print("\nYour order:")
  for item in order.order:
    print(item.name)

  print("Total number of items in order:", len(order))

if __name__ == "__main__":
  main()
