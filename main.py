# ===================================
# WAREHOUSE MANAGEMENT SYSTEM
# ===================================
# Developed by. Angela Adytha Putri
# JCDS - 33

# /************************************/
print("\n=== STORE TRANSACTION MANAGEMENT SYSTEM ===")
# /===== Data Model =====/
products_list = [
    {
        "product_id": "PRO001",
        "product_name": "Mi instan",
        "category": "Food",
        "price": 3500,
        "stock": 100,
        "supplier_name": "PT Indofood CBP Sukses Makmur Tbk.",
        "supplier_price": 3000,
        "supply_date": "2025-07-13",
        "stock_supplied": 50
    },
    {
        "product_id": "PRO002",
        "product_name": "Detergen",
        "category": "Household",
        "price": 30000,
        "stock": 150,
        "supplier_name": "PT Unilever Indonesia Tbk.",
        "supplier_price": 28000,
        "supply_date": "2025-08-28",
        "stock_supplied": 80
    },
    {
        "product_id": "PRO003",
        "product_name": "Cat rambut",
        "category": "Personal care",
        "price": 65000,
        "stock": 60,
        "supplier_name": "PT Eres Revco",
        "supplier_price": 60000,
        "supply_date": "2025-09-01",
        "stock_supplied": 60
    },
    {
        "product_id": "PRO004",
        "product_name": "Coklat",
        "category": "Snack",
        "price": 8000,
        "stock": 120,
        "supplier_name": "PT Nestle Indonesia",
        "supplier_price": 7000,
        "supply_date": "2025-11-19",
        "stock_supplied": 70
    },
    {
        "product_id": "PRO005",
        "product_name": "Air mineral",
        "category": "Beverage",
        "price": 4000,
        "stock": 200,
        "supplier_name": "PT Tirta Fresindo Jaya",
        "supplier_price": 3500,
        "supply_date": "2025-12-23",
        "stock_supplied": 200
    }
]

customers_list = [
    {
        "customer_id": "CUS001",
        "customer_name": "Enjel",
        "gender": "Female",
        "phone_number": "0819-1818-2003",
        "address": "Tangerang Selatan"
    },
    {
        "customer_id": "CUS002",
        "customer_name": "Nadya",
        "gender": "Female",
        "phone_number": "0814-8291-7364",
        "address": "Makassar"
    },
    {
        "customer_id": "CUS003",
        "customer_name": "Valen",
        "gender": "Female",
        "phone_number": "0817-3190-5482",
        "address": "Belitung"
    },
    {
        "customer_id": "CUS004",
        "customer_name": "Elmar",
        "gender": "Male",
        "phone_number": "0815-8420-3917",
        "address": "Jakarta Barat"
    },
    {
        "customer_id": "CUS005",
        "customer_name": "Mika",
        "gender": "Male",
        "phone_number": "0819-2647-1538",
        "address": "Kemang"
    },
    {
        "customer_id": "CUS006",
        "customer_name": "Rafi",
        "gender": "Male",
        "phone_number": "0813-1784-5206",
        "address": "Bintaro"
    },
    {
        "customer_id": "CUS007",
        "customer_name": "Adam",
        "gender": "Male",
        "phone_number": "0816-4091-8275",
        "address": "Aceh"
    }
]

cashiers_list = [
    {
        "cashier_id": "CAS001",
        "cashier_name": "Athiyyah",
        "username": "athiyyah",
        "password": "athiyyah123",
        "shift": "Morning"
    },
    {
        "cashier_id": "CAS002",
        "cashier_name": "Donny",
        "username": "donny",
        "password": "donny123",
        "shift": "Evening"
    },
    {
        "cashier_id": "CAS003",
        "cashier_name": "Hane",
        "username": "hane",
        "password": "hane123",
        "shift": "Night"
    },
    {
        "cashier_id": "CAS004",
        "cashier_name": "Yoanita",
        "username": "yoanita",
        "password": "yoanita123",
        "shift": "Morning"
    },
    {
        "cashier_id": "CAS005",
        "cashier_name": "Yonathan",
        "username": "yonathan",
        "password": "yonathan123",
        "shift": "Evening"
    },
    {
        "cashier_id": "CAS006",
        "cashier_name": "Pirlo",
        "username": "pirlo",
        "password": "pirlo123",
        "shift": "Night"
    },
    {
        "cashier_id": "CAS007",
        "cashier_name": "Zian",
        "username": "zian",
        "password": "zian123",
        "shift": "Night"
    }
]

