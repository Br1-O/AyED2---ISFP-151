import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 5

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1. ¿Qué entiende por memory leak?")
        print("\n")
        print("""
Una memory leak o pérdida de memoria ocurre cuando un programa reserva memoria dinámica y luego no la libera correctamente cuando deja de necesitarla.

En C++, esto puede suceder, por ejemplo, cuando se utiliza new para reservar memoria y se pierde la posibilidad de acceder a esa dirección sin ejecutar el delete correspondiente. Como consecuencia, esa memoria continúa ocupada aunque el programa ya no pueda utilizarla.

Al principio, una pequeña pérdida puede pasar inadvertida, pero si se repite o se acumula con el tiempo puede provocar un rendimiento deficiente e incluso que la aplicación se quede sin memoria y se bloquee. También puede afectar a otras aplicaciones que se ejecutan en el sistema.

Por eso, las pérdidas de memoria son errores sutiles y difíciles de detectar que deben prevenirse mediante una correcta administración de los recursos.
              """)

    def exercise_2(self):
        print("2. ¿Qué es el patrón RAII y qué resuelve?")
        print("\n")
        print("""
RAII (Resource Acquisition Is Initialization, o adquisición de recursos es inicialización) es un patrón de diseño utilizado en C++ que vincula el ciclo de vida de un recurso con el ciclo de vida de un objeto.

Consiste en adquirir el recurso durante la inicialización del objeto, generalmente en su constructor, y liberarlo automáticamente cuando el objeto se destruye, mediante su destructor. De esta manera, no es necesario recordar liberar manualmente el recurso en cada posible camino de ejecución.

RAII puede utilizarse para administrar memoria dinámica, archivos, sockets, bloqueos de exclusión mutua e hilos, entre otros recursos.

¿Qué problemas resuelve?
- Evita pérdidas de memoria al liberar automáticamente la memoria cuando el objeto sale de ámbito.
- Evita dejar bloqueos activos: por ejemplo, una clase como std::scoped_lock bloquea el mutex al construirse y lo desbloquea al destruirse, incluso si se produce una excepción o un retorno anticipado.
- Permite administrar otros recursos, como archivos o hilos, sin depender de que el programador recuerde ejecutar manualmente las operaciones de limpieza.

En síntesis, RAII concentra la adquisición y liberación de un recurso en un mismo objeto y hace que la limpieza sea automática y segura.
              """)

    def exercise_3(self):
        print("3. ¿Qué es el Principio de Exclusión Mutua?")
        print("\n")
        print("""
El principio de exclusión mutua establece que, cuando varios hilos de ejecución pueden acceder a un mismo recurso o sección crítica, el acceso debe coordinarse para evitar que más de un hilo la utilice simultáneamente cuando esa operación no es segura.

En C++, esto puede implementarse mediante un mutex (mutual exclusion). Un hilo adquiere el bloqueo antes de entrar en la sección crítica y los demás deben esperar hasta que el bloqueo sea liberado. Así se evita que varios hilos modifiquen al mismo tiempo un recurso compartido y provoquen inconsistencias o condiciones de carrera.

El bloqueo puede realizarse manualmente con lock() y unlock(), pero este enfoque es propenso a errores: si se olvida desbloquear el mutex o se produce una excepción antes de llamar a unlock(), otros hilos pueden quedar bloqueados indefinidamente.

Por eso se recomienda utilizar mecanismos RAII como std::scoped_lock, que adquiere el bloqueo al inicializarse y lo libera automáticamente cuando el objeto sale de ámbito, incluso ante una excepción.
              """)

    def exercise_4(self):
        print("4. ¿Qué entiende por excepción?")
        print("\n")
        print("""
Una excepción es un evento u objeto que se produce y se lanza durante la ejecución de un programa para señalar una situación excepcional o un error que puede ser tratado.

En C++, las excepciones permiten separar el flujo normal del programa del tratamiento de errores. Las excepciones estándar derivan de std::exception, aunque también se pueden definir excepciones propias.

Por ejemplo, una división por cero puede detectarse antes de realizar la operación y provocar el lanzamiento de una excepción mediante throw. Luego, un bloque catch puede recibirla y realizar el tratamiento correspondiente.

Si una excepción no es capturada por un controlador compatible, el programa puede finalizar. Por eso, el manejo de excepciones permite reaccionar ante errores en tiempo de ejecución y mantener el flujo de la aplicación cuando existe una forma adecuada de recuperarse.
              """)

    def exercise_5(self):
        print("5. Explicar try, catch y throw dentro del ciclo de vida de una excepción.")
        print("\n")
        print("""
En C++, try, catch y throw son las palabras clave principales para trabajar con excepciones:

- try: delimita el bloque de código en el que puede producirse una excepción.
- throw: lanza una excepción cuando se detecta una situación excepcional. Puede lanzar un objeto o valor que represente el error.
- catch: define un controlador que recibe y trata una excepción del tipo correspondiente.

El ciclo de vida de una excepción se puede describir en las siguientes etapas:

1. Se produce y se lanza la excepción: ocurre un error o una condición excepcional y se ejecuta throw.
2. La excepción queda activa y se desenrolla la pila (stack unwinding): las funciones se abandonan antes de tiempo y se ejecutan los destructores de los objetos locales que se encuentran en la pila.
3. Se captura la excepción: al llegar a un bloque try con un catch compatible, se ejecuta el primer controlador que coincide con el tipo de la excepción.
4. Se trata o se traduce la excepción: el controlador puede resolver el error o, cuando corresponde, lanzar otra excepción. Si no existe un catch compatible, la excepción continúa propagándose hacia las funciones anteriores.

Ejemplo:

    try {
        if (divisor == 0) {
            throw std::runtime_error("No se puede dividir por cero");
        }
        resultado = dividendo / divisor;
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }

En este ejemplo, throw lanza la excepción, try contiene la operación que puede fallar y catch recibe el error para tratarlo.
              """)

    def exercise_6(self):
        print("6. Comparar RAII vs. excepciones. ¿Cuándo usar cada uno?")
        print("\n")
        print("""
RAII y las excepciones no son mecanismos que se contradigan; se complementan y cumplen funciones diferentes.

RAII:
- Se utiliza para administrar recursos y responsabilidades.
- Adquiere un recurso en el constructor de un objeto y lo libera en su destructor.
- Realiza la limpieza automáticamente al salir del ámbito, tanto en una ejecución normal como cuando se produce una excepción.
- Es apropiado para memoria dinámica, archivos, mutexes y otros recursos que necesitan liberación o restauración.

Excepciones:
- Se utilizan para comunicar y tratar errores que ocurren durante la ejecución.
- throw permite lanzar el error, try delimita el código que puede producirlo y catch permite capturarlo.
- Conviene capturarlas en el punto donde se dispone de información suficiente para actuar sobre el error, por ejemplo, para registrarlo, recuperarse o traducirlo en el límite de una biblioteca.

¿Cuándo utilizar cada uno?
Se debe utilizar RAII siempre que exista un recurso o estado que necesite una limpieza o liberación, independientemente de que el código utilice excepciones. Se deben utilizar excepciones para comunicar y tratar situaciones de error cuando sea posible tomar una acción adecuada.

No es recomendable utilizar bloques try/catch únicamente para liberar recursos y volver a lanzar la excepción. Esa limpieza debe quedar a cargo de destructores de objetos RAII. De esta forma, RAII garantiza la limpieza y las excepciones se ocupan del manejo de errores.
              """)

    def exercise_7(self):
        print("7. Describir punteros vs. referencias y realizar una comparativa de sus usos.")
        print("\n")
        print("""
Tanto los punteros como las referencias permiten acceder indirectamente a otra variable u objeto, pero tienen diferencias importantes.

Punteros (*):
Un puntero es una variable que almacena la dirección de memoria de otra variable. Para acceder al valor apuntado se utiliza el operador de desreferencia (*), y para acceder a los miembros de un objeto se puede utilizar el operador flecha (->).

Referencias (&):
Una referencia es un alias o nombre alternativo para una variable que ya existe. Debe inicializarse al declararse y, una vez creada, no puede reasignarse para referirse a otro objeto. Se utiliza como si fuera la variable original, sin necesitar un operador de desreferencia.

Comparativa:

1. Inicialización:
   - Puntero: puede declararse sin inicializar y asignársele una dirección posteriormente.
   - Referencia: debe inicializarse en el momento de su declaración.

2. Nulidad:
   - Puntero: puede ser nullptr para indicar que no apunta a un objeto válido.
   - Referencia: no debe ser nula; debe referirse a un objeto existente.

3. Reasignación:
   - Puntero: puede cambiar la dirección a la que apunta.
   - Referencia: no puede cambiar el objeto al que está asociada.

4. Acceso:
   - Puntero: requiere desreferenciar con * o utilizar -> para acceder a miembros.
   - Referencia: se utiliza directamente con el nombre de la referencia y el operador . para acceder a miembros.

5. Niveles de indirección:
   - Puntero: permite múltiples niveles, como punteros dobles (**) o triples (***).
   - Referencia: no permite encadenar niveles de indirección de esa manera.

6. Seguridad y usos:
   - Puntero: es más flexible y resulta útil cuando la ausencia de un objeto es válida, cuando se necesita cambiar el objeto apuntado o para construir estructuras dinámicas como listas enlazadas y árboles.
   - Referencia: suele ser más sencilla y segura cuando se necesita acceder a un objeto existente, modificarlo desde una función o evitar copiar objetos grandes.

Ejemplos de uso de referencias:
- Pasar parámetros por referencia, como en una función swap(), para que los cambios se reflejen en las variables originales.
- Pasar objetos grandes mediante const referencia para evitar copias innecesarias.
- Recorrer contenedores con referencias para modificar sus elementos o evitar copiar objetos.

En general, conviene utilizar referencias cuando el objeto debe existir y no se necesita cambiar el destino; los punteros son adecuados cuando se requiere esa flexibilidad adicional.
              """)

    def exercise_8(self):
        print("8. ¿Cómo evitar la pérdida de memoria?")
        print("\n")
        print("""
Para evitar las pérdidas de memoria en C++ se recomienda reducir al mínimo la administración manual de memoria y utilizar mecanismos que liberen los recursos automáticamente.

Algunas buenas prácticas son:

1. Utilizar punteros inteligentes cuando corresponda, ya que administran automáticamente la vida útil de los objetos.
2. Preferir std::string en lugar de cadenas de caracteres administradas mediante char*, porque std::string controla internamente la memoria.
3. Utilizar contenedores de la biblioteca estándar, como std::vector, en lugar de reservar y liberar manualmente arreglos dinámicos cuando sea posible.
4. Evitar los punteros sin formato para administrar la propiedad de memoria, salvo cuando sea necesario interactuar con bibliotecas antiguas o interfaces que los requieran.
5. Evitar el uso directo de new y delete en el código de aplicación. Cuando se necesite memoria dinámica, conviene encapsularla dentro de objetos RAII o utilizar funciones como std::make_unique y std::make_shared.
6. Vincular la liberación del recurso con el fin del ámbito del objeto, de modo que su destructor se encargue de la limpieza.

La idea principal es que la memoria dinámica quede administrada por objetos que garanticen su liberación automática, en lugar de depender de que el programador recuerde ejecutar delete en todos los caminos posibles.
              """)

    def exercise_9(self):
        print("9. ¿Qué son los punteros inteligentes y qué problema solucionan?")
        print("\n")
        print("""
Los punteros inteligentes (smart pointers) son clases de la biblioteca estándar de C++ que administran automáticamente la memoria dinámica y la vida útil de los objetos a los que apuntan.

A diferencia de un puntero sin formato, un puntero inteligente incorpora reglas de propiedad y utiliza RAII: cuando el objeto que administra el recurso se destruye o deja de ser propietario, se ejecuta la liberación correspondiente.

Su principal objetivo es evitar errores de administración manual de memoria, especialmente las pérdidas de memoria ocasionadas por olvidar delete. También ayudan a controlar quién es responsable de un objeto y durante cuánto tiempo debe permanecer vivo.

Los tres tipos principales son std::unique_ptr, std::shared_ptr y std::weak_ptr. Cada uno representa un modelo de propiedad diferente: exclusiva, compartida y temporal/no propietaria, respectivamente.
              """)

    def exercise_10(self):
        print("10. Describir los 3 tipos de punteros inteligentes.")
        print("\n")
        print("""
1. std::unique_ptr:
Representa la propiedad exclusiva de un recurso. Solo un unique_ptr puede ser propietario de ese objeto a la vez. No se puede copiar, pero sí mover mediante std::move, transfiriendo la propiedad al nuevo puntero. Cuando el unique_ptr se destruye o deja de ser propietario, libera automáticamente el recurso.

Se utiliza cuando un objeto debe tener un único propietario. Para crearlo se recomienda std::make_unique.

2. std::shared_ptr:
Representa la propiedad compartida de un recurso. Varias instancias de shared_ptr pueden administrar el mismo objeto mediante un bloque de control que mantiene un contador de referencias. Al copiar un shared_ptr, el contador aumenta; al destruirlo o dejar de ser propietario, disminuye. Cuando el contador llega a cero, el objeto se libera automáticamente.

Se utiliza cuando varios componentes necesitan compartir la propiedad de un mismo objeto. Para crearlo se recomienda std::make_shared.

3. std::weak_ptr:
Representa una referencia débil o temporal a un objeto administrado por shared_ptr. No comparte la propiedad del recurso ni incrementa el contador de propietarios shared_ptr, por lo que no mantiene vivo al objeto.

Para acceder al recurso se puede utilizar lock(), que intenta obtener un shared_ptr. Si el objeto todavía existe, se obtiene un shared_ptr válido; si ya fue destruido, lock() devuelve un puntero vacío.

Su uso principal es romper referencias cíclicas entre shared_ptr. Si dos o más objetos se poseen mutuamente mediante shared_ptr, sus contadores pueden permanecer por encima de cero y evitar que se ejecuten sus destructores. Reemplazar una de esas relaciones de propiedad por weak_ptr rompe el ciclo.
              """)

    def exercise_11(self):
        print("11. Realizar una comparativa de los tres punteros inteligentes e indicar en qué casos los utilizaría.")
        print("\n")
        print("""
Comparativa:

1. std::unique_ptr – Propiedad exclusiva:
- Cantidad de propietarios: uno.
- Copia: no permite copiarlo.
- Movimiento: sí permite transferir la propiedad mediante std::move.
- Liberación: automática cuando el unique_ptr se destruye o deja de administrar el objeto.
- Uso: lo utilizaría cuando una clase o componente es el único responsable de la vida útil de un objeto. Es la opción preferible cuando no se necesita compartir la propiedad.

2. std::shared_ptr – Propiedad compartida:
- Cantidad de propietarios: varios.
- Copia: permite copiarlo y compartir el mismo recurso.
- Movimiento: también permite transferir la propiedad.
- Liberación: automática cuando el contador de referencias llega a cero.
- Uso: lo utilizaría cuando varios objetos o partes del programa necesitan ser propietarios del mismo recurso y no existe un único propietario claramente responsable.

3. std::weak_ptr – Referencia débil o temporal:
- Cantidad de propietarios: no es propietario del recurso.
- Copia: permite copiar la referencia débil, pero no incrementa el contador de propietarios shared_ptr.
- Acceso: se obtiene temporalmente un shared_ptr mediante lock(), siempre que el objeto siga existiendo.
- Liberación: no libera ni mantiene vivo por sí mismo al objeto; la vida útil depende de los shared_ptr propietarios.
- Uso: lo utilizaría cuando necesito observar un objeto administrado por shared_ptr sin prolongar su vida útil, especialmente para romper referencias cíclicas.

Conclusión:
Utilizaría unique_ptr como primera opción cuando exista un solo propietario, porque expresa claramente la propiedad exclusiva y evita compartir innecesariamente la administración del recurso. Utilizaría shared_ptr únicamente cuando la propiedad compartida sea realmente necesaria. Finalmente, utilizaría weak_ptr cuando necesite una referencia no propietaria a un objeto shared_ptr o cuando deba evitar ciclos de propiedad que impidan liberar la memoria.

Los tres tipos automatizan la administración de la memoria, pero no son intercambiables: la elección depende de quién debe ser responsable de la vida útil del objeto.
              """)


