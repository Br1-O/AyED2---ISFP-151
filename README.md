# Algoritmos y Estructuras de Datos II

Repositorio académico de la cátedra **Algoritmos y Estructuras de Datos II** (ISFT N.º 151).
Reúne el material teórico de las presentaciones, las guías de trabajos prácticos, las
resoluciones de práctica, los parciales y el trabajo práctico final.

El recorrido parte de los paradigmas y el código limpio, continúa con Python y la
programación orientada a objetos, avanza sobre patrones de diseño y buenas prácticas en
C++ moderno, y cierra con testing, CMake y arquitectura hexagonal.

## Mapa del repositorio

| Unidad / carpeta | Tema principal | Enlace |
| --- | --- | --- |
| Unidad 00 | Arquitectura y código limpio | [Unidad00](Unidad00) |
| Unidad 01 | Paradigmas, lenguajes y control de versiones | [Unidad01](Unidad01) |
| Unidad 02 | Python: lenguaje, colecciones, POO, GUI y SQLite | [Unidad02](Unidad02) |
| Unidad 02 - Kata | Code Kata / Code Dojo | [Unidad02-Kata](Unidad02-Kata) |
| Unidad 03 | Patrones de diseño | [Unidad03](Unidad03) |
| Unidad 04 | Templates, STL, SOLID y GRASP | [Unidad04](Unidad04) |
| Unidad 05 | Memoria, RAII, excepciones y punteros inteligentes | [Unidad05](Unidad05) |
| Unidad 07 | Testing y CMake | [Unidad07](Unidad07) |
| Parcial 1 | Primer parcial y práctica | [Parcial_1](Parcial_1) |
| Parcial 2 | Segundo parcial y aplicación en C++ | [Parcial_2](Parcial_2) |
| Simulación Parcial 1 | Simulación y repaso del primer parcial | [Simulacion_Parcial_1](Simulacion_Parcial_1) |
| Trabajo Práctico Final | Proyecto integrador Drone IBag151 | [Trabajo_Practico_Final](Trabajo_Practico_Final) |
| Boilerplate hexagonal | Plantilla de arquitectura hexagonal | [ExampleHexagonalArchitectureBoilerPlate](ExampleHexagonalArchitectureBoilerPlate) |
| Utilidades | Menú genérico para ejecutar ejercicios | [Utils](Utils) |

---

## [Unidad 00 — Arquitectura y Código Limpio](Unidad00)

Introduce la calidad del software desde una perspectiva profesional: qué es el diseño y la
arquitectura, por qué la complejidad es el principal enemigo y cómo se construye código
mantenible. Presenta la filosofía del **Software Craftsman**, la regla del Boy Scout, el
manifiesto del artesano de software, el profesionalismo responsable y la relación entre
TPM/5S y el desarrollo de software. También introduce la arquitectura en capas, la
arquitectura limpia, la arquitectura onion y el patrón **puertos y adaptadores**
(hexagonal), junto con conceptos de SOLID, GRASP, refactoring y testing.

### [Unidad00/CleanCode](Unidad00/CleanCode)

- Código limpio: legibilidad, nombres, funciones, estructura y mantenibilidad.
- Regla del Boy Scout, deuda técnica, refactoring y mejora continua.
- Software Craftsman y profesionalismo responsable.
- TPM, 5S y su aplicación al código.
- Diseño, arquitectura, capas y arquitectura hexagonal.
- Introducción a patrones, SOLID, GRASP y testing.
- Material: `Teoria.py`, `TP0 - Unidad 0 2024.doc.pdf` y
  `Unidad 0 Arq y Codigo Limpio 2024.pptx.pdf`.

---

## [Unidad 01 — Paradigmas, Lenguajes y Control de Versiones](Unidad01)

Presenta los paradigmas como formas de pensar y organizar la solución de problemas, y los
relaciona con los lenguajes, sus ecosistemas y las herramientas de trabajo colaborativo.
Se trabajan los paradigmas imperativo y declarativo, el estructurado, el funcional, el
lógico y el orientado a objetos, además de la calidad, la complejidad y la relación entre
paradigma y lenguaje. La unidad cierra con sistemas de control de versiones, Git, GitHub y
flujos de trabajo colaborativos.

