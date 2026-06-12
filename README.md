# Python CRUD Application for Warehouse Management System

A Python-based Warehouse Management System that supports Create, Read, Update, Delete (CRUD), Search, and Export operations using a MySQL database. This application helps manage products, customers, suppliers, cashiers, and sales transactions in an organized and efficient way.

---

# Business Understanding

Warehouse and retail businesses require accurate inventory management and transaction tracking to ensure smooth daily operations. Manual data recording often causes inconsistencies, duplicate records, and difficulties in monitoring stock movements.

This system was developed to simplify warehouse administration by providing centralized management for products, suppliers, customers, cashiers, and transactions.

## Benefits

- Improve inventory accuracy and stock monitoring.
- Reduce data redundancy and manual recording errors.
- Simplify supplier, customer, and cashier management.
- Support faster transaction processing.
- Automatically calculate transaction totals.
- Facilitate reporting through CSV export features.

## Target Users

This application is intended for:

- Warehouse Staff
- Store Administrators
- Cashiers
- Inventory Managers

---

# Features

## Create

Add new records into the database:

- Products
- Customers
- Cashiers
- Suppliers
- Transactions

Features:

- Auto-generated IDs
- Transaction supports multiple products
- Automatic subtotal calculation
- Automatic total transaction calculation
- Stock validation before transaction creation

---

## Read

### View Records

Display all records in tabular format:

- Products
- Customers
- Cashiers
- Suppliers
- Transactions

### Search Records

Search data based on:

- Product ID or Product Name
- Customer ID or Customer Name
- Cashier ID or Cashier Name
- Supplier ID or Supplier Name
- Transaction ID or Transaction Date

---

## Update

Modify existing records:

### Product

- Product Name
- Category
- Price
- Stock
- Supplier Information
- Supply Information

### Customer

- Customer Information

### Cashier

- Cashier Information

### Supplier

- Supplier Information

### Transaction

- Update purchased product quantity
- Automatically update subtotal
- Automatically recalculate transaction total

---

## Delete

Delete records from the database:

- Products
- Customers
- Cashiers
- Suppliers
- Transactions

Transaction deletion behavior:

- Individual products can be removed from a transaction.
- Transaction total is automatically recalculated.
- Entire transaction is automatically deleted if all transaction details have been removed.

---

## Export

Export records into CSV files:

- Products
- Customers
- Cashiers
- Suppliers
- Transactions

---

## Validation and Security

- Confirmation prompts before Create, Update, and Delete operations.
- Quantity validation during transactions.
- Stock availability checking.
- Duplicate ID prevention through auto-generated IDs.
- Invalid menu handling.

---

# System Architecture

The application follows a layered architecture:

```text
Main Program
    │
    ├── ProductService
    ├── CustomerService
    ├── CashierService
    ├── SupplierService
    ├── TransactionService
    └── TransactionDetailService
            │
            ▼
        MySQL Database
```

This separation improves maintainability and scalability.

---

# Installation

## Prerequisites

- Python 3.10+
- MySQL Server
- mysql-connector-python
- pandas

## Clone Repository

```bash
git clone https://github.com/<watermallencute>/<warehouse_management_program>.git

cd <warehouse_management_program>
```

## Install Dependencies

```bash
pip install pandas mysql-connector-python
```

## Configure Database

Create a MySQL database and import the required tables:

- products
- suppliers
- product_suppliers
- customers
- cashiers
- transactions
- transaction_details

Configure database credentials inside:

```python
config/database.py
```

Example:

```python
host = "localhost"
user = "root"
password = "your_password"
database = "warehouse_management"
```

---

# Usage

Run the application:

```bash
python main.py
```

Main Menu:

```text
1. View Records
2. Add New Records
3. Update Records
4. Delete Records
5. Export to CSV
6. Exit Program
```

---

## Data Model
This project utilizes Python lists and dictionaries as the data structure to represent warehouse management data. The following fields are typically stored:

### Product Data
* product_id: (CHAR) - Unique identifier for each product.
* product_name: (VARCHAR) - Name of the product.
* category: (ENUM) - Product category.
* price: (DECIMAL) - Selling price of the product.
* stock: (INT) - Available stock quantity.
* supplier_name: (CHAR) - Supplier providing the product.
* supplier_price: (DECIMAL) - Purchase price from supplier.
* supply_date: (Date) - Date the stock was supplied.
* stock_supplied: (INT) - Quantity of stock supplied.

### Customer Data
* customer_id: (CHAR) - Unique identifier for each customer.
* customer_name: (VARCHAR) - Customer's name.
* gender: (ENUM) - Customer gender.
* phone_number: (VARCHAR) - Customer contact number.
* address: (VARCHAR) - Customer address.

### Cashier Data
* cashier_id: (CHAR) - Unique identifier for each cashier.
* cashier_name: (VARCHAR) - Cashier's name.
* username: (VARCHAR) - Cashier login username.
* password: (VARCHAR) - Cashier login password.
* shift: (VARCHAR) - Cashier work shift.

### Supplier Data
* supplier_id: (CHAR) - Unique identifier for each supplier.
* supplier_name: (VARCHAR) - Supplier company name.
* contact_number: (VARCHAR) - Supplier contact number.
* address: (VARCHAR) - Supplier address.
* email: (VARCHAR) - Supplier email address.
  
### Transaction Data
* transaction_id: (CHAR) - Unique identifier for each transaction.
* transaction_date: (DATE) - Transaction date.
* customer_name: (VARCHAR) - Customer involved in the transaction.
* cashier_name: (VARCHAR) - Cashier handling the transaction.
* payment_method: (ENUM) - Payment method used.
* product_name: (VARCHAR) - Purchased product name.
* quantity: (INT) - Purchased product quantity.
* sub_total: (DECIMAL) - Sub total transaction price.
* total_price: (DECIMAL) - Total transaction price.

---

# Future Improvements
- User authentication and role management.
- Dashboard and sales analytics.
- Low stock notification system.
- Product stock history tracking.
- Monthly and yearly sales reports.
- GUI version using Tkinter, Streamlit, or PyQt.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to angel.adytha@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.