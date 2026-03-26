# Inventory Management System (M1S3)

## Overview

This project is a console-based inventory management system developed in Python.
It allows users to manage products, calculate statistics, and persist data using CSV files.

The system is modular and uses lists, dictionaries, functions, and file handling.

---

## Features

* Add products to inventory
* Show all products
* Search for a product by name
* Update product information
* Delete products
* Calculate inventory statistics
* Save inventory to CSV file
* Load inventory from CSV file
* Merge or overwrite data when loading
* Input validation and error handling

---

## Project Structure

* app.py: main menu and user interaction
* servicios.py: CRUD operations and statistics
* archivos.py: CSV file handling (save and load)

---

## Data Structure

The inventory is stored as a list of dictionaries:

```python
{
    "name": str,
    "price": float,
    "quantity": int
}
```

---

## How It Works

### Menu System

The program runs in a loop showing options from 1 to 9.
The user selects an option and the system executes the corresponding action.

---

### CRUD Operations

* Add: insert a new product
* Show: display all products
* Search: find a product by name
* Update: modify price and quantity
* Delete: remove a product

---

### Statistics

The system calculates:

* Total units
* Total value
* Most expensive product
* Product with highest stock

A lambda function is used:

```python
subtotal = lambda p: p["price"] * p["quantity"]
```

---

### CSV Persistence

Save CSV:

* Saves inventory to a file
* Uses format: name,price,quantity
* Includes header
* Handles file errors

Load CSV:

* Reads data from file
* Validates header and data
* Skips invalid rows and counts errors

---

### Merge vs Overwrite

When loading data:

* Overwrite (S): replaces current inventory
* Merge (N):

  * If product exists: adds quantity and updates price
  * If not: adds new product

---

## Error Handling

The system handles:

* Invalid input
* File not found
* Encoding errors
* Invalid CSV format
* Negative values

The program always returns to the menu.

---

## How to Run

Run the program with:

```bash
python app.py
```

---

## Requirements Covered

* Lists and dictionaries
* Functions and modular design
* CRUD operations
* Statistics
* CSV persistence
* Input validation
* Exception handling

---

## Notes

* CSV files are created automatically
* Files are saved in the current directory unless another path is used
* All interactions are done through the console
