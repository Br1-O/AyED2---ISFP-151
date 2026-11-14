import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 3.2  # Unidad 3 - Patrones Estructurales

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1. Describir los Tipos de Patrón Estructural.")
        print("\n")
        print("""
Los patrones estructurales explican cómo ensamblar objetos y clases en estructuras más grandes 
a la vez que se mantiene la flexibilidad y eficiencia de la estructura. Se centran en cómo 
se combinan las clases y los objetos para formar nuevas funcionalidades o arquitecturas más complejas 
sin acoplar rígidamente los componentes.
              """)
    
    def exercise_2(self):
        print("2. Qué “tipos” de Problema resuelve.")
        print("\n")
        print("""
Resuelven problemas relacionados con la composición de clases y objetos, tales como:
- Incompatibilidades de interfaces entre distintas clases (Adapter).
- La necesidad de extender una clase o biblioteca cerrada en varias dimensiones ortogonales o independientes 
  sin sufrir una explosión exponencial de subclases (Bridge, Decorator).
- La complejidad de representar estructuras jerárquicas complejas en forma de árbol (Composite).
- La necesidad de simplificar el acceso a subsistemas complejos mediante una interfaz única (Facade).
- Problemas de rendimiento y consumo de memoria excesiva debido a millones de objetos similares (Flyweight).
- El control de acceso o la necesidad de un marcador de posición para un objeto pesado (Proxy).
              """)

    def exercise_4(self):
        print("4. Dar 1 ejemplos del Patrón Composite.")
        print("\n")
        print("""
Un ejemplo clásico es la gestión de componentes y contenedores en un sistema de pedidos de comercio electrónico. 
Un pedido puede contener productos individuales (hojas) y cajas cerradas (contenedores). A su vez, una caja puede contener 
otros productos y más cajas más pequeñas de forma recursiva. El patrón Composite permite tratar tanto a los productos simples 
como a las cajas complejas a través de una interfaz común (por ejemplo, el método calcularPrecio()), ejecutando el comportamiento 
de manera recursiva en toda la estructura de árbol sin que el código cliente deba preocuparse por el nivel de anidación.
              """)
    
    def exercise_5(self):
        print("5. ¿Qué significa en C++ Mixin-Style?")
        print("\n")
        print("""
Se refiere a la técnica conocida formalmente como la Plantilla Curiosamente Recurrente (CRTP) o el uso de Mixins. 
Un mixin es una clase que ofrece cierta funcionalidad para ser heredada por una subclase, pero no está ideada para ser autónoma. 
Heredar de un mixin no busca una especialización estricta (is-a), sino más bien un medio modular de incorporar funcionalidad 
específica de forma limpia mediante herencia múltiple o reutilización de código a nivel de compilación.
              """)

    def exercise_6(self):
        print("6. Por que Programar con Interfaces? ¿Qué Proporciona o Facilita?")
        print("\n")
        print("""
Programar con interfaces (Programación basada en interfaces o IBP) define la aplicación como una colección de módulos interconectados 
que se comunican estrictamente a través de contratos de interfaz. 
Esto proporciona y facilita:
1. Desacoplamiento: Los módulos se pueden desconectar, reemplazar o actualizar sin comprometer el contenido ni la estabilidad de otros módulos.
2. Modularidad y Mantenibilidad: Reduce considerablemente la complejidad total del sistema al aislar las responsabilidades.
3. Trabajo en Equipo de Terceros: Permite que distintos equipos desarrollen componentes paralelos siempre que cumplan con la interfaz acordada como un contrato formal.
              """)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■■■■■■■■■■ De acá para abajo sólo es la definición de clases y funciones para el manejo del menú ■■■■■■■■■■

class Assignment():
    assignmentNumber: float = assignmentNumber
    
    def __init__(self):
        self.exercise_instance = Exercises()
        self.exercises = []

        exercise_methods = [
            (int(name.split("_")[1]), getattr(self.exercise_instance, name))
            for name in dir(self.exercise_instance)
            if callable(getattr(self.exercise_instance, name)) and name.startswith("exercise_")
        ]
        exercise_methods.sort(key=lambda x: x[0])
        self.exercises = [method for _, method in exercise_methods]
        self.totalExercises: int = len(self.exercises)

def isNum(num):
    while(num.isdigit() == False):
        print("No es un dato valido.\n")
        num = input("Ingrese un numero natural entero:")
    return int(num)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    assignment_instance = Assignment()
    assignmentNumber = assignment_instance.assignmentNumber
    totalExercises = assignment_instance.totalExercises
    exercises = assignment_instance.exercises

    option = ""
    global y
    y = True

    chars_per_line = 70
    
    while y:
        option = input("\n" +
                     "═"*chars_per_line + 
                     "\n" + 
                     f"Elija el número de pregunta teórica a revisar (del 1 al {totalExercises})".center(chars_per_line) + 
                     "\n" + 
                     "O ingrese cualquier otro numero para salir: ".center(chars_per_line) + 
                     "\n" + 
                     "═"*chars_per_line + 
                     "\n")
        option = isNum(option)
        
        if 1 <= option <= totalExercises:
            clear_console()
            print("\n" + f"( Pregunta {option} )".center(chars_per_line, "═") + "\n")
            exercises[option - 1]()
        else:
            break

    print(f"""
    ################   Teoría Unidad {assignmentNumber} finalizada.   ####################
    """)
    y = False

def main():
    menu()

if __name__ == "__main__":
    main()