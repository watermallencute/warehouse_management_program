# ===================================
# WAREHOUSE MANAGEMENT SYSTEM
# ===================================
# Developed by. Angela Adytha Putri
# JCDS - 33

# /************************************/

import warnings

from services.product_service import ProductService
from services.cashier_service import CashierService
from services.customer_service import CustomerService
from services.supplier_service import SupplierService
from services.transaction_service import TransactionService
from services.product_suppliers_service import ProductSupplierService
from services.transaction_detail_service import TransactionDetailService

warnings.filterwarnings("ignore")

print("\n=== STORE TRANSACTION MANAGEMENT SYSTEM ===")

# /===== Feature Program =====/
def generate_id(prefix, data_list, key):
    if len(data_list) == 0:
        return f"{prefix}001"

    last_id = data_list[-1][key]
    number = int(last_id.replace(prefix, "")) + 1

    return f"{prefix}{str(number).zfill(3)}"

def view_menu():
    print("\nMenu Lists")
    print("1. View records\n" \
          "2. Add new record(s)\n" \
          "3. Update a record\n" \
          "4. Delete a record\n" \
          "5. Export to CSV\n" \
          "6. Exit program")
    menu = input("Enter the menu number you want to run: ")
    return menu

def back_to_submenu(): # Asks the user whether they want to continue using the submenu
    while True:
        option = input("\nDo you want to choose another submenu (yes/no)? ").lower()
        if option == "yes":
            return True
        elif option == "no":
            return False
        else:
            print("Invalid input!")

def show_product_list():
    print("-" * 157)
    print(
        f"{"ID":<10}  "
        f"{"Product":<15}  "
        f"{"Category":<15}  "
        f"{"Price":<12}  "
        f"{"Stock":<10}  "
        f"{"Supplier Name":<35}  "
        f"{"Supplier Price":<15}  "
        f"{"Supply Date":<15}  "
        f"{"Stock Supplied":<15}"
    )
    print("-" * 157)

    service = ProductService()
    products = service.get_all_products()

    for product in products:
        print(
            f"{product["product_id"]:<10}  "
            f"{product["product_name"]:<15}  "
            f"{product["category"]:<15}  "
            f"Rp{product["price"]:<10,}  "
            f"{product["stock"]:<10}  "
            f"{product["supplier_name"]:<35}  "
            f"Rp{product["supplier_price"]:<13,}  "
            f"{product['supply_date'].strftime('%Y-%m-%d'):<15}  "
            f"{product["stock_supplied"]:<15}"
        )
    print("-" * 157)

def show_customer_list():
    print("-" * 85)
    print(
        f"{"ID":<10}  "
        f"{"Customer":<15}  "
        f"{"Gender":<15}  "
        f"{"Phone Number":<20}  "
        f"{"Address":<20}"
    )
    print("-" * 85)

    service = CustomerService()
    customers = service.get_all_customers()

    for customer in customers:
        print(
            f"{customer["customer_id"]:<10}  "
            f"{customer["customer_name"]:<15}  "
            f"{customer["gender"]:<15}  "
            f"{customer["phone_number"]:<20}  "
            f"{customer["address"]:<20}"
        )
    print("-" * 85)

def show_cashier_list():
    print("-" * 75)
    print(
        f"{"ID":<10}  "
        f"{"Cashier":<15}  "
        f"{"Username":<15}  "
        f"{"Password":<20}  "
        f"{"Shift":<15}"
    )
    print("-" * 75)

    service = CashierService()
    cashiers = service.get_all_cashiers()

    for cashier in cashiers:
        print(
            f"{cashier["cashier_id"]:<10}  "
            f"{cashier["cashier_name"]:<15}  "
            f"{cashier["username"]:<15}  "
            f"{cashier["password"]:<20}  "
            f"{cashier["shift"]:<15}"
        )
    print("-" * 75)

def show_supplier_list():
    print("-" * 117)
    print(
        f"{"ID":<10}  "
        f"{"Supplier":<35}  "
        f"{"Contact Number":<20}  "
        f"{"Address":<20}  "
        f"{"Email":<20}"
    )
    print("-" * 117)

    service = SupplierService()
    suppliers = service.get_all_suppliers()

    for supplier in suppliers:
        print(
            f"{supplier["supplier_id"]:<10}  "
            f"{supplier["supplier_name"]:<35}  "
            f"{supplier["contact_number"]:<20}  "
            f"{supplier["address"]:<20}  "
            f"{supplier["email"]:<20}"
        )
    print("-" * 117)

def show_transaction_list():
    print("-" * 137)
    print(
        f"{"ID":<10}  "
        f"{"Date":<15}  "
        f"{"Customer":<15}  "
        f"{"Cashier":<15}  "
        f"{"Product":<15}  "
        f"{"Quantity":<10}  "
        f"{"Subtotal":<12}"
        f"{"Total price":<17}  "
        f"{"Payment Method":<15}"
    )
    print("-" * 137)

    service = TransactionService()
    transactions = service.get_all_transactions()

    for transaction in transactions:
        print(
            f"{transaction["transaction_id"]:<10}  "
            f"{transaction['transaction_date'].strftime('%Y-%m-%d'):<15}  "
            f"{transaction["customer_name"]:<15}  "
            f"{transaction["cashier_name"]:<15}  "
            f"{transaction["product_name"]:<15}  "
            f"{transaction["quantity"]:<10}  "
            f"Rp{transaction["sub_total"]:<10,}  "
            f"Rp{transaction["total_price"]:<15,}  "
            f"{transaction["payment_method"]:<15}"
            )
    print("-" * 137)