### [Unidad01/1.1.ParadigmasDeProgramacion](Unidad01/1.1.ParadigmasDeProgramacion)

- Qué es un paradigma de programación y por qué es una filosofía de creación de programas.
- Calidad del software, atributos de calidad y complejidad.
- Paradigma imperativo frente a declarativo: el “cómo” frente al “qué”.
- Paradigma estructurado, funcional, lógico y orientado a objetos.
- Clases frente a prototipos.
- Relación entre paradigma, lenguaje y tipo de problema.
- Prácticas de Code Kata y Code Dojo.
- Material: `Teoria.py`, `TP - Unidad 1.1.pdf` y
  `Unidad 1 Paradigmas Parte I.pptx.pdf`.

### [Unidad01/1.2.Lenguajes](Unidad01/1.2.Lenguajes)

- Lenguajes más utilizados y su evolución.
- Puntos fuertes y débiles de cada lenguaje.
- Tipos de aplicaciones para los que resultan más adecuados.
- Paradigmas que soportan y frameworks representativos.
- Lenguajes compilados e interpretados, tipado y ecosistema.
- Comparación entre lenguajes y criterios de elección.
- Material: `Teoria.py`, `TP - Unidad 1.2 1.3.docx.pdf` y
  `Unidad 1 Paradigmas Parte II III.pptx.pdf`.

### [Unidad01/1.3.SVN,Git,Github](Unidad01/1.3.SVN%2CGit%2CGithub)

- Desarrollo en entornos colaborativos y sistemas de control de versiones (CVS).
- Subversion (SVN): sistema centralizado, ventajas y limitaciones.
- Git: sistema distribuido, características y modelo de trabajo.
- Diferencias entre Git y SVN y criterios para elegir uno u otro.
- Repositorios, commits, ramas (branches), etiquetas (tags) y flujos de trabajo.
- GitHub como plataforma de colaboración, publicación y revisión.
- Material: `Teoria y practica.py`, `uno.cpp`, los TP de la unidad y
  `Unidad 1 Paradigmas Parte IV V.pptx.pdf`.

---

## [Unidad 02 — Python](Unidad02)

Desarrolla el lenguaje Python desde sus fundamentos hasta la programación orientada a
objetos, la programación funcional, el manejo de archivos, los módulos, el testing y las
interfaces gráficas con SQLite. La unidad parte de la programación agnóstica del lenguaje,
explica cómo se ejecuta Python y avanza hasta aplicaciones con Tkinter y bases de datos.

### [Unidad02/2.1.IntroduccionAPython](Unidad02/2.1.IntroduccionAPython)

- Programación agnóstica del lenguaje: elegir el lenguaje por idoneidad, no por costumbre.
- Características de Python: alto nivel, interpretado, multiplataforma, multiparadigma.
- Tipado dinámico, legibilidad y filosofía del lenguaje.
- Implementación CPython, bytecode y máquina virtual de Python (PVM).
- Ecosistema de librerías y ámbitos de aplicación.
- Comparación con C++ y otros lenguajes.
- Material: `teoria.py`, `TP Unidad X1 Introduccion.docx.pdf` y
  `Unidad X1 Introduccion.pptx.pdf`.

### [Unidad02/2.2.PythonLenguaje](Unidad02/2.2.PythonLenguaje)

- Instalación de Python, IDLE, consola interactiva y ejecución de scripts.
- Repositorios de paquetes, PyPI, `pip` y gestión de dependencias.
- Entornos virtuales con `venv`.
- Variables como referencias, tipos de datos, operadores y precedencia.
- Control de flujo con `if`, `elif` y `else`.
- Material: `teoria.py`, `TP Unidad X2 Introduccion.docx.pdf`,
  `Unidad X2 Fundamentos del Lenguaje 2.1.pptx.pdf` y la versión actualizada
  [2026](Unidad02/2.2.PythonLenguaje/2026).

### [Unidad02/2.3.PythonColecciones](Unidad02/2.3.PythonColecciones)

