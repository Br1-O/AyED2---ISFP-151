import tkinter as tk
from tkinter import messagebox, ttk
from src.lib.domain.customer.interfaces.ICustomerService import ICustomerService
from src.lib.domain.customer.entities.Customer import Customer
from src.lib.utils.logs import log_info, log_error, log_warn

def start_app(service: ICustomerService):
    root = tk.Tk()
    root.title("Gestión de Clientes - SandTech")
    root.geometry("650x520")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # ----- TAB: Listar -----
    frame_list = ttk.Frame(notebook)
    notebook.add(frame_list, text="Listar Todos")

    tree = ttk.Treeview(frame_list, columns=("Código", "Nombre", "Apellido", "Dirección"), show="headings")
    for col in ("Código", "Nombre", "Apellido", "Dirección"):
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    tree.pack(fill="both", expand=True)

    def refresh_list():
        try:
            tree.delete(*tree.get_children())
            customers = service.get_all_customers()
            for c in customers:
                tree.insert("", tk.END, values=(c.code.value, c.name.value, c.lastname.value, c.address.value))
            log_info("Lista de clientes actualizada.")
        except Exception as e:
            log_error(f"Error listando: {e}")
            messagebox.showerror("Error", str(e))

    # ----- TAB: Crear -----
    frame_create = ttk.Frame(notebook)
    notebook.add(frame_create, text="Crear")

    ttk.Label(frame_create, text="Código (comienza con 100):").pack()
    entry_code_create = ttk.Entry(frame_create)
    entry_code_create.pack()

    ttk.Label(frame_create, text="Nombre:").pack()
    entry_name_create = ttk.Entry(frame_create)
    entry_name_create.pack()

    ttk.Label(frame_create, text="Apellido:").pack()
    entry_lastname_create = ttk.Entry(frame_create)
    entry_lastname_create.pack()

    ttk.Label(frame_create, text="Dirección:").pack()
    entry_address_create = ttk.Entry(frame_create)
    entry_address_create.pack()

    def create_customer():
        try:
            code_str = entry_code_create.get().strip()
            if not code_str.isdigit() or not code_str.startswith("100"):
                raise ValueError("El código debe ser numérico y comenzar con 100")
            code = int(code_str)
            name = entry_name_create.get().strip()
            lastname = entry_lastname_create.get().strip()
            address = entry_address_create.get().strip()
            if not all([name, lastname, address]):
                raise ValueError("Todos los campos deben estar completos.")
            customer = Customer(code, name, lastname, address)
            if service.create_customer(customer):
                log_info(f"Customer creado: {customer}")
                messagebox.showinfo("Éxito", "Cliente creado correctamente.")
                refresh_list()
                entry_code_create.delete(0, tk.END)
                entry_name_create.delete(0, tk.END)
                entry_lastname_create.delete(0, tk.END)
                entry_address_create.delete(0, tk.END)
            else:
                log_warn(f"Duplicado: {code}")
                messagebox.showwarning("Error", "Ya existe un cliente con ese código.")
        except Exception as e:
            log_error(f"Error al crear: {e}")
            messagebox.showerror("Error", str(e))

    ttk.Button(frame_create, text="Crear Cliente", command=create_customer).pack(pady=10)

    # ----- TAB: Buscar -----
    frame_search = ttk.Frame(notebook)
    notebook.add(frame_search, text="Buscar")

    ttk.Label(frame_search, text="Código de Cliente:").pack()
    entry_code_search = ttk.Entry(frame_search)
    entry_code_search.pack()

    result_frame = ttk.LabelFrame(frame_search, text="Resultado")
    result_frame.pack(fill="x", padx=10, pady=10)
    result_label = ttk.Label(result_frame, text="", anchor="center", justify="center")
    result_label.pack(fill="x", pady=10)

    def search_customer():
        try:
            code_str = entry_code_search.get().strip()
            if not code_str.isdigit():
                raise ValueError("Código inválido.")
            code = int(code_str)
            customer = service.get_customer_by_code(code)
            if customer:
                result_label.config(text=f"{customer.code.value} - {customer.name.value} {customer.lastname.value}\nDirección: {customer.address.value}")
                log_info(f"Cliente encontrado: {customer}")
            else:
                result_label.config(text="Cliente no encontrado.")
                log_warn(f"No se encontró el cliente: {code}")
        except Exception as e:
            log_error(f"Error búsqueda: {e}")
            messagebox.showerror("Error", str(e))

    ttk.Button(frame_search, text="Buscar", command=search_customer).pack(pady=10)

    # ----- TAB: Modificar -----
    frame_update = ttk.Frame(notebook)
    notebook.add(frame_update, text="Modificar")

    ttk.Label(frame_update, text="Código (existente):").pack()
    entry_code_update = ttk.Entry(frame_update)
    entry_code_update.pack()

    ttk.Label(frame_update, text="Nuevo Nombre:").pack()
    entry_name_update = ttk.Entry(frame_update)
    entry_name_update.pack()

    ttk.Label(frame_update, text="Nuevo Apellido:").pack()
    entry_lastname_update = ttk.Entry(frame_update)
    entry_lastname_update.pack()

    ttk.Label(frame_update, text="Nueva Dirección:").pack()
    entry_address_update = ttk.Entry(frame_update)
    entry_address_update.pack()

    def update_customer():
        try:
            code = int(entry_code_update.get().strip())
            name = entry_name_update.get().strip()
            lastname = entry_lastname_update.get().strip()
            address = entry_address_update.get().strip()
            if not all([name, lastname, address]):
                raise ValueError("Todos los campos deben estar completos.")
            customer = Customer(code, name, lastname, address)
            if service.update_customer(customer):
                log_info(f"Cliente modificado: {customer}")
                messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
                refresh_list()
            else:
                log_warn(f"Falló la modificación de {code}")
                messagebox.showwarning("Error", "No se pudo modificar el cliente.")
        except Exception as e:
            log_error(f"Error modificación: {e}")
            messagebox.showerror("Error", str(e))

    ttk.Button(frame_update, text="Modificar", command=update_customer).pack(pady=10)

    # ----- TAB: Eliminar -----
    frame_delete = ttk.Frame(notebook)
    notebook.add(frame_delete, text="Eliminar")

    ttk.Label(frame_delete, text="Código de Cliente:").pack()
    entry_code_delete = ttk.Entry(frame_delete)
    entry_code_delete.pack()

    def delete_customer():
        try:
            code = int(entry_code_delete.get())
            if service.delete_customer(code):
                log_info(f"Cliente eliminado: {code}")
                messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                refresh_list()
            else:
                log_warn(f"No se encontró el cliente: {code}")
                messagebox.showwarning("No encontrado", "Cliente no encontrado.")
        except Exception as e:
            log_error(f"Error eliminación: {e}")
            messagebox.showerror("Error", str(e))

    ttk.Button(frame_delete, text="Eliminar", command=delete_customer).pack(pady=10)

    refresh_list()
    root.mainloop()