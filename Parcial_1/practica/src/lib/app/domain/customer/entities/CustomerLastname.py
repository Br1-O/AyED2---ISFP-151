class CustomerLastname:
    """
    Represents the name for the customers. It allows only letters and must be at least 2 chars long.
    """
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("El apellido debe ser una cadena de texto.")
        if not value.strip().isalpha():
            raise ValueError("El apellido solo puede contener letras.")
        if len(value.strip()) < 2:
            raise ValueError("El apellido es demasiado corto.")
        self.value = value.strip().capitalize()

    def __str__(self):
        return self.value