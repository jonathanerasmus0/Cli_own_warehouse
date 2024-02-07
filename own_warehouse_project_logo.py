import os
import argparse
import platform
from colorama import Fore, Style, init

class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity
        print(f"Added {quantity} {item} to stock.")

    def display_logo(self, logo_path):
        if platform.system() == "Windows":
            self.display_logo_windows(logo_path)
        else:
            self.display_logo_non_windows(logo_path)

    def display_logo_windows(self, logo_path):
        init()
        os.system("cls")
        with open(logo_path, "r") as logo_file:
            logo_text = logo_file.read()
        self.print_colored(logo_text, Fore.RED + Style.BRIGHT)
        print("    Welcome to Jonathan's Warehouse!\n")

    def display_logo_non_windows(self, logo_path):
        os.system("clear")
        try:
            with open(logo_path, "r") as logo_file:
                logo_text = logo_file.read()
            self.print_colored(logo_text, "\033[31m\033[1m")
        except FileNotFoundError:
            print("Logo file not found.")
        print("    Welcome to Jonathan's Warehouse!\n")

    def print_colored(self, text, color_style):
        print(color_style + text + Fore.RESET + Style.RESET_ALL)

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

def main(args=None):
    parser = argparse.ArgumentParser(description="Warehouse Management System")
    parser.add_argument("--logo", help="Path to logo image file (optional)")
    parser.add_argument("--no-logo", action="store_true", help="Don't display the logo")
    parser.add_argument("--no-color", action="store_true", help="Don't use color in messages")
    parser.add_argument("item", nargs="?", help="Item to add or ship (optional)")
    parser.add_argument("-q", "--quantity", type=int, help="Quantity to add or ship (required)")
    parser.add_argument("-c", "--country", help="Destination country for shipping (optional)")
    args = parser.parse_args(args)

    warehouse = Warehouse()

    # Find the path to logo.txt 
    current_directory = os.getcwd()
    logo_path = os.path.join(current_directory, "logo.txt")

    if not args.no_logo:
        # For some reason this is not working why?
        if args.logo:
            logo_path = args.logo
        warehouse.display_logo(logo_path)

    welcome_color = Fore.RED if not args.no_color else ""
    print(welcome_color + "\nWelcome to Jonathan's warehouse where the best products are sold" + Fore.RESET)

   

if __name__ == "__main__":
    main()

