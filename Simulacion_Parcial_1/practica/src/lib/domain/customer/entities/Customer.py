from src.lib.domain.customer.entities.CustomerCode import CustomerCode
from src.lib.domain.customer.entities.CustomerName import CustomerName
from src.lib.domain.customer.entities.CustomerLastname import CustomerLastname
from src.lib.domain.customer.entities.CustomerAddress import CustomerAddress

class Customer:
    """
    Entity class for customer. It contains value objects for code, name, lastname and address.
    """
    def __init__(self, code, name, lastname, address):
        self.code = CustomerCode(code)
        self.name = CustomerName(name)
        self.lastname = CustomerLastname(lastname)
        self.address = CustomerAddress(address)

    def __str__(self):
        return f"{self.code.value} - {self.name.value} {self.lastname.value} - Dirección: {self.address.value}"

    def to_dict(self):
        """
        Converts the Customer object to a dict. Mainly for SQLite.
        """
        return {
            "codigo_cliente": self.code.value,
            "nombre": self.name.value,
            "apellido": self.lastname.value,
            "direccion": self.address.value
        }