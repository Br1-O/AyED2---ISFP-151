import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.3

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  ¿Qué entiende por arquitectura Limpia?, dar ejemplos.")
        print("\n")
        print("""
La arquitectura limpia es una forma de estructurar un sistema de software de manera que esté bien organizado, sea fácil de mantener y escalar, 
y permita desacoplar las distintas partes de la aplicación. Se basa en separar responsabilidades por capas, como:

Entidades: representan las reglas de negocio más internas (modelo de dominio).
Casos de uso: orquestan las reglas específicas de la aplicación.
Interfaces (adaptadores): manejan la interacción con usuarios u otros sistemas (como una API).
Infraestructura: acceso a bases de datos, red, archivos, etc.

Un ejemplo común es una aplicación que administra usuarios:

La entidad sería Usuario.
El caso de uso sería CrearUsuario.
Un adaptador web podría ser un controlador REST.
La infraestructura podría usar SQLite para persistencia.

Este enfoque mejora la reusabilidad, testeo independiente y facilita el cambio tecnológico sin afectar la lógica central.
              """)
    
    def exercise_2(self):
        print("2.  Que Diferencia existe ente los paradigmas imperativos y los declarativos. ")
        print("\n")
        print("""
La diferencia principal está en cómo se expresa la lógica de un programa:

Paradigma imperativo: se enfoca en cómo se debe realizar una tarea, detallando cada paso (secuencias, condiciones, bucles). 
Lenguajes como C, C++ o Python (cuando se usa de forma procedural) siguen este paradigma. 
Usa variables, estructuras de control, y mutabilidad.

Paradigma declarativo: se enfoca en qué se quiere lograr, sin especificar cómo lograrlo. 
El control del flujo lo maneja el lenguaje o motor de ejecución. 
Ejemplos incluyen SQL, HTML, y partes funcionales de Python (map(), filter(), expresiones lambda). 
Se basa más en la expresión que en la instrucción.
              """)

    def exercise_3(self):
        print("3.  ¿Dar 5 diferencias entre paradigma estructurado y objetos?")
        print("\n")
        print("""
| Característica          | Paradigma Estructurado                        | Paradigma Orientado a Objetos           |
| ----------------------- | --------------------------------------------- | --------------------------------------- |
| Organización del código | Basado en funciones y procedimientos          | Basado en clases y objetos              |
| Manejo de datos         | Datos separados de las funciones              | Datos y funciones unidos en objetos     |
| Reutilización           | Limitada, requiere copiar o reescribir código | Alta, mediante herencia y composición   |
| Encapsulamiento         | No existe encapsulamiento                     | Sí, oculta detalles internos del objeto |
| Ejemplos de lenguajes   | C, Pascal                                     | C++, Java, Python (modo OO)             |
              """)

    def exercise_4(self):
        print("4.  ¿Qué es un patrón Arquitectónico, software e Idion?")
        print("\n")
        print("""
Patrón arquitectónico: 
    Es una solución general reutilizable para la organización de sistemas a gran escala. 
    Define la estructura del sistema y cómo interactúan sus partes. 
    Ejemplos: Modelo-Vista-Controlador (MVC), Microservicios, Clean Architecture.

Patrón de software: 
    Son soluciones comunes a problemas recurrentes de diseño a nivel medio o bajo del sistema. 
    Son más específicos que los arquitectónicos. 
    Ejemplos: Singleton, Observer, Factory, Adapter.

Idiom (o idiomático): 
    Es una forma típica y recomendada de usar un lenguaje de programación específico, según sus convenciones. 
    No es un patrón formal, pero mejora la legibilidad y mantenibilidad. 
    Ejemplo en Python: with open("archivo.txt") as f: para manejar archivos.
              """)
    
    def exercise_5(self):
        print("5.  Realizar un Diagrama que relacione los niveles de Abstracción y los tipos de Patrones.")
        print("\n")
        print("""
Los patrones de software pueden clasificarse según el nivel de abstracción en el que se aplican dentro de un sistema. 
Generalmente se agrupan en tres niveles: arquitectónico, de diseño y de implementación.

Nivel de arquitectura: 
En este nivel se definen estructuras generales de alto nivel que organizan cómo interactúan los componentes principales del sistema. 
Aquí se aplican patrones arquitectónicos como MVC (Modelo-Vista-Controlador), Clean Architecture y Microservicios, 
que establecen cómo se organiza el flujo de datos y responsabilidades en una aplicación.

Nivel de diseño: 
Es un nivel intermedio, donde se aplican patrones que solucionan problemas comunes relacionados con la estructura y comportamiento de objetos y clases. 
Algunos ejemplos de patrones en este nivel son:
Strategy: permite seleccionar un algoritmo en tiempo de ejecución.
Repository: separa la lógica de acceso a datos del resto del sistema.
Factory Method y Abstract Factory: delegan la creación de objetos a subclases o fábricas.
Observer, Decorator, Command, Adapter, entre otros.

Nivel de implementación: 
Es el nivel más bajo, donde se aplican técnicas específicas y idioms del lenguaje para mejorar la legibilidad, 
el rendimiento o el estilo del código. 
Por ejemplo:
En Python, el uso de list comprehensions, generadores, o el patrón de context manager con with.
En C++, el uso de punteros inteligentes (std::unique_ptr, std::shared_ptr), RAII, etc.

Cada tipo de patrón aporta soluciones reutilizables, mejora la mantenibilidad del código y permite separar las responsabilidades correctamente según el nivel en el que se encuentren.
              """)

    def exercise_6(self):
        print("6.  ¿Establecer 5 diferencias entre Python y C++?")
        print("\n")
        print("""
| Característica          | Python                            | C++                                |
| ----------------------- | --------------------------------- | ---------------------------------- |
| Tipo de lenguaje        | Interpretado                      | Compilado                          |
| Tipado                  | Dinámico                          | Estático                           |
| Manejo de memoria       | Automático (recolector de basura) | Manual (punteros, `new`, `delete`) |
| Complejidad de sintaxis | Simple y legible                  | Más compleja, con reglas estrictas |
| Velocidad de ejecución  | Más lento en general              | Más rápido y eficiente             |
              """)

    def exercise_7(self):
        print("7.  ¿Realizar un Cuadro Comparativo entre las definiciones de Objeto de C++ vs Python?")
        print("\n")
        print("""
| Característica            | C++                                     | Python                                |
| ------------------------- | --------------------------------------- | ------------------------------------- |
| Definición de clase       | `class NombreClase { ... };`            | `class NombreClase:`                  |
| Constructor               | Mismo nombre que la clase (`Persona()`) | Método especial `__init__`            |
| Tipado de atributos       | Declarado explícitamente con tipo       | Dinámico (sin declarar tipos)         |
| Visibilidad (encapsulado) | `public`, `private`, `protected`        | Por convención (guiones bajos)        |
| Herencia múltiple         | Posible, pero con precauciones          | Soportada y más simple de implementar |
              """)

    def exercise_8(self):
        print("8.  ¿Qué es la Biblioteca Tkinter, desarrollar un ejemplo simple?")
        print("\n")
        print("""
Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). 
Permite desarrollar ventanas, botones, menús y otros componentes visuales de manera sencilla, sin necesidad de instalar bibliotecas externas.

Ejemplo simple que muestra una ventana con un mensaje:

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo GUI")
etiqueta = tk.Label(ventana, text="¡Hola Mundo con Tkinter!")
etiqueta.pack()
ventana.mainloop()
              """)
        
    def exercise_9(self):
            print("9.  ¿Cómo Integro SQLite en Python, dar ejemplos de Select, Update, Insert y Delete?")
            print("\n")
            print("""
Python incluye soporte para bases de datos SQLite a través del módulo sqlite3, que permite trabajar con bases de datos locales en archivos .db. 
Un ejemplo básico:

import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Crear tabla (si no existe)
cursor.execute("CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT)")

# INSERT
cursor.execute("INSERT INTO personas (nombre) VALUES (?)", ("Ana",))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM personas")
print(cursor.fetchall())

# UPDATE
cursor.execute("UPDATE personas SET nombre = ? WHERE id = ?", ("Luz", 1))
conn.commit()

# DELETE
cursor.execute("DELETE FROM personas WHERE id = ?", (1,))
conn.commit()

conn.close()
                """)
            
    def exercise_10(self):
            print("10. ¿Cómo puedo realizar pruebas en Python?")
            print("\n")
            print("""
Python permite realizar pruebas con varios frameworks. El más común es unittest, que viene incluido en la biblioteca estándar.
Ejemplo de prueba unitaria:

import unittest

def sumar(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

También se puede usar pytest, una herramienta externa más moderna y legible. 
Las pruebas permiten verificar el comportamiento correcto del código y prevenir errores al modificar funcionalidades.
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
        methods = [name for name in dir(self.exercise_instance) if name.startswith("exercise_")]
        methods.sort(key=lambda x: int(x.split("_")[1]))  # Ordenar por el número

        for name in methods:
            attr = getattr(self.exercise_instance, name)
            self.exercises.append(attr)


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
    
    clear_console()
    print(f"""
    ################   Guía Nro {assignmentNumber} finalizada.   ####################
    """)
    y=False

#Definición Main:

def main():

    menu()

main()