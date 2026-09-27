
# product.py
# This file has the Product class and functions to add, view, update
# and delete products from the database.

from database import run_query, run_select
from logger import log_info, log_error, log_success


class Product:
    # simple class to hold product info
    def __init__(self, product_id, name, category, size, color, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity

    def show(self):
        print("-----------------------------")
        print("ID       :", self.product_id)
        print("Name     :", self.name)
        print("Category :", self.category)
        print("Size     :", self.size)
        print("Color    :", self.color)
        print("Price    : $" + str(self.price))
        print("Quantity :", self.quantity)
        print("-----------------------------")


def add_product(name, category, size, color, price, quantity):
    # adds a new product to the database
    try:
        query = """INSERT INTO products (name, category, size, color, price, quantity)
                   VALUES (?, ?, ?, ?, ?, ?)"""
        new_id = run_query(query, (name, category, size, color, price, quantity))
        log_success("Product added: " + name + " (id=" + str(new_id) + ")")
        return new_id
    except Exception as e:
        log_error("Could not add product: " + str(e))
        return None


def get_all_products():
    # returns a list of Product objects for everything in the table
    rows = run_select("SELECT * FROM products")
    product_list = []
    for row in rows:
        p = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        product_list.append(p)
    return product_list


def get_product_by_id(product_id):
    rows = run_select("SELECT * FROM products WHERE product_id = ?", (product_id,))
    if len(rows) == 0:
        return None
    row = rows[0]
    return Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


def update_product_quantity(product_id, new_quantity):
    try:
        run_query("UPDATE products SET quantity = ? WHERE product_id = ?",
                  (new_quantity, product_id))
        log_info("Updated quantity for product id " + str(product_id) + " to " + str(new_quantity))
    except Exception as e:
        log_error("Could not update quantity: " + str(e))


def delete_product(product_id):
    try:
        run_query("DELETE FROM products WHERE product_id = ?", (product_id,))
        log_info("Deleted product id " + str(product_id))
    except Exception as e:
        log_error("Could not delete product: " + str(e))


        # DB END JOB 
        
