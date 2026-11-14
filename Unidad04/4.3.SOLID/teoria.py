import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 4.3

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  ¿Por qué debes seguir las buenas Prácticas y en que mejoraría?, justificar con 4 respuestas. ")
        print("\n")
        print("""
Seguir las buenas prácticas es fundamental porque son pautas y recomendaciones que permiten producir software de alta calidad, seguro, eficiente y sostenible a lo largo del tiempo. 
Mejora el desarrollo en los siguientes 4 aspectos:

1. Legibilidad y Mantenimiento: Aportan higiene al código y establecen reglas y convenios claros. Un código fácil de leer se traduce en un mantenimiento más sencillo y económico (vital considerando que el mayor porcentaje del costo del software está en su mantenimiento y casi nunca lo mantiene el autor original).
2. Escalabilidad: Facilitan que el software pueda crecer y adaptarse a nuevos requerimientos sin colapsar ni volverse inmanejable.
3. Estandarización y Trabajo en Equipo: Estandarizan el desarrollo mediante convenciones compartidas, permitiendo que distintos desarrolladores puedan colaborar, revisar código e integrarse de manera homogénea.
4. Reutilización y Calidad: Permiten crear componentes modulares que evitan reinventar la rueda, reduciendo la deuda técnica y la aparición de errores (bugs).
              """)
    
    def exercise_2(self):
        print("2.  ¿Que representa el Principio de Responsabilidad única? ")
        print("\n")
        print("""
Representa la idea de que cada módulo, clase o función debe tener responsabilidad sobre una única parte de la funcionalidad proporcionada por el software, y esa responsabilidad debe estar completamente encapsulada dentro de ella.
Como resume Robert C. Martin, "una clase debe tener solo una razón para cambiar". 
Busca lograr componentes altamente cohesivos y ortogonales (autocontenidos e independientes), separando todo lo que no pertenezca estrictamente a esa única tarea para que modificar una funcionalidad no afecte al resto del sistema.
              """)

    def exercise_3(self):
        print("3.  ¿Qué es el Principio de OCP y que evita? ")
        print("\n")
        print("""
El Principio de Abierto/Cerrado (Open/Closed Principle) establece que los artefactos de software (clases, módulos, funciones, etc.) deben estar abiertos para su extensión, pero cerrados para su modificación. 
Es decir, se debe poder agregar nuevas funcionalidades o tipos sin tener que alterar el código fuente ya existente y probado.

¿Qué evita?
Evita la programación procedural rígida basada en tipos (como cadenas interminables de if/else o switch evaluando enumeradores) donde agregar un nuevo caso obliga a modificar múltiples partes del código existente, introducir dependencias innecesarias, recompilar módulos estables y volver el programa esencialmente imposible de mantener.
              """)

    def exercise_4(self):
        print("4.  Que es el Principio de Sustitución de Liskov, dar ejemplos. ")
        print("\n")
        print("""
El Principio de Sustitución de Liskov (LSP) establece que los subtipos (clases hijas) deben ser completamente sustituibles por sus tipos base (clases padres) sin alterar el correcto funcionamiento ni el comportamiento esperado del programa (subtipado conductual). 
Esto implica respetar el contrato de la clase base (mantener invariantes, no fortalecer precondiciones ni debilitar postcondiciones) y asegurar que la herencia se base en el comportamiento y no solo en los datos.

- Ejemplo de violación (Rectángulo - Cuadrado):
  Matemáticamente un cuadrado es un rectángulo, pero si en código hacemos que Square herede de Rectangle (con métodos setWidth y setHeight independientes), rompemos el contrato esperado. Si un cliente recibe un Rectangle y modifica solo su ancho esperando que el alto se mantenga igual para calcular el área, al sustituirlo por un Square cambiarán ambos lados a la vez, dando un resultado inesperado. Lo mismo ocurre a la inversa si Rectangle hereda de Square.

- Ejemplo de cumplimiento (Plantillas/Iteradores o Polimorfismo):
  La función estándar std::copy(first, last, dest) en C++ funciona correctamente con cualquier tipo de iterador (InputIt, OutputIt) siempre y cuando cada implementación concreta respete estrictamente el contrato y los conceptos requeridos por esos iteradores base.
              """)
    
    def exercise_5(self):
        print("5.  Que es la Segregación de Interfaz, como lo Implementaría, realizar un diagrama UML (sin un lenguaje en particular) ")
        print("\n")
        print("""
El Principio de Segregación de Interfaz (ISP) dicta que "los clientes no deben verse forzados a depender de métodos que no utilizan". 
Sostiene que es mucho mejor tener múltiples interfaces pequeñas y específicas para cada cliente que una única interfaz gigante de propósito general.

¿Cómo se implementa?
Dividiendo ("segregando") las interfaces monolíticas o sobrecargadas en interfaces más pequeñas, cohesivas y específicas. De este modo, cada clase implementa únicamente las interfaces cuyos métodos realmente necesita y utiliza, evitando dependencias innecesarias y recompilaciones forzadas cuando cambia un método ajeno.

Diagrama UML (Ejemplo aplicado al caso DrawStrategy):
En lugar de tener una única interfaz DrawStrategy con métodos para todas las figuras (draw(Circle), draw(Square), etc.), se segrega en interfaces específicas:

+-----------------------+          +-----------------------+
|      <<interface>>    |          |      <<interface>>    |
|  CircleDrawStrategy   |          |  SquareDrawStrategy   |
+-----------------------+          +-----------------------+
| + draw(circle): void  |          | + draw(square): void  |
+-----------------------+          +-----------------------+
            ^                                  ^
            | (implementa)                     | (implementa)
+-----------------------+          +-----------------------+
|  OpenGLCircleDrawer   |          |  OpenGLSquareDrawer   |
+-----------------------+          +-----------------------+
| + draw(circle): void  |          | + draw(square): void  |
+-----------------------+          +-----------------------+
            ^                                  ^
            | (usa)                            | (usa)
+-----------------------+          +-----------------------+
|        Circle         |          |        Square         |
+-----------------------+          +-----------------------+
| - drawing: Strategy   |          | - drawing: Strategy   |
| + draw(): void        |          | + draw(): void        |
+-----------------------+          +-----------------------+
              """)

    def exercise_6(self):
        print("6.  ¿Qué entiende con Inversión de Dependencia? ¿Por qué es tan Importante? ")
        print("\n")
        print("""
El Principio de Inversión de Dependencia (DIP) establece dos reglas clave:
a. Los módulos de alto nivel no deben depender de los módulos de bajo nivel; ambos deben depender de abstracciones.
b. Las abstracciones no deben depender de los detalles; los detalles deben depender de las abstracciones.

A nivel arquitectónico, implica que el módulo de alto nivel es el "dueño" de la interfaz (define qué necesita) y el módulo de bajo nivel es quien la implementa, invirtiendo el flujo tradicional de dependencias.

¿Por qué es tan importante?
Porque la dependencia es el problema clave en el desarrollo de software a todas las escalas. El DIP permite desacoplar la lógica de negocio (alto nivel) de los detalles técnicos o de infraestructura (bajo nivel, como vistas, pantallas o bases de datos). Gracias a esto, se pueden cambiar, extender o reemplazar las implementaciones de bajo nivel sin afectar ni recompilar los módulos de alto nivel, logrando sistemas flexibles y mantenibles.
              """)

    def exercise_7(self):
        print("7.  Qué relación hay entre Acoplamiento, Cohesión y Dependencia con S.O.L.I.D. ")
        print("\n")
        print("""
La relación es directa y constituye la razón de ser de los principios S.O.L.I.D.:

- El problema: La dependencia y el alto acoplamiento son los enemigos del cambio, ya que unen componentes que se ven obligados a cambiar en paralelo. Por otro lado, una baja cohesión mezcla responsabilidades no relacionadas dentro de un mismo módulo, dificultando su lectura y mantenimiento.

- La solución (S.O.L.I.D.): Estos principios existen específicamente para romper dependencias, minimizar el acoplamiento y maximizar la cohesión:
  * SRP maximiza la cohesión agrupando solo lo que pertenece a una misma responsabilidad.
  * OCP, LSP, ISP y DIP reducen el acoplamiento y controlan las dependencias mediante el uso de abstracciones limpias, interfaces segregadas y contratos respetados, logrando que el software sea fácil de cambiar y ampliar ("Soft = fácil de cambiar y ampliar").
              """)

    def exercise_8(self):
        print("8.  ¿Qué es la “Inyección de Dependencia”? ")
        print("\n")
        print("""
La Inyección de Dependencias (Dependency Injection) es un mecanismo o técnica que sigue el Principio de Inversión de Dependencias. 
Consiste en suministrar (inyectar) desde el exterior las dependencias o implementaciones concretas que un objeto necesita para funcionar (por ejemplo, pasándolas como parámetros a través de su constructor o mediante métodos setters), en lugar de que la propia clase las cree o instancie internamente. 
Esto permite desacoplar el objeto de una implementación específica e intercambiar comportamientos fácilmente incluso en tiempo de ejecución.
              """)

    def exercise_9(self):
        print("9.  ¿Qué es la delegación en POO? ")
        print("\n")
        print("""
En Programación Orientada a Objetos, la delegación es una técnica de diseño mediante la cual un objeto, en lugar de realizar una tarea por sí mismo, transfiere o delega la ejecución de esa responsabilidad a otro objeto auxiliar especializado al cual referencia (composición). 

Por ejemplo, al aplicar el patrón Strategy junto con SRP, una clase Circle no contiene la lógica de cómo dibujarse en pantalla o impresora, sino que mantiene un atributo de tipo DrawStrategy y, cuando se invoca circle.draw(), simplemente delega esa tarea llamando al método draw() de su estrategia asignada.
              """)

    def exercise_10(self):
        print("10. Nombrar 5 Buenas Prácticas. ")
        print("\n")
        print("""
1. DRY (Don't Repeat Yourself): Evitar la repetición de código, lógica, librerías o conocimiento, fomentando la reutilización y la abstracción.
2. KISS (Keep It Simple, Stupid!): Mantener las soluciones lo más simples posible; menos código innecesario implica menos errores (bugs) y mayor facilidad de comprensión.
3. YAGNI (You Aren't Gonna Need It): Evitar programar funcionalidades o abstracciones complejas "por si acaso" se necesitan en el futuro, enfocándose solo en los requisitos actuales.
4. Uso de Control de Versiones (ej. Git) y Pruebas Unitarias/Automatizadas: Mantener un registro histórico de cambios para facilitar el trabajo en equipo y respaldar cada componente con tests que eviten regresiones.
5. Convenciones de Código y Nombres Descriptivos (Don't make me think): Utilizar nombres claros y autoexplicativos para variables, métodos y clases, respetar estándares de indentación y comentar con criterio pensando siempre en quien deberá mantener el código en el futuro.
              """)

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