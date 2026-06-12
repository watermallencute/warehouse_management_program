import pandas as pd
import os

from config.database import connect_db

class TransactionService:

    def get_all_transactions(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            td.detail_id,
            t.transaction_id,
            t.transaction_date,
            cu.customer_name,
            ca.cashier_name,
            p.product_name,
            td.quantity,
            td.sub_total,
            t.total_price,
            t.payment_method
        FROM transactions t
        JOIN customers cu
            ON t.customer_id = cu.customer_id
        JOIN cashiers ca
            ON t.cashier_id = ca.cashier_id
        JOIN transaction_details td
            ON t.transaction_id = td.transaction_id
        JOIN products p
            ON td.product_id = p.product_id
        """

        cursor.execute(query)

        transactions = cursor.fetchall()

        cursor.close()
        conn.close()

        return transactions
    
    def add_transaction(
        self,
        transaction_id,
        transaction_date,
        customer_id,
        cashier_id,
        total_price,
        payment_method
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO transactions
        (
            transaction_id,
            transaction_date,
            customer_id,
            cashier_id,
            total_price,
            payment_method
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                transaction_id,
                transaction_date,
                customer_id,
                cashier_id,
                total_price,
                payment_method
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_transaction(self, transaction_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        query = f"""
        UPDATE transactions
        SET {column} = %s
        WHERE transaction_id = %s
        """

        cursor.execute(query, (value, transaction_id))
        conn.commit()

        cursor.close()
        conn.close()

    def update_total_price(
        self,
        transaction_id,
        total_price
    ):
        conn = connect_db()
        cursor = conn.cursor()

        query = """
        UPDATE transactions
        SET total_price = %s
        WHERE transaction_id = %s
        """

        cursor.execute(
            query,
            (
                total_price,
                transaction_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def delete_transaction(self, transaction_id):

        conn = connect_db()
        cursor = conn.cursor()

        query_detail = """
        DELETE FROM transaction_details
        WHERE transaction_id = %s
        """

        cursor.execute(query_detail, (transaction_id,))

        query_transaction = """
        DELETE FROM transactions
        WHERE transaction_id = %s
        """

        cursor.execute(query_transaction, (transaction_id,))

        conn.commit()

        cursor.close()
        conn.close()

    def export_transaction(self):

        conn = connect_db()

        query = """
        SELECT 
            t.transaction_id,
            t.transaction_date,
            cu.customer_name,
            ca.cashier_name,
            p.product_name,
            td.quantity,
            td.sub_total,
            t.total_price,
            t.payment_method
        FROM transactions t
        JOIN customers cu
            ON t.customer_id = cu.customer_id
        JOIN cashiers ca
            ON t.cashier_id = ca.cashier_id
        JOIN transaction_details td
            ON t.transaction_id = td.transaction_id
        JOIN products p
            ON td.product_id = p.product_id
        """

        df = pd.read_sql(query, conn)

        os.makedirs("exports", exist_ok=True)
        df.to_csv(
            "exports/transactions.csv",
            index=False
        )

        conn.close()

        print("Export success!")