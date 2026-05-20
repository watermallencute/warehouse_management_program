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
        "stock": 100
    },
    {
        "product_id": "PRO002",
        "product_name": "Detergen",
        "category": "Household",
        "price": 30000,
        "stock": 150
    },
    {
        "product_id": "PRO003",
        "product_name": "Cat rambut",
        "category": "Personal care",
        "price": 65000,
        "stock": 60
    },
    {
        "product_id": "PRO004",
        "product_name": "Coklat",
        "category": "Snack",
        "price": 8000,
        "stock": 120
    },
    {
        "product_id": "PRO005",
        "product_name": "Air mineral",
        "category": "Beverage",
        "price": 4000,
        "stock": 200
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
        "customer_id": "CUS001",
        "cashier_id": "CAS001",
        "total_price": 37000,
        "payment_method": "QRIS"
    },
    {
        "transaction_id": "TRA002",
        "transaction_date": "2026-04-23",
        "customer_id": "CUS002",
        "cashier_id": "CAS002",
        "total_price": 12000,
        "payment_method": "Debit card"
    },
    {
        "transaction_id": "TRA003",
        "transaction_date": "2026-04-28",
        "customer_id": "CUS003",
        "cashier_id": "CAS003",
        "total_price": 95000,
        "payment_method": "Cash"
    },
    {
        "transaction_id": "TRA004",
        "transaction_date": "2026-05-09",
        "customer_id": "CUS004",
        "cashier_id": "CAS004",
        "total_price": 37500,
        "payment_method": "Credit card"
    },
    {
        "transaction_id": "TRA005",
        "transaction_date": "2026-05-20",
        "customer_id": "CUS005",
        "cashier_id": "CAS005",
        "total_price": 30500,
        "payment_method": "QRIS"
    }
]

transaction_details_list = [
    {
        "detail_id": "DET001",
        "transaction_id": "TRA001",
        "product_id": "PRO001",
        "quantity": 2,
        "sub_total": 7000
    },
    {
        "detail_id": "DET002",
        "transaction_id": "TRA001",
        "product_id": "PRO002",
        "quantity": 1,
        "sub_total": 30000
    },
    {
        "detail_id": "DET003",
        "transaction_id": "TRA002",
        "product_id": "PRO004",
        "quantity": 1,
        "sub_total": 8000
    },
    {
        "detail_id": "DET004",
        "transaction_id": "TRA002",
        "product_id": "PRO005",
        "quantity": 1,
        "sub_total": 4000
    },
    {
        "detail_id": "DET005",
        "transaction_id": "TRA003",
        "product_id": "PRO002",
        "quantity": 1,
        "sub_total": 30000
    },
    {
        "detail_id": "DET006",
        "transaction_id": "TRA003",
        "product_id": "PRO003",
        "quantity": 1,
        "sub_total": 65000
    },
    {
        "detail_id": "DET007",
        "transaction_id": "TRA004",
        "product_id": "PRO001",
        "quantity": 5,
        "sub_total": 17500
    },
    {
        "detail_id": "DET008",
        "transaction_id": "TRA004",
        "product_id": "PRO005",
        "quantity": 5,
        "sub_total": 20000
    },
    {
        "detail_id": "DET009",
        "transaction_id": "TRA005",
        "product_id": "PRO001",
        "quantity": 3,
        "sub_total": 10500
    },
    {
        "detail_id": "DET010",
        "transaction_id": "TRA005",
        "product_id": "PRO005",
        "quantity": 5,
        "sub_total": 20000
    }
]

