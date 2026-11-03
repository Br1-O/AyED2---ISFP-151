import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.1 ¿Cómo se define una clase en Python?.")
        print("\n")
        print("""
En Python, una clase se define utilizando la palabra clave class, seguida del nombre de la clase y dos puntos.
Dentro del bloque indentado se definen los atributos y métodos. 
Por ejemplo:
    class Perro:
        pass
Es el esquema básico para comenzar a utilizar la Programación Orientada a Objetos (POO), 
permitiendo usar las propiedades de las clases dentro de este paradigma: abstracción, encapsulación, herencia y polimorfismo.
              """)
    
    def exercise_2(self):
        print("1.2 Que es un atributo de Clase y uno de Instancia, cuales son las diferencias.")
        print("\n")
        print("""
Un atributo de clase es compartido por todas las instancias de la clase y se define fuera de cualquier método, 
directamente dentro del bloque de la clase. Un atributo de instancia se define dentro del método __init__ utilizando self, 
y es exclusivo de cada objeto. 
Por ejemplo, 
    especie = 'mamífero' es un atributo de clase
    self.nombre = nombre es de instancia. 
Esta distinción permite manejar información común y específica de cada objeto.
              """)

    def exercise_3(self):
        print("1.3 ¿Como se define un constructor en Python?")
        print("\n")
        print("""
El constructor se define mediante el método especial __init__. Es llamado automáticamente al crear una instancia de la clase. 
Recibe como primer parámetro self, que representa la instancia, seguido de los parámetros necesarios. 
Se utiliza para inicializar atributos del objeto, como self.nombre = nombre. 
Por ej:
    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart
              """)

    def exercise_4(self):
        print("1.4 ¿Que es un Decorador en Python?")
        print("\n")
        print("""
Un decorador es una función especial que se aplica sobre otra función o método para modificar su comportamiento sin cambiar su código. 
Se indica con @nombre_decorador justo encima de la definición. 
Por ejemplo: 
    @staticmethod, @classmethod, o @property. 
Son muy usados en POO para controlar el acceso a los métodos o para definir diferentes tipos de métodos dentro de una clase.
              """)

    def exercise_5(self):
        print("1.5 Que es un Método de Instancia, clase y Estático. ")
        print("\n")
        print("""
■ Un método de instancia recibe como primer parámetro self, accede y modifica atributos del objeto. 
■ Un método de clase se define con @classmethod y recibe cls como primer parámetro, permitiendo modificar atributos de clase. 
■ Un método estático se define con @staticmethod y no recibe ningún parámetro especial y no accede ni a atributos ni a otros métodos de la clase. 
Se usa cuando una función está relacionada lógicamente con la clase, pero no depende de ella.
              """)

    def exercise_6(self):
        print("1.6 Dar ejemplos de atributos y métodos en Python")
        print("\n")
        print("""
Un ejemplo que muestre todos los atributos y métodos vistos hasta ahora en Python sería:
    class Bicicleta:
        cantidad = 0
                
        def __init__(self, color, rodado):
            self.color = color
            self.rodado = rodado
            Bicicleta.cantidad += 1
                
        def andar(self):
            print(f'la bici {self.color} con rodado {self.rodado} está andando.')
                
        @classmethod
        def contar_instancias(cls):
            return cls.cantidad
        
        @staticmethod
        def andan_en_bici():
            print("hay por lo menos alguien andando en bici)
              """)
        
    def exercise_7(self):
        print("1.7 Crear una Clase en Python")
        print("\n")
        print("""
class Perro:
    pass
                """)
        class Perro:
            pass
            
    def exercise_8(self):
        print("1.8 Asignarles atributos de clase e instancia ")
        print("\n")
        print("""
class Perro:
    patas = 4 #atributo de clase
    ruido = 'ladrido' #atributo de clase
    
    def __init__(self, nombre, raza):
        self.nombre = nombre #atributo de instancia
        self.raza = raza #atributo de instancia
                """)
        class Perro:
            patas = 4 #atributo de clase
            ruido = 'ladrido' #atributo de clase
            
            def __init__(self, nombre, raza):
                self.nombre = nombre #atributo de instancia
                self.raza = raza #atributo de instancia

    def exercise_9(self):
        print("1.9 Asignar métodos de Instancia, Clase y estáticos")
        print("\n")
        print("\n")
        print("""
class Perro:
    patas = 4 #atributo de clase
    ruido = 'ladrido' #atributo de clase
    
    def __init__(self, nombre, raza):
        self.nombre = nombre #atributo de instancia
        self.raza = raza #atributo de instancia

    #método de instancia
    def mostrar_nombre(self):
        print("El nombre de este perro es: ", self.nombre)

    #método de clase
    @classmethod
    def ladrar(cls):
        print((cls.ruido+" ")*5)
    
    #método estático
    @staticmethod
    def morder():
        print("El perro está mordiendote.")
                """)
        class Perro:
            patas = 4 #atributo de clase
            ruido = 'ladrido' #atributo de clase
            
            def __init__(self, nombre, raza):
                self.nombre = nombre #atributo de instancia
                self.raza = raza #atributo de instancia

            #método de instancia
            def mostrar_nombre(self):
                print("El nombre de este perro es: ", self.nombre)

            #método de clase
            @classmethod
            def ladrar(cls):
                print((cls.ruido+" ")*5)
            
            #método estático
            @staticmethod
            def morder():
                print("El perro está mordiendote.")


    def exercise_10(self):
        print("1.10  Realizar una calculadora que consuma estos métodos")
        print("\n")

        class Calculadora:
            tipo_calculadora = "cientifica"

            def __init__(self, marca = "Phillips"):
                self.marca = marca

            @staticmethod
            def sumar(a, b):
                return a + b
            
            @staticmethod
            def restar(a, b):
                return a - b
            
            @staticmethod
            def multiplicar(a, b):
                return a * b
            
            @staticmethod
            def dividir(a, b):
                if b != 0:
                    return a / b
                else:
                    return "No se puede dividir por cero"
                    
            def mostrar_marca(self):
                print("La marca de la calculadora es:", self.marca)
            
            @classmethod
            def mostrar_tipo(cls):
                print("Se usó una calculadora de tipo:",cls.tipo_calculadora,"para hacer estos cálculos.")
            
        print("Calculadora simple \n")
    
        calculadora = Calculadora("Hitachi")
        a = float(input("Ingresá el primer número: "))
        b = float(input("Ingresá el segundo número: "))
        
        print("Suma:", Calculadora.sumar(a, b))
        print("Resta:", Calculadora.restar(a, b))
        print("Multiplicación:", Calculadora.multiplicar(a, b))
        print("División:", Calculadora.dividir(a, b))
        calculadora.mostrar_marca()
        calculadora.mostrar_tipo()
        
            
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■■■■■■■■■■ De acá para abajo sólo es la definición de clases y funciones para el manejo del menú ■■■■■■■■■■

