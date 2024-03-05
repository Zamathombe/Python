class Donut:
    def __init__(self, flavor, price, availability):
        self.flavor = flavor
        self.price = price  # Assuming the price is already in Rands
        self.availability = availability

    def __str__(self):
        return f"{self.flavor} - R{self.price}{' (Available)' if self.availability else ' (Sold Out)'}"


class DonutShop:
    def __init__(self):
        self.available_donuts = [
            Donut("Chocolate Glazed", 15.0, True),  # Adjust prices as needed
            Donut("Strawberry Frosted", 18.0, True),
            Donut("Maple Bacon", 22.0, False),
            # Add more donuts as needed
        ]
        self.orders = []

    def display_menu(self):
        print("Menu:")
        for donut in self.available_donuts:
            print(donut)

    def place_order(self, flavor, quantity):
        donut = next((d for d in self.available_donuts if d.flavor.lower() == flavor.lower() and d.availability), None)
        if donut:
            total_price = donut.price * quantity
            self.orders.append({"flavor": donut.flavor, "quantity": quantity, "total_price": total_price})
            donut.availability = False
            print(f"Order placed: {quantity} {donut.flavor} - Total: R{total_price}")
        else:
            print(f"Sorry, {flavor} is either unavailable or does not exist in the menu.")

    def display_orders(self):
        print("\nCurrent Orders:")
        for order in self.orders:
            print(f"{order['quantity']} {order['flavor']} - Total: R{order['total_price']}")


def main():
    donut_shop = DonutShop()

    while True:
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Display Orders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            donut_shop.display_menu()
        elif choice == "2":
            flavor = input("Enter the flavor of the donut you want to order: ")
            quantity = int(input("Enter the quantity: "))
            donut_shop.place_order(flavor, quantity)
        elif choice == "3":
            donut_shop.display_orders()
        elif choice == "4":
            print("Thank you for ordering from the Donut Shop. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

