class Cashier:
    def __init__(
        self,
        cashier_id,
        cashier_name,
        username,
        password,
        shift
    ):
        self.cashier_id = cashier_id
        self.cashier_name = cashier_name
        self.username = username
        self.password = password
        self.shift = shift

    def __str__(self):
        return (
            f"{self.cashier_id} | "
            f"{self.cashier_name} | "
            f"{self.username} | "
            f"{self.password} | "
            f"{self.shift}"
        )