def show_transaction_detail_list():
    print("-" * 157)
    print(
        f"{"ID":<10}  "
        f"{"Transaction ID":<15}  "
        f"{"Product ID":<15}  "
        f"{"Quantity":<12}  "
        f"{"Sub Total":<10}"
    )
    print("-" * 157)

    service = TransactionDetailService()
    transaction_details = service.get_all_transaction_details()

    for transaction_detail in transaction_details:
        print(
            f"{transaction_detail["detail_id"]:<10} ",
            f"{transaction_detail["transaction_id"]:<15} ",
            f"{transaction_detail["product_id"]:<15} ",
            f"{transaction_detail["quantity"]:<10,} ",
            f"Rp{transaction_detail["sub_total"]:<8,}"
        )
    
def view_record_menu(): # Displays all available records based on selected submenu
    while True:
        print("\n===== VIEW RECORD MENU =====")
        print("Choose a submenu you want to view:")
        print("1. View Products\n" \
              "2. View Customers\n" \
              "3. View Cashiers\n" \
              "4. View Suppliers\n" \
              "5. View Transactions\n" \
              "6. Back to Sub Menu")

        submenu = input("Enter the submenu number you want to view: ")

        if submenu == "1":
            print("\n===== PRODUCT LIST =====")
            service = ProductService()
            products = service.get_all_products()

            if len(products) == 0:
                print("No product data available!")
            else:
                show_product_list()

            if not back_to_submenu():
                break

        elif submenu == "2":
            print("\n===== CUSTOMER LIST =====")
            service = CustomerService()
            customers = service.get_all_customers()

            if len(customers) == 0:
                print("No customer data available!")
            else:
                show_customer_list()

            if not back_to_submenu():
                break

        elif submenu == "3":
            print("\n===== CASHIER LIST =====")
            service = CashierService()
            cashiers = service.get_all_cashiers()

            if len(cashiers) == 0:
                print("No cashier data available!")
            else:
                show_cashier_list()

            if not back_to_submenu():
                break

        elif submenu == "4":
            print("\n===== SUPPLIER LIST =====")

            service = SupplierService()
            suppliers = service.get_all_suppliers()

            if len(suppliers) == 0:
                print("No supplier data available!")
            else:
                show_supplier_list()

            if not back_to_submenu():
                break

        elif submenu == "5":
            print("\n===== TRANSACTION LIST =====")

            service = TransactionService()
            transactions = service.get_all_transactions()

            if len(transactions) == 0:
                print("No transaction data available!")
            else:
                show_transaction_list()

            if not back_to_submenu():
                break

        elif submenu == "6": 
            break

        else:
            print("Invalid submenu!")

            if not back_to_submenu():
                break

