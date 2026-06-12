import pandas as pd
import os

from config.database import connect_db

class CustomerService:

    def get_all_customers(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM customers
        """

        cursor.execute(query)

        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return customers
    
    def add_customer(
        self,
        customer_id,
        customer_name,
        gender,
        phone_number,
        address
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO customers
        (
            customer_id,
            customer_name,
            gender,
            phone_number,
            address
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                customer_id,
                customer_name,
                gender,
                phone_number,
                address
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_customer(self, customer_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        query = f"""
        UPDATE customers
        SET {column} = %s
        WHERE customer_id = %s
        """

        cursor.execute(query, (value, customer_id))
        conn.commit()

        cursor.close()
        conn.close()

    def delete_customer(
        self,
        customer_id
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        DELETE FROM customers
        WHERE customer_id = %s
        """

        cursor.execute(
            query,
            (customer_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

    def export_customer(self):

        conn = connect_db()

        query = """
        SELECT *
        FROM customers
        """

        df = pd.read_sql(query, conn)

        os.makedirs("exports", exist_ok=True)
        df.to_csv(
            "exports/customers.csv",
            index=False
        )

        conn.close()

        print("Export success!")