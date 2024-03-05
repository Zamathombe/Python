class ChickenOrder:
    def __init__(self, flavor, spice_level, quantity):
        self.flavor = flavor
        self.spice_level = spice_level
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        # Assuming each chicken has a base price and additional cost based on spice level
        base_price = 10.0  # Base price per chicken
        spice_price = 2.0 * self.spice_level  # Additional cost based on spice level
        return (base_price + spice_price) * self.quantity

    def display_details(self):
        print(f"{self.quantity} {self.flavor} Chicken(s) - Spice Level {self.spice_level}")
        print(f"Total Price: ${self.total_price}\n")


class ChickenOnlineStore:
    def __init__(self):
        self.available_chickens = [
            "Classic",
            "Spicy",
            "Garlic Parmesan",
            # Add more chicken flavors as needed
        ]
        self.orders = []

    def display_chicken_menu(self):
        print("Chicken Menu:")
        for i, flavor in enumerate(self.available_chickens, start=1):
            print(f"{i}. {flavor}")

    def place_chicken_order(self, flavor, spice_level, quantity):
        if flavor not in self.available_chickens:
            print("Invalid chicken flavor. Please choose from the available options.")
            return

        order = ChickenOrder(flavor, spice_level, quantity)
        self.orders.append(order)
        print("Order placed successfully.")
        order.display_details()

    def display_orders(self):
        if not self.orders:
            print("No orders placed yet.")
        else:
            print("Order Summaries:")
            for order in self.orders:
                order.display_details()


def main():
    store = ChickenOnlineStore()

    while True:
        print("\nOptions:")
        print("1. View Chicken Menu")
        print("2. Place Chicken Order")
        print("3. View Order Summaries")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            store.display_chicken_menu()
        elif choice == "2":
            flavor = input("Enter the chicken flavor you want to order: ")
            spice_level = int(input("Enter the spice level (1-5): "))
            quantity = int(input("Enter the quantity: "))
            store.place_chicken_order(flavor, spice_level, quantity)
        elif choice == "3":
            store.display_orders()
        elif choice == "4":
            print("Thank you for ordering from the Mthombe's Chicken Online Store. Enjoy your meal!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

