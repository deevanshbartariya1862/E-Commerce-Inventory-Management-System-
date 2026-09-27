# Zara Clothing Inventory Management System

A simple Python + SQLite console application to manage clothing inventory,

stock levels, and customer orders for a Zara-style clothing store.

This project was created as a beginner-level practice project to learn:

- Python functions and classes

- SQLite databases

- Splitting a project into multiple files (modules)

- Basic logging

## Features

- Add new clothing products (name, category, size, color, price, quantity)

- View all products in inventory

- Check stock of a specific product

- Restock a product

- View low stock warnings (anything under 5 items)

- Place customer orders (automatically reduces stock)

- View full order history

- All activity is logged to `activity_log.txt`

## Project Structure

```

zara_inventory/

│

├── app.py     # Main file - run this to start the app (menu system)

├── database.py   # Sets up SQLite database and tables, runs queries

├── product.py    # Product class + add/view/update/delete product functions

├── inventory.py   # Stock checking, restocking, low stock alerts

├── order.py     # Order class + placing orders / order history

├── logger.py     # Writes activity logs to a text file

│

├── zara_inventory.db  # (created automatically when you run the app)

└── activity_log.txt  # (created automatically when you run the app)

```

## Requirements

- Python 3.7 or higher

- No external libraries needed! Only uses Python's built-in `sqlite3` and

`datetime` modules.

## How to Run

1. Put all six `.py` files in the same folder.

2. Open a terminal in that folder.

3. Run the app:

```bash

python app.py

```

4. On the first run, the app will automatically create the database file

(`zara_inventory.db`) and the required tables. No extra setup needed.

## How to Use

When you run the app, you will see a menu like this:

```

========================================

ZARA CLOTHING INVENTORY MANAGEMENT

========================================

1. Add New Product

2. View All Products

3. Check Stock of a Product

4. Restock a Product

5. Show Low Stock Items

6. Place an Order

7. View All Orders

8. Exit

========================================

```

Just type the number of what you want to do and press Enter, then follow

the prompts.

### Example Flow

1. Choose `1` to add a product like "Basic Tee", size M, quantity 20.

2. Choose `2` to see it listed in the inventory.

3. Choose `6` to place an order for that product (this reduces stock).

4. Choose `7` to see the order in the order history.

5. Choose `5` anytime to see items running low on stock.

## Notes

- This is a beginner-friendly project, so the code is written in a simple,

straightforward way (no advanced design patterns).

- The low stock limit is set to 5 and can be changed in `inventory.py`

by editing the `LOW_STOCK_LIMIT` variable.

- All logs (info, success, error) are saved in `activity_log.txt` in the

same folder, and also printed to the screen while the app runs.

## Possible Future Improvements

- Add a search function to find products by name or category

- Add ability to edit/update full product details (not just quantity)

- Add a simple GUI using Tkinter

- Export inventory/orders to a CSV or Excel file

- Add user login for staff members