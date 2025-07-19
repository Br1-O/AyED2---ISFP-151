from abc import ABC, abstractmethod
from typing import List, Optional
from src.lib.domain.customer.entities.Customer import Customer

class ICustomerService(ABC):
    """
    Interface for customer application use cases.
    """

    @abstractmethod
    def create_customer(self, customer: Customer) -> bool:
        pass

    @abstractmethod
    def delete_customer(self, customer_code: int) -> bool:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer) -> bool:
        pass

    @abstractmethod
    def get_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def get_customer_by_code(self, customer_code: int) -> Optional[Customer]:
        pass