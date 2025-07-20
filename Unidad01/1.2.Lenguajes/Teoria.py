import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 1.2

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("""
1.  Tomar 4 Lenguajes de los Descriptos (según su gusto o preferencia), para ellos: 
    a.  Describir sus puntos Fuertes y débiles. 
    b.  Describir el Tipo de aplicaciones spa ralos cuales serían mejor aprovechados. 
    c.  Determinar el o los Paradigmas sobre los cuales está basado o responde. 
    d.  Destacar si existe algún framework sobre el que pueden operar. 
    e.  ¿Indicar las características del Framework, que beneficios trae?
""")
        print("\n")
        print("""
1. Java
    a. Puntos fuertes:

        Robusto y multiplataforma (gracias a la JVM).

        Orientado a objetos puro.

        Amplio soporte empresarial.

    b. Puntos débiles:

        Sintaxis verbosa.

        Menor rendimiento frente a lenguajes de bajo nivel.

    c. Aplicaciones recomendadas:

        Aplicaciones empresariales grandes.

        Desarrollo móvil (Android).

        Sistemas bancarios y seguros.

    d. Paradigmas:

        Orientado a Objetos.

    e. Framework destacado: Spring

        Características: Modular, con inyección de dependencias, soporte para REST, seguridad y acceso a bases de datos.

        Beneficios: Escalabilidad, mantenimiento sencillo, gran comunidad.

2. JavaScript
    a. Puntos fuertes:

        Lenguaje nativo del navegador.

        Dinámico, versátil y con gran comunidad.

        Ideal para desarrollo frontend y fullstack.

    b. Puntos débiles:

        Tipado débil que puede causar errores.

        Menor rendimiento en tareas intensivas.

    c. Aplicaciones recomendadas:

        Aplicaciones web dinámicas (SPAs).

        Interfaces interactivas.

        Aplicaciones multiplataforma (con frameworks como Electron).

    d. Paradigmas:

        Imperativo, Funcional, Orientado a Objetos (basado en prototipos).

    e. Framework destacado: React

        Características: Librería para construir interfaces UI con componentes reutilizables.

        Beneficios: Rapidez, estructura clara, compatible con otras tecnologías.

3. C++
    a. Puntos fuertes:

        Alto rendimiento y control de memoria.

        Ideal para programación de sistemas y juegos.

        Soporte para múltiples paradigmas.

    b. Puntos débiles:

        Sintaxis compleja.

        Propenso a errores de memoria si no se usa correctamente.

    c. Aplicaciones recomendadas:

        Motores de videojuegos.

        Sistemas embebidos.

        Software que requiere eficiencia extrema.

    d. Paradigmas:

        Imperativo, Orientado a Objetos, Genérico.

    e. Framework destacado: Qt

        Características: Framework gráfico multiplataforma para GUIs.

        Beneficios: Desarrollo rápido de interfaces profesionales, código portable.

4. Python
    a. Puntos fuertes:

        Sintaxis clara y simple.

        Versátil: scripting, IA, web, automatización.

        Gran comunidad y librerías.

    b. Puntos débiles:

        Más lento que lenguajes compilados.

        No apto para aplicaciones críticas en tiempo real.

    c. Aplicaciones recomendadas:

        Inteligencia Artificial y Machine Learning.

        Automatización y scripting.

        Desarrollo web (backend), análisis de datos.

    d. Paradigmas:

        Imperativo, Orientado a Objetos, Funcional.

    e. Framework destacado: Django

        Características: Framework completo para desarrollo web con ORM, plantillas, panel admin.

        Beneficios: Seguridad, rapidez de desarrollo, arquitectura bien definida.
              """)
    
    def exercise_2(self):
        print("""
2.  Realizar un comentario sobre la cita “Un lenguaje de programación multiparadigma es el 
cual soporta más de un paradigma de programación. Según lo describe Bjarne Stroustrup, 
permiten crear “programas usando más de un estilo de programación””.
""")
        print("\n")
        print("""
Como bien describe Stroustrup, un lenguaje multiparadigma es aquel que incorpora las herramientras necesarias,
así como otras que fáciliten la implementación de determinados paradigmas a la hora de escribir código en ellos.
Así, por ej., Python puede ser un ejemplo de lenguaje multiparadigma, en tanto permite la programación imperativa mediante el uso de bucles y condicionales,
la funcional mediante el uso de funciones incorporadas (map, filter y reduce) y funciones anonimas,
o la programación orientada a objetos, mediante clases, abstracciones y propiedades para métodos.
C++ así mismo es otro ejemplo al permitir las mismas cosas, aunque suela ser más asociado a un paradigma imperativo por su naturaleza de más bajo nivel.
              """)

    def exercise_3(self):
        print("3.  Describir el Concepto de Clase en POO")
        print("\n")
        print("""
Una clase funciona como un plano con el cual podremos dar instrucciones sobre cómo crear un objeto a la hora de instanciarlo,
encapsulando en él atributos, variables donde se almacenaran estados que den información sobre dicho objeto, 
así como métodos, que daran funcionalidades determinadas a dicho objeto.
Esta clase actuará como una representación abstracta del conjunto de esos objetos en la realidad, de su tipo, 
y sus atributos y métodos contenidos representaran las cualidades y acciones que puede realizar dicho conjunto de objetos.
Facilita así mismo la representación de jerarquías entre clases, 
dando lugar a una fácilitación de la reutilización de código y a la posibilidad de brindar soluciones pensando en la polimorfia, 
por medio de la relación entre clases.
              """)
        
    def exercise_4(self):
        print("4.  Describir el Concepto de Prototipo en POO")
        print("\n")
        print("""
Un Prototipo en POO no es más que una instancia de objeto que es usada como base para la creación de otro objeto.
Así, el nuevo objeto será instanciado poseyendo todos los atributos y métodos del objeto prototipo en base al cual fue creado, 
pudiendo además extender su funcionalidad, mediante el agregado de atributos y métodos a la hora de ser creado o en tiempo de ejecución.
              """)
    
    def exercise_5(self):
        print("5.  Realizar un comparativo ente ambos Enfoques")
        print("\n")
        print("""
Enfoque basado en Clases:
    Concepto central: 
        Se define una clase como plantilla para crear objetos.

    Herencia: 
        Jerárquica (una clase hereda de otra).

    Instanciación: 
        Se crean instancias (objetos) a partir de clases.

    Encapsulamiento: 
        Atributos y métodos están definidos dentro de la clase.

    Tipado: 
        Generalmente estático (Java, C++) o dinámico (Python).

    Ventajas:

        Estructura clara, ordenada y predecible.

        Fácil de mantener en sistemas grandes.

        Soporte amplio en lenguajes populares y frameworks.

    Desventajas:

        Puede ser rígido.

        Menos flexible para modificar en tiempo de ejecución.

Enfoque basado en Prototipos:
    Concepto central: 
        No hay clases como tal; los objetos heredan directamente de otros objetos (prototipos).

Herencia: 
    Delegación directa entre objetos (herencia prototípica).

Instanciación: 
    Se clona o extiende otro objeto.

Encapsulamiento: 
    Más dinámico, puede alterarse en tiempo de ejecución.

Tipado: 
    Dinámico.

Ventajas:

    Muy flexible y dinámico.

    Permite modificar objetos y su comportamiento en tiempo real.

    Más natural para ciertos estilos de scripting.

Desventajas:

    Puede generar confusión si no se comprende bien el modelo.

    Difícil de mantener en proyectos grandes y complejos.
              """)

    def exercise_6(self):
        print("6.  ¿En que considera que el Enfoque de Prototipos puede ser más Productivo?")
        print("\n")
        print("""
Considero que el Enfoque de Prototipos puede ser más productivo en tareas donde se requiera mayor dinamismo,
ya que el proceso de prototipado y pasaje de un tipo a otro mediante este enfoque es mucho más rápido y versatil,
permitiendose de forma fácil en proceso de ejecución. 
Así mismo permite el uso de atributos, métodos y el pasaje como argumento de los prototipos, 
cosa que con las clases no se puede realizar, 
al ser abstracciones usadas para la representación de objetos de la realidad o concepciones abstractas de ellos, 
y se requiere una posterior instanciación para poder usarlas normalmente.
Por lo cual considero que se destaca en tareas donde el tipado sea dinamico, 
y se requiera y valore la versatilidad y flexibilidad al cambio antes que la robustez y abstracción representativa.
              """)

    def exercise_7(self):
        print("7.  Como se establece el Concepto de “Herencia” en Lenguajes basados en Prototipos")
        print("\n")
        print("""
Se implementa la herencia permitiendo asociar un objeto prototípico con cualquier función constructor. 
De esta forma, por ej., podrías crear una relación entre Employee y Manager. 
En primer lugar, se define la función constructor para Employee, especificando las propiedades name y dept. 
Luego, se define la función constructor para Manager, especificando la propiedad reports. 
Por último, se asigna un nuevo objeto derivado de Employee.prototype como el prototype para la función constructor de Manager. 
De esta forma, cuando se crea un nuevo Manager, este hereda las propiedades name y dept del objeto Employee.
              """)
    
    def exercise_8(self):
        print("8.  ¿Qué significa que los Métodos o Propiedades pueden cambiarse en Tiempo de ejecución?")
        print("\n")
        print("""
Significa que un programa puede modificar, agregar o eliminar atributos y métodos de un objeto mientras se está ejecutando. 

Por ej.:
    JavaScript:

        Se puede agregar un método nuevo a un objeto en cualquier momento:

            let persona = { nombre: "Ana" };
            persona.saludar = function() {
            console.log("Hola!");
            };

            persona.saludar(); // Imprime: Hola!

Ventajas de poder cambiar propiedades y métodos en tiempo de ejecución:
    Flexibilidad: permite adaptar el comportamiento de los objetos según el contexto o las condiciones del entorno en tiempo real.

    Extensibilidad: se pueden añadir nuevas funcionalidades sin modificar el código fuente original.

    Sobrescritura dinámica: es posible reemplazar métodos por otros nuevos en objetos ya existentes.

Desventajas o riesgos:
    Mantenimiento más difícil: puede resultar confuso seguir el flujo del programa si los objetos cambian durante la ejecución.

    Errores difíciles de detectar: pueden surgir errores que sólo se manifiestan en ciertas condiciones, 
    y no son visibles a simple vista en el código fuente.
              """)

    def exercise_9(self):
        print("9.  ¿Cómo obtengo constructores más flexibles en Prototipado")
        print("\n")
        print("""
Los constructores se pueden hacer más flexibles permitiendo pasar valores como argumentos al momento de crear nuevas instancias. 
Esto se hace de la siguiente manera:

    Usando argumentos en la función constructora y asignando valores predeterminados si no se pasan (por ejemplo, con ||):

        function Engineer(name, projs, mach) {
            this.name = name || "";
            this.dept = "engineering";
            this.projects = projs || [];
            this.machine = mach || "";
        }
    
También se puede reutilizar otro constructor dentro del nuevo, para establecer propiedades heredadas:

    function Engineer(name, projs, mach) {
        this.base = WorkerBee;
        this.base(name, "engineering", projs);
        this.machine = mach || "";
    }

O mejor aún, usando call() para una implementación más limpia:

    function Engineer(name, projs, mach) {
        WorkerBee.call(this, name, "engineering", projs);
        this.machine = mach || "";
    }

Esto permite personalizar objetos al instanciarlos sin repetir código, reutilizando constructores padres.
              """)
        
    def exercise_10(self):
        print("10. ¿Cómo se puede heredar valores de Atributos en Prototipado?")
        print("\n")
        print("""
En los lenguajes basados en prototipos como JavaScript, la herencia no se basa en clases, sino en delegación prototipal. 
Esto significa que los objetos pueden heredar directamente de otros objetos, formando una cadena de prototipos.

1. Usando Object.create() para heredar atributos

    const animal = {
        especie: "Desconocida",
        hacerSonido() {
            console.log("Hace un sonido");
        }
    };

    const perro = Object.create(animal);
    perro.raza = "Labrador";

    console.log(perro.especie); // "Desconocida" (heredado del prototipo)
    perro.hacerSonido();        // "Hace un sonido"
              
    Perro no tiene la propiedad especie, pero la hereda desde animal gracias a la cadena prototipal.

2. Herencia en funciones constructoras

    Cuando usás funciones constructoras, podés asignar un prototipo para que todos los objetos creados hereden de él:

        function Persona(nombre) {
            this.nombre = nombre;
        }

        Persona.prototype.saludar = function() {
            console.log("Hola, soy " + this.nombre);
        };

        const juan = new Persona("Juan");
        juan.saludar(); // "Hola, soy Juan"
              
        saludar() está en el prototipo y no directamente en el objeto juan, pero se puede acceder igual.
              """)
    
    def exercise_11(self):
        print("11. ¿Cómo maneja o Simula “Herencia Múltiple” los Lenguajes Protipados?")
        print("\n")
        print("""
Los Lenguajes Prototipados simulan herencia múltiple usando:

1. Mixins (composición de objetos)
    Un Mixin es un objeto con propiedades o métodos que se copian dentro de otros objetos. Así, podés "heredar" comportamientos de múltiples fuentes.

        let sayHi = {
            hi() {
                console.log("Hola");
            }
        };

        let sayBye = {
            bye() {
                console.log("Chau");
            }
        };

        function Person(name) {
            this.name = name;
        }

        Object.assign(Person.prototype, sayHi, sayBye);

        let bruno = new Person("Bruno");
        bruno.hi();   // Hola
        bruno.bye();  // Chau
    
    Object.assign() copia todas las propiedades de varios objetos a otro.

2. Herencia en cadena + composición
    Podés usar una función constructora base y luego extender comportamientos desde otras funciones u objetos.

    function Worker() {
        this.job = "general";
    }
    Worker.prototype.work = function() {
        console.log("Trabajando...");
    };
    function Musician() {
        this.instrument = "guitarra";
    }
    Musician.prototype.play = function() {
        console.log("Tocando guitarra");
    };

    function MusicianWorker() {
        Worker.call(this);
        Musician.call(this);
    }
    Object.assign(MusicianWorker.prototype, Worker.prototype, Musician.prototype);

    let persona = new MusicianWorker();
    persona.work(); // Trabajando...
    persona.play(); // Tocando guitarra
              
3. Funciones Helper para simular múltiples fuentes
    Podés encapsular comportamientos y luego combinarlos:

        function mixin(target, ...sources) {
            sources.forEach(src => {
                Object.getOwnPropertyNames(src).forEach(prop => {
                    target[prop] = src[prop];
                });
            });
            return target;
        }
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
        for name in dir(self.exercise_instance):
            attr = getattr(self.exercise_instance, name)
            if callable(attr) and name.startswith("exercise_"):
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

    print(f"""
    ################   Guía Nro {assignmentNumber} finalizada.   ####################
    """)
    y=False

#Definición Main:

def main():

    menu()

main()