import pandas as pd
import os

from config.database import connect_db

class ProductService:

    def get_all_products(self):

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            p.price,
            p.stock,
            s.supplier_name,
            ps.supplier_price,
            ps.supply_date,
            ps.stock_supplied
        FROM products p
        LEFT JOIN product_suppliers ps
            ON p.product_id = ps.product_id
        LEFT JOIN suppliers s
            ON ps.supplier_id = s.supplier_id
        """

        cursor.execute(query)

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products
    
    def add_product(
        self,
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
    ):

        conn = connect_db()

        cursor = conn.cursor()

        query = """
        INSERT INTO products
        (
            product_id,
            product_name,
            category,
            price,
            stock
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                product_id,
                product_name,
                category,
                price,
                stock
            )
        )

        cursor.execute(
            """
            INSERT INTO product_suppliers
            (
                product_supplier_id,
                supplier_id,
                supplier_price,
                supply_date,
                stock_supplied,
                product_id
            )
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                product_supplier_id,
                supplier_id,
                supplier_price,
                supply_date,
                stock_supplied,
                product_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def update_product(self, product_id, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        product_columns = [
            "product_name",
            "category",
            "price",
            "stock"
        ]

        supplier_columns = [
            "supplier_price",
            "supply_date",
            "stock_supplied",
            "supplier_id",
            "supplier_name"
        ]

        if column in product_columns:
            query = f"""
            UPDATE products
            SET {column} = %s
            WHERE product_id = %s
            """

        elif column in supplier_columns:
            query = f"""
            UPDATE product_suppliers
            SET {column} = %s
            WHERE product_id = %s
            """

        else:
            raise ValueError("Invalid column")

        cursor.execute(query, (value, product_id))

        conn.commit()

        cursor.close()
        conn.close()

    def delete_product(self, product_id):

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM product_suppliers
            WHERE product_id = %s
            """,
            (product_id,)
        )

        cursor.execute(
            """
            DELETE FROM products
            WHERE product_id = %s
            """,
            (product_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

    def export_product(self):

        conn = connect_db()

        query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            p.price,
            p.stock,
            s.supplier_name,
            ps.supplier_price,
            ps.supply_date,
            ps.stock_supplied
        FROM products p
        LEFT JOIN product_suppliers ps
            ON p.product_id = ps.product_id
        LEFT JOIN suppliers s
            ON ps.supplier_id = s.supplier_id
        """

        df = pd.read_sql(query, conn)

        os.makedirs("exports", exist_ok=True)
        df.to_csv(
            "exports/products.csv",
            index=False
        )

        conn.close()

        print("Export success!")