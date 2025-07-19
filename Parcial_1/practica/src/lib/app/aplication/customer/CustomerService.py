from typing import List, Optional
from src.lib.app.domain.customer.entities.Customer import Customer
from src.lib.app.domain.customer.interfaces.ICustomerService import ICustomerService
from src.lib.app.domain.customer.interfaces.ICustomerRepository import ICustomerRepository

class CustomerService(ICustomerService):
    def __init__(self, repository: ICustomerRepository):
        self.repository = repository

    def create_customer(self, customer: Customer) -> bool:
        return self.repository.create(customer)

    def delete_customer(self, customer_code: int) -> bool:
        return self.repository.delete(customer_code)

    def update_customer(self, customer: Customer) -> bool:
        return self.repository.update(customer)

    def get_all_customers(self) -> List[Customer]:
        return self.repository.get_all()

    def get_customer_by_code(self, customer_code: int) -> Optional[Customer]:
        return self.repository.get_by_code(customer_code)