#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■■■■■■■■■■ De acá para abajo sólo es la definición de clases y funciones para el manejo del menú ■■■■■■■■■■

class Assignment():

    """
    Class that abstracts and represents the assignment and stores the list of exercises
    """

    assignmentNumber: float = assignmentNumber

    def __init__(self):
        self.exercise_instance = Exercises()
        self.exercises = []

        # Checking the name of the methods inside Exercise class
        exercise_methods = [
            (int(name.split("_")[1]), getattr(self.exercise_instance, name))
            for name in dir(self.exercise_instance)
            if callable(getattr(self.exercise_instance, name)) and name.startswith("exercise_")
        ]

        exercise_methods.sort(key=lambda x: x[0])
        self.exercises = [method for _, method in exercise_methods]
        self.totalExercises: int = len(self.exercises)


# Entries Validation w/ error messages:

def isNum(num):
    """
    Function for validation of numbers
    """
    while num.isdigit() == False:
        print("No es un dato valido.\\n")
        num = input("Ingrese un numero natural entero: ")
    return int(num)


# Console clearing

def clear_console():
    """
    Function for console clearing
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Menú showcase:

def menu():
    """
    Function to display the menu with the assignment data based on the user's input
    """

    assignment_instance = Assignment()
    assignmentNumber = assignment_instance.assignmentNumber
    totalExercises = assignment_instance.totalExercises
    exercises = assignment_instance.exercises

    chars_per_line = 70

    while True:
        option = input(
            "\\n" + "═" * chars_per_line +
            "\\n" +
            f"Elija el número de ejercicio a revisar (del 1 al {totalExercises})".center(chars_per_line) +
            "\\n" +
            "O ingrese cualquier otro numero para salir: ".center(chars_per_line) +
            "\\n" + "═" * chars_per_line + "\\n"
        )
        option = isNum(option)

        if 1 <= option <= totalExercises:
            clear_console()
            print("\\n" + f"( {option} )".center(chars_per_line, "═") + "\\n")
            exercises[option - 1]()
        else:
            break

    print(f"""
    ################   Guía Nro {assignmentNumber} finalizada.   ####################
    """)


# Definición Main:

def main():
    menu()


if __name__ == "__main__":
    main()
