import argparse
import sys
import turtle
from colorama import Fore, init

init()  # start colorama to make the welcome message show in red

class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity
        print(f"Added {quantity} {item} to stock.")

    def view_stock(self):
        print("Current Stock:")
        for item, quantity in self.stock.items():
            print(f"{item}: {quantity}")

    def ship_stock(self, item, quantity, country):
        if self.stock.get(item, 0) >= quantity:
            self.stock[item] -= quantity
            print(f"Shipped {quantity} {item} to {country}.")
        else:
            print(f"Not enough stock of {item} to ship {quantity} to {country}.")

    def draw_logo(self):
        # Create a turtle object
        t = turtle.Turtle()

        # Set turtle speed and color
        t.speed(4)
        t.color("red")

        # Draw a simple warehouse shape
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

        # Draw some windows
        t.penup()
        t.goto(-60, 20)
        t.pendown()
        t.forward(40)
        t.backward(20)
        t.left(90)
        t.forward(40)
        t.backward(20)
        t.penup()

        t.goto(0, 20)
        t.pendown()
        t.forward(40)
        t.backward(20)
        t.left(90)
        t.forward(40)
        t.backward(20)
        t.penup()

        t.goto(60, 20)
        t.pendown()
        t.forward(40)
        t.backward(20)
        t.left(90)
        t.forward(40)
        t.backward(20)

        # Hide turtle and display the window
        t.hideturtle()
        turtle.done()

def main(args=None):
    parser = argparse.ArgumentParser(description="Warehouse Management System")
    parser.add_argument("item", nargs="?", help="Item to add or ship (optional)")
    parser.add_argument("-q", "--quantity", type=int, help="Quantity to add or ship (required)")
    parser.add_argument("-c", "--country", help="Destination country for shipping (optional)")
    args = parser.parse_args(args)

    warehouse = Warehouse()

    while True:
        print(Fore.RED + "\nWelcome to Jonathan's warehouse where you get the BEST service and Products" + Fore.RESET)

        print("\nWarehouse Management System")
        print("1. Add Stock")
        print("2. View Stock")
        print("3. Ship Stock")
        print("4. Draw Logo")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item_name = args.item if args.item else input("Enter item name: ")
            quantity = args.quantity if args.quantity else int(input("Enter quantity: "))
            warehouse.add_stock(item_name, quantity)
        elif choice == "2":
            warehouse.view_stock()
        elif choice == "3":
            item_name = args.item if args.item else input("Enter item name: ")
            quantity = args.quantity if args.quantity else int(input("Enter quantity to ship: "))
            country = args.country if args.country else input("Enter destination country: ")
            warehouse.ship_stock(item_name, quantity, country)
        elif choice == "4":
            warehouse.draw_logo()
        elif choice == "5":
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
