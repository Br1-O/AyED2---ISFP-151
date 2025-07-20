import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 0.0

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  Dar un ejemplo de la Regla del Boy scout que Plantea Robert. C. Martin")
        print("\n")
        print("""
La regla del Boy Scout, planteada por Robert C. Martin, sugiere que cada vez que interactuamos con una parte del sistema, 
deberíamos dejarla mejor de lo que la encontramos. 
Por ejemplo, si estamos modificando una función para arreglar un bug, 
y notamos que su nombre no es claro o su estructura es confusa, deberíamos aprovechar para mejorarla. 
No se trata de rehacer todo, sino de pequeñas mejoras constantes que mantienen el sistema saludable.
              """)
    
    def exercise_2(self):
        print("2.  Que entiende por “The Software Crafsman")
        print("\n")
        print("""
Se refiere al desarrollador que actúa como un verdadero artesano del código. 
Esta persona no solo cumple con los requisitos funcionales de un sistema, sino que se esfuerza por escribir código limpio, comprensible y mantenible. 
Entiende que el desarrollo de software es tanto un arte como una técnica, y prioriza la mejora continua, 
el aprendizaje y la calidad como valores esenciales de su profesión.
              """)

    def exercise_3(self):
        print("3. Explicar el Manifiesto Software Craftsman ")
        print("\n")
        print("""
Este manifiesto es una extensión, e incluso desafio, del Manifiesto Ágil que pone foco en el profesionalismo, la maestría y la responsabilidad. 
Valora no solo entregar software que funcione, sino entregar software bien hecho.
Además, promueve la colaboración con los clientes más allá de los contratos, 
y la construcción de una comunidad de profesionales comprometidos con la excelencia.
              """)
        
    def exercise_4(self):
        print("4.  Que entiende por Código Limpio")
        print("\n")
        print("""
El código limpio es aquel que resulta fácil de leer, entender, mantener y mejorar. 
Debería tener nombres descriptivos, estructuras simples, funciones pequeñas y sin duplicación innecesaria. 
No se trata solo de que funcione, sino de que cualquier otro desarrollador pueda leerlo y entender qué hace sin esfuerzo. 
Es el reflejo de un trabajo bien hecho y pensado.
              """)
    
    def exercise_5(self):
        print("5.  Que piensa que se requiere para escribir código Limpio")
        print("\n")
        print("""
Es necesario compromiso, disciplina y conciencia profesional. 
También se requiere conocimiento técnico, experiencia y buenas prácticas adquiridas con el tiempo. 
Pero sobre todo, se necesita voluntad de mejorar continuamente, de pensar en los demás que van a leer el código, 
de prestar atención hasta al más minimo detalle para que todo el conjunto sea limpio, y no sólo aquello que creemos que se verá.
Básicamente de escribir como si estuviéramos contando una historia, con cuidado a cada detalle, de principio a final.
              """)

    def exercise_6(self):
        print("6.  Realizar una “Reflexión” sobre la Cita del autor: “En software, el 80% o más de lo que hacemos se llama curiosamente “Mantenimiento”: el acto de reparar...”")
        print("\n")
        print("""
La cita remarca que la mayor parte del trabajo de un desarrollador es mantener el código ya existente. 
Por eso, si el código no está limpio desde el inicio, su mantenimiento se vuelve más costoso y problemático. 
Esta realidad hace que la calidad del código no sea una opción, sino una necesidad para el futuro del sistema.
              """)

    def exercise_7(self):
        print("7.  Relacionar el TPM y el Desarrollo de software.")
        print("\n")
        print("""
TMP es un enfoque de calidad llamado "Mantenimiento Productivo Total". Se centra en el mantenimiento más que en la producción. 
Uno de los pilares principales de TPM son el conjunto de los llamados principios 5S. 5S es un conjunto de "disciplinas“. 
              
• Seiri u organización: Saber dónde están las cosas: usar enfoques como la denominación adecuada, es crucial. ¿Crees que nombrar identificadores no es importante?.
• Seiton, o tidiness: Un lugar para cada cosa y cada cosa en su lugar. Un fragmento de código debe estar donde espera encontrarlo y, 
si no es así, debe volver a factorizarlo para llegar allí.
• Seiso, o limpieza: mantenga el lugar de trabajo libre de desechos y desperdicios. 
¿Qué dicen los autores aquí sobre tirar basura código con comentarios y líneas de código comentadas que capturan el historial o los deseos 
del futuro? Deshazte de ellos.
• Seiketsu, o estandarización: el grupo acuerda cómo mantener limpio el lugar de trabajo.
• Shutsuke o disciplina: Esto significa tener la disciplina, autodisciplina, para seguir las prácticas y reflexionar con frecuencia sobre el trabajo de uno y estar dispuesto a cambiar.

Así, el profesionalismo responsable en una profesión que debe preocuparse por el ciclo de Vida de un producto. 
Dado que se mantienen automóviles y otras máquinas bajo TPM, trabajar en la avería el mantenimiento, a la espera de que aparezcan errores, es la excepción. 
En cambio, TMP sube un nivel: inspeccione las máquinas todos los días y repare las piezas de desgaste antes de que se rompan.

En código, refactorizar sin piedad. 
Puede mejorar un nivel más, escriba código más fácil de mantener en primer lugar. Haciendo su código legible es tan importante como hacerlo ejecutable.
Y quizá incluso considerar rehacerlo cada X cantidad de tiempo desde cero, para limpiar la acumulación de código ad-hoc agregado a posteriori, 
comentarios y dejos de refactorizaciones pasadas.
              """)
    
    def exercise_8(self):
        print("8.  ¿Qué entiende por Profesionalismo Responsable?")
        print("\n")
        print("""
Se refiere a asumir la responsabilidad de lo que se produce, no solo entregando a tiempo sino con calidad. 
Un profesional responsable no se escuda en las excusas, sino que busca siempre hacer lo correcto, incluso cuando nadie lo está mirando. 
Esto incluye desde escribir buen código hasta comunicar de forma clara y trabajar en equipo.
En desarrollo de software sería apegarse a las buenas prácticas, desarrollo en base a código limpio,
documentar apropiadamente nuestro código, y enfocarnos en la legibilidad, mantenibilidad y escalabilidad.
              """)

    def exercise_9(self):
        print("""
9.  Desarrollar los conceptos de Código Limpio por: 
    a.  Bjanrne Stroustrup 
    b.  Grady Booch 
    c.  Dave Thomas
""")
        print("\n")
        print("""
Bjarne Stroustrup: 
    Destaca que el código limpio hace lo que debe hacer, bien y de forma simple y eficiente.
    Pero así mismo destaca que el código debe hacernos sonreir, sentir bien al leerlo, es elegante y agradable a la vista.
    No debe 'tentar' a otros a obrar erroneamente sobre él, como harían si vieran falta de atención al detalle o malas prácticas en él.
    Debe prestar atención al detalle y estar enfocado en su tarea, haciendo una y sólo una cosa bien.
              
Grady Booch: 
    Lo compara con la prosa bien escrita: debe ser elegante, clara y eficaz.
    Nuestro código debe ser práctico en lugar de especulativo. Debe contener solo lo necesario. 
    Nuestros lectores deberían percibir que hemos sido decisivos al momento de la Codificación.
    Así, destaca la legibilidad diciendo que el código limpio debe ser simple y directo, y no debería oscurecer nuestra intenciones.
    Nuestro código debería tener abstracciones nítidas y lineas sencillas de control.

Dave Thomas: 
    Resalta que debe ser fácil de leer y comprender, como si estuviera contando una historia sencilla.
    El código debe ser alfabetizado, dependiente del idioma en que se lee, destacando la legibilidad. 
    Pero, así mismo, debe ser fácil de cambiar o extender en funcionalidades para otra persona que no sea su desarrollador.
    Menciona las pruebas unitarias y de aceptación como un método de fácilitar esto, y que sin ellas el código no puede ser realmente limpio.
              """)
        
    def exercise_10(self):
        print("10.  Que entiende Por Diseño y Arquitectura, relacionarlos.")
        print("\n")
        print(""" 
Podría pensarse en el diseño como el detalle fino (cómo se organizan los métodos, clases, etc.),
la implementación y detalles. Y aunque en algunos casos es aceptado, muchos sostienen que esto no es así, 
y que en realidad diseño y arquitectura son lo mismo, ya que la arquitectura debería abarcar el todo y plantear el cómo de los detalles.
La arquitectura es la estructura general del sistema. 
Define la forma de trabajar en un sistema, como construir nuevos módulos, pero también debe dejar intuir el tipo de aplicación que describe.
Debe ayudar a expresar la intención de nuestro sistema, pero sin expresar el cómo está hecha.
Fuera de detenernos en distinciones de significados y significantes, la clave está en que trabajen juntos, tanto detalles como estructuración general, 
para garantizar la calidad del software.
              """)
    
    def exercise_11(self):
        print("11. Que Objetivos comunes deben tener las “Arquitecturas Limpias” ")
        print("\n")
        print("""
Las arquitecturas limpias deben buscar desacoplamiento, claridad, mantenibilidad, y facilidad para ser testeadas. 
Además, deben permitir la evolución del sistema con el menor impacto posible en su estructura general. 
Así, deben ser independientes de componentes externos (sean UI, bases de datos, frameworks, etc.)
Son arquitecturas pensadas para durar y adaptarse, no solo para funcionar en el corto plazo.
              """)

    def exercise_12(self):
        print("12. ¿Qué entiende Por “¿Arquitecturas de Capas”, que beneficios Tiene? ")
        print("\n")
        print("""
Se refiere a un estilo de diseño de software en el que la aplicación se organiza en diferentes niveles o capas, 
donde cada capa tiene una función específica y se comunica solo con la capa adyacente. 
Por ejemplo, una arquitectura típica puede ser una que presente a las entidades, el dominio, en el centro. 
La lógica de negocio representada mediante los casos de uso que trabajan sobre el dominio, en la capa media.
Y los componentes externos dependientes de las implementaciones y tecnologias en la capa exterior, 
comunicando a todos mediante interfaces (puertos y adaptadores)

Los beneficios de usar arquitecturas de capas incluyen:
Modularidad: Cada capa es independiente y puede ser desarrollada, modificada o probada sin afectar directamente a las otras capas.
Mantenibilidad: Facilita la identificación y solución de problemas porque el sistema está organizado en partes claras.
Reutilización: Las capas pueden ser reutilizadas en diferentes proyectos o contextos.
Separación de responsabilidades: Cada capa tiene su función definida, lo que mejora la claridad y la organización del código.
Escalabilidad: Permite que el sistema crezca o se adapte más fácilmente a nuevas necesidades sin reescribir todo el sistema.
        """)

    def exercise_13(self):
        print("13. ¿Qué es una Arquitectura Multicapa?")
        print("\n")
        print("""
Arquitectura Multicapa es un patrón de diseño que organiza un sistema software en varias capas jerárquicas, donde cada capa cumple una función específica y puede subdividirse en capas internas según la necesidad.

En un esquema típico de cuatro capas, encontramos:

Capa interna (entidades o dominio): 
    Contiene el modelo de negocio y las reglas básicas que definen la lógica del dominio.
Capa de casos de uso: 
    Aquí se encuentra la lógica propia de la aplicación, que opera sobre el dominio. 
    En este nivel se definen los puertos (interfaces) que permiten la comunicación con el exterior, 
    como Use Case Input Ports (primarios) y Use Case Output Ports (secundarios). 
    La implementación de los puertos de entrada se realiza en los Use Case Interactors.
Capa de adaptadores: 
    Incluye los controladores, presentadores y componentes que permiten interactuar con sistemas externos o presentar información.
Capa externa: 
    Comprende los dispositivos y sistemas con los que se comunica el backend, como bases de datos, interfaces de usuario u otros servicios externos.

Este enfoque es una forma de arquitectura hexagonal, con una separación clara entre el dominio y las dependencias externas, lo que facilita la mantenibilidad, la flexibilidad y la independencia tecnológica.
              """)

    def exercise_14(self):
        print("14. ¿Cuál es el Problema de Modelar como Centro los Datos?")
        print("\n")
        print("""
Enfocarse sólo en la estructura de datos puede llevar a sistemas acoplados a la base, difíciles de testear y poco flexibles. 
Las reglas de negocio quedan dispersas y atadas a detalles técnicos. Esto complica el mantenimiento y la evolución de los sistemas.
              """)

    def exercise_15(self):
        print("15. ¿Es un Problema en si modelar como centro de Datos o habrá motivos para Implementarlo?, dar ejemplos")
        print("\n")
        print("""
No necesariamente. En aplicaciones simples (como CRUDs), puede ser práctico. 
Sin embargo, en sistemas con reglas complejas, lo ideal es separar los datos del comportamiento y usar un enfoque centrado en el dominio para ganar claridad y flexibilidad.
        """)

    def exercise_16(self):
        print("16. Explicar las Onion Architecture (Arquitecturas Cebolla)")
        print("\n")
        print(""" 
Organiza el sistema en capas concéntricas donde el corazón es el dominio. 
Las capas externas (como infraestructura o UI) interactúan con el sistema sin afectar el núcleo. 
Esto permite expresar la lógica de negocio sin depender de detalles externos como bases de datos o frameworks.
              """)
    
    def exercise_17(self):
        print("17. ¿Qué diferencia tiene un Diseño de Construcción en torno a un Modelo de Dominio?")
        print("\n")
        print("""
Modelar desde el dominio implica pensar en las reglas del negocio, actores y comportamientos. 
Esto genera sistemas más robustos y mantenibles. Modelar desde los datos se enfoca en estructuras estáticas que suelen ser menos adaptables y claras.
              """)

    def exercise_18(self):
        print("18. ¿Qué beneficios Presenta respecto a los Modelos Centrados en Datos?")
        print("\n")
        print("""
Permite reflejar mejor la realidad del negocio, es más flexible a cambios, mejora la comunicación con usuarios y facilita pruebas. 
Además, permite tener reglas claras y bien encapsuladas en el sistema.
        """)

    def exercise_19(self):
        print("19. ¿Que entiende por Arquitecturas Hexagonales?")
        print("\n")
        print("""
También conocida como "puertos y adaptadores". 
Propone que el núcleo de la aplicación, que contiene a las entidades y modelos del negocio (dominio), 
se comunique con los casos de uso (aplicación), y ella se conecte a la capa exterior, donde reciden las implementaciones y código dependiente de tecnologias (infraestructura), 
a través del uso de interfaces (puertos) y adaptadores concretos. 
Permite alta flexibilidad y facilidad de testeo.
              """)

    def exercise_20(self):
        print("20. ¿Qué diferencia Plantea con las Onion Architecture? ")
        print("\n")
        print("""
Mientras Onion se estructura por capas concéntricas, Hexagonal se estructura por la interacción con el exterior. 
Ambos protegen el core del sistema, pero Hexagonal es más explícita respecto a entradas y salidas, 
y en especifico en cómo las capas más internas no pueden depender de las capas más externas, y de hecho las desconocen por completo, 
al comunicarse por medio de interfaces. Así mismo pone mayor enfasis en ésta inversión de dependencias, 
al establecer que se debe depender de interfaces, y no de otras capas de forma directa.
              """)

    def exercise_21(self):
        print("21. Que entiende Por “Puertos y Adaptadores”")
        print("\n")
        print("""
"Puertos y Adaptadores" (también conocida como Arquitectura Hexagonal) es un enfoque de diseño que busca desacoplar el núcleo de la aplicación 
(el dominio y los casos de uso) de las tecnologías externas que la rodean (como bases de datos, interfaces gráficas, servicios web, etc.).

Los puertos son interfaces que definen cómo puede comunicarse el mundo externo con la aplicación, o viceversa. 
Pueden ser de entrada (input ports), usados por controladores o interfaces de usuario, o de salida (output ports), 
usados por la aplicación para interactuar con servicios externos.

Los adaptadores son las implementaciones concretas de esos puertos, 
que permiten conectar el código del dominio con tecnologías externas específicas. 
Por ejemplo, un adaptador puede traducir una solicitud HTTP en una llamada a un caso de uso, 
o implementar un acceso a base de datos siguiendo la interfaz de un repositorio.

Así, el núcleo del sistema no depende de nada externo. Solo conoce interfaces.
        """)

    def exercise_22(self):
        print("22. ¿Cómo funcionan estos Componentes?")
        print("\n")
        print(""" 
El flujo básico de funcionamiento es el siguiente:

    1. Un adaptador de entrada (como un controlador web o una interfaz de línea de comandos) recibe una solicitud externa.

    2. Ese adaptador llama a un puerto de entrada (Input Port), que está definido como una interfaz que representa un caso de uso del sistema.

    3. El interactor es la implementación de ese puerto, y ejecuta la lógica del caso de uso sobre el modelo de dominio.

    4. Si el caso de uso necesita comunicarse con algo externo (como una base de datos, un API, o un sistema de archivos), 
    lo hace a través de un puerto de salida (Output Port), otra interfaz.

    5. Finalmente, un adaptador de salida implementa ese puerto y realiza la acción concreta (por ejemplo, hacer una consulta SQL o enviar un email).

Este esquema garantiza que el núcleo del sistema no depende de detalles externos, solo de abstracciones. 
Es decir, el dominio depende de puertos (interfaces), y los adaptadores dependen del dominio, no al revés. 
Esta inversión de dependencias permite testear la lógica de negocio sin necesidad de base de datos, servidor o entorno gráfico.
              """)
    
    def exercise_23(self):
        print("23. Que significa que “...nuestro core queda completamente desvinculado del exterior”")
        print("\n")
        print("""
Significa que el núcleo del sistema no depende de ningún detalle técnico como frameworks, drivers o librerías externas. 
Esto facilita su evolución, pruebas y reutilización en otros contextos, 
al no necesitar ser cambiado con el cambio de cada una de las tecnologias o implementaciones que se usaran en su definición.
Todo esto gracias al uso polimorfico de interfaces para desacoplar las diferentes capas.
              """)

    def exercise_24(self):
        print("24. ¿Que determina la cantidad de Puertos en esta Arquitectura")
        print("\n")
        print("""
Depende de la cantidad de interacciones necesarias entre el core y el exterior. 
Cada puerto representa una necesidad específica de entrada o salida (como repositorios, servicios externos, etc.).
        """)

    def exercise_25(self):
        print("25. ¿Qué se entiende por Puertos Primarios y Secundarios")
        print("\n")
        print("""
Los puertos primarios y secundarios son:
              
    Puertos primarios (o de entrada):
        Representan las acciones que el exterior (como una interfaz gráfica, una API o una CLI) puede invocar sobre la aplicación. 
        Es decir, son el punto de entrada para ejecutar un caso de uso.
        Se definen como interfaces (por ejemplo, ICrearUsuario, IProcesarCompra) y sus implementaciones están en los Use Case Interactors.

    Puertos secundarios (o de salida):
        Son las interfaces que la aplicación necesita para comunicarse con el exterior, como guardar datos, enviar correos, consultar servicios externos, etc.
        El núcleo define lo que necesita (IRepositorioDeUsuarios, INotificador), pero no sabe cómo se implementa, 
        ya que esa parte queda delegada a los adaptadores de salida (como una clase que conecta con la base de datos o con un servicio externo).
              """)

    def exercise_26(self):
        print("26. Realizar un Resumen a “Modo de Cierre” de la Diapositiva de Conclusiones. ")
        print("\n")
        print("""
La calidad del software no se mide solo en funcionalidad. 
Debemos pensar en mantenibilidad, claridad y profesionalismo. 
Y los modelos por capas que hemos visto fácilitan eso, 
casi volviendose un estandar en la industria para aplicaciones a gran escala que se beneficien de aplicarla.
La arquitectura debe facilitar ese camino de legibilidad, mantenibilidad y escalabilidad. 
Y al elegir y desarrollar nuestra propia arquitectura en un sistema debemos tener siempre en cuenta esto, 
y que ella será un modo de organizar, estructurar, y pensar qué y cómo hará las cosas nuestro software.
Pero siempre en vistas del cambio y evolución, no deteniendonos así en implementaciones o tecnologias, 
sino en el modo en que se organizarán, relacionaran y desarrollaran las cosas dentro de nuestro sistema.
              """)

    def exercise_27(self):
        print("27. Relacionar Software Craftsman, Code Clean y Clean Arquitecture. ")
        print("\n")
        print("""
Un buen desarrollador, también llamado Software Craftsman, no se limita a que el código funcione,
se compromete con la calidad, la mejora continua y el desarrollo de software como una disciplina profesional. 
Es alguien que ve el código como un arte que requiere técnica, cuidado y responsabilidad.

Este enfoque va de la mano con los principios de Clean Code, que promueven escribir código claro, legible, simple, y fácil de mantener. 
Un código limpio no solo es más fácil de entender para otros desarrolladores, 
sino que también reduce los errores, facilita el testing y acelera la evolución del sistema.

Así mismo, Clean Architecture propone una estructura sólida y desacoplada, donde las decisiones técnicas 
(como frameworks, bases de datos, APIs externas) están en los bordes, y el dominio del negocio está en el centro. 
Esto permite que el sistema sea duradero, flexible ante cambios y resistente al paso del tiempo.

Cuando estos tres enfoques se combinan, se potencia la creación de sistemas que no solo funcionan, sino que se pueden mantener con bajo costo y sin miedo.
Son fáciles de testear y escalar, y reflejan un compromiso ético del desarrollador con su equipo, su cliente y el producto final.

En conjunto, Software Craftsmanship, Clean Code y Clean Architecture forman una base para construir software profesional, ético y sostenible, 
pensado para crecer sin volverse una carga técnica en el futuro.
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