suppliers_list = [
    {
        "supplier_id": "SUP001",
        "supplier_name": "PT Indofood CBP Sukses Makmur Tbk.",
        "contact_number": "021-5795-8822",
        "address": "Jakarta Selatan",
        "email": "indofood@gmail.com"
    },
    {
        "supplier_id": "SUP002",
        "supplier_name": "PT Unilever Indonesia Tbk.",
        "contact_number": "025-1867-2409",
        "address": "Bogor",
        "email": "unilever@gmail.com"
    },
    {
        "supplier_id": "SUP003",
        "supplier_name": "PT Eres Revco",
        "contact_number": "021-525-6976",
        "address": "Jakarta Selatan",
        "email": "eres.revco@gmail.com"
    },
    {
        "supplier_id": "SUP004",
        "supplier_name": "PT Nestle Indonesia",
        "contact_number": "021-7883-6000",
        "address": "Bekasi",
        "email": "nestle@gmail.com"
    },
    {
        "supplier_id": "SUP005",
        "supplier_name": "PT Tirta Fresindo Jaya",
        "contact_number": "0838-3924-0777",
        "address": "Jakarta Barat",
        "email": "tirta.fresindo@gmail.com"
    }
]

transactions_list = [
    {
        "transaction_id": "TRA001",
        "transaction_date": "2026-04-15",
        "customer_name": "Enjel",
        "cashier_name": "Athiyyah",
        "payment_method": "QRIS",
        "products": [
            {
                "product_name": "Mi instan",
                "quantity": 2,
                "sub_total": 7000
            },
            {
                "product_name": "Detergen",
                "quantity": 1,
                "sub_total": 30000
            }
        ],
        "total_price": 37000
    },

    {
        "transaction_id": "TRA002",
        "transaction_date": "2026-04-23",
        "customer_name": "Nadya",
        "cashier_name": "Donny",
        "payment_method": "Debit card",
        "products": [
            {
                "product_name": "Coklat",
                "quantity": 1,
                "sub_total": 8000
            },
            {
                "product_name": "Air mineral",
                "quantity": 1,
                "sub_total": 4000
            }
        ],
        "total_price": 12000
    },

    {
        "transaction_id": "TRA003",
        "transaction_date": "2026-04-28",
        "customer_name": "Valen",
        "cashier_name": "Hane",
        "payment_method": "Cash",
        "products": [
            {
                "product_name": "Detergen",
                "quantity": 1,
                "sub_total": 30000
            },
            {
                "product_name": "Cat rambut",
                "quantity": 1,
                "sub_total": 65000
            }
        ],
        "total_price": 95000
    },

    {
        "transaction_id": "TRA004",
        "transaction_date": "2026-05-09",
        "customer_name": "Elmar",
        "cashier_name": "Yoanita",
        "payment_method": "Credit card",
        "products": [
            {
                "product_name": "Mi instan",
                "quantity": 5,
                "sub_total": 17500
            },
            {
                "product_name": "Air mineral",
                "quantity": 5,
                "sub_total": 20000
            }
        ],
        "total_price": 37500
    },

    {
        "transaction_id": "TRA005",
        "transaction_date": "2026-05-20",
        "customer_name": "Mika",
        "cashier_name": "Yonathan",
        "payment_method": "QRIS",
        "products": [
            {
                "product_name": "Mi instan",
                "quantity": 3,
                "sub_total": 10500
            },
            {
                "product_name": "Air mineral",
                "quantity": 5,
                "sub_total": 20000
            }
        ],
        "total_price": 30500
    }
]

# /===== Feature Program =====/
def view_menu():
    print("\nMenu Lists")
    print("1. View records\n" \
          "2. Add new record(s)\n" \
          "3. Update a record\n" \
          "4. Delete a record\n" \
          "5. Exit program")
    menu = input("Enter the menu number you want to run: ")
    return menu

def back_to_submenu():
    while True:
        option = input("\nDo you want to choose another submenu (yes/no)? ").lower()
        if option == "yes":
            return True
        elif option == "no":
            return False
        else:
            print("Invalid input!")

