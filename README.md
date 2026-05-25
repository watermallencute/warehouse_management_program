# Python CRUD Application for Warehouse Management System

A comprehensive Python application for managing warehouse management data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the retail and warehouse management industry, specifically addressing the need to manage products, customers, cashiers, suppliers, and transaction data efficiently. These data entities plays a crucial role in inventory control, sales transactions, supplier management, and customer service processes..

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* Easier monitoring of stock availability and product supply
* Better organization of customer, cashier, and supplier records
* Faster transaction processing and record maintenance

**Target Users:**

This application is designed for warehouse staff, cashiers, and store administrators within the organization to facilitate their inventory management, transaction handling, customer management, and supplier management activities related to warehouse operations.

## Features

* **Create:**
    * Add new product, customer, cashier, supplier, and transaction entries with essential details like IDs, names, categories, prices, stock, contact information, and payment methods.
    * Implement validation rules to ensure data integrity such as unique IDs and numeric value checks.
* **Read:**
    * Search and retrieve specific records by applying filters based on IDs, names, or transaction dates.
    * Display comprehensive information for each entity in a user-friendly tabular format.
* **Update:**
    * Modify existing records to reflect changes in product details, customer information, supplier data, cashier data, or transaction records.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted records with appropriate authorization checks.
    * Automatically remove transaction data when all products in a transaction have been deleted.
* **Security:**
    * Input validation to reduce invalid data entries.
    * Confirmation prompts before create, update and delete operations.
* **Reporting:**
    * Display organized tables for products, customers, cashiers, suppliers, and transactions.
    * Search functionality for quick record lookup.

## Installation

1. **Prerequisites:**
    * Python 3.10.13
    * No additional external dependencies required

2. **Installation:**
    ```bash
    git clone https://github.com/<watermallencute>/<warehouse_management_program>.git
    cd <warehouse_management_program>
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new product, customer, supplier, cashier, or transaction record.
    * **Read:** Search and retrieve records by ID, name, or transaction date.
    * **Update:** Modify existing records such as stock, prices, addresses, or transaction details.
    * **Delete:** Remove records from the system with confirmation prompts.

## Data Model
This project utilizes Python lists and dictionaries as the data structure to represent warehouse management data. The following fields are typically stored:

### Product Data
* product_id: (String) - Unique identifier for each product.
* product_name: (String) - Name of the product.
* category: (String) - Product category.
* price: (Integer) - Selling price of the product.
* stock: (Integer) - Available stock quantity.
* supplier_name: (String) - Supplier providing the product.
* supplier_price: (Integer) - Purchase price from supplier.
* supply_date: (String) - Date the stock was supplied.
* stock_supplied: (Integer) - Quantity of stock supplied.

### Customer Data
* customer_id: (String) - Unique identifier for each customer.
* customer_name: (String) - Customer's name.
* gender: (String) - Customer gender.
* phone_number: (String) - Customer contact number.
* address: (String) - Customer address.

### Cashier Data
* cashier_id: (String) - Unique identifier for each cashier.
* cashier_name: (String) - Cashier's name.
* username: (String) - Cashier login username.
* password: (String) - Cashier login password.
* shift: (String) - Cashier work shift.

### Supplier Data
* supplier_id: (String) - Unique identifier for each supplier.
* supplier_name: (String) - Supplier company name.
* contact_number: (String) - Supplier contact number.
* address: (String) - Supplier address.
* email: (String) - Supplier email address.
  
### Transaction Data
* transaction_id: (String) - Unique identifier for each transaction.
* transaction_date: (String) - Transaction date.
* customer_name: (String) - Customer involved in the transaction.
* cashier_name: (String) - Cashier handling the transaction.
* payment_method: (String) - Payment method used.
* products: (List) - List of purchased products.
* total_price: (Integer) - Total transaction price.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to angel.adytha@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.
