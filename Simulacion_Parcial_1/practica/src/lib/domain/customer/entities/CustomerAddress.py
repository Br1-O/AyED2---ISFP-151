class CustomerAddress:
    """
    Represents the name for the customers. It must not be empty and must be at least 5 chars long.
    """
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("La dirección debe ser una cadena de texto.")
        if len(value.strip()) < 5:
            raise ValueError("La dirección es demasiado corta.")
        self.value = value.strip()

    def __str__(self):
        return self.value