from abc import ABC, abstractmethod
from typing import List, Optional
from src.lib.domain.customer.entities.Customer import Customer

class ICustomerRepository(ABC):
    """
    Interface for customer repository.
    """

    @abstractmethod
    def create(self, customer: Customer) -> bool:
        pass

    @abstractmethod
    def delete(self, customer_code: int) -> bool:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def get_by_code(self, customer_code: int) -> Optional[Customer]:
        pass
