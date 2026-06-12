class Supplier:
    def __init__(
        self,
        supplier_id,
        supplier_name,
        contact_number,
        address,
        email
    ):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_number = contact_number
        self.address = address
        self.email = email

    def __str__(self):
        return (
            f"{self.supplier_id} | "
            f"{self.supplier_name} | "
            f"{self.contact_number} | "
            f"{self.address} | "
            f"{self.email}"
        )