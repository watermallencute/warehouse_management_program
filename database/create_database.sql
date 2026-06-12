CREATE DATABASE IF NOT EXISTS store;

USE store;

-- DROP DATABASE store;

-- DROP TABLE products;

CREATE TABLE IF NOT EXISTS products(
    product_id 		CHAR(6) 																					PRIMARY KEY,
    product_name 	VARCHAR(50) 																				NOT NULL,
    category		ENUM('Food', 'Beverage', 'Snack', 'Personal care', 'Household', 'Medicine', 'Stationery')	NOT NULL,
    price 			DECIMAL(10) 																				NOT NULL,
    stock 			INT 																						NOT NULL
);

CREATE TABLE IF NOT EXISTS customers(
    customer_id 		CHAR(6) 										PRIMARY KEY,
    customer_name 		VARCHAR(50) 									NOT NULL,
    gender 				ENUM('Male', 'Female', 'Prefer not to say') 	NOT NULL,
    phone_number 		VARCHAR(15) 									NOT NULL		UNIQUE,
    address 			VARCHAR(255) 									NOT NULL
);
    
CREATE TABLE IF NOT EXISTS cashiers(
    cashier_id 			CHAR(6) 								PRIMARY KEY,
    cashier_name 		VARCHAR(50) 							NOT NULL,
    username 			VARCHAR(50) 							NOT NULL		UNIQUE,
    password 			VARCHAR(50) 							NOT NULL,
    shift 				ENUM('Morning', 'Evening', 'Night') 	NOT NULL
);
    
CREATE TABLE IF NOT EXISTS suppliers(
    supplier_id 		CHAR(6) 		PRIMARY KEY,
    supplier_name 		VARCHAR(50) 	NOT NULL,
    contact_number 		VARCHAR(15) 	NOT NULL		UNIQUE,
    address 			VARCHAR(255) 	NOT NULL,
    email				VARCHAR(50)		NOT NULL
);
    
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id 		CHAR(6) 											PRIMARY KEY,
    transaction_date 	DATE 												NOT NULL,
    customer_id 		CHAR(6) 											NOT NULL,
    cashier_id 			CHAR(6) 											NOT NULL,
    total_price 		DECIMAL(12) 										NOT NULL,
    payment_method 		ENUM('Cash', 'Debit card', 'Credit card', 'QRIS') 	NOT NULL,
    
    FOREIGN KEY(customer_id) 	REFERENCES 		customers(customer_id),
    FOREIGN KEY(cashier_id) 	REFERENCES 		cashiers(cashier_id)
);

CREATE TABLE IF NOT EXISTS transaction_details(
    detail_id 			CHAR(6) 			PRIMARY KEY,
    transaction_id 		CHAR(6) 			NOT NULL,
    product_id 			CHAR(6) 			NOT NULL,
    quantity 			INT 				NOT NULL,
    sub_total 			DECIMAL(10) 		NOT NULL,
    
    FOREIGN KEY(product_id) 		REFERENCES 		products(product_id),
    FOREIGN KEY(transaction_id) 	REFERENCES 		transactions(transaction_id)
);

CREATE TABLE IF NOT EXISTS product_suppliers(
    product_supplier_id 	CHAR(6) 			PRIMARY KEY,
    supplier_id 			CHAR(6) 			NOT NULL,
    supplier_price 			DECIMAL(10) 		NOT NULL,
    supply_date 			DATE 				NOT NULL,
    stock_supplied 			INT 				NOT NULL,
    product_id 				CHAR(6) 			NOT NULL,
    
    FOREIGN KEY(product_id) 	REFERENCES 		products(product_id),
    FOREIGN KEY(supplier_id) 	REFERENCES 		suppliers(supplier_id)
);