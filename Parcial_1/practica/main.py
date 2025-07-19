from src.lib.app.infra.customer.SQLiteCustomerRepository import SQLiteCustomerRepository
from src.lib.app.aplication.customer.CustomerService import CustomerService
from src.lib.ui.customer.customer_view import run

# db path for SQLite
DB_PATH = "customers.db"

def main():
    repo = SQLiteCustomerRepository(DB_PATH)
    service = CustomerService(repo)

    # Launches the GUI for the customer module and injects the service, with the repo already injected
    run(service)

if __name__ == "__main__":
    main()