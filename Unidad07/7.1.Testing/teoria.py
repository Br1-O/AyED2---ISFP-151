import os

#■■■■■■■■■■ Guía Número ■■■■■■■■■■:
assignmentNumber = 7  # Unidad 7 - Testing, CMake y GTest

#■■■■■■■■■■ Listado de ejercicios ■■■■■■■■■■:
class Exercises:

    def exercise_1(self):
        print("1. Que entiende por Proceso de Testing?. ¿Que Busca?")
        print("\n")
        print("""
El proceso de testing es el proceso de verificación y validación de que el software o la aplicación no tienen
errores, cumplen con los requisitos técnicos guiados por su diseño y desarrollo, y satisfacen los requisitos del
usuario de manera efectiva y eficiente (manejando casos excepcionales y límite).

Se divide en dos pasos fundamentales:
- Verificación: conjunto de tareas que aseguran que el software implemente correctamente una función específica
  ("¿Estamos construyendo el producto correctamente?").
- Validación: conjunto de tareas que garantizan que el software construido sea rastreable según los requisitos del
  cliente ("¿Estamos construyendo el producto correcto?").

¿Qué busca?
No solo busca encontrar fallas o errores en el software existente al ejecutarlo, sino también medir la
especificación, funcionalidad y rendimiento, y encontrar medidas para mejorar el software en términos de
eficiencia, precisión y usabilidad.
              """)

    def exercise_2(self):
        print("2. Dar ejemplos de Pruebas de Caja Negra y Blanca.")
        print("\n")
        print("""
- Prueba de Caja Negra (basada en datos / validación): no requiere conocer el funcionamiento interno ni el
  código fuente; se enfoca en las entradas y salidas requeridas en la interfaz.
  Ejemplo: probar una función de suma o un formulario/sistema ingresando valores de entrada (por ejemplo,
  sumar 5 y 5) y verificando que la salida esperada sea 10 sin inspeccionar cómo está codificada la función
  internamente.

- Prueba de Caja Blanca (estructural / verificación): exige conocer el funcionamiento interno y tener acceso
  al código fuente para verificar que las operaciones internas se ejecuten según las especificaciones.
  Ejemplo: revisar la estructura interna de un bucle, una condición, la precedencia aritmética o la
  inicialización de variables dentro de una función o método (como verificar cómo `accelerate` o `brake`
  modifican `speed` y `BRAKING_FACTOR` en `Car.cpp`) para comprobar dominios de datos y límites internos.
              """)

    def exercise_3(self):
        print("3. Describir los Distintos niveles de Pruebas y dar ejemplos de estos niveles.")
        print("\n")
        print("""
1. Prueba unitaria: se prueban unidades o componentes individuales de software (la unidad más pequeña de
   diseño) para validar que cada unidad funcione según lo diseñado.
   Ejemplo: verificar de forma aislada si una función `sum(a, b)` o un método como `accelerate(intensity)`
   funciona correctamente con entradas de muestra.

2. Prueba de integración: las unidades individuales ya probadas se combinan y prueban en grupo para exponer
   fallas en la interacción entre unidades integradas.
   Ejemplo: integrar módulos o componentes probados por unidad (por ejemplo, combinar módulos de personal,
   estudiantes y finanzas o enlazar funciones y clases de una librería) para comprobar que interactúan bien
   (mediante enfoques arriba-abajo, abajo-arriba, sándwich o Big-Bang).

3. Prueba del sistema: se prueba el sistema o software completo e integrado para evaluar el cumplimiento con
   los requisitos especificados en distintos sistemas operativos (abarcando pruebas funcionales y no funcionales).
   Ejemplo: probar la aplicación completa ya integrada en el sistema operativo objetivo verificando requisitos
   funcionales y no funcionales (rendimiento, seguridad, recuperación, estrés).

4. Prueba de aceptación: evalúa la aceptabilidad del sistema y su cumplimiento con los requisitos comerciales para
   determinar si es aceptable para la entrega.
   Ejemplo: pruebas de aceptación internas de calidad (Prueba Alfa) antes de entregar al cliente, o pruebas
   realizadas por usuarios finales en entornos en tiempo real o sitios del cliente (Prueba Beta).
              """)

    def exercise_4(self):
        print("4. Describir (brevemente) los distintos Tipos de Testing.")
        print("\n")
        print("""
Las pruebas pueden ser manuales (sin scripts ni herramientas automatizadas, asumiendo rol de usuario o
explorando) o automatizadas (usando scripts y herramientas para repetir escenarios, regresión, carga,
rendimiento y estrés). Según el material, los tipos principales son:

1. Prueba unitaria: evalúa la unidad mínima de código (bucle, método o función) con entradas y salidas.
2. Prueba de integración: verifica la combinación e interacción entre componentes ya probados unitariamente.
3. Prueba de regresión: asegura que el programa y sus componentes existentes sigan funcionando bien tras
   agregar nuevos módulos o realizar cambios.
4. Prueba de humo (Smoke test): pasada inicial rápida para comprobar que el build o módulo básico arranca y
   está estable antes de continuar con más pruebas.
5. Prueba alfa: prueba de validación/aceptación realizada antes de entregar el producto, habitualmente de
   forma interna por control de calidad.
6. Prueba beta: realizada por usuarios finales en número limitado y en entornos reales o del cliente.
7. Prueba del sistema: evalúa el sistema completo e integrado frente a los requisitos (funcionales y no
   funcionales) y sistemas operativos.
8. Prueba de estrés: somete al sistema a condiciones desfavorables o extremas (máxima memoria, sobrecarga en
   SO virtual o exigencia excesiva de disco) para ver cómo responde.
9. Pruebas de rendimiento: mide velocidad, eficacia y comportamiento en tiempo de ejecución bajo una carga
   dada (también llamada prueba de carga).
10. Pruebas orientadas a objetos: combina técnicas para verificar y validar software OO a lo largo de
    requisitos, diseño, código, integración, sistema y usuario.
              """)

    def exercise_5(self):
        print("5. Relacionar los Principios de Pruebas y las Directrices.")
        print("\n")
        print("""
Los 7 principios y las directrices de prueba se complementan de forma directa:

- "Las pruebas muestran la presencia de defectos" <-> "El software nunca puede estar completamente libre de errores":
  ninguna serie de pruebas garantiza un sistema completamente libre de fallas; solo evidencian defectos y reducen
  su presencia.
- "No es posible realizar pruebas exhaustivas" <-> "El tiempo disponible es limitado" y "Priorizar secciones":
  probar todas las entradas y combinaciones es impráctico y el tiempo es finito, por lo que hay que priorizar
  secciones críticas según riesgo y definir criterios de corte.
- "Pruebas tempranas" <-> "Comience lo antes posible": iniciar las pruebas desde el análisis de requisitos
  reduce costos y evita la migración de defectos a etapas avanzadas.
- "Agrupación de defectos" (regla 80/20: ~80 porciento de defectos en ~20 porciento de módulos) <-> "Priorizar secciones":
  concentrar esfuerzos tempranos y prioritarios en los módulos críticos o propensos a fallos.
- "Paradoja de los pesticidas" <-> "Entradas inesperadas y negativas" y "Validación de supuestos": repetir
  siempre los mismos casos no descubre fallos nuevos; hay que actualizar/ampliar casos, incluir entradas
  negativas/inesperadas y no basarse en supuestos no validados.
- "Las pruebas dependen del contexto" <-> "Inspección adecuada de los resultados": cada tipo de software
  requiere enfoques adaptados a su contexto y una evaluación cuantitativa respaldada por documentación y
  automatización.
- "Falacia de ausencia de errores" <-> "El equipo de desarrollo debe evitar probar el software": un producto
  puede tener pocos errores técnicos pero no servir si no cumple los requisitos del usuario; además, contar con
  evaluadores externos/independientes al desarrollo evita el sesgo de "propietario".
              """)

    def exercise_6(self):
        print("6. ¿Que es un Plan de Pruebas? Dar un ejemplo.")
        print("\n")
        print("""
Un Plan de Pruebas de software es el documento elaborado para cumplir los objetivos de calidad de un
desarrollo, definiendo módulos o funcionalidades a verificar, alcance, estrategia, tipos de pruebas, criterios
de aceptación/inicio/suspensión, entornos, infraestructura, recursos/personal y planificación.
Sus cinco pasos principales son:
1) Analizar los requerimientos de desarrollo de software.
2) Identificar las funcionalidades nuevas a probar.
3) Identificar las funcionalidades de sistemas existentes impactadas a probar.
4) Definir la estrategia de pruebas (por ejemplo, según el marco del ISTQB).
5) Definir los criterios de inicio, aceptación y suspensión de pruebas.

Ejemplo:
En una iteración de un sistema de gestión académico/escolar donde se agrega un módulo de finanzas y se
modifica la lógica compartida de legajos:
- Alcance y funcionalidades: probar el nuevo módulo de finanzas y aplicar pruebas de regresión sobre los
  módulos existentes de personal y estudiantes impactados.
- Estrategia: pruebas unitarias, de integración y de regresión.
- Criterios: iniciar cuando el entorno esté instalado y pase la verificación inicial; aceptar si el 100% de
  los casos clave pasan sin incidencias y al menos el 20% de los casos borde; suspender si se bloquean todos
  los casos por una incidencia crítica.
              """)

    def exercise_7(self):
        print("7. Para que sirve CMake")
        print("\n")
        print("""
CMake ("cross platform make") es un sistema extensible, libre y de código abierto que gestiona y automatiza
el proceso de compilación/construcción de proyectos de C/C++ de forma multiplataforma e independiente del
compilador, trabajando junto con el entorno de compilación nativo (como Makefiles en Unix/MinGW o proyectos
de Visual Studio / Xcode).
              """)

    def exercise_8(self):
        print("8. Que resuelve?")
        print("\n")
        print("""
Resuelve la necesidad de configurar y automatizar la compilación en distintos sistemas operativos y
compiladores sin acoplarse a un único archivo de compilación manual, soportando:
- Jerarquías de directorios complejas y aplicaciones que dependen de múltiples bibliotecas.
- Compilación de código fuente, bibliotecas estáticas o dinámicas, ejecutables y generación de código previo
  a la compilación final.
- Compilaciones fuera de lugar (por ejemplo, en una carpeta `build` separada del código fuente), múltiples
  configuraciones en paralelo y reutilización de información mediante la caché (`CMakeCache.txt`).
              """)

    def exercise_9(self):
        print("9. Que es el CMakeLists.Txt")
        print("\n")
        print("""
Es el script de configuración en texto plano que se coloca en el directorio raíz y en los directorios/
subdirectorios de un proyecto CMake. Contiene comandos de la forma `COMANDO(args...)` (y
comentarios con `#`) que definen la versión mínima requerida, el nombre del proyecto, los archivos fuente,
bibliotecas, subdirectorios y los "destinos" (targets: ejecutables, bibliotecas o pruebas) que CMake
utilizará durante los pasos de configuración y generación.
              """)

    def exercise_10(self):
        print("10. Describir las Instrucciones de Tunelización y Compilación para generar Exes.")
        print("\n")
        print("""
En el flujo de CMake desde línea de comandos (separando carpeta fuente y carpeta binaria):

1. Crear y entrar a la carpeta binaria (por ejemplo, `build`) para mantener limpio el código fuente:
     mkdir build
     cd build

2. Ejecutar `cmake` indicando el generador (`-G`) y la ruta a la carpeta fuente (`..`), lo cual ejecuta el
   paso de configuración (lee `CMakeLists.txt` y crea la caché) y el paso de generación (crea la
   canalización de compilación, como Makefiles):
     cmake -G "MinGW Makefiles" ..

3. Invocar la herramienta de compilación nativa (por ejemplo, `make` o `make -j8`) para compilar y enlazar
   los objetivos definidos en `CMakeLists.txt` y generar los binarios/ejecutables (`.exe` en Windows):
     make
     make Uno / make Principal / make runUnitTests
              """)

    def exercise_11(self):
        print("11. Que es un Framework de Prueba?")
        print("\n")
        print("""
Es un marco de trabajo (como `googletest` / GTest, basado en la arquitectura xUnit) que provee estructura,
macros y utilidades para escribir, organizar, aislar y ejecutar pruebas automatizadas en C++.
Aísla cada prueba en su propio objeto para que sean independientes y repetibles, agrupa pruebas relacionadas
en conjuntos (TestSuite) o fixtures, funciona en múltiples plataformas y compiladores, notifica fallos con
detalle sin frenar necesariamente la ejecución completa, gestiona el registro de pruebas y permite
reutilizar recursos compartidos.
              """)

    def exercise_12(self):
        print("12. Que es una Prueba Unitaria en GTest?")
        print("\n")
        print("""
En GTest, una prueba unitaria se define habitualmente mediante la macro `TEST(NombreSuite, NombrePrueba)`
(donde `NombreSuite` agrupa pruebas relacionadas y `NombrePrueba` identifica el caso individual).
Su función es ejercitar una ruta particular del programa o unidad de código (una función, método o clase)
con valores de entrada específicos y verificar mediante afirmaciones (`EXPECT_*` / `ASSERT_*`) si el resultado
obtenido coincide con el esperado.
              """)

    def exercise_13(self):
        print("13. Que “Macros” tenemos y podemos usar en GTest?")
        print("\n")
        print("""
En GTest disponemos de macros de prueba como `TEST(...)` y macros de afirmación divididas en dos familias:
- `EXPECT_*`: generan fallas no fatales (no abortan la función actual y permiten detectar múltiples fallas
  en una misma prueba; suelen preferirse cuando es útil seguir evaluando).
- `ASSERT_*`: generan fallas fatales (abordan la función actual de inmediato si fallan; conviene usarlas
  cuando no tiene sentido continuar, cuidando posibles fugas de recursos si se salta limpieza).

Entre las macros de afirmación vistas se encuentran:
- Igualdad y comparaciones relacionales: `EXPECT_EQ`, `ASSERT_EQ`, `EXPECT_NE`, `ASSERT_NE`, `EXPECT_LT`,
  `ASSERT_LT`, `EXPECT_LE`, `ASSERT_LE`, `EXPECT_GT`, `ASSERT_GT`, `EXPECT_GE`, `ASSERT_GE`.
- Booleanas: `EXPECT_TRUE`, `ASSERT_TRUE`, `EXPECT_FALSE`, `ASSERT_FALSE`.
- Cadenas (C-strings): `EXPECT_STREQ`, `ASSERT_STREQ`, `EXPECT_STRNE`, `ASSERT_STRNE`, `EXPECT_STRCASEEQ`,
  `ASSERT_STRCASEEQ`, `EXPECT_STRCASENE`, `ASSERT_STRCASENE`.
(Además admiten mensajes personalizados concatenados con `<<`).
              """)

    def exercise_14(self):
        print("14. Dar un ejemplo de Equal y Assert.")
        print("\n")
        print("""
Ejemplo usando macros de igualdad (`EXPECT_EQ` / `ASSERT_EQ`):

  TEST(Suma, Prueba) {
      EXPECT_EQ(10, sum(5, 5));
      EXPECT_EQ(50, sum(20, 30));
  }

Ejemplo combinando `ASSERT_EQ` y `EXPECT_EQ` con mensaje personalizado (`<<`):

  ASSERT_EQ(x.size(), y.size()) << "Vectors x and y are of unequal length";
  for (int i = 0; i < x.size(); ++i) {
      EXPECT_EQ(x[i], y[i]) << "Vectors x and y differ at index " << i;
  }

Aquí `ASSERT_EQ` aborta la prueba si los tamaños difieren (no tendría sentido recorrer índices distintos),
mientras que `EXPECT_EQ` verifica cada elemento e informa las diferencias sin detener el resto del bucle.
              """)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■■■■■■■■■■ De acá para abajo sólo es la definición de clases y funciones para el manejo del menú ■■■■■■■■■■

