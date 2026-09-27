
# order.py
# This file handles customer orders. When someone orders a product,
# we reduce the stock and save the order info in the database.

import datetime
from database import run_query, run_select
from product import get_product_by_id
from inventory import reduce_stock
from logger import log_success, log_error


class Order:
    def __init__(self, order_id, product_id, customer_name, quantity_ordered, total_price, order_date):
        self.order_id = order_id
        self.product_id = product_id
        self.customer_name = customer_name
        self.quantity_ordered = quantity_ordered
        self.total_price = total_price
        self.order_date = order_date

    def show(self):
        print("-----------------------------")
        print("Order ID   :", self.order_id)
        print("Product ID :", self.product_id)
        print("Customer   :", self.customer_name)
        print("Quantity   :", self.quantity_ordered)
        print("Total Price: $" + str(self.total_price))
        print("Date       :", self.order_date)
        print("-----------------------------")


def place_order(product_id, customer_name, quantity_ordered):
    product = get_product_by_id(product_id)

    if product is None:
        print("Sorry, that product does not exist.")
        return None

    # try to take the stock away first
    stock_ok = reduce_stock(product_id, quantity_ordered)
    if not stock_ok:
        log_error("Order failed for " + customer_name + " - not enough stock")
        return None

    total_price = product.price * quantity_ordered
    today = datetime.date.today().strftime("%Y-%m-%d")

    query = """INSERT INTO orders (product_id, customer_name, quantity_ordered, total_price, order_date)
               VALUES (?, ?, ?, ?, ?)"""
    new_order_id = run_query(query, (product_id, customer_name, quantity_ordered, total_price, today))

    log_success("Order placed! Order id=" + str(new_order_id) + " for " + customer_name)
    print("Order placed successfully! Total price is $" + str(total_price))
    return new_order_id


def get_all_orders():
    rows = run_select("SELECT * FROM orders")
    order_list = []
    for row in rows:
        o = Order(row[0], row[1], row[2], row[3], row[4], row[5])
        order_list.append(o)
    return order_list


def show_all_orders():
    orders = get_all_orders()
    if len(orders) == 0:
        print("No orders yet.")
        return

    print("\n===== ORDER HISTORY =====")
    for o in orders:
        o.show()
    print("==========================\n")
