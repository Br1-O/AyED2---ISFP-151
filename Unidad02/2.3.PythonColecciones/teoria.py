import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.3

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.1 Que es una Tupla, como funciona, dar ejemplos.")
        print("\n")
        print("""
Las tuplas son colecciones ordenadas e inmutables. 
Es decir, una vez asignados los elementos, no pueden ser alterados. 
En términos funcionales, podría decirse que las tuplas son un subconjunto de las listas, 
por cuanto soportan las operaciones con índices para acceder a sus elementos, al ser ordenadas; 
pero no así las de asignación, por su naturaleza inmutable.
              """)
    
    def exercise_2(self):
        print("1.2 Que es una Lista, como funciona, dar ejemplos.")
        print("\n")
        print("""
Una lista es un conjunto ordenado de objetos, admitiendo cualquier tipo de objetos, en cualquier combinación posible.
(es decir, que podrá agrupar: numbers, strings, objetos creados por nosotros, y así mismo otras colecciones, como otras listas, tuplas, o diccionarios)
Al ser un conjunto ordenado admite el acceso por indices a sus elementos. 
Así mismo permite la asignación por indice, al ser de caracter mutable.
              """)

    def exercise_3(self):
        print("1.3 Que es Diccionario, como funciona, dar ejemplos.")
        print("\n")
        print("""
Los diccionarios son colecciones no ordenadas de objetos. 
Además, sus elementos tienen una particularidad: siempre conforman un par clave-valor. 
Es decir, cuando añadimos un valor a un diccionario, se le asigna una clave única con la que luego se podrá acceder a él 
(pues la posición ya no es un determinante, no utilizamos un indice para acceder y asignar elementos, 
sino una clave asignada por nosotros para dicho elemento)
              """)

    def exercise_4(self):
        print("3.1 Mete los valores del 1 al 100 en una lista.")
        print("\n")

        number_list = []
        for i in range (1, 101):
            number_list.append(i)
        print(number_list)
    
    def exercise_5(self):
        print("3.2 Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.")
        print("\n")

        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        try:
            month_number = int(input("Por favor, ingrese el número del mes que desea visualizar:")) - 1
            if 0 <= month_number <= 11:
                print("El mes que seleccionó es: " + months[month_number] + ".")
            else:
                print("Por favor, debe ingresar un número entre 1 y 12.")
        except:
            print("Por favor, debe ingresar un número.")

    def exercise_6(self):
        print("3.3 Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50")
        print("\n")
        
        try:
            number = int(input("Por favor, ingrese un número para visualizar su tabla de múltiplicar hasta el numero 10:"))
            multiply_table = []

            for i in range(1, 11):
                multiply_table.append(number*i)
                print("\n" + str(i) + "x" + str(number) + ": " + str(multiply_table[i - 1]))
        except:
            print("Por favor, debe ingresar un número.")

    def exercise_7(self):
        print("3.4 Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.")
        print("\n")

        print("¡Bienvenido a tu agenda telefonica en memoria! \n")
        personal_phone_book = {}
        keep_adding = True
        while keep_adding:
            name = input("Por favor, ingresa el nombre de un contacto a agregar: \n (Si ya no deseas agregar contactos, por favor ingresa 'fin') \n")
            
            if name == "fin":
                break

            if name in personal_phone_book:
                print("¡El nombre ingresado ya existe en tu agenda telefonica en memoria! \n")
            else:
                phone_number = input(f"Por favor, ingresa un número de telefono para tu contacto {name}: ")
                personal_phone_book[name] = phone_number
        
        print("Tus numeros telefonicos en memoria son: ")
        for name, phone_number in personal_phone_book.items():
            print("- " + name + ": " + phone_number)

    def exercise_8(self):
        print("4.1 Describir las sentencias While y For")
        print("\n")
        print("""
Las sentencias While y For son palabras claves reservadas por el lenguaje Python para identificar a dos formas de dar lugar a bucles.
Estos bucles son formas de controlar el flujo del programa, de modo que provocan que una cierta pieza de código se ejecute de forma reiterada.
En el caso del While, la pieza de código en su interior se ejecutará siempre que la condición que la sigue sea verdad. 
Es ideal cuando desconocemos cuántas iteraciones deberemos hacer, y queremos que dichas iteraciones sucedan sólo mientras una cierta condición se cumpla.
En el caso del For, la pieza de código en su interior se ejecutará por una cantidad X de iteraciones pre establecida. 
Es ideal si ya conocemos cuántas iteraciones debemos realizar, o si queremos ejecutar una cierta pieza de código por cada elemento dentro de un conjunto.
              """)
        
    def exercise_9(self):
            print("4.2 Describir y dar ejemplos de Range y Switch")
            print("\n")
            print("""
Range es una función que viene incorporada en Python y genera una serie de números enteros, 
pudiendo pasarsele el número inicial, el número final (que no se incluye), 
y la tasa de incremento entre cada elemento.
Por ej: for i in range(2,11,2):
            print (i) (imprimirá 2,4,6,8,10)
Switch es una palabra clave reservada para la sentencia que permite seleccionar diferentes piezas de código a ejecutarse en base a un valor que actúa como condición,
así, su funcionamiento es similar al del if, 
pero brinda una mayor facilidad y legibilidad en casos donde la condición depende de valores ya conocidos de una variable.
Por ej: switch(value):
            case 1:
                print("Éste es el caso donde value vale 1")
            case 2:
                print("Esto sólo se ejecuta si value vale 2")
            case 3:
                print("Y esto si value vale 3")
                """)
            
    def exercise_10(self):
            print("4.3 Que función tiene la sentencia Breack y Continue")
            print("\n")
            print("""
Break tiene la función de detener el bucle que se está ejecutando actualmente en el scope en el que fue declarado.
Continue, en cambio, provocará que el código por debajo no se ejecute en la iteración actual, y provoque un salto a la siguiente iteración.
                """)

    def exercise_11(self):
        print("4.1 Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.  ")
        print("\n")

        try:
            number1 = int(input("Por favor, ingrese un número entero para que sea el inicio de la colección de números pares/impares:"))
            number2 = int(input("Por favor, ingrese un número entero para que sea el final de la colección de números pares/impares:"))

            even = []
            odd = []

            for i in range(number1, number2 + 1):
                if i%2 == 0:
                    even.append(i)
                else:
                    odd.append(i)

            print(f"\n Entre {number1} y {number2}: \n")
            print("Los números pares son: ", even, "\n")
            print("Los números impares son: ", odd, "\n")

        except:
            print("Por favor, debe ingresar un número.")

    def exercise_12(self):
        print("4.2 pide un número positivo al usuario una y otra vez hasta que el usuario lo haga correctamente")
        print("\n")

        number = -1
        while number < 0:
            try:
                number = int(input("Por favor, ingrese un número positivo:"))
            except:
                print("Eso no es un número.")
        print("¡Muy bien! ¡Ingresaste un número positivo!")

    def exercise_13(self):
        print("4.3 Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.")
        print("\n")

        try:
            number1 = int(input("Por favor, ingrese un número:"))
            number2 = number1 - 1

            while number1 >= number2:
                try:
                    number2 = int(input("Por favor, ingrese un número que sea mayor al primer número:"))
                except:
                    print("Por favor, sólo debe ingresar números.")

            print(f"\n ¡Muy bien! {number1} es menor que {number2}. \n")

        except:
            print("Por favor, sólo debe ingresar números.")

    def exercise_14(self):
        print("4.4  Escriba un programa que pida dos números enteros y escriba la lista de números consecutivos que hay entre ellos, de menor a mayor.")
        print("\n")

        try:
            number1 = int(input("Por favor, ingrese un número para iniciar el listado de números:"))
            number2 = int(input("Por favor, ingrese un número para finalizar el listado de números:"))

            numbers = []

            for i in range(number1 + 1, number2):
                numbers.append(i)

            print(f"\n Los números entre {number1} y {number2} son: {numbers} \n")

        except:
            print("Por favor, sólo debe ingresar números.")

    def exercise_15(self):
            print("5.1 Como se Define una función en Python, explicar la forma de manejo de los Argumentos.")
            print("\n")
            print("""
En Python una función es definida por la palabra clave "def", seguida del nombre de la función y parentesis, 
donde podrán ir opcionalmente parametros a pasarse al momento de llamar a la función:
    Por ej: def sumar(num1, num2):
                return num1+num2
Los argumentos pueden manejarse de dos formas para ser pasados a la función:
    - Como argumentos posicionales, correspondiendose su pasaje con la posición de la variable en los parametros de la declaración de la función,
    pudiendo opcionalmente tener o no un valor por defecto.
    Por ej: sumar(num1, num2=2):
                return num1+num2
            ---> sumar(1) (retornará 3)
    - Como argumentos por nombre, correspondiendose el argumento con el nombre de la variable en los parametros de la declaración de la función,
    debiendo ir primero los argumentos posicionales, de poseerlos, y luego los argumentos por nombre.
    Por ej: sumar(num1, num2=2):
                return num1+num2
            ---> sumar(1, num2=9) (retornará 10)
                """)
    
    def exercise_16(self):
            print("5.2 Definir como Python maneja el pasaje x valor y x referencia.")
            print("\n")
            print("""
En Python, los argumentos se pasan por asignación de objeto, se pasa una referencia al objeto, no una copia.
Sin embargo, el comportamiento puede parecer distinto según si el objeto es mutable o inmutable.

Para tipos inmutables como enteros, strings o tuplas, aunque se pasa una referencia, no se puede modificar el objeto original.
Por eso, si cambiamos el valor dentro de la función, simplemente estamos creando una nueva referencia local, y la original no se ve afectada.

Para tipos mutables como listas, diccionarios o sets, si modificamos sus contenidos dentro de la función 
(por ejemplo, agregando o eliminando elementos), esos cambios sí afectarán al objeto original fuera de la función.

Este comportamiento está relacionado con el concepto de mutabilidad.
Así, los tipos inmutables no se pueden cambiar, cualquier modificación crea un nuevo objeto.
En cambio, los tipos mutables pueden modificarse, y esos cambios son visibles fuera de la función.

Si queremos evitar modificar una colección original, podemos usar copy o deepcopy.
                """)

    def exercise_17(self):
            print("5.3 Definir los Argumentos “Especiales” en Python: *Args y **Kwargs en Python")
            print("\n")
            print("""
En Python, *args y **kwargs son formas de permitir que una función reciba una cantidad variable de argumentos.

*Args se utiliza para recibir cualquier número de argumentos posicionales. Dentro de la función, se accede a ellos como una tupla.

**Kwargs se usa para recibir cualquier número de argumentos nombrados (clave=valor). Dentro de la función, se accede a ellos como un diccionario.

También se pueden usar *args y **kwargs para desempaquetar listas o diccionarios al llamar una función.
                """)
            
    def exercise_18(self):
            print("5.5 Que es recursividad, que tipos de problemas soluciona, sar ejemplos.")
            print("\n")
            print("""
La recursividad aplicado al mundo de la programación nos permite resolver problemas o tareas,
donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma. 
Dado que los subproblemas a resolver son de la misma naturaleza, se puede usar la misma función para resolverlos. 
Dicho de otra manera, una función recursiva es aquella que está definida en función de sí misma, 
por lo que se llama repetidamente a sí misma hasta llegar a un punto de salida.
Por ej:
    Uno de los ejemplos mas usados para entender la recursividad, es el cálculo del factorial de un número n!. El factorial de un número n se define como la 
    multiplicación de todos sus números predecesores hasta llegar a uno. Por lo tanto 5!, leído como cinco factorial, sería 5*4*3*2*1

        def factorial_recursivo(n):
            if n == 1:
                return 1
            else:
                return n * factorial_recursivo(n-1)
        
        factorial_recursivo(5) # 120
                  
    Otro ejemplo muy usado para ilustrar las posibilidades de la recursividad, es calcular la serie de fibonacci. Dicha serie calcula el elemento n sumando los dos 
    anteriores n-1 + n-2. Se asume que los dos primeros elementos son 0 y 1.
                  
        def fibonacci_recursivo(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
                  
        fibonacci_recursivo(7) # 13
                """)
            
    def exercise_19(self):
            print("5.6 Que es una Función Lambda, que permite o facilita, de ser posible, completamente la diferencia con otros lenguajes  ")
            print("\n")
            print("""
Las funciones lambda o anónimas son un tipo de funciones en Python que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño. 
Se podría expresar en forma de una función lambda de la siguiente manera.
    lambda a, b : a + b
Lo mismo puede salvarse dicha función en una variable, y en cuyo caso actuará en su llamado igual que una función convencional con nombre.
Igualmente admite el llamado directo en la misma linea.
    (lambda a, b: a + b)(2, 4)
Así como el pasaje de argumentos posicionales, *args y **kwargs. Y permiten también retornar más de un valor.
Son útiles cuando queremos definir pequeñas funciones simples sin tener que declarar una función completa con `def`.
Facilitan la legibilidad y escritura cuando queremos crear una función que contenga una sola linea como definición, 
y que sabemos no necesitaremos reutilizar en un futuro. (o si lo hacemos podríamos almacenarla en una variable igualmente)

En comparación con otros lenguajes:
- En JavaScript hay funciones flecha ('=>'), que cumplen un propósito similar.
- En Java, C++ o C#, las funciones anónimas o expresiones lambda existen, pero su sintaxis es más extensa.
                """)
            
    def exercise_20(self):
            print("5.1 Escriba un programa que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo")
            print("\n")

            try:
                #Multiplico por 2 para mejorar legibilidad general del rectangulo
                width = int(input("Por favor, ingrese un número para la anchura del rectángulo:"))*2
                height = int(input("Por favor, ingrese un número para la altura del rectángulo:"))*2
                char = input("Por favor, ingrese el carácter con el que quiere que se dibuje el rectangulo:")

                horizontal_line = char*width
                vertical_lines = char + " "*(width -2) + char + "\n"

                print( "\n" + horizontal_line + "\n" + vertical_lines*(height - 2) + horizontal_line + "\n")

            except:
                print("Por favor, sólo debe ingresar números.")

    def exercise_21(self):
            print("5.2 Escriba un programa que pida un año y que escriba si es bisiesto o no. ")
            print("\n")

            try:
                year = int(input("Por favor, ingrese un año para verificar si es bisiesto: "))

                if year > 0:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        print(f"{year} es bisiesto.")
                    else:
                        print(f"{year} no es bisiesto.")
                else:
                    print("Por favor, debe ingresar un año válido (número entero positivo).")
            except:
                print("Por favor, debe ingresar un año válido (número entero positivo).")

    def exercise_22(self):
            print("5.3 Escriba un programa que permita crear una lista de palabras (que puede ser vacía). Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.")
            print("\n")

            try:
                number_of_words = int(input("Por favor, ingrese cuántas palabras ingresará a su lista: "))
                list_of_words = []

                if number_of_words > 0:
                    for i in range(number_of_words):
                        word = input("Por favor, ingrese la palabra número "+ str(i + 1) + ":")
                        list_of_words.append(word)

                    print("\n Su lista de palabras es: \n", list_of_words)
                else:
                    print("Por favor, debe ingresar un número válido de palabras (número entero positivo).")
            except:
                print("Por favor, debe ingresar un número válido de palabras (número entero positivo).")
                
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