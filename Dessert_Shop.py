from Dessert import Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt


class DessertShop:
    def user_prompt_candy(self):
        name = input("Enter the name of the candy: ")
        while True:
            try:
                weight = float(input("Enter the weight (in pounds): "))
                if weight <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for weight.")

        while True:
            try:
                price_per_pound = float(input("Enter the price per pound: "))
                if price_per_pound <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for price per pound.")

        candy = Candy(name, weight, price_per_pound)
        candy.packaging = "Bag"  # Set the default packaging
        return candy

    def user_prompt_cookie(self):
        name = input("Enter the name of the cookie: ")
        while True:
            try:
                quantity = int(input("Enter the quantity purchased: "))
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive integer for quantity.")

        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: "))
                if price_per_dozen <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for price per dozen.")

        cookie = Cookie(name, quantity, price_per_dozen)
        cookie.packaging = "Box"  # Set the default packaging
        return cookie

    def user_prompt_icecream(self):
        name = input("Enter the name of the ice cream: ")
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive integer for the number of scoops.")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for price per scoop.")

        ice_cream = IceCream(name, scoops, price_per_scoop)
        ice_cream.packaging = "Bowl"  # Set the default packaging
        return ice_cream

    def user_prompt_sundae(self):
        name = input("Enter the name of the sundae: ")
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive integer for the number of scoops.")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for price per scoop.")

        topping_name = input("Enter the topping: ")
        while True:
            try:
                topping_price = float(input("Enter the price for the topping: "))
                if topping_price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number for topping price.")

        sundae = Sundae(name, scoops, price_per_scoop, topping_name, topping_price)
        sundae.packaging = "Boat"  # Set the default packaging
        return sundae


def main():
    shop = DessertShop()
    order = Order()

    print("\nEnter the quantities for each item type. If you don't want an item, enter 0.")

    try:
        candy_qty = int(input("How many types of candy? "))
        for _ in range(candy_qty):
            order.add(shop.user_prompt_candy())

        cookie_qty = int(input("How many types of cookies? "))
        for _ in range(cookie_qty):
            order.add(shop.user_prompt_cookie())

        icecream_qty = int(input("How many types of ice cream? "))
        for _ in range(icecream_qty):
            order.add(shop.user_prompt_icecream())

        sundae_qty = int(input("How many types of sundaes? "))
        for _ in range(sundae_qty):
            order.add(shop.user_prompt_sundae())

    except ValueError:
        print("Invalid input. Please restart and provide valid quantities.")
        return

    print("\nReceipt:")
    print(order)

    data = [["Name", "Packaging", "Item Cost", "Tax"]]
    for item in order.order:
        data.append(
            [item.name, item.packaging, f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"]
        )
    subtotal = order.order_cost()
    tax = order.order_tax()
    data.append(["Order Subtotals", "", f"${subtotal:.2f}", f"${tax:.2f}"])
    data.append(["Order Total", "", "", f"${subtotal + tax:.2f}"])
    data.append(["Total items in the order", "", "", len(order)])

    make_receipt.build(data, "receipt.pdf")
    print("\nReceipt has been generated as 'receipt.pdf'.")


if __name__ == "__main__":
    main()
