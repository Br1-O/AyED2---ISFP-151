/**
 * ============================================================================
 * TEORIA
 * ============================================================================
 *
 * 1. DESCRIBIR LOS TIPOS DE PATRONES DE COMPORTAMIENTO
 *    Los patrones de comportamiento se encargan de una comunicación efectiva y
 *    de la asignación de responsabilidades entre objetos. Según la
 *    bibliografía de la cátedra, los principales tipos son:
 *    - Strategy (Estrategia): Define una familia de algoritmos intercambiables,
 *      encapsulando cada uno en una clase separada para variar el
 *      comportamiento de un objeto en tiempo de ejecución.
 *    - Command (Comando): Convierte una solicitud en un objeto independiente
 *      que contiene toda la información sobre la petición, permitiendo
 *      parametrizar, encolar, retrasar o deshacer operaciones.
 *    - Observer (Observador): Define un mecanismo de suscripción (uno a muchos)
 *      para notificar automáticamente a múltiples objetos suscriptores sobre
 *      eventos o cambios de estado en un objeto notificador/sujeto.
 *    - State (Estado): Permite a un objeto alterar su comportamiento cuando su
 *      estado interno cambia, extrayendo las ramas condicionales hacia clases
 *      de estado independientes.
 *    - Chain of Responsibility (Cadena de Responsabilidad): Pasa solicitudes a
 *      lo largo de una cadena de manejadores; cada manejador decide si procesa
 *      la solicitud o la pasa al siguiente eslabón.
 *    - Iterator (Iterador): Permite recorrer secuencialmente los elementos de
 *      una colección sin exponer su representación subyacente (lista, árbol,
 *      grafo, etc.).
 *    - Mediator (Mediador): Reduce las dependencias caóticas entre objetos
 *      restringiendo las comunicaciones directas y forzándolos a colaborar a
 *      través de un objeto mediador central.
 *    - Template Method (Método Plantilla): Define el esqueleto de un algoritmo
 *      en una superclase y delega o permite sobrescribir pasos específicos en
 *      las subclases sin alterar la estructura general.
 *    - Visitor (Visitante): Separa algoritmos u operaciones de las estructuras
 *      de objetos sobre las que operan mediante técnicas como Double Dispatch.
 *
 * 2. ¿QUÉ TIPOS DE PROBLEMAS RESUELVEN?
 *    - Acoplamiento rígido entre clases: Evitan que los objetos dependan
 *      directamente de implementaciones concretas (por ejemplo, acoplar la GUI
 *      con la lógica de negocio o una clase principal con algoritmos fijos).
 *    - Explosión combinatoria de subclases: Evitan tener que crear cientos de
 *      subclases solo para variar una parte del comportamiento o una acción.
 *    - Condicionales extensos y difíciles de mantener: Eliminan bloques
 *      monstruosos de `if/else` o `switch` que seleccionan comportamientos o
 *      transiciones de estado.
 *    - Código duplicado y baja cohesión: Separan algoritmos complejos,
 *      recorridos de estructuras o validaciones secuenciales de la lógica
 *      principal del dominio, facilitando el mantenimiento y la extensión
 *      (cumpliendo con los principios de Responsabilidad Única y
 *      Abierto/Cerrado).
 *
 * 3. EJEMPLOS DE PROBLEMA - PATRONES DE COMPORTAMIENTO
 *    - Problema: Una aplicación de navegación crece demasiado porque integra
 *      dentro de una misma clase el cálculo de rutas en coche, a pie, en
 *      transporte público y en bicicleta.
 *      -> Solución (Strategy): Se extrae cada algoritmo de cálculo de ruta a su
 *      propia clase estrategia intercambiable en tiempo de ejecución.
 *    - Problema: En un editor de texto, una operación como "Copiar" o "Guardar"
 *      debe ejecutarse desde un botón, un menú contextual o un atajo de teclado
 *      sin duplicar código ni acoplar la interfaz a la lógica de negocio.
 *      -> Solución (Command): Se encapsula cada acción en un objeto comando con
 *      un método único `execute()`.
 *    - Problema: Un cliente desea saber cuándo llega un producto nuevo a una
 *      tienda sin tener que consultar todos los días (polling) y sin que la
 *      tienda envíe correo masivo (spam) a clientes no interesados.
 *      -> Solución (Observer): La tienda actúa como publicador y notifica
 *      únicamente a los clientes suscritos al evento de disponibilidad.
 *    - Problema: Un documento pasa por distintos estados (Borrador, Moderación,
 *      Publicado) y el método `publicar()` actúa distinto según el estado,
 *      generando condicionales difíciles de escalar.
 *      -> Solución (State): Se crea una clase por cada estado que encapsula su
 *      propio comportamiento y gestiona las transiciones.
 *    - Problema: Un sistema de pedidos online debe ejecutar una serie de
 *      validaciones secuenciales (autenticación, saneamiento de datos, filtro
 *      de IP, caché) donde cualquiera puede detener el flujo.
 *      -> Solución (Chain of Responsibility): Cada validación es un manejador
 *      encadenado al siguiente.
 *
 * 4. ¿QUÉ ROL JUEGA LA INTERFAZ EN LOS PATRONES DE COMPORTAMIENTO Y QUÉ FACILITA?
 *    - Rol: Actúa como un contrato abstracto y punto único de comunicación
 *      entre el objeto emisor/contexto y las implementaciones concretas
 *      (estrategias, comandos, observadores, estados o manejadores). Encapsula
 *      la firma del método que dispara el comportamiento sin exponer detalles
 *      internos ni estructuras de datos privadas.
 *    - Qué facilita:
 *      1. Desacoplamiento: El contexto o cliente interactúa únicamente con la
 *         interfaz genérica, ignorando qué clase concreta ejecuta la tarea.
 *      2. Polimorfismo e intercambio dinámico: Permite sustituir o agregar
 *         nuevos comportamientos en tiempo de ejecución sin modificar el
 *         código existente (Principio Abierto/Cerrado).
 *      3. Reutilización y modularidad: Permite que distintos contextos o
 *         clientes reutilicen los mismos módulos de comportamiento sin
 *         duplicar código.
 * ============================================================================
 */

