class CustomerCode:
    """
    Represents the code for the customers. It must be an integer >= 100.
    """
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("El código de cliente debe ser un número entero.")
        if value < 100:
            raise ValueError("El código de cliente debe comenzar desde 100.")
        self.value = value

    def __str__(self):
        return str(self.value)