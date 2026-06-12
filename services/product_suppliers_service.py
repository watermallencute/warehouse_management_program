import pandas as pd

from config.database import connect_db

class ProductSupplierService:

    def get_all_product_suppliers(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM product_suppliers
        """

        cursor.execute(query)

        product_suppliers = cursor.fetchall()

        cursor.close()
        conn.close()

        return product_suppliers