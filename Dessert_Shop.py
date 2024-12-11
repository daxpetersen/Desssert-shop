from Dessert import Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt

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
            name = input("Enter candy name: ")
            weight = float(input("Enter weight in pounds: "))
            price_per_pound = float(input("Enter price per pound: "))
            order.add(Candy(name, weight, price_per_pound))
        elif choice == '2':
            name = input("Enter cookie name: ")
            quantity = int(input("Enter quantity: "))
            price_per_dozen = float(input("Enter price per dozen: "))
            order.add(Cookie(name, quantity, price_per_dozen))
        elif choice == '3':
            name = input("Enter ice cream flavor: ")
            scoops = int(input("Enter number of scoops: "))
            price_per_scoop = float(input("Enter price per scoop: "))
            order.add(IceCream(name, scoops, price_per_scoop))
        elif choice == '4':
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

    data = [["Name", "Item Cost", "Tax"]]
    for item in order.order:
        data.append([item.name, f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"])
    data.append(["Order Subtotals", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
    data.append(["Order Total", "", f"${order.order_cost() + order.order_tax():.2f}"])
    data.append(["Total items in the order", "", len(order)])

    make_receipt(data, "receipt.pdf")
    print("\nReceipt has been generated as 'receipt.pdf'.")

if __name__ == "__main__":
    main()
