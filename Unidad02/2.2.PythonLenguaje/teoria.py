import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.2

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.1 ¿Que la Consola Interactiva?, que permite y facilita. ")
        print("\n")
        print("""
La consola interactiva es una herramienta que nos permite escribir sentencias de código de Python 
al mismo tiempo que se ejecutan. Es ideal para probar pequeñas porciones de código que no nos interesa guardar,
pues una vez cerrada todo lo escrito en ella es borrado de la memoria.
              """)
    
    def exercise_2(self):
        print("1.2 Que es un Repositorio de Paquetes, que repositorios existen.")
        print("\n")
        print("""
Un repositorio de paquetes es un sistema que almacena archivos de código y nos permite instalarlos en nuestro proyecto,
así fácilitando que desarrollemos diversas tareas sin necesidad de tener que nosotros escribir o descargar de forma externa esos archivos.
El PyPI, Python Package Index, es el más grande y utilizado en Python, cualquier persona puede registrarse 
y subir paquetes para que sean descargados mediante gestores de paquetes. Algunos repositorios muy usados son: Pandas, Numpy, Tensorflow, Flask, Django, etc.
              """)

    def exercise_3(self):
        print("1.3 Que es un Paquete en Python, como se descarga un Paquete y como se Gestiona.")
        print("\n")
        print("""
Un paquete en Python no es más que un conjunto de modulos, archivos, que normalmente son descargados mediante un gestor de paquetes, como pip, normalmente.
Se gestionan mediante los gestores de paquetes, que son una interfaz de consola que permite la administración facilitada de dependencias dentro de nuestra aplicación,
es decir, del conjunto de librerias y frameworks de terceros, que usamos para facilitar diferentes tareas dentro de nuestro código.
Como el conjunto de dependencias, y las dependencias de dichas dependencias, puede expandirse muy rápidamente en un proyecto a medida que va escalando,
este tipo de gestores fácilitan la tarea de administrar qué paquetes usa nuestro proyecto.
Generalmente la forma más simple de descargar un paquete será ir a la consola y escribir:
pip install [nombre del paquete que se desea instalar]
Si poseemos pip y está habilitado en nuestras variables de entorno del sistema, procederá a instalar dicho paquete en el directorio de nuestro proyecto.
              """)

    def exercise_4(self):
        print("1.4 ¿Qué es un Entorno Virtual?, para que Sirve, ¿como se gestiona? Dar Ejemplos.")
        print("\n")
        print("""
Es un espacio donde podemos instalar paquetes para nuestros proyectos, de forma que dichos paquetes estén aislados del resto de nuestros proyectos en Python.
Así, sirve para separar dependencias de un proyecto u otro, 
fácilitando que no se creen conflictos no deseados entre versiones o existencia de paquetes determinados
de un proyecto nuevo a otro existente.
Se gestiona, normalmente, usando el módulo venv, que viene con Python 3.3 en adelante por defecto.
Por ej:
    - Crearemos el entorno virtual mediante el comando:
        C:/>python -m venv c:/ruta/al/entorno/virtual
    - Activaremos el entorno virtual mediante el comando:
        C:/>c:/ruta/al/entorno/virtual/scripts/activate.bat
    Sea cual sea nuestro sistema operativo sabremos que el entorno virtual se ha activado porque su nombre aparece entre paréntesis delante del promt.
    
    - Desactivaremos el entorno virtual mediante el comando:
        $ deactivate
    - Eliminaremos el entorno virtual mediante el comando:
        C:/>rmdir c:/ruta/al/entorno/virtual /s
              
    (Todo esto dado por sentado que se trabaja en Windows, en este ejemplo.)
              """)
    
    def exercise_5(self):
        print("2.1 Cuál es el concepto de Variables que maneja Python a diferencia de otros lenguajes.")
        print("\n")
        print("""
A diferencia de otros lenguajes Python maneja el concepto de referencias, nombres o identificadores en cuanto variables,
así una variable no es una caja que contiene al dato, sino más bien un objeto que apunta, o hace referencia, a ese valor en memoria.
Así, variables que apunten al mismo valor no lo duplican, sino que sólo son diferentes referencias a él.
              """)

    def exercise_6(self):
        print("2.3 Describir Operaciones aritméticas y orden de precedencia.")
        print("\n")
        print("""
Python, al igual que la gran mayoria de lenguajes de programación, permite realizar operaciones aritméticas básicas como:

- Suma:           +
- Resta:          -
- Multiplicación: *
- División:       /
- División integral: //
- Módulo (resto): %
- Potenciación:   **

El orden de precedencia determina el orden en que se ejecutan estas operaciones en una expresión.

Orden (de mayor a menor prioridad):
1. Paréntesis        ( )
2. Potenciación      **
3. Signos + y - unarios (-5, +8)
4. Multiplicación, División, División integral, Módulo (*, /, //, %)
5. Suma y Resta (+, -)

Python evalúa de izquierda a derecha, salvo en el caso de la **potenciación**, que se evalúa de derecha a izquierda.
              """)

    def exercise_7(self):
        print("2.4 Dar ejemplos del Comando IF.")
        print("\n")
        print("""
En comando if es una estructura de control de flujo condicional, un ejemplo de ella en Python es:
              
edad = input("Ingrese su edad, por favor.")
if edad >= 18: 
    print("¡Puedes pasar!") 
else:
    print("¡Vuelve en unos años!") 
              
- Otro ejemplo puede involucrar elif:

grados = int(input("¿Cuántos grados hacen en su ciudad ahora mismo?"))
if grados <=10:
    print("Ta helao!")
elif 10 < grados <= 18:
    print("Bueno, no está mal.")
else:
    print("¡Qué calorsito, eh!")
              """)

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