class CustomerCode:
    """
    Represents the code for the customers. It must be an integer that starts with '100'.
    """
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("El código de cliente debe ser un número entero.")
        
        if not str(value).startswith("100"):
            raise ValueError("El código de cliente debe comenzar con '100'.")
        
        self.value = value

    def __str__(self):
        return str(self.value)