def view_record_menu():
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
            for product in products_list:
                print(
                    f"{product["product_id"]:<10}  "
                    f"{product["product_name"]:<15}  "
                    f"{product["category"]:<15}  "
                    f"Rp{product["price"]:<10,}  "
                    f"{product["stock"]:<10}  "
                    f"{product["supplier_name"]:<35}  "
                    f"Rp{product["supplier_price"]:<13,}  "
                    f"{product["supply_date"]:<15}  "
                    f"{product["stock_supplied"]:<15}"
                )
            print("-" * 157)

            if not back_to_submenu():
                break

        elif submenu == "2":
            print("\n===== CUSTOMER LIST =====")
            print("-" * 85)
            print(
                f"{"ID":<10}  "
                f"{"Customer":<15}  "
                f"{"Gender":<15}  "
                f"{"Phone Number":<20}  "
                f"{"Address":<20}"
            )
            print("-" * 85)
            for customer in customers_list:
                print(
                    f"{customer["customer_id"]:<10}  "
                    f"{customer["customer_name"]:<15}  "
                    f"{customer["gender"]:<15}  "
                    f"{customer["phone_number"]:<20}  "
                    f"{customer["address"]:<20}"
                )
            print("-" * 85)

            if not back_to_submenu():
                break

        elif submenu == "3":
            print("\n===== CASHIER LIST =====")
            print("-" * 75)
            print(
                f"{"ID":<10}  "
                f"{"Cashier":<15}  "
                f"{"Username":<15}  "
                f"{"Password":<20}  "
                f"{"Shift":<15}"
            )
            print("-" * 75)
            for cashier in cashiers_list:
                print(
                    f"{cashier["cashier_id"]:<10}  "
                    f"{cashier["cashier_name"]:<15}  "
                    f"{cashier["username"]:<15}  "
                    f"{cashier["password"]:<20}  "
                    f"{cashier["shift"]:<15}"
                )
            print("-" * 75)

            if not back_to_submenu():
                break

        elif submenu == "4":
            print("\n===== SUPPLIER LIST =====")
            print("-" * 117)
            print(
                f"{"ID":<10}  "
                f"{"Supplier":<35}  "
                f"{"Contact Number":<20}  "
                f"{"Address":<20}  "
                f"{"Email":<20}"
            )
            print("-" * 117)
            for supplier in suppliers_list:
                print(
                    f"{supplier["supplier_id"]:<10}  "
                    f"{supplier["supplier_name"]:<35}  "
                    f"{supplier["contact_number"]:<20}  "
                    f"{supplier["address"]:<20}  "
                    f"{supplier["email"]:<20}"
                )
            print("-" * 117)

            if not back_to_submenu():
                break

        elif submenu == "5":
            print("\n===== TRANSACTION LIST =====")
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

            for transaction in transactions_list:
                for product in transaction["products"]:
                    print(
                        f"{transaction["transaction_id"]:<10}  "
                        f"{transaction["transaction_date"]:<15}  "
                        f"{transaction["customer_name"]:<15}  "
                        f"{transaction["cashier_name"]:<15}  "
                        f"{product["product_name"]:<15}  "
                        f"{product["quantity"]:<10}  "
                        f"Rp{product["sub_total"]:<10,}  "
                        f"Rp{transaction["total_price"]:<15,}  "
                        f"{transaction["payment_method"]:<15}"
                    )
            print("-" * 137)

            if not back_to_submenu():
                break

        elif submenu == "6":
            break

        else:
            print("Invalid submenu!")

            if not back_to_submenu():
                break

def search_record_menu():
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

            found = False

            for product in products_list:
                if (keyword in product["product_id"].lower() or
                    keyword in product["product_name"].lower()):

                    print("\nProduct details:")
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
                        f"{product["supply_date"]:<15}  "
                        f"{product["stock_supplied"]:<15}"
                    )
                    print("-" * 157)
                    
                    found = True

            if not found:
                print("Product not found!")

            if not back_to_submenu():
                break

        elif choice == "2":
            keyword = input("Enter customer ID or name: ").lower()

            found = False

            for customer in customers_list:
                if (keyword in customer["customer_id"].lower() or
                    keyword in customer["customer_name"].lower()):

                    print("\Customer details:")
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

                    found = True

            if not found:
                print("Customer not found!")

            if not back_to_submenu():
                break

        elif choice == "3":
            keyword = input("Enter cashier ID or name: ").lower()

            found = False

            for cashier in cashiers_list:
                if (keyword in cashier["cashier_id"].lower() or
                    keyword in cashier["cashier_name"].lower()):

                    print("\nCashier details: ")
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

                    found = True

            if not found:
                print("Cashier not found!")

            if not back_to_submenu():
                break

        elif choice == "4":
            keyword = input("Enter supplier ID or name: ").lower()

            found = False

            for supplier in suppliers_list:
                if (keyword in supplier["supplier_id"].lower() or
                    keyword in supplier["supplier_name"].lower()):

                    print("\nSupplier details:")
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

                    found = True

            if not found:
                print("Supplier not found!")

            if not back_to_submenu():
                break

        elif choice == "5":
            keyword = input("Enter transaction ID or date: ").lower()

            found = False

            for transaction in transactions_list:
                if (keyword in transaction["transaction_id"].lower() or
                    keyword in transaction["transaction_date"].lower()):

                    print("\nTransaction details:")
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
                    for product in transaction["products"]:
                        print(
                            f"{transaction["transaction_id"]:<10}  "
                            f"{transaction["transaction_date"]:<15}  "
                            f"{transaction["customer_name"]:<15}  "
                            f"{transaction["cashier_name"]:<15}  "
                            f"{product["product_name"]:<15}  "
                            f"{product["quantity"]:<10}  "
                            f"Rp{product["sub_total"]:<10,}  "
                            f"Rp{transaction["total_price"]:<15,}  "
                            f"{transaction["payment_method"]:<15}"
                        )
                    print("-" * 137)

                    found = True

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
    