- Tuplas, listas y diccionarios: características, mutabilidad, índices y operaciones.
- Recorrido de colecciones y métodos principales.
- Bucles `while` y `for`, `range`, `break` y `continue`.
- Estructuras de selección y comparación con `switch`/`match`.
- Funciones: definición, argumentos, paso por valor y por referencia, `*args` y `**kwargs`.
- Recursividad y funciones lambda.
- Ejercicios integradores con listas, tuplas y diccionarios.
- Material: `teoria_y_practica.py`, el TP de colecciones y
  `Unidad X2 Fundamentos del Lenguaje.pptx (1).pdf`.

### [Unidad02/2.4.PythonAspectosEstructurados](Unidad02/2.4.PythonAspectosEstructurados)

- Programación funcional: `map`, `filter`, `reduce` y funciones lambda.
- Comparación con C++ y con el enfoque estructurado.
- Excepciones: `try`, `except`, `raise` y tipos frecuentes (`TypeError`, `KeyError`,
  `IndexError`, `ZeroDivisionError`, etc.).
- Archivos: lectura y escritura.
- Módulos, paquetes, scripts de nivel superior y organización de aplicaciones.
- Testing: pruebas manuales y automáticas, `assert`, `unittest`, `setUp` y `tearDown`.
- Material: `teoria_y_practica.py`, el TP de la unidad y
  [directorioAplicacionesEjemplo](Unidad02/2.4.PythonAspectosEstructurados/directorioAplicacionesEjemplo).
  La carpeta también incluye una PPT de POO (`Unidad X3 POO Python.pptm.pdf`).

### [Unidad02/2.5.1.PythonPOO](Unidad02/2.5.1.PythonPOO)

- Clases y objetos en Python.
- Atributos de clase y de instancia.
- Constructores y método `__init__`.
- Decoradores.
- Métodos de instancia, de clase y estáticos.
- Herencia, métodos mágicos, polimorfismo y encapsulamiento.
- Composición y diseño orientado a objetos.
- Ejemplos y ejercicios con calculadora y clases del mundo real.
- Material: `teoria_y_practica.py`, `TP Unidad X3 POO.docx.pdf`,
  `Unidad X3 POO Python.pptm (1).pdf` y la versión actualizada
  [2026](Unidad02/2.5.1.PythonPOO/2026).

### [Unidad02/2.5.2.PythonTkinter&SQLite](Unidad02/2.5.2.PythonTkinter%26SQLite)

- Interfaces gráficas de usuario (GUI): concepto y elementos.
- Frameworks de GUI en Python: PyQt5, Tkinter y PySide2.
- Diferencias entre Tk y ttk.
- Widgets, `Notebook`, menús y administradores de geometría.
- Manejo de eventos y `bind`.
- SQLite: conexión desde Python, sentencias SQL, creación de tablas y CRUD.
- Aplicaciones integradas: calculadora y gestión de un “Repair Center”.
- Material: `TP Unidad X4 TKinter SQLite.docx.pdf` y
  `Unidad X4 GUI Tkintter SQLite.pptx.pdf`.

### [Unidad02/2.5.3.PythonMemoriaMutableEInmutable](Unidad02/2.5.3.PythonMemoriaMutableEInmutable)

- Tipos mutables e inmutables en Python.
- Variables como referencias a objetos en memoria.
- Comportamiento de strings, enteros, tuplas, listas y diccionarios.
- Paso de argumentos a funciones y copia de referencias.
- Implicaciones en el diseño y en la depuración de programas.
- Material: `Unidad X2 Mutables Inmutables.pptx.pdf`.

### [Unidad02-Kata](Unidad02-Kata)

- Práctica de **Code Kata** y **Code Dojo**.
- Construcción de una calculadora en C++ y en Python.
- Implementación con paradigma estructurado y con paradigma orientado a objetos.
- Análisis comparativo de lenguajes, paradigmas e implementaciones.
- Material: [kata.txt](Unidad02-Kata/kata.txt).

---

## [Unidad 03 — Patrones de Diseño](Unidad03)

