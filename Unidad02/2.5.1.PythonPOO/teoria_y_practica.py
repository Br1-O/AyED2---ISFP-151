import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 2.5

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.1 ¿Cómo se define una clase en Python?.")
        print("\n")
        print("""
En Python, una clase se define utilizando la palabra clave class, seguida del nombre de la clase y dos puntos.
Dentro del bloque indentado se definen los atributos y métodos. 
Por ejemplo:
    class Perro:
        pass
Es el esquema básico para comenzar a utilizar la Programación Orientada a Objetos (POO), 
permitiendo usar las propiedades de las clases dentro de este paradigma: abstracción, encapsulación, herencia y polimorfismo.
              """)
    
    def exercise_2(self):
        print("1.2 Que es un atributo de Clase y uno de Instancia, cuales son las diferencias.")
        print("\n")
        print("""
Un atributo de clase es compartido por todas las instancias de la clase y se define fuera de cualquier método, 
directamente dentro del bloque de la clase. Un atributo de instancia se define dentro del método __init__ utilizando self, 
y es exclusivo de cada objeto. 
Por ejemplo, 
    especie = 'mamífero' es un atributo de clase
    self.nombre = nombre es de instancia. 
Esta distinción permite manejar información común y específica de cada objeto.
              """)

    def exercise_3(self):
        print("1.3 ¿Como se define un constructor en Python?")
        print("\n")
        print("""
El constructor se define mediante el método especial __init__. Es llamado automáticamente al crear una instancia de la clase. 
Recibe como primer parámetro self, que representa la instancia, seguido de los parámetros necesarios. 
Se utiliza para inicializar atributos del objeto, como self.nombre = nombre. 
Por ej:
    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart
              """)

    def exercise_4(self):
        print("1.4 ¿Que es un Decorador en Python?")
        print("\n")
        print("""
Un decorador es una función especial que se aplica sobre otra función o método para modificar su comportamiento sin cambiar su código. 
Se indica con @nombre_decorador justo encima de la definición. 
Por ejemplo: 
    @staticmethod, @classmethod, o @property. 
Son muy usados en POO para controlar el acceso a los métodos o para definir diferentes tipos de métodos dentro de una clase.
              """)

    def exercise_5(self):
        print("1.5 Que es un Método de Instancia, clase y Estático. ")
        print("\n")
        print("""
■ Un método de instancia recibe como primer parámetro self, accede y modifica atributos del objeto. 
■ Un método de clase se define con @classmethod y recibe cls como primer parámetro, permitiendo modificar atributos de clase. 
■ Un método estático se define con @staticmethod y no recibe ningún parámetro especial y no accede ni a atributos ni a otros métodos de la clase. 
Se usa cuando una función está relacionada lógicamente con la clase, pero no depende de ella.
              """)

    def exercise_6(self):
        print("1.6 Dar ejemplos de atributos y métodos en Python")
        print("\n")
        print("""
Un ejemplo que muestre todos los atributos y métodos vistos hasta ahora en Python sería:
    class Bicicleta:
        cantidad = 0
                
        def __init__(self, color, rodado):
            self.color = color
            self.rodado = rodado
            Bicicleta.cantidad += 1
                
        def andar(self):
            print(f'la bici {self.color} con rodado {self.rodado} está andando.')
                
        @classmethod
        def contar_instancias(cls):
            return cls.cantidad
        
        @staticmethod
        def andan_en_bici():
            print("hay por lo menos alguien andando en bici)
              """)
        
    def exercise_7(self):
        print("1.7 Crear una Clase en Python")
        print("\n")
        print("""
class Perro:
    pass
                """)
        class Perro:
            pass
            
    def exercise_8(self):
        print("1.8 Asignarles atributos de clase e instancia ")
        print("\n")
        print("""
class Perro:
    patas = 4 #atributo de clase
    ruido = 'ladrido' #atributo de clase
    
    def __init__(self, nombre, raza):
        self.nombre = nombre #atributo de instancia
        self.raza = raza #atributo de instancia
                """)
        class Perro:
            patas = 4 #atributo de clase
            ruido = 'ladrido' #atributo de clase
            
            def __init__(self, nombre, raza):
                self.nombre = nombre #atributo de instancia
                self.raza = raza #atributo de instancia

    def exercise_9(self):
        print("1.9 Asignar métodos de Instancia, Clase y estáticos")
        print("\n")
        print("\n")
        print("""
class Perro:
    patas = 4 #atributo de clase
    ruido = 'ladrido' #atributo de clase
    
    def __init__(self, nombre, raza):
        self.nombre = nombre #atributo de instancia
        self.raza = raza #atributo de instancia

    #método de instancia
    def mostrar_nombre(self):
        print("El nombre de este perro es: ", self.nombre)

    #método de clase
    @classmethod
    def ladrar(cls):
        print((cls.ruido+" ")*5)
    
    #método estático
    @staticmethod
    def morder():
        print("El perro está mordiendote.")
                """)
        class Perro:
            patas = 4 #atributo de clase
            ruido = 'ladrido' #atributo de clase
            
            def __init__(self, nombre, raza):
                self.nombre = nombre #atributo de instancia
                self.raza = raza #atributo de instancia

            #método de instancia
            def mostrar_nombre(self):
                print("El nombre de este perro es: ", self.nombre)

            #método de clase
            @classmethod
            def ladrar(cls):
                print((cls.ruido+" ")*5)
            
            #método estático
            @staticmethod
            def morder():
                print("El perro está mordiendote.")


    def exercise_10(self):
        print("1.10  Realizar una calculadora que consuma estos métodos")
        print("\n")

        class Calculadora:
            tipo_calculadora = "cientifica"

            def __init__(self, marca = "Phillips"):
                self.marca = marca

            @staticmethod
            def sumar(a, b):
                return a + b
            
            @staticmethod
            def restar(a, b):
                return a - b
            
            @staticmethod
            def multiplicar(a, b):
                return a * b
            
            @staticmethod
            def dividir(a, b):
                if b != 0:
                    return a / b
                else:
                    return "No se puede dividir por cero"
                    
            def mostrar_marca(self):
                print("La marca de la calculadora es:", self.marca)
            
            @classmethod
            def mostrar_tipo(cls):
                print("Se usó una calculadora de tipo:",cls.tipo_calculadora,"para hacer estos cálculos.")
            
        print("Calculadora simple \n")
    
        calculadora = Calculadora("Hitachi")
        a = float(input("Ingresá el primer número: "))
        b = float(input("Ingresá el segundo número: "))
        
        print("Suma:", Calculadora.sumar(a, b))
        print("Resta:", Calculadora.restar(a, b))
        print("Multiplicación:", Calculadora.multiplicar(a, b))
        print("División:", Calculadora.dividir(a, b))
        calculadora.mostrar_marca()
        calculadora.mostrar_tipo()

    def exercise_11(self):
        print("2.1 Como Implementa la Herencia Python, dar ejemplos.")
        print("\n")
        print("""
Python permite crear clases que heredan de otras simplemente indicando entre paréntesis el nombre de la clase padre. 
La clase hija hereda todos los métodos y atributos de la clase base, y puede sobrescribirlos o extenderlos. 
Esto permite evitar la duplicación de código y aplicar el principio DRY. 
Por ejemplo:
    class Animal:
        def moverse(self):
            pass
              
    class Perro(Animal):
        def moverse(self):
            print("El perro está moviendose!")
                """)

    def exercise_12(self):
        print("2.2 ¿Para que sirven los métodos “Mágicos” __bases__ y __subclases__ ?")
        print("\n")
        print("""
El atributo __bases__ permite ver las clases padre de una clase. 
__subclasses__() devuelve una lista de clases que heredan directamente de una clase dada. 
Son útiles para el análisis y depuración del árbol de herencia, especialmente en estructuras complejas donde intervienen muchas clases.
                """)

    def exercise_13(self):
        print("2.3 Como se Implementa la Extensión y modificación de métodos.")
        print("\n")
        print("""
Una clase hija puede sobrescribir un método de la clase padre simplemente redefiniéndolo. 
También puede extenderlo usando super(), lo que permite ejecutar el comportamiento del método original además del nuevo. 
Esto se usa frecuentemente en constructores y métodos complejos que deben mantener comportamiento previo más nuevas funcionalidades.
                """)
    
    def exercise_14(self):
        print("2.4 Para que sirve la palabra super()")
        print("\n")
        print("""
La función super() permite acceder a métodos y atributos de la clase padre sin nombrarla directamente. 
Es especialmente útil en herencia múltiple o cuando el nombre de la clase base podría cambiar. 
Se usa comúnmente para inicializar atributos heredados dentro de __init__, evitando repetir código.
                """)

    def exercise_15(self):
        print("2.5 ¿Como implementa Python la Herencia múltiple?")
        print("\n")
        print("""
Python permite heredar de más de una clase separando los nombres con comas en la definición de la clase. 
Esta característica permite combinar funcionalidades de varias clases, aunque puede traer complejidades como ambigüedades en los métodos heredados. 
Por ejemplo:
    class Clase1:
        pass
    class Clase2:
        pass
    class MiClase(Clase1, Clase2):
        pass
                """)
            
    def exercise_16(self):
        print("2.6 Que es el  MRO o Method Resolution Order, para que sirve?")
        print("\n")
        print("""
El MRO es el orden en que Python busca los métodos y atributos en una jerarquía de herencia. Se puede consultar con Clase.__mro__. 
Esto es clave en herencia múltiple, ya que define con claridad cuál método se ejecutará en caso de que varias clases definan el mismo. 
                """)
            
    def exercise_17(self):
        print("""
2.1 Desarrollar una APP por consola que Cree una estructura como la de la figura:  
2.2 Implementar la Herencia 
2.3 Implementar __bases__ y __subclases__ 
2.4 Implementar base() 
2.5 Crear Objetos y mostrar por consola.
""")
        print("\n")
        class Animal:
            def hablar(self):
                pass
            def moverse(self):
                pass
            def describirme(self):
                print(f"Soy un Animal de tipo {type(self).__name__} \n")

        class Perro(Animal):
            def hablar(self):
                print("Guau!")
            def moverse(self):
                print("Caminando con 4 patas")

        class Vaca(Animal):
            def hablar(self):
                print("Muuu!")
            def moverse(self):
                print("Caminando con 4 patas")

        class Abeja(Animal):
            def hablar(self):
                print("Bzzzz!")
            def moverse(self):
                print("Volando")

        # Uso de __bases__ y __subclasses__
        print("El padre de la clase perro es: \n", Perro.__bases__, "\n")
        print("Las subclases de la clase Animal son: \n", Animal.__subclasses__(), "\n")

        # Crear objetos y mostrar por consola
        perro = Perro()
        perro.hablar()
        perro.moverse()
        perro.describirme()

        vaca = Vaca()
        vaca.hablar()
        vaca.moverse()
        vaca.describirme()

        abeja = Abeja()
        abeja.hablar()
        abeja.moverse()
        abeja.describirme()
        print("El mro para perro es: \n", Perro.__mro__)
            
    def exercise_18(self):
        print("3.1 Que función tiene @property, que emula?")
        print("\n")
        print("""
El decorador @property convierte un método en un atributo de sólo lectura. 
Es decir, permite acceder a un método como si fuera un atributo sin necesidad de paréntesis. 
Emula el comportamiento de las propiedades en otros lenguajes como Java o C#, 
y ayuda a ocultar la lógica de acceso sin cambiar la interfaz de uso del objeto.
            """)

    def exercise_19(self):
        print("3.2 Que relación tiene @property con encapsulamiento?")
        print("\n")
        print("""
El decorador @property facilita el encapsulamiento al permitir definir una interfaz clara para obtener el valor de un atributo, 
sin necesidad de acceder directamente al mismo. 
Se puede controlar el acceso, validarlo o transformarlo al mismo tiempo que se mantiene una sintaxis simple y clara para quien utiliza la clase.
            """)

    def exercise_20(self):
        print("3.3 Que relación tiene @property con Set() y Get()? ")
        print("\n")
        print("""
@property reemplaza el uso explícito de los métodos get() y set() al permitir definir métodos con el mismo nombre del atributo. 
A través de los decoradores @property y @<atributo>.setter se puede controlar completamente el acceso y modificación de un atributo, 
manteniendo la simplicidad de la sintaxis.
""")
        
    def exercise_21(self):
        print("3.4 ¿Para que sirve y se utiliza “__” antes de una variable?")
        print("\n")
        print("""
El doble guión bajo __ delante de un nombre de variable le decimos a Python que deseamos hacerlo menos accesible desde fuera de la clase.
Python entonces ocultará dicho atributo para que no sea accesible mediante la notación objeto.propiedad. 
Esto refuerza el encapsulamiento, previniendo que el estado interno de los objetos de esa clase pueda ser visto o modificado desde el exterior de forma directa.
""")
            
    def exercise_22(self):
        print("3.5 Que relación tiene con el método setter()")
        print("\n")
        print("""
El @<atributo>.setter permite definir la lógica que se ejecuta al modificar un atributo decorado con @property. 
De este modo, podemos incluir validaciones, disparar efectos colaterales o transformar valores antes de que se asignen. 
En conjunto con @property, forma una interfaz de acceso controlado sin cambiar la sintaxis de uso.
""")

    def exercise_23(self):
        print("""
3.1 Implementar dos métodos en alguna Clase y usar @property 
3.2 Implementar Encapsulamiento vía “__” 
3.3 Implementar los setter()
""")
        class Animal:
            def hablar(self):
                pass
            def moverse(self):
                pass
            def describirme(self):
                print(f"Soy un Animal de tipo {type(self).__name__} \n")

        class Perro(Animal):

            def __init__(self, nombre, raza):
                self.__nombre = nombre
                self.__raza = raza
               
            @property
            def nombre(self):
                return self.__nombre
            
            @nombre.setter
            def nombre(self, nombre):
                self.__nombre = nombre

            @property
            def raza(self):
                return self.__raza
            
            @raza.setter
            def raza(self, raza):
                self.__raza = raza
            
            def hablar(self):
                print("Guau!")
            def moverse(self):
                print("Caminando con 4 patas")

        # Crear objetos y mostrar por consola
        perro = Perro("Toby", "beagle")
        perro.hablar()
        perro.moverse()
        perro.describirme()
        print(perro.nombre, "es de raza:",perro.raza)
        perro.raza = "cocker"
        print("¡No, esperá un momento!", perro.nombre, "en realidad era un", perro.raza)
        print("Y", perro.nombre, "ya no será 'Toby', ahora se llamará:")
        perro.nombre = "Tijuana"
        print("'", perro.nombre, "'")

    def exercise_24(self):
        print("""
4.1 Explicar la cita: La abstracción es un término que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, 
centrándose sólo en cómo puede ser usada, lo que se conoce como interfaz. 
""")
        print("\n")
        print("""
La abstracción permite ocultar los detalles internos de implementación de una clase y exponer sólo lo necesario para interactuar con ella. 
Esto permite centrarse en “qué hace” un objeto en lugar de “cómo lo hace”.
Por ejemplo, un método pagar() puede ejecutar múltiples validaciones internas, pero el usuario sólo necesita saber que lo llama para realizar un pago. 
Esta técnica mejora la claridad, mantenibilidad y reutilización del código.
            """)

    def exercise_25(self):
        print("""
4.2 Explicar: El acoplamiento en programación (denominado coupling en Inglés) es un concepto que mide la dependencia entre dos módulos distintos de software, como pueden ser por ejemplo las clases.
""")
        print("\n")
        print("""
El acoplamiento mide cuán conectadas están dos clases o módulos entre sí. 
Un alto acoplamiento implica que una clase depende fuertemente de otra, 
lo que puede dificultar el mantenimiento y la escalabilidad. En cambio, el bajo acoplamiento favorece que los cambios en una clase no afecten a otras, 
haciendo el sistema más flexible. El uso de interfaces, abstracciones y dependencias mínimas favorece el bajo acoplamiento.
            """)

    def exercise_26(self):
        print("4.3 ¿A que se le denomina un “efecto mariposa” en programación?")
        print("\n")
        print("""
El efecto mariposa refiere a que un pequeño cambio en una parte del código puede desencadenar consecuencias imprevistas en otras partes. 
Esto suele ocurrir en sistemas con alto acoplamiento y baja cohesión, donde las clases están muy interdependientes. 
Evitar este efecto es uno de los objetivos del diseño orientado a objetos bien estructurado.
""")
    
    def exercise_27(self):
        print("4.4 ¿Qué entiende por Cohesión?, dar ejemplos.")
        print("\n")
        print("""
La cohesión se refiere al grado en que los métodos y atributos de una clase están relacionados con una única responsabilidad o propósito. 
Una clase con alta cohesión tiene métodos bien enfocados que colaboran en torno a un mismo objetivo. 
Por ejemplo, una clase Factura que contiene métodos como agregar_item(), quitar_item() y calcular_total() está cohesionada. 
Si además tuviera enviar_correo() o conectar_DB(), perdería cohesión.
            """)

    def exercise_28(self):
        print("4.5 ¿Qué relación hay entre Acoplamiento y Cohesión?")
        print("\n")
        print("""
Idealmente se busca bajo acoplamiento y alta cohesión. 
Si las clases están bien cohesionadas, cada una tiene una responsabilidad clara, lo que disminuye la necesidad de depender de otras clases,
al encargarse todas de tareas bien diferenciadas (bajo acoplamiento). Ambas características son deseables para sistemas mantenibles y fáciles de escalar, 
ya que cada clase puede evolucionar de forma independiente y predecible.
""")
        
    def exercise_29(self):
        print("4.6 ¿Que es el Encapsulamiento?")
        print("\n")
        print("""
El encapsulamiento es un principio de la POO que consiste en ocultar el estado interno de un objeto y controlar el acceso a sus atributos y métodos. 
Esto se logra restringiendo el acceso directo a los datos mediante convenciones como __atributo, y ofreciendo métodos públicos para accederlos (getters y setters). 
Así protege la integridad del objeto y evita que el usuario modifique datos en forma indebida.
""")
            
    def exercise_30(self):
        print("4.1 Revisar la App anterior y tratar de Implementar los conceptos anteriores. Comentar los Cambios en el Código.")
        print("\n")
        print("""
class Animal:
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describirme(self):
        print(f"Soy un Animal de tipo {type(self).__name__} \n")

class Perro(Animal):

    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def raza(self):
        return self.__raza
    
    @raza.setter
    def raza(self, raza):
        self.__raza = raza
    
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

# Crear objetos y mostrar por consola
perro = Perro("Toby", "beagle")
perro.hablar()
perro.moverse()
perro.describirme()
print(perro.nombre, "es de raza:",perro.raza)
perro.raza = "cocker"
print("¡No, esperá un momento!", perro.nombre, "en realidad era un", perro.raza)
print("Y", perro.nombre, "ya no será 'Toby', ahora se llamará:")
perro.nombre = "Tijuana"
print("'", perro.nombre, "'")
              
Este ejemplo presenta una clase Perro que hereda de Animal y demuestra:

    Encapsulamiento: mediante __nombre y __raza, con @property y @setter para controlar su acceso.
    Cohesión: cada clase tiene un rol claro: Animal define la interfaz común, y Perro implementa el comportamiento específico.
    Bajo acoplamiento: Perro depende de Animal pero puede evolucionar sin afectar otras posibles subclases.
    Abstracción: los métodos como hablar() y moverse() permiten usar el objeto sin conocer su implementación interna.
""")

    def exercise_31(self):
        print("5.1 ¿Que entiende por polimorfismo?")
        print("\n")
        print("""
El polimorfismo es un principio de la programación orientada a objetos que permite que distintas clases compartan una misma interfaz (método o mensaje),
pero con diferentes implementaciones. En otras palabras, objetos de diferentes clases pueden responder a la misma llamada de método, 
cada uno de acuerdo a su propia lógica. Esto permite escribir código más general, flexible y extensible.
""")
        
    def exercise_32(self):
        print("5.2 Como se implementa el Polimorfismo en Lenguajes estáticos ")
        print("\n")
        print("""
En lenguajes estáticos como Java o C++, el polimorfismo se implementa mayormente a través de herencia y sobreescritura de métodos, 
controlado por tipos estáticos. También puede lograrse mediante sobrecarga de métodos, en la que una misma función puede tener múltiples firmas. 
El compilador determina en tiempo de compilación cuál método se debe usar.
            """)

    def exercise_33(self):
        print("5.3 Como se implementa el Polimorfismo en Lenguajes dinámicos ")
        print("\n")
        print("""
En Python, el polimorfismo se apoya principalmente en el tipado dinámico y el concepto de duck typing. 
Esto significa que no es necesario que los objetos compartan una interfaz explícita; basta con que tengan los métodos que se desea utilizar. 
Por ejemplo, si varias clases implementan un método hablar(), entonces se pueden tratar por igual en un bucle sin importar si comparten o no herencia. 
El comportamiento correcto se resuelve en tiempo de ejecución. Python no admite sobrecarga de métodos como otros lenguajes,
pero permite usar argumentos opcionales (*args, valores por defecto) para lograr un comportamiento similar.
En cambio, la anulación de métodos (overriding) sí está completamente soportada y es una forma habitual de aplicar polimorfismo en Python.
""")
    
    def exercise_34(self):
        print("""
5.1 analizar y describir le siguiente código: 
    for animal in Perro(), Gato(): 
        animal.hablar() 
    # Guau! 
    # Miau!
""")
        print("\n")
        print("""
Se crea un bucle for que itera sobre dos objetos: uno de la clase Perro y otro de la clase Gato. 
Durante cada iteración del bucle, la variable animal toma uno de los dos objetos, y se invoca el método hablar() sobre él.

El método hablar() fue anulado (override) en ambas clases respecto de una clase base común (por ejemplo, Animal),
por lo que se ejecuta una implementación distinta dependiendo del tipo real del objeto: Perro imprime “Guau!” y Gato imprime “Miau!”.
Este comportamiento dinámico en tiempo de ejecución es una clara manifestación del polimorfismo:
una misma interfaz (hablar()) invocada sobre objetos de distintos tipos, con resultados diferentes según su clase.
Incluso si Perro y Gato no compartieran una clase base, este ejemplo seguiría funcionando gracias al duck typing de Python.
            """)

    def exercise_35(self):
        print("6.1 Que entiende por Interface (conceptualmente)")
        print("\n")
        print("""
Una interfaz es un contrato que define un conjunto de métodos que una clase debe implementar. Conceptualmente, una interfaz no contiene lógica,
sino solo la firma de los métodos. Sirve para establecer una estructura común entre distintas clases,
permitiendo que todas respondan a los mismos mensajes, incluso si su comportamiento interno varía.
Es fundamental en la programación orientada a objetos para garantizar consistencia y facilitar el polimorfismo.
""")
        
    def exercise_36(self):
        print("6.2 Que diferencia y que relación tiene con la Implementación")
        print("\n")
        print("""
La interfaz define 'qué' debe hacer una clase, mientras que la implementación define 'cómo' lo hace.
Por ejemplo, una interfaz puede establecer que una clase debe tener un método despegar(), pero no indica cómo despega.
Cada clase que implemente esa interfaz puede tener una lógica distinta, funcionando la interfaz como una abstracción de dicha lógica interna.
Esto separa la declaración de funcionalidades del detalle de su ejecución, lo que mejora la modularidad y el desacoplamiento.
""")
            
    def exercise_37(self):
        print("6.3 Que tipos de Interfaces tiene Python.")
        print("\n")
        print("""
En Python se pueden crear interfaces 'informales' usando clases base con métodos no implementados.
También ofrece clases abstractas (ABCs - Abstract Base Classes) que permiten definir interfaces formales usando el módulo abc.
Este módulo permite forzar que una subclase implemente ciertos métodos, funcionando como interfaces clásicas.
""")

    def exercise_38(self):
        print("6.4 que es una Interfaz “Informal”, como se Implementa.")
        print("\n")
        print("""
Una interfaz informal se implementa en Python definiendo una clase con métodos que deben ser implementados por las subclases,
pero sin usar mecanismos de validación formal. Es decir, no se usa el módulo abc, y no hay verificación explícita de que los métodos estén sobreescritos.
Este enfoque funciona gracias al duck typing: si un objeto implementa los métodos esperados, se considera válido.
""")
        
    def exercise_39(self):
        print("6.5 Que problemas puede ocasionar la implementación de Interfaces Informales?")
        print("\n")
        print("""
El principal problema es la falta de verificación en tiempo de desarrollo. Si una subclase olvida implementar un método esperado,
el error no se detectará hasta que el método sea invocado en tiempo de ejecución, lo que puede generar fallos difíciles de depurar.
Por eso, para proyectos grandes o colaborativos, se recomienda usar interfaces formales con abc.
""")
        
    def exercise_40(self):
        print("6.6 Que son las Interfaces Formales?")
        print("\n")
        print("""
Son estructuras que usan mecanismos del lenguaje (como el módulo abc) para garantizar que las clases hijas implementen ciertos métodos.
En Python, esto se logra marcando métodos como abstractos con el decorador @abstractmethod, y haciendo que la clase base herede de ABC.
Las interfaces formales ayudan a detectar errores más temprano y a mantener una arquitectura coherente.
""")
        
    def exercise_41(self):
        print("6.7 Como se implementan las ABC?")
        print("\n")
        print("""
Las ABC (Abstract Base Classes) se definen usando el módulo abc. Se crea una clase que hereda de ABC y se definen métodos abstractos con el decorador @abstractmethod.
Cualquier clase que herede de esta base deberá implementar los métodos marcados como abstractos, de lo contrario no podrá instanciarse. Esto obliga a cumplir una interfaz determinada.
            """)

    def exercise_42(self):
        print("6.8 Para que sirve el decorador @abstractmethod?")
        print("\n")
        print("""
@abstractmethod se usa para declarar un método como obligatorio dentro de una clase abstracta. Obliga a que cualquier clase hija lo implemente.
Si no se lo hace, Python lanzará un error cuando se intente instanciar la subclase. Es una forma de reforzar el contrato de una interfaz formal.
""")
    
    def exercise_43(self):
        print("6.9 Que entiende por clase virtual en Python?")
        print("\n")
        print("""
Una clase virtual es una clase que no está en la jerarquía de herencia directa, pero que se considera “subclase” de una ABC.
Python permite registrar clases virtuales usando el método register() de una ABC. Esto es útil cuando no se puede modificar la jerarquía pero se quiere hacer cumplir una interfaz común.
            """)

    def exercise_44(self):
        print("6.10 como se define una clase virtual dar ejemplo.")
        print("\n")
        print("""
Una clase virtual se define registrando una clase con una ABC.
Por ejemplo:
    from abc import ABC, abstractmethod

    class Volador(ABC):
        @abstractmethod
        def volar(self):
            pass

    class Avion:
        def volar(self):
            print("Volando como avión")

    Volador.register(Avion)  # Avion ahora es una clase virtual de Volador
              
Así, aunque Avion no hereda de Volador, se la considera como si lo hiciera, siempre y cuando implemente el método requerido.
""")
        
    def exercise_45(self):
        print("6.11 Explicar la Librería ABC para colecciones, que permite crear interfaces de colecciones, explicar el ejemplo de la Teoria.")
        print("\n")
        print("""
El módulo collections.abc permite definir interfaces formales para tipos de datos como listas, diccionarios, conjuntos, etc.
Al implementar estas interfaces, una clase puede comportarse como una colección estándar.
Por ejemplo, si se implementan __len__(), __getitem__() y __iter__(), una clase puede comportarse como una lista iterable.
Esto permite extender estructuras de datos con comportamientos personalizados manteniendo compatibilidad con el ecosistema de Python.
""")
            
    def exercise_46(self):
        print("""
6.1 Desarrollar una App que permita a un cliente, manejar distintos drones: Tricópteros. Cuadricópteros. 
Hexacópteros. Octocópteros. Coaxiales. 
6.2 Implementar interfaz Abstracta que permita al Cliente pilotear (despegar, aterrizar, acelerar, frenar, doblar 
derecha-izquierda, sacar fotos)
""")
        print("\n")
        from abc import ABC, abstractmethod

        class Dron(ABC):
            @abstractmethod
            def despegar(self): 
                pass
            @abstractmethod
            def aterrizar(self): 
                pass
            @abstractmethod
            def acelerar(self): 
                pass
            @abstractmethod
            def frenar(self): 
                pass
            @abstractmethod
            def doblar_derecha(self): 
                pass
            @abstractmethod
            def doblar_izquierda(self): 
                pass
            @abstractmethod
            def sacar_foto(self): 
                pass

        class Tricoptero(Dron):
            def despegar(self): print("Tricóptero despegando")
            def aterrizar(self): print("Tricóptero aterrizando")
            def acelerar(self): print("Tricóptero acelerando")
            def frenar(self): print("Tricóptero frenando")
            def doblar_derecha(self): print("Tricóptero doblando a la derecha")
            def doblar_izquierda(self): print("Tricóptero doblando a la izquierda")
            def sacar_foto(self): print("Tricóptero sacando foto \n")

        class Cuadricoptero(Dron):
            def despegar(self): print("Cuadricóptero despegando")
            def aterrizar(self): print("Cuadricóptero aterrizando")
            def acelerar(self): print("Cuadricóptero acelerando")
            def frenar(self): print("Cuadricóptero frenando")
            def doblar_derecha(self): print("Cuadricóptero doblando a la derecha")
            def doblar_izquierda(self): print("Cuadricóptero doblando a la izquierda")
            def sacar_foto(self): print("Cuadricóptero sacando foto \n")

        class Hexacoptero(Dron):
            def despegar(self): print("Hexacóptero despegando")
            def aterrizar(self): print("Hexacóptero aterrizando")
            def acelerar(self): print("Hexacóptero acelerando")
            def frenar(self): print("Hexacóptero frenando")
            def doblar_derecha(self): print("Hexacóptero doblando a la derecha")
            def doblar_izquierda(self): print("Hexacóptero doblando a la izquierda")
            def sacar_foto(self): print("Hexacóptero sacando foto \n")
        
        class Octocoptero(Dron):
            def despegar(self): print("Octocóptero despegando")
            def aterrizar(self): print("Octocóptero aterrizando")
            def acelerar(self): print("Octocóptero acelerando")
            def frenar(self): print("Octocóptero frenando")
            def doblar_derecha(self): print("Octocóptero doblando a la derecha")
            def doblar_izquierda(self): print("Octocóptero doblando a la izquierda")
            def sacar_foto(self): print("Octocóptero sacando foto \n")

        class Coaxial(Dron):
            def despegar(self): print("Coaxial despegando")
            def aterrizar(self): print("Coaxial aterrizando")
            def acelerar(self): print("Coaxial acelerando")
            def frenar(self): print("Coaxial frenando")
            def doblar_derecha(self): print("Coaxial doblando a la derecha")
            def doblar_izquierda(self): print("Coaxial doblando a la izquierda")
            def sacar_foto(self): print("Coaxial sacando foto \n")

        def ejecutar_vuelo(drone):
            drone.despegar()
            drone.acelerar()
            drone.doblar_derecha()
            drone.frenar()
            drone.doblar_izquierda()
            drone.aterrizar()
            drone.sacar_foto()

        ejecutar_vuelo(Tricoptero())
        ejecutar_vuelo(Cuadricoptero())
        ejecutar_vuelo(Hexacoptero())
        ejecutar_vuelo(Octocoptero())
        ejecutar_vuelo(Coaxial())

    def exercise_47(self):
        print("7.1 Explicar el concepto que subyace a la frase: “If it walks like a duck and it quacks like a duck, then it must be a duck”")
        print("\n")
        print("""
Esta frase representa el principio del duck typing, muy característico de lenguajes con tipado dinámico como Python. 
Lo importante no es que un objeto sea de un tipo determinado (como una clase específica), sino que se comporte como tal. 
Si un objeto tiene los métodos o atributos esperados, entonces puede usarse como si fuera del tipo requerido, sin importar su jerarquía de herencia. 
Esta flexibilidad permite escribir código más desacoplado y reutilizable.
""")
        
    def exercise_48(self):
        print("""
7.2 Que no dice el autor: Don’t check whether it is-a duck: check whether it quacks-like-a duck, walks-like-a duck, 
etc, etc, depending on exactly what subset of duck-like behavior you need to play your language-games with. 
(comp.lang.python, Jul. 26, 2000) — Alex Martell
""")
        print("\n")
        print("""
Alex Martelli señala que en Python no importa si una instancia es realmente de una clase específica (no importa el tipo exacto). 
Lo importante es que implemente los métodos o comportamientos que necesitamos. 
En lugar de usar isinstance() o verificar tipos, basta con chequear que el objeto tenga los métodos necesarios. 
Esto refuerza el diseño basado en interfaces implícitas y favorece la libertad estructural del código.
""")
        
    def exercise_49(self):
        print("7.3 Que significa que a , a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos.")
        print("\n")
        print("""
Significa que en Python no es necesario declarar ni restringir el tipo de un objeto. 
El intérprete ejecutará un método mientras este exista en el objeto, sin preocuparse por si el objeto es de una clase u otra. 
Este comportamiento permite aplicar polimorfismo sin necesidad de herencia, y es una base para las interfaces informales y la programación orientada a comportamientos en lugar de tipos.
""")
        
    def exercise_50(self):
        print("""
7.4 Explicar el siguiente Código:  
    lista = [Perro(), Gato(), Vaca()] 
    for animal in lista: 
        animal.hablar()
""")
        print("\n")
        print("""
Este código define una lista con tres objetos de clases distintas, pero todos implementan el método hablar(). 
Gracias al duck typing, Python no necesita que estos objetos compartan una clase base ni una interfaz explícita: basta con que todos tengan el método hablar(). 
El bucle recorre la lista y llama a hablar() sobre cada objeto. Cada uno responde de manera distinta, demostrando polimorfismo dinámico sin herencia. 
Esto refleja el espíritu de “si se comporta como un pato… es un pato”.
""")
        
    def exercise_51(self):
        print("7.1 crear una App que genere animales con métodos iguales (implementados de diferente manera), cargarlos a una lista y ejecutar un método usando las bondades del Duck Typing.")
        print("\n")
        
        class Perro:
            def hablar(self):
                print("Guau!")

        class Gato:
            def hablar(self):
                print("Miau!")

        class Loro:
            def hablar(self):
                print("Hola! Soy un loro")

        class Dinosaurio:
            def hablar(self):
                print("¡Rawr!")

        animales = [Perro(), Gato(), Loro(), Dinosaurio()]

        for animal in animales:
            animal.hablar()
        
            
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