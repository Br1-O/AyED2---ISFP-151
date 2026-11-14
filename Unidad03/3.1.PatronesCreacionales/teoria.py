import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 3.1  # Unidad 3 - Patrones Creacionales

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1. Describir los Tipos de Patrones.")
        print("\n")
        print("""
Los patrones de diseño se agrupan por su propósito y ámbito de aplicación en tres grandes grupos:
- Patrones de Creación: Proporcionan mecanismos de creación de objetos que aumentan la flexibilidad y la reutilización de código existente.
- Patrones Estructurales: Explican cómo ensamblar objetos y clases en estructuras más grandes a la vez que se mantiene la flexibilidad y eficiencia.
- Patrones de Comportamiento: Se encargan de una comunicación efectiva y la asignación adecuada de responsabilidades entre objetos.
              """)
    
    def exercise_2(self):
        print("2. ¿Qué es un patrón de Software?")
        print("\n")
        print("""
Un patrón de software es una solución general, reutilizable y probada a un problema recurrente que surge dentro de un contexto determinado en el diseño de software. 
No se trata de código terminado que se puede copiar directamente, sino de una plantilla o descripción conceptual sobre cómo resolver un problema de diseño arquitectónico o de código.
              """)

    def exercise_3(self):
        print("3. Clasificar los Patrones de Software.")
        print("\n")
        print("""
Además de su clasificación por propósito (Creación, Estructura y Comportamiento), los patrones se clasifican por su nivel de escala y abstracción en:
1. Idioms (Patrones de bajo nivel): Específicos y aplicados a un único lenguaje de programación.
2. Patrones de Diseño (Nivel medio): Estructuras de clases y relaciones de objetos aplicables de forma independiente del lenguaje.
3. Patrones de Arquitectura (Alto nivel): Patrones universales utilizados para diseñar la estructura global y completa de una aplicación (ej. MVC, Microservicios).
              """)

    def exercise_4(self):
        print("4. Clasificar los Patrones de Creación y realizar una Descripción.")
        print("\n")
        print("""
Los patrones de creación (o creacionales) definen cómo puede crearse un objeto, aislando los detalles de su instanciación para que el código no dependa de clases concretas. Se clasifican en 5 tipos principales:
1. Abstract Factory: Permite producir familias de objetos relacionados sin especificar sus clases concretas.
2. Builder (Constructor): Permite construir objetos complejos paso a paso separando el código de construcción de su representación.
3. Factory Method: Proporciona una interfaz para crear objetos en una superclase, permitiendo a las subclases alterar el tipo de objetos a instanciar.
4. Prototype: Permite clonar objetos existentes (prototipos) sin acoplar el código a sus clases concretas.
5. Singleton: Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.
              """)
    
    def exercise_5(self):
        print("5. Dar un ejemplo de uso de cada uno.")
        print("\n")
        print("""
- Abstract Factory: Una interfaz gráfica (GUI) multiplataforma que crea familias de componentes coherentes (botones y ventanas estilo Windows o Mac).
- Builder: La creación de objetos complejos configurables con múltiples parámetros opcionales (como un objeto 'Casa' con piscina, jardín, etc.), evitando constructores gigantescos.
- Factory Method: Un sistema logístico que crea objetos de transporte ('Camión' o 'Barco') dependiendo de si la ruta es terrestre o marítima.
- Prototype: La clonación de enemigos o elementos complejos en un videojuego a partir de un prototipo base para optimizar recursos.
- Singleton: Un administrador centralizado de conexiones a una Base de Datos que requiere una única instancia activa en todo el sistema.
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