def confirm_data(data):
    print("\n===== DATA PREVIEW =====")

    for key, value in data.items():
        print(f"{key} : {value}")

    confirm = input("\nAre you sure (yes/no)? ").lower()

    return confirm == "yes"

def create_record_menu():
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
            product_id = input("Enter product ID: ").upper()

            found = False
            for product in products_list:
                if product["product_id"] == product_id:
                    found = True
                    break

            if found:
                print("Product ID already exists!")

            else:
                product_name = input("Enter product name: ")
                category = input("Enter category: ")
                price = int(input("Enter selling price: "))
                stock = int(input("Enter stock: "))
                supplier_name = input("Enter supplier name: ")
                supplier_price = int(input("Enter supplier price: "))
                supply_date = input("Enter supply date (YYYY-MM-DD): ")
                stock_supplied = int(input("Enter stock supplied: "))

                new_product = {
                    "product_id": product_id,
                    "product_name": product_name,
                    "category": category,
                    "price": price,
                    "stock": stock,
                    "supplier_name": supplier_name,
                    "supplier_price": supplier_price,
                    "supply_date": supply_date,
                    "stock_supplied": stock_supplied
                }

                if confirm_data(new_product):
                    products_list.append(new_product)
                    print("Product added successfully!")
                else:
                    print("Add product cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "2":
            customer_id = input("Enter customer ID: ").upper()

            found = False
            for customer in customers_list:
                if customer["customer_id"] == customer_id:
                    found = True
                    break

            if found:
                print("Customer ID already exists!")

            else:
                customer_name = input("Enter customer name: ")
                gender = input("Enter gender: ")
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
                    customers_list.append(new_customer)
                    print("Customer added successfully!")
                else:
                    print("Add customer cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "3":
            cashier_id = input("Enter cashier ID: ").upper()

            found = False
            for cashier in cashiers_list:
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
                    cashiers_list.append(new_cashier)
                    print("Cashier added successfully!")
                else:
                    print("Add cashier cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "4":
            supplier_id = input("Enter supplier ID: ").upper()

            found = False
            for supplier in suppliers_list:
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
                    suppliers_list.append(new_supplier)
                    print("Supplier added successfully!")
                else:
                    print("Add supplier cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "5":
            transaction_id = input("Enter transaction ID: ").upper()

            found = False
            for transaction in transactions_list:
                if transaction["transaction_id"] == transaction_id:
                    found = True
                    break

            if found:
                print("Transaction ID already exists!")

            else:
                transaction_date = input("Enter transaction date: ")
                customer_name = input("Enter customer name: ")
                cashier_name = input("Enter cashier name: ")
                payment_method = input("Enter payment method: ")

                products = []
                total_price = 0

                while True:
                    product_name = input("Enter product name: ")
                    product_found = False

                    for product in products_list:
                        if product["product_name"].lower() == product_name.lower():
                            product_found = True
                            quantity = int(input("Enter quantity: "))
                            sub_total = product["price"] * quantity
                            transaction_product = {
                                "product_name": product["product_name"],
                                "quantity": quantity,
                                "sub_total": sub_total
                            }

                            products.append(transaction_product)
                            total_price += sub_total
                            print("Product added to transaction!")
                            break

                    if not product_found:
                        print("Product not found!")

                    again = input("Add another product (yes/no)? ").lower()

                    if again == "no":
                        break

                new_transaction = {
                    "transaction_id": transaction_id,
                    "transaction_date": transaction_date,
                    "customer_name": customer_name,
                    "cashier_name": cashier_name,
                    "payment_method": payment_method,
                    "products": products,
                    "total_price": total_price
                }

                if confirm_data(new_transaction):
                    transactions_list.append(new_transaction)
                    print("Transaction added successfully!")
                else:
                    print("Add transaction cancelled!")

            if not back_to_submenu():
                break

        elif submenu == "6":
            break

        else:
            pass

def create_menu():
    while True:
        print("\n===== VIEW MENU =====")
        print("1. Add Records\n" \
              "2. Back to Main Menu")
        
        submenu = input("Enter the submenu number: ")
        if submenu == "1":
            create_record_menu()
        elif submenu == "2":
            break
        else:
            print("Invalid submenu!")

def update_menu():
    """Function for update the data
    """
    return

def delete_menu():
    """Function for delete the data
    """
    return

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
            print("You have exited the program!")
            break

        else:
            print("Menu you entered is not available!")

if __name__ == "__main__":
    main()