#include <iostream>
#include <memory>
#include <string>
#include <vector>

// Representación simple de un punto de control en el mapa
struct PuntoControl {
    std::string descripcion;
    double latitud;
    double longitud;
};

// ============================================================================
// INTERFAZ STRATEGY 
// ============================================================================
class Strategy {
public:
    virtual ~Strategy() = default;

    // Método equivalente a executeAlgorithm() / calcularRuta(A, B) del UML
    virtual std::vector<PuntoControl> calcularRuta(const std::string& origen,
                                                   const std::string& destino) const = 0;

    virtual std::string getNombreMedio() const = 0;
};

// ============================================================================
// ESTRATEGIAS CONCRETAS (ConcreteStrategyA, ConcreteStrategyB, ConcreteStrategyC)
// ============================================================================

// ConcreteStrategyA: Peatón
class PeatonStrategy : public Strategy {
public:
    std::vector<PuntoControl> calcularRuta(const std::string& origen,
                                           const std::string& destino) const override {
        return {
            {"Salida a pie desde " + origen, -38.0055, -57.5426},
            {"Cruzar plaza peatonal y tomar senda aeróbica", -38.0080, -57.5400},
            {"Llegada peatonal a " + destino, -38.0112, -57.5375}
        };
    }

    std::string getNombreMedio() const override {
        return "Peatón (A pie)";
    }
};

// ConcreteStrategyB: Coche
class CocheStrategy : public Strategy {
public:
    std::vector<PuntoControl> calcularRuta(const std::string& origen,
                                           const std::string& destino) const override {
        return {
            {"Inicio en vehículo desde " + origen, -38.0055, -57.5426},
            {"Incorporarse a Avenida Principal (onda verde)", -38.0150, -57.5510},
            {"Tomar rotonda hacia acceso rápido", -38.0210, -57.5450},
            {"Estacionamiento en " + destino, -38.0112, -57.5375}
        };
    }

    std::string getNombreMedio() const override {
        return "Coche (Automóvil)";
    }
};