Estudia los patrones de software como soluciones reutilizables a problemas recurrentes de
diseño. Se revisan los niveles de abstracción (idioms, patrones de diseño y patrones de
arquitectura) y la clasificación del GoF según el propósito: creacionales, estructurales y
de comportamiento. Cada patrón se presenta con su problema, solución, estructura y
ejemplos en C++ y Python.

### [Unidad03/3.1.PatronesCreacionales](Unidad03/3.1.PatronesCreacionales)

- Qué es un patrón de software y cómo se clasifica.
- Diferencia entre idiom, patrón de diseño y patrón arquitectónico.
- Patrones creacionales: Builder, Factory Method, Abstract Factory, Prototype y Singleton.
- Problemas que resuelven y ejemplos de aplicación.
- Laboratorio de patrones de creación.
- Material: `teoria.py`, `practica.cpp`, el TP de creación,
  `U3 P1 POO & Patrones Creacion.pdf` y `Patrones de Creacion Labs.rar`.

### [Unidad03/3.2.PatronesEstructurales](Unidad03/3.2.PatronesEstructurales)

- Patrones estructurales: Adapter, Bridge, Composite, Decorator, Facade, Flyweight y Proxy.
- Plantilla curiosamente recurrente (CRTP) y programación basada en interfaces (IBP).
- Composición de objetos y clases para formar estructuras mayores.
- Mixin-style en C++ y programación orientada a interfaces.
- Problemas que resuelve cada patrón y ejemplos.
- Material: `teoria.py`, `practica.cpp`, el TP de estructurales,
  `U3 P2 POO & Patrones Estructurales.pptx` y
  `Patrones Estructurales Labs(1).rar`.

### [Unidad03/3.3.PatronesDeComportamiento](Unidad03/3.3.PatronesDeComportamiento)

- Patrones de comportamiento: Chain of Responsibility, Command, Interpreter, Iterator,
  Mediator, Memento, Observer, State, Strategy, Template Method, Visitor y MVC.
- Comunicación entre objetos y asignación de responsabilidades.
- Ejemplos de implementación en C++ y Python.
- Material: `teoriaYPractica.cpp`, el TP de comportamiento y
  `U3 P3 POO & Patrones Comportamiento.pptx`.

---

## [Unidad 04 — Buenas Prácticas de Diseño en C++](Unidad04)

Reúne programación genérica, biblioteca estándar y principios de diseño. Se estudian
plantillas (templates), la STL, los principios SOLID y los patrones GRASP, con ejemplos en
C++ y aplicación al diseño de clases y responsabilidades.

### [Unidad04/4.1.Templates](Unidad04/4.1.Templates)

- Programación genérica y plantillas en C++.
- Plantillas de funciones y plantillas de clases.
- Parámetros de tipo y parámetros que no son de tipo.
- Parámetros predeterminados, instanciación y especialización.
- Restricciones de compilación y proyectos de varios archivos.
- Relación con la STL, `concepts` y punteros inteligentes.
- Material: `teoriaYPractica.cpp`, el TP de plantillas y
  `Unidad 4.1 Templates 2026 copy.pptx`.

### [Unidad04/4.2.STL](Unidad04/4.2.STL)

- Standard Template Library: contenedores, iteradores y algoritmos.
- Contenedores secuenciales, asociativos y adaptadores.
- Algoritmos de la STL y objetos invocables.
- Programación genérica y desacoplamiento entre datos y algoritmos.
- Ejemplos con `vector`, `map`, `list`, `array`, `sort`, etc.
- Material: [practica](Unidad04/4.2.STL/practica) con los ejemplos `1.cpp` a `4.cpp`,
  el TP de STL y `Unidad 4.1 STL Free Function Templates 2026.pptx`.

### [Unidad04/4.3.SOLID](Unidad04/4.3.SOLID)

- Buenas prácticas de desarrollo y por qué se escribe software de baja calidad.
- Principio de Responsabilidad Única (SRP).
- Principio Abierto/Cerrado (OCP).
- Principio de Sustitución de Liskov (LSP).
- Principio de Segregación de Interfaces (ISP).
- Principio de Inversión de Dependencias (DIP).
- Acoplamiento, cohesión, dependencia, delegación e inyección de dependencias.
- Refactoring, revisión de código y pruebas.
- Material: `teoria.py`, el TP de SOLID y
  `Unidad 4.2 SOLID Buenas Practicas POO 2026.pptx`.

