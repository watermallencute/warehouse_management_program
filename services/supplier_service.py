import pandas as pd
import os

from config.database import connect_db

class SupplierService:

    def get_all_suppliers(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM suppliers
        """

        cursor.execute(query)

        suppliers = cursor.fetchall()

        cursor.close()
        conn.close()

        return suppliers
    
    def add_supplier(
        self,
        supplier_id,
        supplier_name,
        contact_number,
        address,
        email
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO suppliers
        (
            supplier_id,
            supplier_name,
            contact_number,
            address,
            email
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                supplier_id,
                supplier_name,
                contact_number,
                address,
                email
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_supplier(self, supplier_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        query = f"""
        UPDATE suppliers
        SET {column} = %s
        WHERE supplier_id = %s
        """

        cursor.execute(query, (value, supplier_id))
        conn.commit()

        cursor.close()
        conn.close()

    def delete_supplier(
        self,
        supplier_id
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        DELETE FROM suppliers
        WHERE supplier_id = %s
        """

        cursor.execute(
            query,
            (supplier_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

    def export_supplier(self):

        conn = connect_db()

        query = """
        SELECT *
        FROM suppliers
        """

        df = pd.read_sql(query, conn)

        os.makedirs("exports", exist_ok=True)
        df.to_csv(
            "exports/suppliers.csv",
            index=False
        )

        conn.close()

        print("Export success!")