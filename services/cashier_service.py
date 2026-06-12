import pandas as pd
import os

from config.database import connect_db

class CashierService:

    def get_all_cashiers(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM cashiers
        """

        cursor.execute(query)

        cashiers = cursor.fetchall()

        cursor.close()
        conn.close()

        return cashiers
    
    def add_cashier(
        self,
        cashier_id,
        cashier_name,
        username,
        password,
        shift
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO cashiers
        (
            cashier_id,
            cashier_name,
            username,
            password,
            shift
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                cashier_id,
                cashier_name,
                username,
                password,
                shift
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_cashier(self, cashier_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        query = f"""
        UPDATE cashiers
        SET {column} = %s
        WHERE cashier_id = %s
        """

        cursor.execute(query, (value, cashier_id))
        conn.commit()

        cursor.close()
        conn.close()

    def delete_cashier(
        self,
        cashier_id
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        DELETE FROM cashiers
        WHERE cashier_id = %s
        """

        cursor.execute(
            query,
            (cashier_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

    def export_cashier(self):

        conn = connect_db()

        query = """
        SELECT *
        FROM cashiers
        """

        df = pd.read_sql(query, conn)

        os.makedirs("exports", exist_ok=True)
        df.to_csv(
            "exports/cashiers.csv",
            index=False
        )

        conn.close()

        print("Export success!")