### [Unidad04/4.4.GRASP](Unidad04/4.4.GRASP)

- Responsability-Driven Design (RDD) y asignación de responsabilidades.
- Relación entre UML, principios de diseño y patrones.
- Patrones GRASP: Information Expert, Creator, Controller, Low Coupling, High Cohesion,
  Polymorphism, Pure Fabrication, Indirection y Protected Variations.
- Clase, conocer y hacer: responsabilidades de los objetos.
- Ejemplo práctico de calculadora con el patrón Controller.
- Material: `teoria_y_practica.py`, el TP de GRASP y
  `Unidad 4.3 Patrones GRASP 2026.pptx`.

---

## [Unidad 05 — Memoria, RAII, Excepciones y Punteros Inteligentes](Unidad05)

Aborda la gestión de memoria en C++ moderno y los errores asociados a la asignación y
liberación manual. Se estudian las fugas de memoria, el patrón **RAII**, el manejo de
excepciones, la diferencia entre punteros y referencias y los punteros inteligentes
`unique_ptr`, `shared_ptr` y `weak_ptr`.

### [Unidad05](Unidad05)

- Memory leaks: causas, síntomas y consecuencias.
- RAII (*Resource Acquisition Is Initialization*): adquisición en el constructor y
  liberación en el destructor.
- Excepciones en C++: `try`, `catch`, `throw` y ciclo de vida de una excepción.
- RAII frente a excepciones: cuándo usar cada enfoque.
- Punteros frente a referencias: comparación y usos.
- Cómo evitar pérdidas de memoria.
- Punteros inteligentes: `unique_ptr`, `shared_ptr` y `weak_ptr`.
- Comparativa y criterios de elección.
- Material: `teoria.py`, `TP5. Memory Leak.docx`, `Unidad 5 Memory Leak.pptx` y
  `MemoryLeakSptr.rar`.

---

## [Unidad 07 — Testing y CMake](Unidad07)

Introduce el proceso de pruebas de software y las herramientas para automatizarlas en
C++. Se trabajan los conceptos de verificación y validación, las técnicas de caja negra y
caja blanca, los niveles y tipos de pruebas, los principios y directrices, el plan de
pruebas y la integración con CMake y GoogleTest.

### [Unidad07/7.1.Testing](Unidad07/7.1.Testing)

- Proceso de testing: objetivos y alcance.
- Verificación y validación.
- Pruebas manuales y automatizadas.
- Pruebas de caja negra y de caja blanca.
- Niveles: unitarias, de integración, de sistema y de aceptación.
- Tipos de testing y ejemplos.
- Siete principios de las pruebas y directrices.
- Plan de pruebas.
- CMake, CMakeLists.txt y frameworks de prueba.
- GoogleTest (GTest) y pruebas simples.
- Material: `teoria.py`, `TP7. Testing.docx` y `U7 Testing.pptx`.

### [Unidad07/7.2.Testing&CMake](Unidad07/7.2.Testing%26CMake)

- Repaso del proceso de testing y de los niveles de prueba.
- CMake: qué es, qué problema resuelve y cómo se usa.
- Estructura de `CMakeLists.txt`.
- Configuración, compilación y ejecución de proyectos.
- Integración de GoogleTest con CMake.
- Proyecto de práctica y ejemplos de laboratorio.
- Material: `teoria.py`, `TP7. Testing CMake Gtest.docx`,
  [practica](Unidad07/7.2.Testing%26CMake/practica) y
  [Unidad CMake](Unidad07/7.2.Testing%26CMake/Unidad%20CMake).

---

## Parciales y simulaciones

### [Parcial_1](Parcial_1)

Primer parcial (Grupo B). El marco teórico pregunta por el uso de paradigmas imperativos y
declarativos, las ventajas de las arquitecturas limpias y tres soluciones con Tkinter y
SQLite. El marco práctico propone el módulo de clientes de una aplicación de pedidos
(“NicBread”) en Python, con Tkinter, SQLite, POO, modularización y logs.

