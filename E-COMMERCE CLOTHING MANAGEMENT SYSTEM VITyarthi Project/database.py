
# database.py
# This file is for connecting to our database and making the tables.
# I am using sqlite3 because it comes with python already and its easy.

import sqlite3
from logger import log_info, log_error

DB_NAME = "zara_inventory.db"


def get_connection():
    # this just gives back a connection to the database
    connection = sqlite3.connect(DB_NAME)
    return connection


def setup_database():
    # this function makes the tables if they dont exist yet
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # table for products
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                size TEXT,
                color TEXT,
                price REAL,
                quantity INTEGER
            )
        """)

        # table for orders
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                customer_name TEXT,
                quantity_ordered INTEGER,
                total_price REAL,
                order_date TEXT,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)

        connection.commit()
        connection.close()
        log_info("Database setup done. Tables are ready.")

    except Exception as e:
        log_error("Something went wrong while setting up database: " + str(e))


# little helper function to run any query easily
def run_query(query, params=()):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    last_id = cursor.lastrowid
    connection.close()
    return last_id


# little helper to get results back (for SELECT queries)
def run_select(query, params=()):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    connection.close()
    return rows
