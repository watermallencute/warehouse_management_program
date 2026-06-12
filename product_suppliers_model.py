class ProductSupplier:
    def __init__(
        self,
        product_supplier_id,
        supplier_id,
        supplier_price,
        supply_date,
        stock_supplied,
        product_id
    ):
        self.product_supplier_id = product_supplier_id
        self.supplier_id = supplier_id
        self.supplier_price = supplier_price
        self.supply_date = supply_date
        self.stock_supplied = stock_supplied
        self.product_id = product_id

    def __str__(self):
        return (
            f"{self.product_supplier_id} | "
            f"{self.supplier_id} | "
            f"{self.supplier_price} | "
            f"{self.supply_date} | "
            f"{self.stock_supplied} | "
            f"{self.product_id}"
        )