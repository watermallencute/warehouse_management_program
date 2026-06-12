class Transaction:
    def __init__(
        self,
        transaction_id,
        transaction_date,
        customer_id,
        cashier_id,
        total_price,
        payment_method
    ):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.customer_id = customer_id
        self.cashier_id = cashier_id
        self.total_price = total_price
        self.payment_method = payment_method

    def __str__(self):
        return (
            f"{self.transaction_id} | "
            f"{self.transaction_date} | "
            f"{self.customer_id} | "
            f"{self.cashier_id} | "
            f"{self.total_price} | "
            f"{self.payment_method}" 
        )