product_suppliers_list = [
    {
        "product_supplier_id": "PSU001",
        "supplier_id": "SUP001",
        "supplier_price": 3000,
        "supply_date": "2025-07-13",
        "stock_supplied": 50,
        "product_id": "PRO001"
    },
    {
        "product_supplier_id": "PSU002",
        "supplier_id": "SUP002",
        "supplier_price": 28000,
        "supply_date": "2025-08-28",
        "stock_supplied": 80,
        "product_id": "PRO002"
    },
    {
        "product_supplier_id": "PSU003",
        "supplier_id": "SUP003",
        "supplier_price": 60000,
        "supply_date": "2025-09-01",
        "stock_supplied": 60,
        "product_id": "PRO003"
    },
    {
        "product_supplier_id": "PSU004",
        "supplier_id": "SUP004",
        "supplier_price": 7000,
        "supply_date": "2025-11-19",
        "stock_supplied": 70,
        "product_id": "PRO004"
    },
    {
        "product_supplier_id": "PSU005",
        "supplier_id": "SUP005",
        "supplier_price": 3500,
        "supply_date": "2025-12-23",
        "stock_supplied": 200,
        "product_id": "PRO005"
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
              "6. View Transaction Details\n" \
              "7. Back to Sub Menu")

        submenu = input("Enter the submenu number you want to view: ")

        if submenu == "1":
            print("\n===== PRODUCT LIST =====")
            print("-" * 69)
            print(
                f"{"ID":<10}  "
                f"{"Product":<15}  "
                f"{"Category":<15}  "
                f"{"Price":<12}  "
                f"{"Stock":<10}"
            )
            print("-" * 69)
            for product in products_list:
                print(
                    f"{product["product_id"]:<10}  "
                    f"{product["product_name"]:<15}  "
                    f"{product["category"]:<15}  "
                    f"Rp{product["price"]:<10,}  "
                    f"{product["stock"]:<10}"
                )
            print("-" * 69)

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
            print("-" * 96)
            print(
                f"{"ID":<10}  "
                f"{"Date":<15}  "
                f"{"Customer ID":<15}  "
                f"{"Cashier ID":<15}  "
                f"{"Total price":<17}  "
                f"{"Payment Method":<15}"
            )
            print("-" * 96)
            for transaction in transactions_list:
                print(
                    f"{transaction["transaction_id"]:<10}  "
                    f"{transaction["transaction_date"]:<15}  "
                    f"{transaction["customer_id"]:<15}  "
                    f"{transaction["cashier_id"]:<15}  "
                    f"Rp{transaction["total_price"]:<15,}  "
                    f"{transaction["payment_method"]:<15}"
                )
            print("-" * 96)

            if not back_to_submenu():
                break

        elif submenu == "6":
            print("\n===== TRANSACTION DETAIL LIST =====")
            print("-" * 66)
            print(
                f"{"ID":<10}  "
                f"{"Transaction ID":<15}  "
                f"{"Product ID":<15}  "
                f"{"Quantity":<10}  "
                f"{"Subtotal":<12}"
            )
            print("-" * 66)
            for detail in transaction_details_list:
                print(
                    f"{detail["detail_id"]:<10}  "
                    f"{detail["transaction_id"]:<15}  "
                    f"{detail["product_id"]:<15}  "
                    f"{detail["quantity"]:<10}  "
                    f"Rp{detail["sub_total"]:<10,}"
                )
            print("-" * 66)

            if not back_to_submenu():
                break

        elif submenu == "7":
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
                    print("-" * 69)
                    print(
                        f"{"ID":<10}  "
                        f"{"Product":<15}  "
                        f"{"Category":<15}  "
                        f"{"Price":<12}  "
                        f"{"Stock":<10}"
                    )
                    print("-" * 69)
                    print(
                        f"{product["product_id"]:<10}  "
                        f"{product["product_name"]:<15}  "
                        f"{product["category"]:<15}  "
                        f"Rp{product["price"]:<10,}  "
                        f"{product["stock"]:<10}"
                    )
                    print("-" * 69)
                    
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
                    print("-" * 96)
                    print(
                        f"{"ID":<10}  "
                        f"{"Date":<15}  "
                        f"{"Customer ID":<15}  "
                        f"{"Cashier ID":<15}  "
                        f"{"Total price":<17}  "
                        f"{"Payment Method":<15}"
                    )
                    print("-" * 96)
                    print(
                        f"{transaction["transaction_id"]:<10}  "
                        f"{transaction["transaction_date"]:<15}  "
                        f"{transaction["customer_id"]:<15}  "
                        f"{transaction["cashier_id"]:<15}  "
                        f"Rp{transaction["total_price"]:<15,}  "
                        f"{transaction["payment_method"]:<15}"
                    )
                    print("-" * 96)

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
    
def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
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
            create()

        elif menu == "3":
            update()

        elif menu == "4":
            delete()

        elif menu == "5":
            print("You have exited the program!")
            break

        else:
            print("Menu you entered is not available!")

if __name__ == "__main__":
    main()