def search_record_menu(): # Displays detail information if data exists
    while True:
        print("\n===== SEARCH MENU =====")
        print("1. Search Products\n" \
              "2. Search Customers\n" \
              "3. Search Cashiers\n" \
              "4. Search Suppliers\n" \
              "5. Search Transactions\n" \
              "6. Back to Sub Menu")

        choice = input("Enter submenu number: ")

        if choice == "1":
            keyword = input("Enter product ID or name: ").lower()

            service = ProductService()
            products = service.get_all_products()

            found = False

            print("\n===== PRODUCT DETAIL =====")
            print("-" * 157)
            print(
                f"{"ID":<10}  "
                f"{"Product":<15}  "
                f"{"Category":<15}  "
                f"{"Price":<12}  "
                f"{"Stock":<10}  "
                f"{"Supplier Name":<35}  "
                f"{"Supplier Price":<15}  "
                f"{"Supply Date":<15}  "
                f"{"Stock Supplied":<15}"
            )
            print("-" * 157)

            for product in products:
                if (keyword in product["product_id"].lower() or
                    keyword in product["product_name"].lower()):
                    print(
                        f"{product["product_id"]:<10}  "
                        f"{product["product_name"]:<15}  "
                        f"{product["category"]:<15}  "
                        f"Rp{product["price"]:<10,}  "
                        f"{product["stock"]:<10}  "
                        f"{product["supplier_name"]:<35}  "
                        f"Rp{product["supplier_price"]:<13,}  "
                        f"{product['supply_date'].strftime('%Y-%m-%d'):<15}  "
                        f"{product["stock_supplied"]:<15}"
                    )
                    
                    found = True

            print("-" * 157)

            if not found:
                print("Product not found!")

            if not back_to_submenu():
                break

        elif choice == "2":
            keyword = input("Enter customer ID or name: ").lower()

            service = CustomerService()
            customers = service.get_all_customers()

            found = False

            print("\n===== CUSTOMER DETAIL =====")
            print("-" * 85)
            print(
                f"{"ID":<10}  "
                f"{"Customer":<15}  "
                f"{"Gender":<15}  "
                f"{"Phone Number":<20}  "
                f"{"Address":<20}"
            )
            print("-" * 85)

            for customer in customers:
                if (keyword in customer["customer_id"].lower() or
                    keyword in customer["customer_name"].lower()):
                    print(
                        f"{customer["customer_id"]:<10}  "
                        f"{customer["customer_name"]:<15}  "
                        f"{customer["gender"]:<15}  "
                        f"{customer["phone_number"]:<20}  "
                        f"{customer["address"]:<20}"
                    )

                    found = True

            print("-" * 85)

            if not found:
                print("Customer not found!")

            if not back_to_submenu():
                break

        elif choice == "3":
            keyword = input("Enter cashier ID or name: ").lower()

            service = CashierService()
            cashiers = service.get_all_cashiers()

            found = False

            print("\n===== CASHIER DETAIL =====")
            print("-" * 75)
            print(
                f"{"ID":<10}  "
                f"{"Cashier":<15}  "
                f"{"Username":<15}  "
                f"{"Password":<20}  "
                f"{"Shift":<15}"
            )
            print("-" * 75)

            for cashier in cashiers:
                if (keyword in cashier["cashier_id"].lower() or
                    keyword in cashier["cashier_name"].lower()):
                    print(
                        f"{cashier["cashier_id"]:<10}  "
                        f"{cashier["cashier_name"]:<15}  "
                        f"{cashier["username"]:<15}  "
                        f"{cashier["password"]:<20}  "
                        f"{cashier["shift"]:<15}"
                    )

                    found = True

            print("-" * 75)

            if not found:
                print("Cashier not found!")

            if not back_to_submenu():
                break

        elif choice == "4":
            keyword = input("Enter supplier ID or name: ").lower()

            service = SupplierService()
            suppliers = service.get_all_suppliers()

            found = False

            print("\n===== SUPPLIER DETAIL =====")
            print("-" * 117)
            print(
                f"{"ID":<10}  "
                f"{"Supplier":<35}  "
                f"{"Contact Number":<20}  "
                f"{"Address":<20}  "
                f"{"Email":<20}"
            )
            print("-" * 117)

            for supplier in suppliers:
                if (keyword in supplier["supplier_id"].lower() or
                    keyword in supplier["supplier_name"].lower()):
                    print(
                        f"{supplier["supplier_id"]:<10}  "
                        f"{supplier["supplier_name"]:<35}  "
                        f"{supplier["contact_number"]:<20}  "
                        f"{supplier["address"]:<20}  "
                        f"{supplier["email"]:<20}"
                    )

                    found = True

            print("-" * 117)

            if not found:
                print("Supplier not found!")

            if not back_to_submenu():
                break

        elif choice == "5":
            keyword = input("Enter transaction ID or date: ").lower()

            service = TransactionService()
            transactions = service.get_all_transactions()

            found = False

            print("\n===== TRANSACTION DETAIL =====")
            print("-" * 137)
            print(
                f"{"ID":<10}  "
                f"{"Date":<15}  "
                f"{"Customer":<15}  "
                f"{"Cashier":<15}  "
                f"{"Product":<15}  "
                f"{"Quantity":<10}  "
                f"{"Subtotal":<12}"
                f"{"Total price":<17}  "
                f"{"Payment Method":<15}"
            )
            print("-" * 137)
            
            for transaction in transactions:
                if (keyword in transaction["transaction_id"].lower() or
                    keyword in transaction['transaction_date'].strftime('%Y-%m-%d')):
                    print(
                        f"{transaction["transaction_id"]:<10}  "
                        f"{transaction['transaction_date'].strftime('%Y-%m-%d'):<15}  "
                        f"{transaction["customer_name"]:<15}  "
                        f"{transaction["cashier_name"]:<15}  "
                        f"{transaction["product_name"]:<15}  "
                        f"{transaction["quantity"]:<10}  "
                        f"Rp{transaction["sub_total"]:<8,}  "
                        f"Rp{transaction["total_price"]:<15,}  "
                        f"{transaction["payment_method"]:<15}"
                    )
                    
                    found = True
            
            print("-" * 137)

            if not found:
                print("Transaction not found!")

            if not back_to_submenu():
                break

        elif choice == "6":
            break

