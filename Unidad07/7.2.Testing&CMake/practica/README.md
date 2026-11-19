# Drone IBag151 — Trabajo Práctico Final Integrador

Aplicación de consola en C++17 para controlar el drone de reparto **IBag151**.
El proyecto implementa arquitectura hexagonal, SOLID, GRASP, TDD, CMake y
GoogleTest, con énfasis en Clean Code, RAII y uso de abstracciones de la STL.

La API real del drone está simulada mediante un adaptador de salida que imprime
en consola el texto de cada comando. De esta forma, cada acción validada por el
dominio se traduce a un texto que representa el envío hacia la API del drone.

## Actividades implementadas

| Actividad | Comando de consola | Texto enviado a la API |
|---|---|---|
| Despegar | `despegar` | `DESPEGAR` |
| Aterrizar | `aterrizar` | `ATERRIZAR` |
| Elevar | `elevar` | `ELEVAR` |
| Bajar | `bajar` | `BAJAR` |
| Girar a la derecha | `derecha` | `GIRAR DERECHA` |
| Girar a la izquierda | `izquierda` | `GIRAR IZQUIERDA` |
| Descargar el paquete | `descargar` | `DESCARGAR PAQUETE` |
| Sacar foto de la recepción | `foto` | `SACAR FOTO DE RECEPCION` |
| Notificar la entrega | `notificar` | `NOTIFICAR ENTREGA` |
| Acelerar | `acelerar` | `ACELERAR` |
| Frenar | `frenar` | `FRENAR` |

Comandos auxiliares: `estado` (telemetría), `ayuda` (lista de comandos) y
`salir`. También se aceptan `girar derecha`, `girar-izquierda`, mayúsculas y
espacios extra.

## Arquitectura y documentación

- [Diseño, decisiones y mapeo SOLID/GRASP](public/docs/DISENO.md)
- [Diagrama de clases](public/docs/class-diagram.svg) ·
  [fuente DrawIO](public/docs/DroneIBag151-ClassDiagram.drawio)
- [Diagrama de arquitectura hexagonal](public/docs/hexagonal-architecture.svg) ·
  [fuente DrawIO](public/docs/DroneIBag151-HexagonalArchitecture.drawio)

Regla de dependencia respetada:

```text
Infraestructura  →  Aplicación  →  Dominio
```

El dominio no conoce CMake, GoogleTest, `iostream`, la consola ni la API del
drone. La aplicación depende de interfaces. Los adaptadores implementan los
puertos y `AppConfig` actúa como composition root.

## Estructura del proyecto

```text
.
├── CMakeLists.txt
├── CMakePresets.json
├── include/
│   ├── application/
│   │   ├── ports/in/IDroneControlUseCase.hpp
│   │   └── services/DroneControlService.hpp
│   ├── domain/
│   │   ├── entities/Drone.hpp
│   │   ├── entities/IDrone.hpp
│   │   ├── ports/out/IDroneApi.hpp
│   │   └── valueObjects/
│   │       ├── DroneAction.hpp
│   │       ├── DroneTelemetry.hpp
│   │       └── FlightStatus.hpp
│   └── infrastructure/
│       ├── adapters/in/ConsoleDroneController.hpp
│       ├── adapters/out/ConsoleDroneApiAdapter.hpp
│       └── config/AppConfig.hpp
├── src/
│   ├── application/services/DroneControlService.cpp
│   ├── domain/entities/Drone.cpp
│   ├── infrastructure/adapters/in/ConsoleDroneController.cpp
│   ├── infrastructure/adapters/out/ConsoleDroneApiAdapter.cpp
│   ├── infrastructure/config/AppConfig.cpp
│   └── main.cpp
├── tests/
│   ├── domain/DroneTest.cpp
│   ├── application/DroneControlServiceTest.cpp
│   └── infrastructure/
│       ├── ConsoleDroneApiAdapterTest.cpp
│       └── ConsoleDroneControllerTest.cpp
└── public/docs/
    ├── DISENO.md
    ├── class-diagram.svg / .png / .dot
    ├── hexagonal-architecture.svg / .png / .dot
    ├── DroneIBag151-ClassDiagram.drawio
    └── DroneIBag151-HexagonalArchitecture.drawio
```

La separación de carpetas sigue el boilerplate
`ExampleHexagonalArchitectureBoilerPlate`: `application/ports/in`,
`domain/entities`, `domain/ports/out`, `domain/valueObjects`,
`infrastructure/adapters/out` e `infrastructure/config`. Se agregó
`infrastructure/adapters/in` porque la consola es el adaptador de entrada del
sistema y `application/services` porque el caso de uso concreto no es un puerto.

## Requisitos

- CMake 3.21 o superior.
- Compilador con C++17 (GCC 9+, Clang 10+ o MSVC 2019+).
- GoogleTest. Si no está instalado, CMake lo descarga automáticamente con
  `FetchContent` en la primera configuración (requiere conexión a Internet).
- VS Code: se recomiendan las extensiones declaradas en `.vscode/extensions.json`
  (C/C++, CMake Tools y Draw.io Integration).

## Compilar, probar y ejecutar

Con los presets de CMake (recomendado para VS Code):

```bash
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
./build/debug/src/DroneIBag151
```

Alternativa sin presets:

```bash
cmake -S . -B build/debug -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=ON
cmake --build build/debug -j
ctest --test-dir build/debug --output-on-failure
./build/debug/src/DroneIBag151
```

Para una compilación con AddressSanitizer y UndefinedBehaviorSanitizer:

```bash
cmake -S . -B build/san -DCMAKE_BUILD_TYPE=Debug \
  -DDRONE_ENABLE_SANITIZERS=ON
cmake --build build/san -j
ctest --test-dir build/san --output-on-failure
```

## Ejemplo de sesión

```text
> despegar
[API Drone] DESPEGAR

> elevar
[API Drone] ELEVAR

> derecha
[API Drone] GIRAR DERECHA

> acelerar
[API Drone] ACELERAR

> frenar
[API Drone] FRENAR

> bajar
[API Drone] BAJAR

> aterrizar
[API Drone] ATERRIZAR

> descargar
[API Drone] DESCARGAR PAQUETE

> foto
[API Drone] SACAR FOTO DE RECEPCION

> notificar
[API Drone] NOTIFICAR ENTREGA

> estado
--- Estado del drone IBag151 ---
Estado: En tierra
Altitud: 0 m
Velocidad: 0 km/h
Rumbo: 90 grados
Paquete: descargado
Foto de recepcion: tomada
Entrega: notificada
```

Si se intenta una operación inválida (por ejemplo, aterrizar en tierra), el
dominio lanza un `std::domain_error`, el adaptador de entrada lo informa y **no**
se envía ningún comando a la API.

## Pruebas

La suite contiene **53 tests** de GoogleTest:

- Dominio: estado inicial, despegue, aterrizaje, elevación, descenso, giros,
  descarga, foto, notificación, aceleración, frenado, límites e invariantes.
- Aplicación: cada actividad actualiza el dominio y publica la acción correcta;
  las acciones rechazadas no llegan a la API.
- Infraestructura: traducción de todas las acciones a texto de API y despacho de
  todos los comandos de consola, incluyendo alias, estado, ayuda y errores.

El detalle de los ciclos TDD y la matriz actividad → prueba está en
[`public/docs/DISENO.md`](public/docs/DISENO.md).
