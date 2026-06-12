class Customer:
    def __init__(
        self,
        customer_id,
        customer_name,
        gender,
        phone_number,
        address
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.gender = gender
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return (
            f"{self.customer_id} | "
            f"{self.customer_name} | "
            f"{self.gender} | "
            f"{self.phone_number} | "
            f"{self.address}"
        )