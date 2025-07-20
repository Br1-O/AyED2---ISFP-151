import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 1.3

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1.  ¿Cómo se desarrolla o que aspectos hay que tener en cuenta cuando trabajamos en sistemas Colaborativos?")
        print("\n")
        print("""
Trabajar en sistemas colaborativos implica organizar bien las tareas, 
tener control sobre las versiones del código y facilitar la comunicación entre todos los que participan del proyecto. 
Es fundamental definir cómo se sincroniza el trabajo, cómo se integran los cambios y qué herramientas se van a utilizar para evitar conflictos. 
Por eso, se recomienda usar un sistema de control de versiones como Git o SVN, 
que permiten que varios desarrolladores trabajen sobre los mismos archivos sin pisarse el trabajo, incluso si están en lugares distintos.
              """)
    
    def exercise_2(self):
        print("2.  ¿Porque es importante la Inclusión de un sistema de Subversionado?")
        print("\n")
        print("""
Un sistema de subversionado permite llevar un registro detallado de todos los cambios realizados en el código a lo largo del tiempo. 
Esto facilita identificar errores, volver a versiones anteriores, trabajar con ramas para experimentar sin arruinar lo que ya funciona, 
y colaborar con otros sin sobrescribir el trabajo del resto. Además, mejora la organización y la trazabilidad del proyecto, 
especialmente en equipos grandes o distribuidos.
              """)

    def exercise_3(self):
        print("3.  ¿Qué es Git que características tiene?")
        print("\n")
        print("""
Git es un sistema de control de versiones distribuido. 
Su principal ventaja es que cada usuario tiene una copia completa del repositorio, 
lo que permite trabajar sin conexión a Internet. 
Es rápido, seguro y permite experimentar sin riesgo de perder información. 
Tiene una gran comunidad, integración con casi todos los entornos de desarrollo, y permite flujos de trabajo muy flexibles, 
como el uso de ramas para desarrollos paralelos.
              """)
        
    def exercise_4(self):
        print("4.  Que es SVN y que permite")
        print("\n")
        print("""
SVN (Subversion) es un sistema de control de versiones centralizado. 
Esto significa que todo el trabajo se guarda en un único servidor central, al que los desarrolladores deben conectarse para hacer cambios. 
Permite una estructura más simple y controlada del proyecto, 
especialmente útil para equipos donde es importante gestionar permisos de acceso o trabajar con archivos grandes y directorios vacíos.
              """)
    
    def exercise_5(self):
        print("5.  Establecer las Diferencias entre Git y SVN")
        print("\n")
        print("""
Git es distribuido, lo que permite trabajar sin conexión, hacer commits locales y tener múltiples repositorios. 
En cambio, SVN es centralizado y depende de una conexión permanente al servidor para realizar la mayoría de las acciones. 
Git es más rápido, flexible y potente en cuanto a ramificación (branching), 
mientras que SVN es más fácil de aprender y puede ser más útil en estructuras jerárquicas con control de accesos más detallado.
              """)

    def exercise_6(self):
        print("6.  ¿Cuándo recomendaría usar Git o SVN")
        print("\n")
        print("""
Git es ideal para proyectos con muchos colaboradores, donde se necesita trabajar offline y se quiere aprovechar la rapidez y flexibilidad de las ramas. 
SVN, en cambio, es recomendable cuando se prioriza la simplicidad, 
se requiere un control centralizado más estricto o se trabaja con archivos binarios grandes o estructuras complejas con directorios vacíos que Git no maneja bien.
              """)

    def exercise_7(self):
        print("7.  Que es GIT y que es Representa Un flujo de Trabajo")
        print("\n")
        print("""
Git es una herramienta que registra los cambios realizados sobre archivos. 
Un flujo de trabajo en Git es el conjunto de pasos que seguimos para modificar, registrar, revisar y compartir esos cambios. 
Incluye etapas como modificar archivos en tu directorio de trabajo, prepararlos en la zona de staging, 
confirmarlos al repositorio local y luego compartirlos con otros mediante un repositorio remoto como GitHub.
              """)
    
    def exercise_8(self):
        print("""
8.  Describir y Ejemplificar el Uso de; 
    a.  Working Directory Area 
    b.  Stagin Area 
    c.  Repository Area 
    d.  Que rol representa GitHub en Remote Area
""")
        print("\n")
        print("""
a. Working Directory Area: 
    Es la carpeta local donde editamos los archivos, como un proyecto en VS Code.
b. Staging Area: 
    Es el área intermedia donde preparamos los cambios antes de confirmarlos. Se usa con el comando git add.
c. Repository Area: 
    Es donde se guardan los commits (cambios confirmados), con historial completo.
d. GitHub como Remote Area: 
    GitHub actúa como repositorio remoto donde subimos (push) los cambios para compartirlos con otros,
    y también desde donde podemos bajar (pull) lo que otros hicieron.
              """)

    def exercise_9(self):
        print("9.  Que entiende por Branch (Ramas)")
        print("\n")
        print("""
Una rama en Git es una línea separada de desarrollo. 
Permite trabajar en nuevas funcionalidades o corregir errores sin afectar el código principal. 
Esto facilita experimentar, colaborar y mantener versiones estables. 
Una vez terminados los cambios, se puede hacer un merge para unir la rama con el proyecto principal.
              """)
        
    def exercise_10(self):
        print("10.  Que es Tags o sistema de Versionado")
        print("\n")
        print("""
Los tags son etiquetas que se usan para marcar puntos importantes en el desarrollo del proyecto, como una versión estable o un lanzamiento oficial. 
Sirven para identificar fácilmente estados del código que pueden ser útiles para volver atrás o distribuir públicamente, por ejemplo, 
la versión 1.0.0 de una app.
              """)
    
    def exercise_11(self):
        print("11.  Que es GitHub? ¿Que Permite o Facilita?")
        print("\n")
        print("""
GitHub es una plataforma en la nube que permite alojar repositorios Git y trabajar de forma colaborativa. 
Facilita la gestión de versiones, compartir código, revisar cambios mediante pull requests, 
y hasta publicar páginas web estáticas con GitHub Pages. 
También funciona como red social para desarrolladores y proyectos open source.
              """)
        
    def exercise_12(self):
        print("12.  Que entiende por un Repositorio GitHub (¿o similar?)")
        print("\n")
        print("""
Un repositorio en GitHub es un espacio donde se guarda todo el historial de un proyecto, incluyendo archivos, commits, ramas, tags, y más. 
Es como una copia completa del proyecto en la nube, accesible por todos los colaboradores, y sincronizable con repositorios locales.
              """)

    def exercise_13(self):
        print("13.  Que es Push y Pull en GitHub? Que permite?")
        print("\n")
        print("""
Push es el comando que usamos para subir nuestros cambios locales al repositorio remoto (GitHub). 
Pull, en cambio, baja los cambios que otros hicieron en el remoto hacia nuestro repositorio local. 
Son esenciales para sincronizar el trabajo entre varios colaboradores.
              """)
        
    def exercise_14(self):
        print("14.  Que es clonar un Repo en GitHub")
        print("\n")
        print("""
Clonar un repositorio significa descargar una copia completa del proyecto desde GitHub a tu computadora. 
Con el comando git clone, obtenés todo el historial, archivos y configuraciones para trabajar localmente desde el principio.
              """)
    
    def exercise_15(self):
        print("15.  Proponer al menos 2 alternativas a GitHub que funciones con Git, describirlas?")
        print("\n")
        print("""
GitLab: 
    Plataforma similar a GitHub, con control de versiones Git, integración continua y herramientas de DevOps. 
    Permite repositorios privados de forma gratuita.

Bitbucket: 
    De Atlassian, también permite usar Git y está muy integrada con otras herramientas como Jira. 
    Ideal para equipos que ya usan ese ecosistema.
              """)
        
    def exercise_16(self):
        print("16.  Como se trabaja en entornos colaborativos?")
        print("\n")
        print("""
Se suele trabajar mediante ramas por funcionalidad (branch per feature) y luego se proponen cambios mediante pull requests. 
Esto permite revisar y discutir código antes de integrarlo al proyecto principal. 
Se hace uso de plataformas como GitHub para coordinar, registrar el progreso, y automatizar pruebas o despliegues. 
El control de versiones y una buena comunicación son claves para que todos los miembros puedan colaborar de forma eficiente.
              """)
        
    def exercise_17(self):
        print("Crear un nuevo repo jloemig.github.io (Reemplazar x tu nombre) (y todos los puntos consecuentes al manejo de un repositorio)")
        print("\n")
        print("""
Adjunto el repositorio que cree para una página portfolio personal usando Github Pages, de manera identica a cómo se instruye en la guía:
    https://br1-o.github.io/ (cabe aclarar que posteriormente hice una re versión más visual y dinámica en: https://bruno-ortuno.vercel.app/)
Así mismo adjunto el repositorio que cree para ir guardando el material de la materia:
    https://github.com/Br1-O/AyED2---ISFP-151
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