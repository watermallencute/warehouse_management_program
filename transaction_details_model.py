class TransactionDetail:
    def __init__(
        self,
        detail_id,
        transaction_id,
        product_id,
        quantity,
        sub_total
    ):
        self.detail_id = detail_id
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.sub_total = sub_total

    def __str__(self):
        return (
            f"{self.detail_id} | "
            f"{self.transaction_id} | "
            f"{self.product_id} | "
            f"{self.quantity} | "
            f"{self.sub_total}"
        )