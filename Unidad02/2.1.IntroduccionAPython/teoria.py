import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.1

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  ¿Que Es Agnostic Programing?, justifique la respuesta. ")
        print("\n")
        print("""
Es un paradigma de desarrollo de software donde se elige el uso de un lenguaje de programación,
no guiandose por las habilidades y conocimientos del equipo de trabajo,
sino por la idoneidad de dicho lenguaje para el proyecto a llevar a cabo.
              """)
    
    def exercise_2(self):
        print("2.   Dar ejemplos de Agnostic Programing y por que debería pensar así?. ")
        print("\n")
        print("""
Un ejemplo es cuando se eligen lenguajes fuertemente tipados y que prioricen el control sobre la seguridad y muchos aspectos de bajo nivel 
para tareas donde cometer un simple error puede acarrear consecuencias gigantescas.
(por ej: Java en sistemas bancarios o C en sistemas aeroespaciales y medicos)
Así mismo cuando se emplean lenguajes más versatiles o de alto nivel para sistemas que se favorezcan por un desarrollo rápido,
que permita el acceso a múltiples frameworks y librerias diversas, 
y favorezca un diseño más centrado a eventos y reaccionar a acciones del usuario 
(por ej: Js en desarrollo web o Python en desarrollo de IA y manejo de grandes caudales de datos)
Una ventaja de la programación agnostica al lenguaje es que da una mayor versatilidad a la hora de confrontar un problema,
encontrando la herramienta adecuada para la tarea 
y no quedando relegado el equipo completo al uso de un lenguaje que puede no ser el más apto para el proyecto.
              """)

    def exercise_3(self):
        print("3.  Describir Python y algunas de sus Características. ")
        print("\n")
        print("""
Python es un lenguaje multiplataforma, interpretado, y de alto nivel. 
Posee tipado dinamico, multiparadigma y soporta el OOP.
Su interprete más usado está escrito en C, y su sintaxis se basa principalmente en evitar la verbosidad excesiva y facilitar la legibilidad para el humano.
Posee una gran cantidad de librerias, muchas de las más usadas centradas al manejo de datos y desarrollo de machine learning.
Aunque en muchos casos es elegido por dichas librerias especificas, 
también es muy usado en múltiples areas de desarrollo que puedan beneficiarse de su rico ecosistema de librerias y facilidad en el desarrollo.
              """)

    def exercise_4(self):
        print("4.  Dar ejemplos de Utilización de Python, determinar los puntos “Fuertes” del Lenguaje que lo posicionaron hoy como el mas utilizado en esos Segmentos.  ")
        print("\n")
        print("""
Ejemplos de lo dicho en el punto anterior son en desarrollo web al usar Flask, Django, FastAPI. Desarrollando juegos rápidos mediante PyGame. O desarrollando GUI simples y rápidas con Tkinter.
Fuera de esos ámbitos menos especificos, como ya se ha mencionado, Python brilla por sus librerias de manejo de datos, como Numpy o Pandas. 
O librerias de machine learning y desarrollo de IA en general, como es PyTorch y TensorFlow.
Sus puntos fuertes son principalmente su fácilidad en cuanto sintaxis y bajos tiempos de desarrollo en comparación a otros lenguajes,
así como su rico ecosistema de librerias generales, y, 
en particular, sus librerias de manejo de datos, desarrollo de IA y machine learning.
              """)
    
    def exercise_5(self):
        print("5.  Que significa Tipado Dinámico ")
        print("\n")
        print("""
Significa que no se realiza ningún tipo de verificación del tipo de variables, y sus datos contenidos, al momento de compilación.
Esto hace que a una misma variable puedan asignarsele datos de diferentes tipos de datos en tiempo de ejecución.
(aunque en realidad por debajo lo único que se hace es una reasignación de la dirección a la que apunta el puntero que representa la variable,
cambiando así la referencia de un objeto a otro)
              """)

    def exercise_6(self):
        print("6.  Como compila y Ejecuta Python. ")
        print("\n")
        print("""
El intérprete de Python se puede dividir en dos partes principales: 
un compilador de Python y una máquina virtual de Python (PVM).

Cada vez que ejecutamos un programa Python, el compilador traduce el código fuente en 
bytecode (bytecode representa una serie de instrucciones diferentes). Dado que una CPU no 
puede entender el bytecode, este bytecode se convierte en código máquina utilizando PVM.
Una vez que el código fuente se convierte en código máquina, nuestro programa es ejecutado por la 
CPU. 
El intérprete de Python realiza todo este proceso de conversión de código fuente en código 
máquina, y este intérprete de Python está escrito en el lenguaje de programación C.
              """)

    def exercise_7(self):
        print("7.  Dentro de lo Posible, realizar una Comparativa entre C++ & Python. ")
        print("\n")
        print("""
Python y C++ son lenguajes muy distintos, cada uno con sus ventajas.
C++ es un lenguaje compilado, de tipado estático, rápido y eficiente, ideal para sistemas donde el rendimiento es clave. 
Tiene una sintaxis más compleja y requiere mayor atención al manejo de memoria, pero ofrece gran control sobre el hardware.

Por otro lado, Python es interpretado, de tipado dinámico y muy fácil de escribir y leer. 
Es más lento en ejecución, pero favorece el desarrollo rápido y automatización, gracias a su amplia biblioteca estándar.
              """)

    def exercise_8(self):
        print("8.  Elegir 3 preguntas frecuentes y Desarrollarlas. ")
        print("\n")
        print("""
¿Es mejor aprender C ++ o Python?
- En realidad depende de a qué se quiera apuntar y con qué objetivos. 
Si se desea aprender sobre programación de bajo nivel, cómo funcionan la mayoria de sistemas por debajo de las interfaces de usuario/desarrollador,
o se quiere apuntar a desarrollar uno mismo sistemas de cero, C++ sería la mejor opción.
Ahora bien, si lo que se quiere es simplemente aprender a desarrollar de forma rápida, sin tener que aprender demasiados técnicismo o sintaxis laboriosa,
o se quiere apuntar sólo a un ámbito en particular donde ya haya un gran ecosistema de librerias y frameworks que faciliten aún más dicho desarrollo,
entonces sería mejor optar por Python (o así mismo Ruby o Js, si hablamos de web)
              
¿Python puede reemplazar a C ++?
- C++, así como C, son usados ampliamente en el desarrollo de bajo nivel por permitir el manejo de recursos de forma optima, 
así como la interacción con partes del hardware que otros lenguajes de más alto nivel no permiten.
Python está desarrollado sobre C, entonces que lo reemplace es como decir que los transistores reemplazan la electricidad 
o que los booleanos reemplazan los states digitales fisicos.
Una interfaz no puede reemplazar a su implementación, por más que sea ella la usada, debajo siempre debe haber algo que no sea la misma interfaz.

¿Qué es mejor C ++, Java o Python?
- Depende. Todos los lenguajes tienen idoneidad para campos, tareas o prácticas especificas, 
por algo fueron pensados y desarrollados, y aún siguen en uso.
C++, así como C, son lenguajes que son pensados para el manejo de hardware y alto rendimiento,
así como el control a detalle de recursos donde una falla puede ser critica.
Java es pensado en sistemas donde se quiere independencia de plataforma, permitiendo escribir el código una sola vez y ejecurtarlo donde sea.
O así mismo si se quiere rendimiento y acceso a recursos, pero no al nivel de detalle de C++ o C, 
pero así mismo teniendo acceso a librerias y frameworks que faciliten el desarrollo de ciertas tareas (como es Spring y Springboot en desarrollo web)
Y Python es extremadamente adecuado cuando se desean tiempos de desarrollo bajos, dinamismo, 
acceso a recursos que faciliten tareas y permitir el alcance al código a la mayor cantidad de personas, 
sin necesidad de que sean altamente letradas en lenguajes de programación, al tener una sintaxis facilmente legible para el lenguaje humano.
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