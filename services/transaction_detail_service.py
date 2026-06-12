import pandas as pd

from config.database import connect_db

class TransactionDetailService:

    def get_all_transaction_details(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM transaction_details
        """

        cursor.execute(query)

        transaction_details = cursor.fetchall()

        cursor.close()
        conn.close()

        return transaction_details
    
    def add_transaction_detail(
        self,
        detail_id,
        transaction_id,
        product_id,
        quantity,
        sub_total
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO transaction_details
        (
            detail_id,
            transaction_id,
            product_id,
            quantity,
            sub_total
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                detail_id,
                transaction_id,
                product_id,
                quantity,
                sub_total
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_transaction_detail(self, detail_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        query = f"""
        UPDATE transaction_details
        SET {column} = %s
        WHERE detail_id = %s
        """

        cursor.execute(query, (value, detail_id))
        conn.commit()

        cursor.close()
        conn.close()

    def delete_transaction_detail(
        self,
        detail_id
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        DELETE FROM transaction_details
        WHERE detail_id = %s
        """

        cursor.execute(
            query,
            (detail_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()