// ConcreteStrategyC: Transporte Público
class TransportePublicoStrategy : public Strategy {
public:
    std::vector<PuntoControl> calcularRuta(const std::string& origen,
                                           const std::string& destino) const override {
        return {
            {"Caminar hasta parada de colectivo cercana a " + origen, -38.0060, -57.5430},
            {"Abordar Línea 511 hacia el centro", -38.0100, -57.5480},
            {"Combinar en estación de transbordo con Línea 542", -38.0145, -57.5415},
            {"Descender a 100m de " + destino, -38.0112, -57.5375}
        };
    }

    std::string getNombreMedio() const override {
        return "Transporte Público";
    }
};

// ============================================================================
// CONTEXTO (Clase Navigator del diagrama UML)
// ============================================================================
class Navigator {
private:
    std::unique_ptr<Strategy> strategy_;

public:
    explicit Navigator(std::unique_ptr<Strategy> strategy = nullptr)
        : strategy_(std::move(strategy)) {}

    void setStrategy(std::unique_ptr<Strategy> strategy) {
        strategy_ = std::move(strategy);
    }

    const Strategy* getStrategy() const {
        return strategy_.get();
    }

    void mostrarRutaEnMapa(const std::string& origen, const std::string& destino) const {
        if (!strategy_) {
            std::cout << "[Error] No se ha seleccionado un medio de transporte.\n";
            return;
        }

        std::cout << "\n------------------------------------------------------------\n";
        std::cout << "Calculando ruta [" << strategy_->getNombreMedio() << "]\n";
        std::cout << "Origen : " << origen << "\n";
        std::cout << "Destino: " << destino << "\n";
        std::cout << "------------------------------------------------------------\n";

        std::vector<PuntoControl> puntos = strategy_->calcularRuta(origen, destino);

        for (size_t i = 0; i < puntos.size(); ++i) {
            std::cout << "  Paso " << (i + 1) << ": " << puntos[i].descripcion
                      << " (" << puntos[i].latitud << ", " << puntos[i].longitud << ")\n";
        }
        std::cout << "------------------------------------------------------------\n";
    }
};

// ============================================================================
// CLIENTE
// ============================================================================
int main() {
    Navigator navigator;
    std::string origen = "ISFT N° 151";
    std::string destino = "Catedral de Mar del Plata";
    int opcion = 0;

    std::cout << "=== SISTEMA DE NAVEGACIÓN (PATRÓN STRATEGY) ===\n";

    do {
        std::cout << "\nSeleccione el medio de transporte para calcular la ruta:\n"
                  << "  1. Peatón (ConcreteStrategyA)\n"
                  << "  2. Coche (ConcreteStrategyB)\n"
                  << "  3. Transporte público (ConcreteStrategyC)\n"
                  << "  4. Cambiar origen y destino\n"
                  << "  0. Salir\n"
                  << "Opción: ";

        if (!(std::cin >> opcion)) {
            std::cin.clear();
            std::cin.ignore(10000, '\n');
            std::cout << "Entrada inválida. Intente nuevamente.\n";
            continue;
        }

        switch (opcion) {
            case 1:
                navigator.setStrategy(std::make_unique<PeatonStrategy>());
                navigator.mostrarRutaEnMapa(origen, destino);
                break;
            case 2:
                navigator.setStrategy(std::make_unique<CocheStrategy>());
                navigator.mostrarRutaEnMapa(origen, destino);
                break;
            case 3:
                navigator.setStrategy(std::make_unique<TransportePublicoStrategy>());
                navigator.mostrarRutaEnMapa(origen, destino);
                break;
            case 4:
                std::cin.ignore(10000, '\n');
                std::cout << "Ingrese nuevo origen: ";
                std::getline(std::cin, origen);
                std::cout << "Ingrese nuevo destino: ";
                std::getline(std::cin, destino);
                if (navigator.getStrategy() != nullptr) {
                    navigator.mostrarRutaEnMapa(origen, destino);
                }
                break;
            case 0:
                std::cout << "Cerrando aplicación de navegación...\n";
                break;
            default:
                std::cout << "Opción no reconocida.\n";
                break;
        }
    } while (opcion != 0);

    return 0;
}