class Assignment():

    """
    Class that abstracts and represents the assignment and stores the list of exercises
    """

    assignmentNumber:int = assignmentNumber
    
    def __init__(self):
        self.exercise_instance = Exercises()
        self.exercises = []

        # Checking the name of the methods inside Exercise class, so methods that start with "exercise_" are added to the list of exercises
        exercise_methods = [
            (int(name.split("_")[1]), getattr(self.exercise_instance, name))
            for name in dir(self.exercise_instance)
            if callable(getattr(self.exercise_instance, name)) and name.startswith("exercise_")
        ]
        #sort them
        exercise_methods.sort(key=lambda x: x[0])

        self.exercises = [method for _, method in exercise_methods]

        self.totalExercises:int = len(self.exercises)

#Entries Validation w/ error messages:

def isNum(num):
    """
    Function for validation of numbers
    """
    while(num.isdigit()==False):
        print("No es un dato valido.\n")
        num=input("Ingrese un numero natural entero:")
    return int(num)

def isString(str):
    """
    Function for validation of strings
    """
    while(str.isalpha()==False):
        print("No es un dato valido.\n")
        str=input("Ingreselo nuevamente:")
    str=str.lower()
    return str

#Console clearing

def clear_console():
    """
    Function for console clearing
    """
    os.system('cls' if os.name == 'nt' else 'clear')

#Menú showcase:

def menu():
    """
    Function to display the menu with the assignment data based on the user's input
    """

    assignment_instance = Assignment()
    assignmentNumber = assignment_instance.assignmentNumber
    totalExercises = assignment_instance.totalExercises
    exercises = assignment_instance.exercises

    option=""
    global y
    y=True

    chars_per_line = 70
    
    while y:

        option=input("\n" +
                     "═"*chars_per_line + 
                     "\n" + 
                     f"Elija el número de ejercicio a revisar (del 1 al {totalExercises})".center(chars_per_line) + 
                     "\n" + 
                     "O ingrese cualquier otro numero para salir: ".center(chars_per_line) + 
                     "\n" + 
                     "═"*chars_per_line + 
                     "\n")
        option=isNum(option)
        
        if 1 <= option <= totalExercises:
            clear_console()
            print("\n" + f"( {option} )".center(chars_per_line, "═") + "\n")
            exercises[option - 1]()
        else:
            break

    print(f"""
    ################   Guía Nro {assignmentNumber} finalizada.   ####################
    """)
    y=False

#Definición Main:

def main():

    menu()

main()