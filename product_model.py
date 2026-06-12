class Product:
    def __init__(
        self,
        product_id,
        product_name,
        category,
        price,
        stock
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return (
            f"{self.product_id} | "
            f"{self.product_name} | "
            f"{self.category} | "
            f"{self.price} | "
            f"{self.stock}"
        )