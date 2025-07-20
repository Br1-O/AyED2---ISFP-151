from functools import reduce
import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.4

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("6.1 Que entiende por programación Funcional")
        print("\n")
        print("""
La programación funcional es un paradigma de programación donde el uso de funciones es prácticamente todo lo que nos ofrece el lenguaje
para elaborar nuestro código, incluso llegando a no haber bucles. Pero, así mismo, los lenguajes que soportan este paradigma suelen brindar herramientas
que faciliten la resolución de ciertos problemas, normalmente mediante funciones primitivas incluidas en el mismo lenguaje.
              """)
    
    def exercise_2(self):
        print("6.2 Que herramientas provee Python para la programación Funciona")
        print("\n")
        print("""
En el caso de Python, para ayudar en la programación funcional, provee la existencia de expresiones lambda,
así como la existencia de 3 funciones primitivas: map, filter y reduce, que pueden usarse como alternativa al uso de bucles.
              """)

    def exercise_3(self):
        print("6.3 Para que sirve la función Map, ¿que facilita o permite?")
        print("\n")
        print("""
La función map sirve para transformar los elementos contenidos en una colección o iterable, aplicandoles una función a cada uno.
Al finalizar de iterar sobre todos los elementos y transformarlos, 
la función map retornará una nueva colección que contendrá a esos nuevos elementos resultantes de la transformación.
Por ej:
    lista = [1, 2, 3, 4, 5]
    lista_pordos = map(lambda x: 2*x, lista)
    print(list(lista_pordos))
    # [2, 4, 6 , 8, 10 ]
              """)

    def exercise_4(self):
        print("6.4 ¿Que utilidad tiene la Función Filter?, como se realizaría en estructurado?")
        print("\n")
        print("""
La función filter permite aplicar una función a una colección o iterable,
pero dicha función deberá retornar un booleano. 
Así, filter iterará sobre dicho iterable, aplicará la función a cada elemento, 
e ira agregando cada elemento a una lista nueva sólo si el resultado, tras aplicarle la función, es True.
En otras palabras, filtrará a los elementos entre los que cumplen o no con la condición creada por la función que se le pasa para aplicar a cada elemento.
Por ej:
    lista = [7, 4, 16, 3, 8]
    pares = filter(lambda x: x % 2 == 0, lista)
    print(list(pares))
    # [4, 16, 8]
En un paradigma estructura esa misma funcionalidad debería aplicarse mediante un if estableciendo en él la condición a cumplirse.
Por ej:
    lista = [7, 4, 16, 3, 8]
    def getEvenNums(numbers):
        even = []
        for number in numbers:
            if number%2 == 0:
              even.append(number)  
        return even
    print(getEvenNums(lista))
    # [4, 16, 8]
              """)

    def exercise_5(self):
        print("6.5 ¿Que permite la Función Reduce en Python?")
        print("\n")
        print("""
La función Reduce en Python permite reducir todos los elementos de una colección o iterable a un solo valor.
Para esto se le pasará a la función Reduce, además del iterable,
también una función que permita juntar el valor de todos los elementos en un solo elemento en base a un criterio determinado.
Por ej:
    from functools import reduce
    lista = [1, 2, 3, 4, 5]
    suma = reduce(lambda acc, val: acc + val, lista)
    print(suma) # 15
              """)

    def exercise_6(self):
        print("6.6  Explicar el Siguiente Código de Ejemplo de programación Funcional")
        print("\n")
        print("""
    from functools import reduce 
    ●  personas = [ 
    ●      {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'}, 
    ●      {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'}, 
    ●      {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'}, 
    ●      {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'}, 
    ●      {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'}, 
    ●      {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'}, 
    ●  ] 
    ●  hombres = list(filter(lambda x: x['Sexo'] == 'M', personas)) 
    ●  suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0) 
    ●  media_edad = suma_edades/(len(hombres)) 
    ●  print(media_edad) # 33.0
              
    El código muestra cómo se útiliza en la variable hombres la función filter para seleccionar a todas las personas de la lista 'personas' que tengan sexo 'M'.
    Una vez creada la nueva lista de sólo hombres, en la variable suma_edades se utiliza la función reduce, para sumar todas las edades del listado de hombres.
    Y luego, en media_edad, se utilizar esa suma de edades para dividirla por la cantidad de hombres en el listado, para así conseguir el promedio de sus edades.
    Finalmente sólo se imprime el resultado por consola mediante la función print.
              """)
        
    def exercise_7(self):
        print("6.7 De ser Posible comparar con C++")
        print("\n")
        print("""
En C++, al ser más imperativo/estructurado, no posee estas funciones de orden superior por defecto.
Por lo cual se optaría a realizar las mismas funcionalidades mediante el uso de un bucle que itere sobre el listado de personas, 
y en su interior un condicional para afectar sólo a las personas con sexo 'M' del listado.
Y luego sólo sumaría las edades de las personas que respondan con dicha caracteristica, 
almacenandola en una variable para luego dividirla por la extensión del listado.
Y para finalizar sólo se mostraría el resultado por consola.
Es decir, sólo se usarían bucles y condionales para crear nosotros mismos la implementación,
o nuestra propia versión de ella, de cada una de estas funciones ya incluidas en paradigmas funcionales.
                """)
            
    def exercise_8(self):
        print("6.1 Obtener el cuadrado de todos los elementos en la lista.")
        print("\n")
        numbers = [1,2,3,4,5,6,7,8,9,10]
        print("Los números de la lista son: ", numbers, "\n")
        print("El cuadrado de esos números es: ", list(map(lambda x: x*x, numbers)))

    def exercise_9(self):
        print("6.2 Obtengamos la cantidad de elementos mayores a 5 en una tupla.")
        print("\n")
        numbers = (1,2,3,4,5,6,7,8,9,10,50,100,25000)
        print("Los números de la tupla son: ", numbers, "\n")
        print("La cantidad de números mayores a 5 son: ", len(list(filter(lambda x: x>5, numbers))))

    def exercise_10(self):
        print("6.3 Obtengamos la cantidad de elementos mayores a 5 en una tupla, usando Reduce")
        print("\n")
        numbers = (1,2,3,4,5,6,7,8,9,10,50,100,25000)
        print("Los números de la tupla son: ", numbers, "\n")
        print("La cantidad de números mayores a 5 son: ", reduce(lambda acc, x: acc+(1 if x>5 else 0), numbers, 0))

    def exercise_11(self):
        print("7.1 Que es una Excepción, que significa “Lanza” una Excepción y “Capturarla”")
        print("\n")
        print("""
Una Excepción es una clase en Python que está diseñada para representar errores posibles a lo largo de la ejecución de un programa,
los cuales de suceder detendrían la ejecución del mismo. 
"Lanzar" una excepción significa que esa pieza de código provocará la creación de una instancia de estas excepciones,
causando la interrupción del programa.
"Capturar" una excepción es el acto de contener esa instancia de la excepción, al encerrar la pieza de código que podría provocarla entre bloques try/except,
evitando así la interrupción del programa, y en su lugar ejecutando el código contenido en el bloque except que hemos declarado.
                """)

    def exercise_12(self):
        print("7.2 Complementar con ejemplos de TypeError, KeyError, IndexError, NameError, RuntimeError, ZeroDivisionError")
        print("\n")
        print("""
- TypeError
Ocurre cuando se usa un tipo de dato inapropiado en una operación o función.

    x = "5"
    y = 2
    print(x + y)  # TypeError: can only concatenate str (not "int") to str
              
- KeyError
Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.

    person = {"nombre": "Ana", "edad": 30}
    print(person["altura"])  # KeyError: 'altura'

- IndexError
Se produce al acceder a un índice inexistente en una lista, tupla, etc.

    numeros = [1, 2, 3]
    print(numeros[5])  # IndexError: list index out of range

- NameError
Se lanza cuando se intenta usar una variable que no fue definida.

    print(nombre)  # NameError: name 'nombre' is not defined

- RuntimeError
Se produce cuando ocurre un error que no entra específicamente en otras categorías, pero que ocurre en tiempo de ejecución.

    import threading

    def tarea():
        print("Hola desde un hilo")

    hilo = threading.Thread(target=tarea)
    hilo.start()

    # Intentamos iniciar el mismo hilo otra vez (esto no está permitido)
    hilo.start()

- ZeroDivisionError
Ocurre al intentar dividir un número entre cero.

    x = 5
    y = 0
    print(x / y)  # ZeroDivisionError: division by zero
                """)

    def exercise_13(self):
        print("7.3 Que utilidad tiene la palabra Raise.")
        print("\n")
        print("""
La palabra reservada Raise se utiliza para provocar una excepción del tipo especificado, 
opcionalmente pudiendo pasarle un mensaje personalizado para informar qué sucedió a quien lo lea.
Por ej:
    def sumar(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a y b tienen que ser números enteros.")
        return a + b
Así mismo podremos provocar excepciones personalizadas creadas por nosotros, siempre y cuando creemos una clase que herede de Exception para ello.
Por ej:
    class InvalidUser(Exception):
    pass
                """)
    
    def exercise_14(self):
        print("7.1 Crear una Función que divia hasta cero, ej: dividir(27,0), verificar: ZeroDivisionError")
        print("\n")
        def div():
            while True:
                try:
                    num = int(input("Por favor, ingrese un número a ser dividido: "))
                    div = int(input("Por favor, ingrese el divisor de la operación: "))
                    return num/div
                except ZeroDivisionError:
                    print("¡No se puede dividir por cero!")
                except ValueError:
                    print("¡Sólo se pueden dividir números!")
        print(div())

    def exercise_15(self):
        print("7.2 llamar a la función mas_10() con cualquier número, además: add_10('cinco') verificar TypeError")
        print("\n")
        def mas_10():
            while True:
                try:
                    num = input("Por favor, ingrese un número para agregarle 10: ")
                    if num.isdigit():
                        num = int(num)
                    else: 
                        raise(TypeError)
                    return num+10
                except TypeError:
                    print("¡Por favor, sólo ingrese números!")
        print(mas_10())
            
    def exercise_16(self):
        print("7.3 Crear una Lista e Iterar mas allá del limite del Index, verídica: IndexError")
        print("\n")
        nums = [1,2,3,4,5,6,7,8,9,10]
        print("La lista de números es: ", nums)
        
        while True:
            try:
                index = int(input("Ingrese el indice del número que desea mostrar: "))
                print("El número en el indice",index, "es:",nums[index])
                break
            except IndexError:
                print("El elemento que desea mostrar no existe en la lista. Por favor, ingrese un indice válido.")
            except ValueError:
                print("¡El indice debe ser un número!")
            
    def exercise_17(self):
            print("7.3 Crear un Diciconario en Python y buscar una clave Inexistente, verificar keyError:")
            print("\n")
            nums = {"num1": 1, "num2": 2, "num3": 3, "num4": 4, "num5": 5, "num6": 6, "num7": 7, "num8": 8, "num9": 9, "num10": 10}
            print("El diccionario de números es: ", nums)
            
            while True:
                try:
                    key = input("Ingrese la clave del número que desea mostrar: ")
                    print("El número con clave",key, "es:",nums[key])
                    break
                except KeyError:
                    print("Esa clave no existe en el diccionario. Por favor, ingrese una clave válida.")
            
    def exercise_18(self):
        print("8.1 Explicar las Funciones Open() y Close() de Python.")
        print("\n")
        print("""
Open() en Python permite la apertura de un archivo, pasandosele como primer parametro el path del archivo, ya sea relativo o absoluto;
y como segundo parametro el modo de apertura de dicho archivo (pudiendo ser lectura, escritura, sobre escritura total, 
o una combinación de ambas, así como modalidad de archivos binarios para windows)
Close() es su contraparte, y permite cerrar el archivo para finalizar su uso y guardar los cambios que se realizaron, de haberse realizado alguno.
Es buena práctica siempre cerrar un archivo tras abrirlo, pues sino estariamos gastando recursos sin sentido, 
y de hacerlo a lo largo del programa podríamos provocar malos funcionamientos así como conductas inesperadas al manipular el archivo.
            """)

    def exercise_19(self):
        print("8.2 Explicar los distintos “Modos” de Apertura")
        print("\n")
        print("""
Los modos de apertura son el segundo argumento que puede pasarsele a la función Open() de la API de Python para manejo de archivos.
Los modos de apertura son: 
■ "w" para write, permitiendo sobre escribir por completo el antiguo contenido de un archivo con el nuevo contenido que escribamos, 
o crear un archivo si no existía ya.
■ "r" para read, permitiendo leer el contenido de un archivo.
■ "a" para append, permitiendo escribir en un archivo, pero sin sobre escribir el contenido existente, sino agregando el nuevo contenido al final.
Y no creará el archivo si éste no existe previamente.
■ "w+", "r+", "a+" amplian las combinaciones para que puedan leer y escribir al mismo tiempo, manteniendo sus caracteristicas principales.
(cabe aclarar que el método de escritura que implementa "r+" no sobreescribe todo el archivo como el modo "w", sino que sobreescribe desde el inicio,
CONSERVANDO el resto del archivo intacto. Así mismo no creará el archivo si no existe previamente.)
■ "wb", "rb", "ab" son los mismos modos pero aplicados a archivos de tipo binario, útilizado sólo en windows, 
donde existe tal distinción entre archivos comunes y archivos binarios. Conservan las mismas caracteristicas y funcionalidades que los modos anteriores.
            """)

    def exercise_20(self):
        print("8.3 Definir y dar Ejemplos de seek(), readline() y readlines()")
        print("\n")
        print("""
El método seek() sirve para mover el cursor a una determinada posición de caracter, 
y a partir de esa posición empezar a manejar el archivo.
Por ej:
    with open("path.txt") as f:
        f.seek(30)
        f.read() (leerá desde el carácter número 30 en nuestro archivo)
              
El método readline() leerá una linea por vez, manteniendo el cursor al inicio de la siguiente linea. 
Los saltos de carrusel serán los que delimiten dónde termina cada linea.
Por ej:
    with open("path.txt") as f:
        print(f.readline()) (muestra la primera linea)
              
El método readlines() permite leer todas las lineas de un archivo, representando así la totalidad de dicho archivo, 
pero representado como un conjunto de lineas sucesivas en una lista de strings.
Por ej:
    with open("path.txt") as f:
        print(f.readlines()) (mostrará todo el archivo como una lista, cuyos elementos son cada una de las lineas del archivo)
""")
        
    def exercise_21(self):
        print("8.1 Crear un programa que abra un fichero en modo lectura y escritura, si no existe lo creará, y añadir la frase 'Estoy aprendiendo Python'")
        print("\n")
        f = open("ejemplo_ejercicio_21.txt", "w+")
        f.write("Estoy aprendiendo Python")
        f.seek(0)
        print(f.read())
        f.close()
            
    def exercise_22(self):
        print("8.2 Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero, el modo en el que fue abierto, el nombre y la codificación de caracteres del mismo.")
        print("\n")
        f = open("ejemplo_ejercicio_21.txt", "r")
        print("Texto: ", f.read())
        print("Modo de apertura: ", f.mode)
        print("Nombre del archivo: ", f.name)
        print("Codificación: ", f.encoding)
        f.close()

    def exercise_23(self):
        print("8.3 Realizar un programa que realice los ejercicios 1 y 2 utilizando la estructura with.")
        print("\n")
        with open("ejemplo_ejercicio_21.txt", "w+") as f:
            f.write("Estoy aprendiendo Python")
            f.seek(0)

            print("Texto: ", f.read())
            print("Modo de apertura: ", f.mode)
            print("Nombre del archivo: ", f.name)
            print("Codificación: ", f.encoding)

    def exercise_24(self):
        print("9.1 Definir y relacionar los Conceptos de Módulos y Paquetes.")
        print("\n")
        print("""
Un módulo es una unidad de software que provee una funcionalidad, y así podemos exportar librerias como módulos para utilizarlas en nuestro código,
o dividir nuestro programa en diferentes módulos para facilitar la utilización de recursos y mejorar la administración de archivos, mantenibilidad y reutilización.
En cambio, un paquete es un archivo o carpeta que puede contener uno o más módulos.
            """)

    def exercise_25(self):
        print("9.2 Que función tiene sys.path()")
        print("\n")
        print("""
La función que tiene sys.path() es la de permitirnos ver las rutas contenidas en nuestro path, que es donde nuestro programa buscará todos los módulos importados.
Así mismo, si queremos agregar una nueva ruta podremos hacerlo mediante sys.path().append(r"ruta/del/modulo"), 
permitiendole así a nuestro programa saber de dónde importar los módulos que deseamos importar.
            """)

    def exercise_26(self):
        print("9.3 Por qué usaría “AS” para cambiar o poner alias a paquetes en Python.")
        print("\n")
        print("""
Usaría "as" para cambiar o poner alias a paquetes en Python al importarlos para fácilitar su uso a lo largo de mi programa,
pues puedo poner "m" a un módulo que posea un nombre muy largo, como "módulo_de_nombre_muy_largo". Y así podré usar sus clases y funciones mediante:
    m.función()
En lugar de tener que usar el nombre completo siempre.
Además esto ayuda a la legibilidad de nuestro código, al evitar verbosidad excesiva innecesaria.
""")
    
    def exercise_27(self):
        print("9.4 ¿Como maneja Python las Excepciones al Importar Módulos?")
        print("\n")
        print("""
Importar un módulo puede lanzar una excepción, cuando se intenta importar un módulo que no ha sido encontrado. 
Se trata de ModuleNotFoundError.
Por ej:
    import moduloquenoexiste
    # ModuleNotFoundError: No module named 'moduloquenoexiste'
Dicha excepción puede ser capturada para evitar la interrupción del programa.
Por ej:
    try:
        import moduloquenoexiste
    except ModuleNotFoundError as e:
        print("Hubo un error:", e)
            """)

    def exercise_28(self):
        print("9.5 Como maneja Python la inclusión Multiple de  Módulos")
        print("\n")
        print("""
En Python la inclusión de módulos se realiza una sola vez mediante import, si realizamos otros imports tras ese, 
el módulo no será nuevamente incluido. En cambio, si lo que deseamos es recargar el módulo para que se actualice el import, 
debemos declararlo mediante importlib.reload("nombre_de_modulo").
""")
        
    def exercise_29(self):
        print("9.1: Hacer un paquete simple")
        print("\n")
        print("""
Ver Estructura de carpetas.
""")
            
    def exercise_30(self):
        print("9.2: Crear un directorio de aplicaciones")
        print("\n")
        print("""
Ver Estructura de carpetas.
""")

    def exercise_31(self):
        print("9.3: Scripts de nivel superior")
        print("\n")
        print("""
Ver directorioAplicacionesEjemplo -> main.
""")
        
    def exercise_32(self):
        print("10.1 ¿Que entiende x Testing?")
        print("\n")
        print("""
Se entiende por Testing a realizar pruebas sobre nuestro código, asegurandonos de que la funcionalidad que brinda, es decir, los resultados que produce,
coinciden con lo esperado. Para hacerlo podemos probar nuestro código manualmente, o automatizar pruebas que lo comprueben por nosotros.
            """)

    def exercise_33(self):
        print("10.2¿Que diferencia tenemos entre Test Manual y Automático?")
        print("\n")
        print("""
Se diferencian en que:
El Test Manual es aquel realizado por una persona, que ingresa datos de forma manual, comprobando que los resultados retornados por la función,
o las acciones provocadas por ella, son las esperables en base a los datos ingresados. Es más lento y dedende integramente del criterio humano.
En cambio, el Test Automático es aquel que realiza otro programa o función, para comprobar el código que le ingresamos. Así, 
chequeará de forma automatica si la función ingresada retorna y se comporta de forma esperable en base a los resultados que se le proveyeron 
para realizar la comprobación. El Test Automático es más rápido y fiable, pero no todas las funciones o códigos son automatizables para su comprobación,
como sucede con GUIs o efectos visuales.
""")
    
    def exercise_34(self):
        print("10.3¿Que es un Assert en Test Automaticos?")
        print("\n")
        print("""
Un assert es una función que fácilita el realizar tests automaticos. Recibirá 2 argumentos, la función a ser testeada, 
y el resultado esperado por parte de la función para el valor de argumentos que se le pasaron en la declaración.
Por ej:
    assert(suma([3, 7, 5]) == 15)
    assert(suma([30, 0]) == 30)
En caso de alguna declaración de assert comprobar que la función no haya coincidido con el valor esperado, 
entonces provocará una excepción de tipo AssertionError, 
para facilitarnos ver que los tests no han sido exitosos y que debemos modificar algo en nuestro código antes de lanzarlo a producción.
            """)

    def exercise_35(self):
        print("10.4 Que es unittest, como se Implementa en Python?")
        print("\n")
        print("""
Para facilitar el implementar tests en nuestro código podemos usar librerías, que brindarán funcionalidades extras para realizar tests.
Una librería que podemos usar para estoy en Python es unittest. 
Esta libreria trae múltiples clases, métodos y funciones para que podamos realizar nuestras pruebas de una forma más simple y completa.
Para usarla en Python podremos hacer algo como esto:
    ■ Creamos una clase Test<NombreDeLoQueSePrueba> que hereda de unittest.TestCase.
              
    ■ Definimos varios tests como métodos de la clase, usando test_<NombreDelTest> para nombrarlos.
              
    ■ En cada test ejecutamos las comprobaciones necesarias, usando assertEqual en vez de assert, pero su comportamiento es totalmente análogo.

    Por ej:
                 
        # tests.py
        from funciones import calcula_media
        import unittest
        class TestCalculaMedia(unittest.TestCase):
            def test_1(self):
                resultado = calcula_media([10, 10, 10])
                self.assertEqual(resultado, 10)
            def test_2(self):
                resultado = calcula_media([5, 3, 4])
                self.assertEqual(resultado, 4
              
    ■ Por otro lado, usando -v podemos obtener más información sobre cada test ejecutado con su resultado 
    individualmente. Si tenemos gran cantidad de tests suele ser recomendable usarla, ya que será más fácil 
    localizar los tests que han fallado.
    $ python -m unittest -v tests
              
    ■ Por último, si tenemos varios ficheros de test, podemos usar discover, para decirle a Python que busque en 
    la carpeta todos los tests y los ejecute.
    $ python -m unittest discover -v

    ■ Otras funcionalidades para realizar tests automaticos en unittest son:
        .assertEqual(a, b): Verifica la igualdad de ambos valores.
        .assertTrue(x): Verifica que el valor es True.
        .assertFalse(x): Verifica que el valor es False.
        .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
        .assertIsNone(x): Verifica que el valor es None.
        .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
        .assertIsInstance(a, b): Verifica que a es una instancia de b
        .assertRaises(x): Verifica que se lanza una excepción
""")
        
    def exercise_36(self):
        print("""
        10.5 Explicar el Siguiente Codigo: 
        
        # funciones.py 
            def calcula_media(*args): 
                    return(sum(*args)/len(*args)) 
              
        # tests.py 
        from funciones import calcula_media 
        import unittest 
        class TestCalculaMedia(unittest.TestCase): 
            def test_1(self): 
                resultado = calcula_media([10, 10, 10]) 
                self.assertEqual(resultado, 10) 
            def test_2(self): 
                resultado = calcula_media([5, 3, 4]) 
                self.assertEqual(resultado, 4) 
        if __name__ == '__main__': 
            unittest.main()
        """)
        print("\n")
        print("""
El código está realizando un test automático mediante unittest.
Crea una clase siguiendo las convenciones de nombre (Test+NombreDeLaFuncionalidadATestear), 
y hace que herede de unittest.TestCase, que es la clase incluida en la libreria para englobar casos de prueba.
Luego a eso define los diferentes test, nuevamente siguiendo las convenciones de nombre para cada uno de los métodos.
En los test usa assertEqual para comparar la función con determinados argumentos, 
así como el resultado esperado para dicha función implementada de esa forma.
Por último limita la ejecución de funciones al archivo main del programa de testing.
""")
            
    def exercise_37(self):
        print("""
10.6  Realizar una Breve descripcion de las siguientes funciones de UnitTes: 
    .assertEqual(a, b): Verifica la igualdad de ambos valores. 
    .assertTrue(x): Verifica que el valor es True. 
    .assertFalse(x): Verifica que el valor es False. 
    .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is). 
    .assertIsNone(x): Verifica que el valor es None. 
    .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in). 
    .assertIsInstance(a, b): Verifica que a es una instancia de b 
    .assertRaises(x): Verifica que se lanza una excepción. 
""")
        print("\n")
        print("""
.assertEqual(a, b): Verifica que a == b. Falla si los valores son diferentes.

.assertTrue(x): Verifica que x sea True. Falla si es False.

.assertFalse(x): Verifica que x sea False. Falla si es True.

.assertIs(a, b): Verifica que a y b sean el mismo objeto (mismo id()), usando el operador is.

.assertIsNone(x): Verifica que x sea None.

.assertIn(a, b): Verifica que a se encuentre dentro del iterable b (como usar a in b).

.assertIsInstance(a, b): Verifica que el objeto a sea una instancia de la clase o tipo b.

.assertRaises(x): Verifica que se lance una excepción del tipo x cuando se ejecuta el código que se le pase. Se puede usar con with:
    with self.assertRaises(ZeroDivisionError):
    1 / 0
""")

    def exercise_31(self):
        print("10.7  Que permite Usando setUp y tearDown en UnitTest? ")
        print("\n")
        print("""
En UnitTest setUp permite definir una función que se ejecutará siempre al inicio de todo test que realicemos, 
permitiendonos poner en ella todas las condiciones necesarias para establecer correctamente nuestro entorno de prueba.
Mientras que tearDown permite definir una función que se ejecutará siempre al final de todo test que realicemos, 
permitiendonos limpiar en ella todas las condiciones que creamos al inicio para manejar nuestro entorno, mediante setUp.
""")
        
    def exercise_31(self):
        print("""
10.1 Explicar el Siguiente Código: 
    import unittest 
    class TestEjemplos(unittest.TestCase): 
        def setUp(self): 
            print("Entra setUp") 
        def tearDown(self): 
            print("Entra tearDown") 
        def test_1(self): 
            print("Test: test_1") 
        def test_2(self): 
            print("Test: test_2")  
    python -m unittest -v tests
    """)
        print("\n")
        print("""
Al igual que antes, establece una clase para realizar pruebas automatizadas mediante unittest, estableciendo que la clase hereda de unittest.TestCase,
pero esta vez además se establece una función setUp y otra TearDown, para que se ejecuten al inicio y final de los 2 tests establecidos.
Así, el resultados de ambos test tendrá además de su propio print, "Entra setUp" al inicio y "Entra tearDown" al final.
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