class Assignment():
    assignmentNumber: float = assignmentNumber
    
    def __init__(self):
        self.exercise_instance = Exercises()
        self.exercises = []

        exercise_methods = [
            (int(name.split("_")[1]), getattr(self.exercise_instance, name))
            for name in dir(self.exercise_instance)
            if callable(getattr(self.exercise_instance, name)) and name.startswith("exercise_")
        ]
        exercise_methods.sort(key=lambda x: x[0])
        self.exercises = [method for _, method in exercise_methods]
        self.totalExercises: int = len(self.exercises)

def isNum(num):
    while(num.isdigit() == False):
        print("No es un dato valido.\n")
        num = input("Ingrese un numero natural entero:")
    return int(num)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    assignment_instance = Assignment()
    assignmentNumber = assignment_instance.assignmentNumber
    totalExercises = assignment_instance.totalExercises
    exercises = assignment_instance.exercises

    option = ""
    global y
    y = True

    chars_per_line = 70
    
    while y:
        option = input("\n" +
                     "═"*chars_per_line + 
                     "\n" + 
                     f"Elija el número de pregunta teórica a revisar (del 1 al {totalExercises})".center(chars_per_line) + 
                     "\n" + 
                     "O ingrese cualquier otro numero para salir: ".center(chars_per_line) + 
                     "\n" + 
                     "═"*chars_per_line + 
                     "\n")
        option = isNum(option)
        
        if 1 <= option <= totalExercises:
            clear_console()
            print("\n" + f"( Pregunta {option} )".center(chars_per_line, "═") + "\n")
            exercises[option - 1]()
        else:
            break

    print(f"""
    ################   Teoría Unidad {assignmentNumber} finalizada.   ####################
    """)
    y = False

def main():
    menu()

if __name__ == "__main__":
    main()