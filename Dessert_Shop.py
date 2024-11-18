import pygame
from Dessert import Candy, Cookie, IceCream, Sundae, Order
pygame.init()
screen = pygame.display.set_mode((400,720))
def main():
    def __init__(self):
        self.active = True
        self.color = 255,255,255
    def show_screen(self,color):
        print(screen(self.color))
    order = Order()

    while True:
        print("Choose a dessert to add to your order:")
        print("1. Candy")
        print("2. Cookie")
        print("3. Ice Cream")
        print("4. Sundae")
        print("5. Finish Order")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nAvailable Candies:")
            print("1. Candy Corn")
            print("2. Gummy Bears")
            print("3. Chocolate")
            name = input("Enter candy name: ")
            weight = float(input("Enter amount of pounds: "))
            price_per_pound = float(input("Enter price per pound: "))
            order.add(Candy(name, weight, price_per_pound))

        elif choice == '2':
            print("\nAvailable Cookies:")
            print("1. Chocolate Chip")
            print("2. Oatmeal Raisin")
            print("3. Peanut Butter")
            name = input("Enter cookie name: ")
            quantity = int(input("Enter quantity: "))
            price_per_dozen = float(input("Enter price per dozen: "))
            order.add(Cookie(name, quantity, price_per_dozen))

        elif choice == '3':
            print("\nAvailable Ice Cream Flavors:")
            print("1. Vanilla")
            print("2. Chocolate")
            print("3. Pistachio")
            print("4. Strawberry")
            name = input("Enter ice cream flavor: ")
            scoops = int(input("Enter number of scoops: "))
            price_per_scoop = float(input("Enter price per scoop: "))
            order.add(IceCream(name, scoops, price_per_scoop))

        elif choice == '4':
            print("\nAvailable Sundae Flavors:")
            print("1. Vanilla")
            print("2. Chocolate")
            print("3. Strawberry")
            name = input("Enter sundae flavor: ")
            scoops = int(input("Enter number of scoops: "))
            price_per_scoop = float(input("Enter price per scoop: "))
            topping_name = input("Enter topping name: ")
            topping_price = float(input("Enter topping price: "))
            order.add(Sundae(name, scoops, price_per_scoop, topping_name, topping_price))

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
