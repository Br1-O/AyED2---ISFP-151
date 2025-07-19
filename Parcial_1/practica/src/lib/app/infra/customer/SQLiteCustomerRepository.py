import sqlite3
from typing import List, Optional
from src.lib.app.domain.customer.entities.Customer import Customer
from src.lib.app.domain.customer.interfaces.ICustomerRepository import ICustomerRepository

class SQLiteCustomerRepository(ICustomerRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _initialize_db(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo_cliente INTEGER UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    direccion TEXT NOT NULL
                )
            ''')
            conn.commit()

    def create(self, customer: Customer) -> bool:
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO customers (codigo_cliente, nombre, apellido, direccion) VALUES (?, ?, ?, ?)",
                    (customer.code.value, customer.name.value, customer.lastname.value, customer.address.value)
                )
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete(self, customer_code: int) -> bool:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE codigo_cliente = ?", (customer_code,))
            conn.commit()
            return cursor.rowcount > 0

    def update(self, customer: Customer) -> bool:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE customers SET nombre = ?, apellido = ?, direccion = ? WHERE codigo_cliente = ?",
                (customer.name.value, customer.lastname.value, customer.address.value, customer.code.value)
            )
            conn.commit()
            return cursor.rowcount > 0

    def get_all(self) -> List[Customer]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_cliente, nombre, apellido, direccion FROM customers")
            rows = cursor.fetchall()
            return [Customer(code, name, lastname, address) for code, name, lastname, address in rows]

    def get_by_code(self, customer_code: int) -> Optional[Customer]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_cliente, nombre, apellido, direccion FROM customers WHERE codigo_cliente = ?", (customer_code,))
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            return None