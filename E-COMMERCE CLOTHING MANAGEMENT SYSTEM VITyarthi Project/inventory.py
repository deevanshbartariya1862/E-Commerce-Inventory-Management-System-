
# inventory.py
# This file manages the inventory logic, like checking stock levels
# and showing low stock warnings. It uses functions from product.py

from product import get_all_products, get_product_by_id, update_product_quantity
from logger import log_info, log_error

LOW_STOCK_LIMIT = 5  # if quantity goes below this, we warn the user


def show_all_inventory():
    products = get_all_products()

    if len(products) == 0:
        print("No products in inventory yet.")
        return

    print("\n===== ZARA INVENTORY LIST =====")
    for p in products:
        p.show()
        if p.quantity < LOW_STOCK_LIMIT:
            print("!!! LOW STOCK WARNING for", p.name, "!!!")
    print("================================\n")


def check_stock(product_id):
    product = get_product_by_id(product_id)
    if product is None:
        print("Product not found.")
        return None
    print(product.name, "has", product.quantity, "items left.")
    return product.quantity


def reduce_stock(product_id, amount):
    # this is used when an order is placed
    product = get_product_by_id(product_id)
    if product is None:
        log_error("Tried to reduce stock but product not found: " + str(product_id))
        return False

    if product.quantity < amount:
        print("Not enough stock! Only INCREASE IT ", product.quantity, "left.")
        return False

    new_quantity = product.quantity - amount
    update_product_quantity(product_id, new_quantity)
    log_info("Reduced stock of " + product.name + " by " + str(amount))
    return True


def add_stock(product_id, amount):
    # used to restock items
    product = get_product_by_id(product_id)
    if product is None:
        print("Product not found ERROR 404.")
        return False

    new_quantity = product.quantity + amount
    update_product_quantity(product_id, new_quantity)
    log_info("Restocked " + product.name + " by " + str(amount))
    print("New quantity for", product.name, "is", new_quantity)
    return True


def show_low_stock_items():
    products = get_all_products()
    print("\n----- LOW STOCK ITEMS -----")
    found_any = False
    for p in products:
        if p.quantity < LOW_STOCK_LIMIT:
            p.show()
            found_any = True
    if not found_any:
        print("Nothing is low on stock right now. Good job PROMOTION AAYEGI!")
    print("----------------------------\n")