def read_menu():
    while True:
        print("\n===== VIEW MENU =====")
        print("1. View Records\n" \
              "2. Search Records\n" \
              "3. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            view_record_menu()
        elif submenu == "2":
            search_record_menu()
        elif submenu == "3":
            break
        else:
            print("Invalid submenu!")
    
def show_detail(data): # Displays dictionary data in key-value format
    for key, value in data.items():
        print(f"{key} : {value}")
 
def confirm_data(data): # Returns True if user confirms
    print("\n===== DATA PREVIEW =====")
    show_detail(data)

    confirm = input("\nAre you sure (yes/no)? ").lower()
    return confirm == "yes"

def create_record_menu(): # Add new records into lists
    while True:
        print("\n===== ADD RECORD MENU =====")
        print("Choose a submenu you want to add:")
        print("1. Add Products\n" \
              "2. Add Customers\n" \
              "3. Add Cashiers\n" \
              "4. Add Suppliers\n" \
              "5. Add Transactions\n" \
              "6. Back to Sub Menu")

        submenu = input("Enter the submenu number you want to add: ")
        if submenu == "1":
            service = ProductService()
            products = service.get_all_products()

            product_id = generate_id("PRO", products, "product_id")

            product_supplier_service = ProductSupplierService()
            product_suppliers = product_supplier_service.get_all_product_suppliers()

            product_supplier_id = generate_id("PSU", product_suppliers, "product_supplier_id")

            print(f"Product ID: {product_id}")

            found = False
            for product in products:
                if product["product_id"] == product_id:
                    found = True
                    break

            if found:
                print("Product ID already exists!")

            else:
                product_name = input("Enter product name: ")
                category = input("Enter category (Food / Household / Personal care / Snack / Beverage): ")
                price = int(input("Enter selling price: "))
                stock = int(input("Enter stock: "))
                supplier_id = input("Enter supplier ID: ")
                supplier_price = int(input("Enter supplier price: "))
                supply_date = input("Enter supply date (YYYY-MM-DD): ")
                stock_supplied = int(input("Enter stock supplied: "))

                new_product = {
                    "product_id": product_id,
                    "product_name": product_name,
                    "category": category,
                    "price": price,
                    "stock": stock,
                    "product_supplier_id": product_supplier_id,
                    "supplier_id": supplier_id,
                    "supplier_price": supplier_price,
                    "supply_date": supply_date,
                    "stock_supplied": stock_supplied
                }

                if confirm_data(new_product):
                    service.add_product(
                        product_id,
                        product_name,
                        category,
                        price,
                        stock,
                        product_supplier_id,
                        supplier_id,
                        supplier_price,
                        supply_date,
                        stock_supplied
                    )
                    print("Product added successfully!")
                else:
                    print("Add product cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "2":
            service = CustomerService()
            customers = service.get_all_customers()

            customer_id = generate_id("CUS", customers, "customer_id")
            print(f"Customer ID: {customer_id}")

            found = False
            for customer in customers:
                if customer["customer_id"] == customer_id:
                    found = True
                    break

            if found:
                print("Customer ID already exists!")

            else:
                customer_name = input("Enter customer name: ")
                gender = input("Enter gender (Female / Male): ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")

                new_customer = {
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "gender": gender,
                    "phone_number": phone_number,
                    "address": address
                }
           
                if confirm_data(new_customer):
                    service.add_customer(
                        customer_id,
                        customer_name,
                        gender,
                        phone_number,
                        address
                    )
                    print("Customer added successfully!")
                else:
                    print("Add customer cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "3":

            service = CashierService()
            cashiers = service.get_all_cashiers()

            cashier_id = generate_id("CAS", cashiers, "cashier_id")
            print(f"Cashier ID: {cashier_id}")

            found = False
            for cashier in cashiers:
                if cashier["cashier_id"] == cashier_id:
                    found = True
                    break

            if found:
                print("Cashier ID already exists!")

            else:
                cashier_name = input("Enter cashier name: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                shift = input("Enter shift: ")

                new_cashier = {
                    "cashier_id": cashier_id,
                    "cashier_name": cashier_name,
                    "username": username,
                    "password": password,
                    "shift": shift
                }

                if confirm_data(new_cashier):
                    service.add_cashier(
                        cashier_id,
                        cashier_name,
                        username,
                        password,
                        shift
                    )
                    print("Cashier added successfully!")
                else:
                    print("Add cashier cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "4":
            service = SupplierService()
            suppliers = service.get_all_suppliers()

            supplier_id = generate_id("SUP", suppliers, "supplier_id")
            print(f"Supplier ID: {supplier_id}")

            found = False
            for supplier in suppliers:
                if supplier["supplier_id"] == supplier_id:
                    found = True
                    break

            if found:
                print("Supplier ID already exists!")

            else:
                supplier_name = input("Enter supplier name: ")
                contact_number = input("Enter contact number: ")
                address = input("Enter address: ")
                email = input("Enter email: ")

                new_supplier = {
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "contact_number": contact_number,
                    "address": address,
                    "email": email
                }

                if confirm_data(new_supplier):
                    service.add_supplier(
                        supplier_id,
                        supplier_name,
                        contact_number,
                        address,
                        email
                    )
                    print("Supplier added successfully!")
                else:
                    print("Add supplier cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "5":
            service = TransactionService()
            transactions = service.get_all_transactions()

            transaction_id = generate_id("TRA", transactions, "transaction_id"
            )

            print(f"Transaction ID: {transaction_id}")

            found = False
            for transaction in transactions:
                if transaction["transaction_id"] == transaction_id:
                    found = True
                    break

            if found:
                print("Transaction ID already exists!")

            else:
                transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
                customer_id = input("Enter customer ID: ").upper()
                cashier_id = input("Enter cashier ID: ").upper()
                payment_method = input("Enter payment method (Cash / Credit card / Debit card / QRIS): ")

                products = []
                total_price = 0

                product_service = ProductService()
                all_products = product_service.get_all_products()

                while True:
                    product_id = input("Enter product ID: ").upper()

                    product_found = False

                    for product in all_products:
                        if product["product_id"] == product_id:

                            product_found = True

                            quantity = int(input("Enter quantity: "))

                            if quantity <= 0:
                                print("Quantity must be greater than 0!")

                            elif quantity > product["stock"]:
                                print("Stock is not enough!")

                            else:
                                sub_total = product["price"] * quantity

                                products.append({
                                    "product_id": product_id,
                                    "quantity": quantity,
                                    "sub_total": sub_total
                                })

                                total_price += sub_total

                                print("Product added to transaction!")

                            break

                    if not product_found:
                        print("Product not found!")

                    again = input("\nAdd another product (yes/no)? ").lower()

                    if again == "no":
                        break

                new_transaction = {
                    "transaction_id": transaction_id,
                    "transaction_date": transaction_date,
                    "customer_id": customer_id,
                    "cashier_id": cashier_id,
                    "payment_method": payment_method,
                    "products": products,
                    "total_price": total_price
                }

                if confirm_data(new_transaction):
                    service.add_transaction(
                        transaction_id,
                        transaction_date,
                        customer_id,
                        cashier_id,
                        total_price,
                        payment_method
                    )

                    detail_service = TransactionDetailService()

                    details = detail_service.get_all_transaction_details()

                    for item in products:
                        detail_id = generate_id("DET", details, "detail_id"
                        )

                        detail_service.add_transaction_detail(
                            detail_id,
                            transaction_id,
                            item["product_id"],
                            item["quantity"],
                            item["sub_total"]
                        )

                        details.append({
                            "detail_id": detail_id
                        })

                    print("Transaction added successfully!")

                else:
                    print("Add transaction cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "6":
            break

        else:
            print("Invalid submenu!")

def create_menu():
    while True:
        print("\n===== ADD MENU =====")
        print("1. Add Records\n" \
              "2. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            create_record_menu()
        elif submenu == "2":
            break
        else:
            print("Invalid submenu!")

def update_record_menu(): # Update existing records 
    while True:
        print("\n===== UPDATE RECORD MENU =====")
        print("Choose a submenu you want to update:")
        print("1. Update Products\n" \
              "2. Update Customers\n" \
              "3. Update Cashiers\n" \
              "4. Update Suppliers\n" \
              "5. Update Transactions\n" \
              "6. Back to Sub Menu")

        submenu = input("Enter the submenu number you want to update: ")

        if submenu == "1":
            product_id = input("Enter product ID: ").upper()

            service = ProductService()
            products = service.get_all_products()

            found = False

            for product in products:
                if product["product_id"] == product_id:
                    found = True

                    print("\n===== PRODUCT DETAILS =====")
                    print("-" * 157)
                    print(
                        f"{"ID":<10}  "
                        f"{"Product":<15}  "
                        f"{"Category":<15}  "
                        f"{"Price":<12}  "
                        f"{"Stock":<10}  "
                        f"{"Supplier Name":<35}  "
                        f"{"Supplier Price":<15}  "
                        f"{"Supply Date":<15}  "
                        f"{"Stock Supplied":<15}"
                    )
                    print("-" * 157)
                    print(
                        f"{product["product_id"]:<10}  "
                        f"{product["product_name"]:<15}  "
                        f"{product["category"]:<15}  "
                        f"Rp{product["price"]:<10,}  "
                        f"{product["stock"]:<10}  "
                        f"{product["supplier_name"]:<35}  "
                        f"Rp{product["supplier_price"]:<13,}  "
                        f"{product['supply_date'].strftime('%Y-%m-%d'):<15}  "
                        f"{product["stock_supplied"]:<15}"
                    )
                    print("-" * 157)

                    option = input("\nDo you want to update this product (yes/no)? ").lower()

                    if option == "yes":
                        column = input("Enter column name to update (product_id / product_name / category / price / stock / supplier_name / supplier_price / supply_date / stock_supplied): ")

                        if column in product:
                            new_value = input("Enter new value: ")

                            if column in ["price", "stock", "supplier_price", "stock_supplied"]:
                                new_value = int(new_value)

                            updated_product = product.copy()
                            updated_product[column] = new_value

                            if confirm_data(updated_product):
                                service.update_product(
                                    product_id,
                                    column,
                                    new_value
                                )

                                print("Product updated successfully!")
                            else:
                                print("Update cancelled!")
                        else:
                            print("Column does not exist!")

                    break

            if not found:
                print("Product data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "2":
            customer_id = input("Enter customer ID: ").upper()

            service = CustomerService()
            customers = service.get_all_customers()

            found = False

            for customer in customers:
                if customer["customer_id"] == customer_id:
                    found = True

                    print("\n===== CUSTOMER DETAILS =====")
                    print("-" * 85)
                    print(
                        f"{"ID":<10}  "
                        f"{"Customer":<15}  "
                        f"{"Gender":<15}  "
                        f"{"Phone Number":<20}  "
                        f"{"Address":<20}"
                    )
                    print("-" * 85)
                    print(
                        f"{customer["customer_id"]:<10}  "
                        f"{customer["customer_name"]:<15}  "
                        f"{customer["gender"]:<15}  "
                        f"{customer["phone_number"]:<20}  "
                        f"{customer["address"]:<20}"
                    )
                    print("-" * 85)

                    option = input("\nDo you want to update this customer (yes/no)? ").lower()

                    if option == "yes":
                        column = input("Enter column name to update (customer_id / customer_name / gender / phone_number / address): ")

                        if column in customer:
                            new_value = input("Enter new value: ")

                            updated_customer = customer.copy()
                            updated_customer[column] = new_value

                            if confirm_data(updated_customer):
                                service.update_customer(
                                    customer_id,
                                    column,
                                    new_value
                                )
                                print("Customer updated successfully!")
                            else:
                                print("Update cancelled!")
                        else:
                            print("Column does not exist!")

                    break

            if not found:
                print("Customer data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "3":
            cashier_id = input("Enter cashier ID: ").upper()

            service = CashierService()
            cashiers = service.get_all_cashiers()

            found = False

            for cashier in cashiers:
                if cashier["cashier_id"] == cashier_id:
                    found = True

                    print("\n===== CASHIER DETAILS =====")
                    print("-" * 75)
                    print(
                        f"{"ID":<10}  "
                        f"{"Cashier":<15}  "
                        f"{"Username":<15}  "
                        f"{"Password":<20}  "
                        f"{"Shift":<15}"
                    )
                    print("-" * 75)
                    print(
                        f"{cashier["cashier_id"]:<10}  "
                        f"{cashier["cashier_name"]:<15}  "
                        f"{cashier["username"]:<15}  "
                        f"{cashier["password"]:<20}  "
                        f"{cashier["shift"]:<15}"
                    )
                    print("-" * 75)

                    option = input("\nDo you want to update this cashier (yes/no)? ").lower()

                    if option == "yes":
                        column = input("Enter column name to update (cashier_id / cashier_name / username / password / shift): ")

                        if column in cashier:
                            new_value = input("Enter new value: ")

                            updated_cashier = cashier.copy()
                            updated_cashier[column] = new_value

                            if confirm_data(updated_cashier):                
                                service.update_cashier(
                                    cashier_id,
                                    column,
                                    new_value
                                )

                                print("Cashier updated successfully!")
                            else:
                                print("Update cancelled!")
                        else:
                            print("Column does not exist!")

                    break

            if not found:
                print("Cashier data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "4":
            supplier_id = input("Enter supplier ID: ").upper()

            service = SupplierService()
            suppliers = service.get_all_suppliers()

            found = False

            for supplier in suppliers:
                if supplier["supplier_id"] == supplier_id:
                    found = True

                    print("\n===== SUPPLIER DETAILS =====")
                    print("-" * 117)
                    print(
                        f"{"ID":<10}  "
                        f"{"Supplier":<35}  "
                        f"{"Contact Number":<20}  "
                        f"{"Address":<20}  "
                        f"{"Email":<20}"
                    )
                    print("-" * 117)
                    print(
                        f"{supplier["supplier_id"]:<10}  "
                        f"{supplier["supplier_name"]:<35}  "
                        f"{supplier["contact_number"]:<20}  "
                        f"{supplier["address"]:<20}  "
                        f"{supplier["email"]:<20}"
                    )
                    print("-" * 117)

                    option = input("\nDo you want to update this supplier (yes/no)? ").lower()

                    if option == "yes":
                        column = input("Enter column name to update (supplier_id / supplier_name / contact_number / address / email): ")

                        if column in supplier:
                            new_value = input("Enter new value: ")

                            updated_supplier = supplier.copy()
                            updated_supplier[column] = new_value

                            if confirm_data(updated_supplier):                
                                service.update_supplier(
                                    supplier_id,
                                    column,
                                    new_value
                                )
                                print("Supplier updated successfully!")
                            else:
                                print("Update cancelled!")
                        else:
                            print("Column does not exist!")

                    break

            if not found:
                print("Supplier data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "5":
            transaction_id = input("Enter transaction ID: ").upper()

            service = TransactionService()
            transactions = service.get_all_transactions()

            selected_transactions = [
                t for t in transactions
                if t["transaction_id"] == transaction_id
            ]

            if len(selected_transactions) == 0:
                print("Transaction data does not exist!")

            else:
                print("\n===== TRANSACTION DETAILS =====")
                print("-" * 145)
                print(
                    f"{"No":<5}  "
                    f"{"ID":<10}  "
                    f"{"Date":<15}  "
                    f"{"Customer":<15}  "
                    f"{"Cashier":<15}  "
                    f"{"Product":<15}  "
                    f"{"Quantity":<10}  "
                    f"{"Subtotal":<12}"
                    f"{"Total price":<17}  "
                    f"{"Payment Method":<15}"
                )
                print("-" * 145)

                for i, transaction in enumerate(selected_transactions, start=1):
                    print(
                        f"{i:<5}  "
                        f"{transaction['transaction_id']:<10}  "
                        f"{transaction['transaction_date'].strftime('%Y-%m-%d'):<15}  "
                        f"{transaction['customer_name']:<15}  "
                        f"{transaction['cashier_name']:<15}  "
                        f"{transaction['product_name']:<15}  "
                        f"{transaction['quantity']:<10}  "
                        f"Rp{transaction['sub_total']:<8,}  "
                        f"Rp{transaction['total_price']:<15,}  "
                        f"{transaction['payment_method']:<15}"
                    )

                print("-" * 145)

                option = input("\nDo you want to update this transaction (yes/no)? ").lower()

                if option == "yes":
                    product_number = int(
                        input("Choose product number to update: ")
                    )

                    if 1 <= product_number <= len(selected_transactions):

                        selected_product = (selected_transactions[product_number - 1])

                        print("\nSelected product:")
                        show_detail(selected_product)

                        product_service = ProductService()
                        products = product_service.get_all_products()

                        product_price = 0

                        for product in products:
                            if product["product_name"] == selected_product["product_name"]:
                                product_price = product["price"]
                                break

                        column = input("\nEnter column name to update (quantity): ")

                        if column in ["quantity", "sub_total"]:
                            new_quantity = int(input("Enter new quantity: "))
                            new_subtotal = product_price * new_quantity
                            detail_service = TransactionDetailService()
                            detail_service.update_transaction_detail(
                                selected_product["detail_id"],
                                "quantity",
                                new_quantity
                            )

                            detail_service.update_transaction_detail(
                                selected_product["detail_id"],
                                "sub_total",
                                new_subtotal
                            )

                            details = detail_service.get_all_transaction_details()

                            new_total = 0
                            for detail in details:
                                if detail["transaction_id"] == transaction_id:
                                    new_total += detail["sub_total"]
                            transaction_service = TransactionService()
                            transaction_service.update_total_price(
                                transaction_id,
                                new_total
                            )

                            print("Transaction updated successfully!")

                        else:
                            print("Column does not exist!")

                    else:
                        print("Invalid product number!")

            if not back_to_submenu():
                break

        elif submenu == "7":
            detail_id = input("Enter transaction detail ID: ").upper()

            service = TransactionDetailService()
            transaction_details = service.get_all_transaction_details()

            found = False

            for transaction_detail in transaction_details:
                if transaction_detail["detail_id"] == detail_id:
                    found = True

                    print("\n===== TRANSACTION DETAILS =====")
                    print("-" * 85)
                    print(
                        f"{"ID":<10}  "
                        f"{"Transaction ID":<15}  "
                        f"{"Product ID":<15}  "
                        f"{"Quantity":<20}  "
                        f"{"Sub Total":<20}"
                    )
                    print("-" * 85)
                    print(
                        f"{transaction_detail["detail_id"]:<10}  "
                        f"{transaction_detail["transaction_id"]:<15}  "
                        f"{transaction_detail["product_id"]:<15}  "
                        f"{transaction_detail["quantity"]:<20}  "
                        f"{transaction_detail["sub_total"]:<20}"
                    )
                    print("-" * 85)

                    option = input("\nDo you want to update this transaction detail (yes/no)? ").lower()

                    if option == "yes":
                        column = input("Enter column name to update (detail_id / transaction_id / product_id / quantity / sub_total): ")

                        if column in transaction_detail:
                            new_value = input("Enter new value: ")

                            if column in ["quantity", "sub_total"]:
                                new_value = int(new_value)

                            updated_transaction_detail = transaction_detail.copy()
                            updated_transaction_detail[column] = new_value

                            if confirm_data(updated_transaction_detail):
                                service.update_transaction_detail(
                                    detail_id,
                                    column,
                                    new_value
                                )
                                print("Transaction detail updated successfully!")
                            else:
                                print("Update cancelled!")
                        else:
                            print("Column does not exist!")

                    break

            if not found:
                print("Customer data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "8":
            break

        else:
            print("Invalid submenu!")

def update_menu():
    while True:
        print("\n===== UPDATE MENU =====")
        print("1. Update Records\n" \
              "2. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            update_record_menu()

        elif submenu == "2":
            break
        else:
            print("Invalid submenu!")

def delete_record_menu(): # Delete unused records
    while True:
        print("\n===== DELETE RECORD MENU =====")
        print("Choose a submenu you want to delete:")
        print("1. Delete Products\n" \
              "2. Delete Customers\n" \
              "3. Delete Cashiers\n" \
              "4. Delete Suppliers\n" \
              "5. Delete Transactions\n" \
              "6. Back to Sub Menu")

        submenu = input("Enter the submenu number you want to delete: ")

        if submenu == "1":
            product_id = input("Enter product ID: ").upper()

            service = ProductService()
            products = service.get_all_products()

            found = False

            for product in products:
                if product["product_id"] == product_id:
                    found = True

                    print("\n===== PRODUCT DETAILS =====")
                    print("-" * 65)
                    print(
                        f"{"ID":<10}  "
                        f"{"Product":<15}  "
                        f"{"Category":<15}  "
                        f"{"Price":<12}  "
                        f"{"Stock":<10}  "
                    )
                    print("-" * 65)
                    print(
                        f"{product["product_id"]:<10}  "
                        f"{product["product_name"]:<15}  "
                        f"{product["category"]:<15}  "
                        f"Rp{product["price"]:<10,}  "
                        f"{product["stock"]:<10}  "
                    )
                    print("-" * 65)

                    option = input("\nDo you want to delete this product (yes/no)? ").lower()

                    if option == "yes":
                        service.delete_product(product_id)
                        print("Product deleted successfully!")
                    else:
                        print("Delete cancelled!")

                    break

            if not found:
                print("Product data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "2":
            customer_id = input("Enter customer ID: ").upper()

            service = CustomerService()
            customers = service.get_all_customers()

            found = False

            for customer in customers:
                if customer["customer_id"] == customer_id:
                    found = True

                    print("\n===== CUSTOMER DETAILS =====")
                    print("-" * 85)
                    print(
                        f"{"ID":<10}  "
                        f"{"Customer":<15}  "
                        f"{"Gender":<15}  "
                        f"{"Phone Number":<20}  "
                        f"{"Address":<20}"
                    )
                    print("-" * 85)
                    print(
                        f"{customer["customer_id"]:<10}  "
                        f"{customer["customer_name"]:<15}  "
                        f"{customer["gender"]:<15}  "
                        f"{customer["phone_number"]:<20}  "
                        f"{customer["address"]:<20}"
                    )
                    print("-" * 85)

                    option = input("\nDo you want to delete this customer (yes/no)? ").lower()
            
                    if option == "yes":
                        service.delete_customer(customer_id)
                        print("Customer deleted successfully!")
                    else:
                        print("Delete cancelled!")

                    break

            if not found:
                print("Customer data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "3":
            cashier_id = input("Enter cashier ID: ").upper()

            service = CashierService()
            cashiers = service.get_all_cashiers()

            found = False

            for cashier in cashiers:
                if cashier["cashier_id"] == cashier_id:
                    found = True

                    print("\n===== CASHIER DETAILS =====")
                    print("-" * 75)
                    print(
                        f"{"ID":<10}  "
                        f"{"Cashier":<15}  "
                        f"{"Username":<15}  "
                        f"{"Password":<20}  "
                        f"{"Shift":<15}"
                    )
                    print("-" * 75)
                    print(
                        f"{cashier["cashier_id"]:<10}  "
                        f"{cashier["cashier_name"]:<15}  "
                        f"{cashier["username"]:<15}  "
                        f"{cashier["password"]:<20}  "
                        f"{cashier["shift"]:<15}"
                    )
                    print("-" * 75)

                    option = input("\nDo you want to delete this cashier (yes/no)? ").lower()

                    if option == "yes":
                        service.delete_cashier(cashier_id)
                        print("Cashier deleted successfully!")
                    else:
                        print("Delete cancelled!")

                    break

            if not found:
                print("Cashier data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "4":
            supplier_id = input("Enter supplier ID: ").upper()

            service = SupplierService()
            suppliers = service.get_all_suppliers()

            found = False

            for supplier in suppliers:
                if supplier["supplier_id"] == supplier_id:
                    found = True

                    print("\n===== SUPPLIER DETAILS =====")
                    print("-" * 117)
                    print(
                        f"{"ID":<10}  "
                        f"{"Supplier":<35}  "
                        f"{"Contact Number":<20}  "
                        f"{"Address":<20}  "
                        f"{"Email":<20}"
                    )
                    print("-" * 117)
                    print(
                        f"{supplier["supplier_id"]:<10}  "
                        f"{supplier["supplier_name"]:<35}  "
                        f"{supplier["contact_number"]:<20}  "
                        f"{supplier["address"]:<20}  "
                        f"{supplier["email"]:<20}"
                    )
                    print("-" * 117)

                    option = input("\nDo you want to delete this supplier (yes/no)? ").lower()

                    if option == "yes":            
                        service.delete_supplier(supplier_id)
                        print("Supplier deleted successfully!")
                    else:
                        print("Delete cancelled!")

                    break

            if not found:
                print("Supplier data does not exist!")

            if not back_to_submenu():
                break

        elif submenu == "5":
            transaction_id = input("Enter transaction ID: ").upper()

            service = TransactionService()
            transactions = service.get_all_transactions()

            details = [
                t for t in transactions
                if t["transaction_id"] == transaction_id
            ]

            if not details:
                print("Transaction data does not exist!")

            else:
                print("\n===== TRANSACTION DETAILS =====")
                print("-" * 145)

                print(
                    f"{"No":<5}  "
                    f"{"ID":<10}  "
                    f"{"Date":<15}  "
                    f"{"Customer":<15}  "
                    f"{"Cashier":<15}  "
                    f"{"Product":<15}  "
                    f"{"Quantity":<10}  "
                    f"{"Subtotal":<12}"
                    f"{"Total price":<17}  "
                    f"{"Payment Method":<15}"
                )

                print("-" * 145)

                for i, row in enumerate(details, start=1):
                    print(
                        f"{i:<5}  "
                        f"{row['transaction_id']:<10}  "
                        f"{row['transaction_date'].strftime('%Y-%m-%d'):<15}  "
                        f"{row['customer_name']:<15}  "
                        f"{row['cashier_name']:<15}  "
                        f"{row['product_name']:<15}  "
                        f"{row['quantity']:<10}  "
                        f"Rp{row['sub_total']:<8,}  "
                        f"Rp{row['total_price']:<15,}  "
                        f"{row['payment_method']:<15}"
                    )

                print("-" * 145)

                option = input("\nDo you want to delete product transaction (yes/no)? ").lower()

                if option == "yes":
                    product_number = int(input("Choose product number to delete: "))

                    if 1 <= product_number <= len(details):

                        selected_product = details[product_number - 1]

                        print("\nSelected product:")
                        show_detail(selected_product)

                        confirm = input("\nAre you sure to delete this product (yes/no)? ").lower()

                        if confirm == "yes":

                            detail_service = TransactionDetailService()

                            detail_service.delete_transaction_detail(
                                selected_product["detail_id"]
                            )

                            remaining_details = [
                                d for d in detail_service.get_all_transaction_details()
                                if d["transaction_id"] == transaction_id
                            ]

                            transaction_service = TransactionService()

                            if len(remaining_details) == 0:

                                transaction_service.delete_transaction(transaction_id)

                                print("Transaction deleted successfully!")

                            else:
                                new_total = sum(
                                    d["sub_total"]
                                    for d in remaining_details
                                )

                                transaction_service.update_total_price(
                                    transaction_id,
                                    new_total
                                )

                                print(
                                    "Transaction deleted successfully!"
                                )

                        else:
                            print("Delete cancelled!")

                    else:
                        print("Invalid transaction number!")

                else:
                    print("Delete cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "6":
            break

        else:
            print("Invalid submenu!")

            if not back_to_submenu():
                break
  
def delete_menu():
    while True:
        print("\n===== DELETE MENU =====")
        print("1. Delete Records\n" \
              "2. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            delete_record_menu()

        elif submenu == "2":
            break
        else:
            print("Invalid submenu!")

def export_record_menu():
    while True:
        print("\n===== EXPORT RECORD MENU =====")
        print("Choose a submenu you want to export:")
        print("1. Export Products\n" \
              "2. Export Customers\n" \
              "3. Export Cashiers\n" \
              "4. Export Suppliers\n" \
              "5. Export Transactions\n" \
              "6. Back to Sub Menu")
        
        submenu = input("Enter the submenu number you want to export: ")

        if submenu == "1":
            service = ProductService()
            service.export_product()

            if not back_to_submenu():
                break

        elif submenu == "2":
            service = CustomerService()
            service.export_customer()

            if not back_to_submenu():
                break

        elif submenu == "3":
            service = CashierService()
            service.export_cashier()

            if not back_to_submenu():
                break

        elif submenu == "4":
            service = SupplierService()
            service.export_supplier()

            if not back_to_submenu():
                break

        elif submenu == "5":
            service = TransactionService()
            service.export_transaction()

            if not back_to_submenu():
                break

        elif submenu == "6":
            break

        else:
            print("Invalid submenu!")

            if not back_to_submenu():
                break
        

def export_menu():
    while True:
        print("\n===== EXPORT MENU =====")
        print("1. Export Records\n" \
              "2. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            export_record_menu()

        elif submenu == "2":
            break
        else:
            print("Invalid submenu!")

# /===== Main Program =====/
def main():
    while True:
        menu = view_menu()
        
        if menu == "1":
            read_menu()

        elif menu == "2":
            create_menu()

        elif menu == "3":
            update_menu()

        elif menu == "4":
            delete_menu()

        elif menu == "5":
            export_menu()

        elif menu == "6":
            print("You have exited the program!")
            break

        else:
            print("Menu you entered is not available!")

if __name__ == "__main__":
    main()