- [Teoría](Parcial_1/teoria): respuestas y apuntes del parcial.
- [Práctica](Parcial_1/practica): implementación del módulo de clientes con capas de
  dominio, aplicación, infraestructura y UI; repositorio SQLite y servicio de clientes.
- Documento: `Algo II Primer Parcial B.docx.pdf`.

### [Parcial_2](Parcial_2)

Segundo parcial. Plantea una aplicación para gestionar la compra de materia prima de una
empresa de productos de goma: artículos, proveedores y pedidos. Requiere diagrama de
clases, implementación en C++, aplicación de RAII, IoC, SOLID y GRASP, y CRUD de
proveedores con refactorización.

- [App](Parcial_2/App): resolución en C++ con arquitectura hexagonal, entidades de
  dominio, puertos, servicios de aplicación, adaptadores de consola y repositorios en
  memoria.
- Documento: `Segundo Parcial 2026.pdf`.
- `App.zip`: copia comprimida de la aplicación.

### [Simulacion_Parcial_1](Simulacion_Parcial_1)

Simulación del primer parcial. Repasa arquitectura limpia, paradigmas imperativos y
declarativos, diferencias entre paradigma estructurado y orientado a objetos, patrones
arquitectónicos, de software e idioms, comparación Python/C++, objetos en ambos lenguajes,
Tkinter, SQLite y pruebas en Python.

- [Teoría](Simulacion_Parcial_1/teoria): respuestas de repaso en `teoria.py`.
- [Práctica](Simulacion_Parcial_1/practica): módulo de clientes con Tkinter, SQLite y
  separación por capas.
- Documento: `Algo II - Simulación Primer Parcial V2.0 (1).pdf`.

---

## Trabajo Práctico Final

### [Trabajo_Practico_Final](Trabajo_Practico_Final)

Proyecto integrador final: aplicación de consola en **C++17** para controlar el drone de
reparto **IBag151**. Implementa arquitectura hexagonal, SOLID, GRASP, TDD, CMake,
GoogleTest, Clean Code, RAII y abstracciones de la STL. La API real del drone se simula
mediante un adaptador de salida que imprime los comandos en consola.

- [include](Trabajo_Practico_Final/include): puertos, servicios, entidades, objetos de
  valor y adaptadores.
- [src](Trabajo_Practico_Final/src): implementación de dominio, aplicación e
  infraestructura, y `main.cpp`.
- [tests](Trabajo_Practico_Final/tests): pruebas de dominio, aplicación e infraestructura
  con GoogleTest.
- [public/docs](Trabajo_Practico_Final/public/docs): diseño, diagramas de clases y
  diagramas de arquitectura hexagonal.
- Documento: `TP Final IBag.docx`.
- El proyecto tiene su propio [README](Trabajo_Practico_Final/README.md) con comandos de
  compilación, ejecución y pruebas.

---

## Material de apoyo

### [ExampleHexagonalArchitectureBoilerPlate](ExampleHexagonalArchitectureBoilerPlate)

Plantilla base de **arquitectura hexagonal** utilizada como referencia para organizar
proyectos. Separa las capas de dominio, aplicación e infraestructura y define carpetas
para entidades, objetos de valor, puertos de entrada y salida, adaptadores y configuración.

- [include](ExampleHexagonalArchitectureBoilerPlate/include): contratos e interfaces.
- [src](ExampleHexagonalArchitectureBoilerPlate/src): implementaciones.
- [public/docs](ExampleHexagonalArchitectureBoilerPlate/public/docs): documentación.

### [Utils](Utils)

Utilidades del repositorio. `menu_for_exercises.py` implementa un menú de consola
reutilizable para listar y ejecutar los ejercicios de las guías de teoría y práctica.

---

## Notas

- Cada carpeta de unidad incluye el material teórico en PDF/PPTX, la guía de trabajos
  prácticos y los scripts de teoría y práctica cuando corresponden.
- Algunas unidades tienen una subcarpeta `2026` con versiones actualizadas del material.
- La carpeta `build/` contiene artefactos generados por CMake y no forma parte del
  material teórico del repositorio.
