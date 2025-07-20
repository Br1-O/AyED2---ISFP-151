import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 1.1

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  Que entiende por paradigma")
        print("\n")
        print("""
Un paradigma es una forma de pensar y abordar los problemas. 
En programación, se refiere al conjunto de principios y métodos que guían cómo se estructura y escribe el código. 
Cada paradigma propone una manera diferente de entender y organizar el software.
En concreto se lo puede definir como un conjunto de métodos sistematicos aplicables a todos los niveles del diseño de programas.
Es decir, son una filosofia para la creación de programas.
              """)
    
    def exercise_2(self):
        print("2. Realizar un comentario de la cita de Martin Fowler en la bibliografía")
        print(" \n \n ")
        print("""
Martin Fowler plantea que lo importante realmente es la legibilidad y simpleza del código,
pues los lenguajes ya fácilitan interfaces que traduzcan lo que programamos en lenguaje maquina,
con lo cual la maquina siempre entenderá lo que compilemos y ejecutemos.
Pero no hay ningún compilador o interprete para hacer que nuestro código sea entendible por parte de humanos,
y somos nosotros los que debemos encargarnos de ello. Esto documentando correctamente, usando nombres de variables explicativas,
respetando espacios e identaciones, etc. 
Debemos seguir estas buenas prácticas, entre otras, para fácilitar el uso compartido de nuestros programas.
              """)

    def exercise_3(self):
        print("3.  Describir el Concepto de “Complejidad del Software” ")
        print(" \n \n ")
        print("""
Cuanto menos complejidad tengamos, más fácil será depurar y comprender. Cuanto más complejo se 
vuelve un programa, más difícil es trabajar en él
Así, reducir la complejidad del software propuesto es una de las principales tareas y preocupaciones de un buen desarrollador.
Siempre es mejor intentar plantear una solución simple a un problema, antes que complejizarlo innecesariamente.
Si se dispone del tiempo suficiente esto será lo ideal, pues más adelante facilitará el mantenerlo, corregir errores o extender funcionalidades.
              """)
        
    def exercise_4(self):
        print("4.  Relacionar los “Aspectos” de Calidad y “Propiedades del Software”")
        print("\n")
        print("""
Los aspectos de calidad del software abarcan no sólo a las propiedades del software, éstas siendo qué hace y cómo lo hace, 
en concreto su eficiencia y eficacia al resolver una tarea. Sino, así mismo, abarcan los aspectos que ayuden a la mantenibilidad, 
escalabilidad y reutilización de ese código. Es decir, todo lo que favorezca al entendimiento de ese software por parte de humanos,
sean o no su desarrollador inicial. Comentarios, nombres de clases, objetos, variables y funciones claros, 
una correcta división y estructura de carpetas, etc. Todos estos aspectos hacen a la calidad del software.
              """)
    
    def exercise_5(self):
        print("5.  Relacionar Paradigma y Lenguaje")
        print(" \n \n ")
        print("""
Un paradigma es una estrategia para abordar problemas,
propone una manera propia de entenderlos y de plantear soluciones que sigan una misma linea para organizar y facilitar la resolución.
Así, un paradigma es completamente agnostico del lenguaje. Es decir, no está ligado a un lenguaje en particular, sino que es una forma de entender y comprender a los problemas y sus soluciones.
Aunque cabe aclarar que, al tener que eventualmente plantear la solución como una pieza de código, 
se tendrá que recurrir a un lenguaje de programación en particular para realizar esa resolución.
Y es ahí donde el escoger un lenguaje que se adecue y fácilite el tipo de paradigma que buscamos implementar se vuelve clave, 
pues no todos los lenguajes soportan todos los paradigmas.
              """)

    def exercise_6(self):
        print("6.  Que s e entiende por paradigma “Imperativo”")
        print(" \n \n ")
        print("""
Se entiende por paradigma "Imperativo" a la filosofia de mandar sobre la computadora por completo, 
dandole ordenes especificas de cómo hacer lo que queremos que haga. Así, la computadora ejecutará nuestras ordenes linea por linea, 
tal cual nosotros lo planteamos, teniendo así control total sobre qué hace y CÓMO lo hace para la resolución del problema planteado.
Es por esto que en este paradigma hay que tener mucho cuidado con el orden en que se expresan las ordenes,
pues las instrucciones además soleran cambiar estados de variables sobre el sistema, y así,
una instrucción correcta, pero dada en el momento incorrecto, provocará cambios inesperados al actuar sobre valores que no son los esperados.
              """)

    def exercise_7(self):
        print("7.  Que s e entiende por paradigma “Declarativo”")
        print("\n")
        print("""
La programación declarativa es un estilo de creación de programas que expresa la lógica de un cálculo sin hablar de su flujo de control.
La programación declarativa es un paradigma de programación en el que el programador define lo que debe lograr el programa sin definir cómo debe implementarse. 
En otras palabras, el enfoque se centra en lo que se necesita lograr en lugar de instruir cómo lograrlo.
En general se pueden distinguir 2 grandes caracteristicas: Que poseen un lenguaje especificio de dominio (DSL), 
y que utilizan ese lenguaje para abstraer y ocultar la capa inferior al usuario que lo esté usando.
              """)
    
    def exercise_8(self):
        print("8.  Que “diferencias” presentan entre estos dos Paradigmas")
        print(" \n \n ")
        print("""
Estos dos paradigmas se diferencian en cómo entienden y plantean el abordaje de la resolución de un problema.
En el caso imperativo lo hace diciendo el cómo, centrandose en las implementaciones y dando instrucciones expresas, 
concisas y en un orden especifico en el que deben ejecutarse. 
Se busca tener el mayor control posible sobre lo que hará la computadora, y en especifico en cómo lo hará.
En cambio en el caso descriptivo lo hace diciendo qué debe hacerse, utilizandose interfaces y abstracciones que faciliten el plantear el problema, 
y su solución, sin enfocarse en lo que hay por debajo o en cómo se realiza todo el proceso.
De esta forma, en el enfoque descriptivo ya no se trabaja con implementaciones imperativas, sino con abstracciones descriptivas que faciliten las tareas.
Pero cuando se desee un mayor control sobre el cómo de dichas implementaciones, el paradigma imperativo será una mejor elección.
              """)

    def exercise_9(self):
        print("9.  Porque Afirmamos que el Paradigma de Objetos es Imperativo?")
        print(" \n \n ")
        print("""
Se afirma que el paradigma de Objetos es imperativo porque, más allá de aprovechar conceptos como la abstracción a lo largo de su desarrollo,
cosa que también podría verse en un paradigma descriptivo, 
así mismo se basa principalmente en decir cómo se van a realizar las implementaciones de esas abstracciones, 
cómo van a funcionar sus relaciones jerarquicas y polimorficas, cómo se van a encapsular sus atributos y métodos, 
y cómo serán las implementaciones de esos métodos. 
Y dado este enfoque en el cómo es que se puede afirmar que el paradigma de Objetos es Imperativo.
              """)
        
    def exercise_10(self):
        print("10. Que ventajas propone la programación Declarativa?")
        print("\n")
        print("""
Este enfoque ayuda y mejora la mantenibilidad/legibilidad al ser más cercano al lenguaje humano, 
es más conciso, más reutilizable y facilita el trabajo con estados, 
permitiendo trabajar con sólo los estados finales y que el sistema por debajo se encargue de los estados más especificos, 
así como del manejo de sus errores.
              """)
    
    def exercise_11(self):
        print("11. Que es el Paradigma “Funcional”")
        print(" \n \n ")
        print("""
El paradigma de la programación funcional tiene sus raíces en las matemáticas y es independiente del lenguaje. 
El principio clave de este paradigma es la ejecución de una serie de funciones matemáticas.
Tú compones tu programa de funciones cortas. Todo el código está dentro de una función. 
Todas las variables tienen como ámbito la función.
En el paradigma de programación funcional, las funciones no modifican ningún valor fuera del alcance de esa función y las 
funciones en sí mismas no se ven afectadas por ningún valor fuera de su alcance.
              """)

    def exercise_12(self):
        print("12. Buscar en Internet la relación entre paradigma Funcional y Javascript?")
        print(" \n \n ")
        print("""
JavaScript permite programación funcional: 
funciones como ciudadanos de primera clase, funciones puras, inmutabilidad, uso de map, filter, reduce. 
Aunque es multi-paradigma, se usa cada vez más funcionalmente. 
Así mismo el desarrollo de frameworks que ahondan aún más en la programación funcional como fundamento en este lenguaje reafirma su relación. 
Casos de esto son frameworks como React, que plantea la modularización en componentes, que son funciones reutilizables a lo largo del código.
        """)

    def exercise_13(self):
        print("13. Que tipos de sistemas se podrían desarrollar bajo el Paradigma de Bases de Datos")
        print("\n")
        print("""
Básicamente todo sistema que deba trabajar con una base de datos, 
un conjunto de información estructurada y organizada que debe ser almacenada en un sistema electronico para su persistencia y posterior acceso.
Esto permitirá:
• Trabajar con bases de datos para estructurarlas.
• Acceder, modificar, actualizar datos en la base de datos.
• Comunicarse con servidores.
Todo realizado bajo el uso de la abstracción de un lenguaje de manipulación de datos, 
fácilitando todas estas tareas al no tener que preocuparse quien lo usa de las implementaciones por debajo.
              """)

    def exercise_14(self):
        print("14. Explicar la Programación “Reactiva” sus conceptos Clave")
        print(" \n \n ")
        print("""
La programación reactiva es un paradigma enfocado en el trabajo con flujos de datos finitos o infinitos de manera asíncrona, o dicho de forma más simple,
en la reacción a eventos o cambios de estado. 
Su concepción y evolución ha ido ligada a la publicación del Reactive Manifesto, que establecía las bases de los 
sistemas reactivos, los cuales deben ser:
■ Responsivos: aseguran la calidad del servicio cumpliendo unos tiempos de 
respuesta establecidos.
■ Resilientes: se mantienen responsivos incluso cuando se enfrentan a 
situaciones de error.
■ Elásticos: se mantienen responsivos incluso ante aumentos en la carga de 
trabajo.
■ Orientados a mensajes: minimizan el acoplamiento entre componentes al 
establecer interacciones basadas en el intercambio de mensajes de manera 
asíncrona.
              """)

    def exercise_15(self):
        print("15. Dar ejemplos de uso de Programación Reactiva.")
        print(" \n \n ")
        print("""
Un ejemplo de uso de Programación Reactiva es el desarrollo de GUIs, 
normalmente hoy en día usando algún framework que lo fácilite (como React, Angular, Vue, Astro, etc.)
Esas GUI deberán responder al cambio de estado de variables (como son variables de inicio de sesión o de productos en un carrito de compras, por ej.),
o a eventos que puede desencadenar el usuario (como puede ser el click en un botón o apertura de una ventana emergente, por ej.)
Así mismo otro ejemplo puede ser aplicaciones que reaccionen a cambios de estado en la información que recibe de medios externos, 
como un sistema financiero que reaccione al cambio en el valor de acciones o bienes digitales.
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