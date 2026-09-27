
# app.py
# This is the main file that runs the Zara Clothing Inventory app.
# It shows a simple menu in the terminal and calls functions
# from the other files depending what the user picks.

from database import setup_database
from product import add_product, get_all_products
from inventory import show_all_inventory, add_stock, show_low_stock_items, check_stock
from order import place_order, show_all_orders
from logger import log_info


def print_menu():
    print("\n========================================")
    print("   ZARA CLOTHING INVENTORY MANAGEMENT")
    print("========================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Check Stock of a Product")
    print("4. Restock a Product")
    print("5. Show Low Stock Items")
    print("6. Place an Order")
    print("7. View All Orders")
    print("8. Exit")
    print("========================================")


def add_product_menu():
    print("\n-- Add New Product --")
    name = input("Enter product name: ")
    category = input("Enter category (like Shirts, Jeans, Jackets): ")
    size = input("Enter size (S, M, L, XL): ")
    color = input("Enter color: ")

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter starting quantity: "))
    except ValueError:
        print("Price and quantity must be numbers! Try again.")
        return

    add_product(name, category, size, color, price, quantity)
    print("Product added!")


def view_products_menu():
    show_all_inventory()


def check_stock_menu():
    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("That is not a valid ID.")
        return
    check_stock(product_id)


def restock_menu():
    try:
        product_id = int(input("Enter product ID to restock: "))
        amount = int(input("How many to add: "))
    except ValueError:
        print("Please enter numbers only.")
        return
    add_stock(product_id, amount)


def low_stock_menu():
    show_low_stock_items()


def place_order_menu():
    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("That is not a valid ID.")
        return

    customer_name = input("Enter customer name: ")

    try:
        quantity = int(input("Enter quantity to order: "))
    except ValueError:
        print("Quantity must be a number.")
        return

    place_order(product_id, customer_name, quantity)


def view_orders_menu():
    show_all_orders()


def main():
    # make sure the database and tables exist before we start
    setup_database()
    log_info("Zara Inventory App started")

    running = True
    while running:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_product_menu()
        elif choice == "2":
            view_products_menu()
        elif choice == "3":
            check_stock_menu()
        elif choice == "4":
            restock_menu()
        elif choice == "5":
            low_stock_menu()
        elif choice == "6":
            place_order_menu()
        elif choice == "7":
            view_orders_menu()
        elif choice == "8":
            print("Thanks for using Zara Inventory App. Bye!")
            log_info("App closed by user")
            running = False
        else:
            print("Invalid choice, please pick a number from 1 to 8.")


# this makes sure main() only runs when we run this file directly
if __name__ == "__main__":
    main()
