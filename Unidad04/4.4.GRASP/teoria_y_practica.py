import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 4.4

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  Comentar y Reflexionar sobre las citas de Craig Larman y Martin Fowler. ")
        print("\n")
        print("""
- Cita de Craig Larman: "La herramienta de diseño fundamental para el desarrollo de software es una mente bien educada en los principios del diseño. No es UML ni ninguna otra tecnología."
- Cita de Martin Fowler: "Comprender las responsabilidades es clave para un buen diseño orientado a objetos."

Reflexión:
Ambas citas apuntan a desmitificar la idea de que las herramientas visuales o los lenguajes (como UML o un lenguaje de programación específico) hacen el diseño por sí solos. 
Saber dibujar diagramas o conocer la sintaxis de un lenguaje no enseña a pensar en objetos. El verdadero núcleo del Diseño Orientado a Objetos (OOAD) radica en la capacidad mental y analítica del desarrollador para comprender y distribuir correctamente las responsabilidades entre los objetos que colaboran en un sistema. Las herramientas son solo un medio de expresión; los principios de diseño son lo que garantiza la calidad del software.
              """)
    
    def exercise_2(self):
        print("2.  Relacionar UML, prácticas y Patrones. ")
        print("\n")
        print("""
UML es un lenguaje estándar de modelado visual que nos permite explorar y representar tanto el aspecto estático (diagramas de clases) como el dinámico (diagramas de interacción, como secuencia, actividades o estado) de un sistema, yendo más allá del texto plano.

Sin embargo, el verdadero valor de UML no está en el diagrama en sí, sino en las decisiones de diseño que tomamos mientras lo dibujamos (y luego al codificar). Al trazar un diagrama de secuencia y decidir qué objeto envía qué mensaje a otro, estamos asignando responsabilidades. 
Es exactamente en ese momento donde entran en juego las prácticas de diseño como RDD (Diseño Impulsado por la Responsabilidad) y los patrones (como GRASP, SOLID o GoF), que actúan como guías metódicas y racionales para tomar buenas decisiones sobre cómo asignar esas responsabilidades y estructurar las colaboraciones en UML.
              """)

    def exercise_3(self):
        print("3.  ¿Qué es Responsibility Driven Design (RDD)? ")
        print("\n")
        print("""
El Diseño Impulsado por la Responsabilidad (RDD, concebido por Rebecca Wirfs-Brock) es un enfoque o metáfora general para pensar el diseño de software orientado a objetos. 
Propone dejar de ver a los objetos simplemente como contenedores de datos y algoritmos (Data-Driven Design), para concebirlos como una "comunidad de personas" (objetos colaboradores) donde cada uno asume roles específicos, tiene contratos/obligaciones (responsabilidades) y colabora con otros para cumplir el trabajo del sistema.

Según Rebecca Wirfs-Brock, RDD se basa en 3 principios fundamentales:
1. Maximizar la abstracción.
2. Distribuir el comportamiento.
3. Preservar la flexibilidad del diseño.
              """)

    def exercise_4(self):
        print("4.  Comentar la cita de Autor: 'Una responsabilidad no es lo mismo que un método, es una abstracción, pero los métodos cumplen con las responsabilidades.' ")
        print("\n")
        print("""
Esta frase marca la diferencia entre el nivel conceptual/de diseño y el nivel de implementación:

- Una responsabilidad es una obligación o contrato abstracto de alto nivel sobre lo que un objeto debe saber o hacer (por ejemplo: "conocer el total de una venta" o "proporcionar acceso a la base de datos").
- Un método es la implementación concreta en código que ejecuta una acción para cumplir con esa responsabilidad.

La traducción de una responsabilidad a métodos depende de su granularidad: una responsabilidad pequeña puede resolverse con un único método en una clase, mientras que una responsabilidad grande puede requerir decenas de clases y cientos de métodos colaborando entre sí mediante el envío de mensajes.
              """)
    
    def exercise_5(self):
        print("5.  ¿Qué entiende por Patrón (en Software y Arquitectura de Software)? ")
        print("\n")
        print("""
Un patrón es una solución probada, comprensible y reutilizable a un problema recurrente de diseño dentro de un contexto determinado. 
No se trata de inventar ideas nuevas, sino de capturar y codificar la experiencia colectiva de ingenieros y diseñadores expertos para evitar "reinventar la rueda".

Todo patrón expresa una relación de tres partes:
Contexto -> Problema -> Solución (Patrón) = Calidad de Diseño.

Además, los patrones proveen un vocabulario común y compartido entre desarrolladores, permitiendo comunicar conceptos arquitectónicos complejos de forma rápida, clara y precisa con solo nombrarlos.
              """)

    def exercise_6(self):
        print("6.  ¿Qué significa y qué se pretende con GRASP? ")
        print("\n")
        print("""
GRASP significa "General Responsibility Assignment Software Patterns" (Patrones Generales de Software para Asignar Responsabilidades), término acuñado por Craig Larman (y cuya regla mnemotécnica sugiere que un OOAD exitoso requiere comprensión / "grasp").

¿Qué se pretende con GRASP?
Proporcionar una ayuda de aprendizaje y un conjunto de 9 principios fundamentales (Experto en Información, Creador, Controlador, Bajo Acoplamiento, Alta Cohesión, Polimorfismo, Fabricación Pura, Indirección y Variaciones Protegidas) para guiar de forma metódica, racional y explicable la asignación de responsabilidades a clases y objetos. 
Con esto se busca evitar diseños frágiles, difíciles de mantener o reutilizar, logrando sistemas flexibles, robustos y con bajo acoplamiento y alta cohesión.
              """)

    def exercise_7(self):
        print("7.  Relacionar Clase, Conocer y Hacer. ")
        print("\n")
        print("""
En el Diseño Orientado a Objetos (OOAD / RDD), una Clase es la abstracción o plantilla que encapsula un conjunto de responsabilidades relacionadas (un contrato u obligación sobre su comportamiento y estado). 
Estas responsabilidades que asume una clase se dividen exactamente en dos categorías:

1. Conocer (Knowing): Lo que la clase sabe o mantiene en su estado:
   - Conocer sus propios datos encapsulados (atributos privados).
   - Conocer a otros objetos relacionados con los que colabora.
   - Saber cosas que puede derivar o calcular a partir de sus datos.

2. Hacer (Doing): Las acciones que la clase ejecuta:
   - Hacer algo por sí misma (crear objetos, calcular, asignar valores).
   - Iniciar una acción en otros objetos (enviar mensajes).
   - Controlar y coordinar actividades en otros objetos.

En síntesis, una clase cumple su rol dentro del sistema combinando lo que "conoce" (sus atributos y asociaciones) con lo que "hace" (sus métodos y colaboraciones).
              """)

    def exercise_8(self):
        print("8.  Desarrollo Práctico: Calculadora con Patrón Controlador (GRASP). ")
        print("\n")
        print("Ejecutando demostración de Calculadora desacoplada (UI Consola -> Controller -> Lógica de Ecuación)...\n")

        # =========================================================================
        # CAPA DE DOMINIO / LÓGICA DE NEGOCIO (Ecuación y Operaciones)
        # =========================================================================
        class Ecuacion:
            """
            Experto en Información (Information Expert):
            Conoce los operandos y realiza las operaciones matemáticas puras,
            totalmente desacoplada de la consola o interfaz de usuario.
            """
            def sumar(self, a: float, b: float) -> float:
                return a + b

            def restar(self, a: float, b: float) -> float:
                return a - b

            def multiplicar(self, a: float, b: float) -> float:
                return a * b

            def dividir(self, a: float, b: float) -> float:
                if b == 0:
                    raise ZeroDivisionError("No es posible dividir por cero.")
                return a / b

        # =========================================================================
        # CAPA DE APLICACIÓN / PATRÓN GRASP CONTROLADOR (Controller)
        # =========================================================================
        class CalculadoraController:
            """
            Patrón GRASP Controller:
            Primer objeto más allá de la capa de UI que recibe los eventos/solicitudes
            del usuario, valida/coordina la operación y delega el cálculo real
            al objeto de dominio (Ecuacion).
            """
            def __init__(self):
                self._ecuacion = Ecuacion()

            def procesar_operacion(self, opcion: str, num1: float, num2: float) -> float:
                if opcion == "1":
                    return self._ecuacion.sumar(num1, num2)
                elif opcion == "2":
                    return self._ecuacion.restar(num1, num2)
                elif opcion == "3":
                    return self._ecuacion.multiplicar(num1, num2)
                elif opcion == "4":
                    return self._ecuacion.dividir(num1, num2)
                else:
                    raise ValueError("Operación no válida.")

        # =========================================================================
        # CAPA DE INTERFAZ DE USUARIO (UI - Consola)
        # =========================================================================
        class CalculadoraConsolaUI:
            """
            Responsable únicamente de interactuar con el usuario (capturar entradas
            y mostrar resultados) y delegar la petición al Controlador.
            """
            def __init__(self, controller: CalculadoraController):
                self._controller = controller

            def iniciar(self):
                while True:
                    print("\n--- CALCULADORA (Patrón GRASP Controller) ---")
                    print("1. Suma")
                    print("2. Resta")
                    print("3. Multiplicación")
                    print("4. División")
                    print("5. Volver al menú principal de la guía")
                    
                    opcion = input("Seleccione una operación (1-5): ").strip()
                    
                    if opcion == "5":
                        print("Saliendo de la calculadora...")
                        break
                    
                    if opcion not in ("1", "2", "3", "4"):
                        print("Error: Opción inválida. Intente nuevamente.")
                        continue

                    try:
                        num1 = float(input("Ingrese el primer número: "))
                        num2 = float(input("Ingrese el segundo número: "))
                        
                        # La UI no calcula nada: envía el evento al Controlador
                        resultado = self._controller.procesar_operacion(opcion, num1, num2)
                        print(f"--> Resultado: {resultado}")
                        
                    except ValueError as e:
                        print(f"Error de entrada: Ingrese valores numéricos válidos. ({e})")
                    except ZeroDivisionError as e:
                        print(f"Error matemático: {e}")

        # Instanciación y ejecución del flujo desacoplado
        controlador = CalculadoraController()
        vista_consola = CalculadoraConsolaUI(controlador)
        vista_consola.iniciar()


#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■■■■■■■■■■ De acá para abajo sólo es la definición de clases y funciones para el manejo del menú ■■■■■■■■■■

class Assignment():

    """
    Class that abstracts and represents the assignment and stores the list of exercises
    """

    assignmentNumber:float = assignmentNumber
    
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