#include <iostream>
#include <memory>
#include <string>

using namespace std;

// =========================================================================
// 1. INTERFAZ COMPONENTE
// =========================================================================
class Alojamiento {
public:
    virtual ~Alojamiento() = default;
    virtual string getDescripcion() const = 0;
    virtual double getCosto() const = 0;
};

// =========================================================================
// 2. COMPONENTE CONCRETO (Hotel Base)
// =========================================================================
class HotelBase : public Alojamiento {
public:
    string getDescripcion() const override {
        return "Hotel Standard con servicios basicos";
    }

    double getCosto() const override {
        return 50.0; 
    }
};

// =========================================================================
// 3. CLASE DECORADORA BASE (Wrapper)
// =========================================================================
class AlojamientoDecorator : public Alojamiento {
protected:
    shared_ptr<Alojamiento> alojamientoPrimitivo;

public:
    AlojamientoDecorator(shared_ptr<Alojamiento> alojamiento) 
        : alojamientoPrimitivo(alojamiento) {}

    string getDescripcion() const override {
        return alojamientoPrimitivo->getDescripcion();
    }

    double getCosto() const override {
        return alojamientoPrimitivo->getCosto();
    }
};

// =========================================================================
// 4. DECORADORES CONCRETOS (Nuevos tipos de alojamiento o servicios extra)
// =========================================================================

// Decorador que convierte o adapta a un 'Hostel' con desayuno compartido
class HostelDecorator : public AlojamientoDecorator {
public:
    HostelDecorator(shared_ptr<Alojamiento> alojamiento) : AlojamientoDecorator(alojamiento) {}

    string getDescripcion() const override {
        return alojamientoPrimitivo->getDescripcion() + ", adaptado a modalidad Hostel (con areas compartidas)";
    }

    double getCosto() const override {
        return alojamientoPrimitivo->getCosto() + 15.0; 
    }
};

// Decorador que convierte el alojamiento en un 'Apartamento' independiente
class ApartamentoDecorator : public AlojamientoDecorator {
public:
    ApartamentoDecorator(shared_ptr<Alojamiento> alojamiento) : AlojamientoDecorator(alojamiento) {}

    string getDescripcion() const override {
        return alojamientoPrimitivo->getDescripcion() + ", equipado como Apartamento Privado con cocina";
    }

    double getCosto() const override {
        return alojamientoPrimitivo->getCosto() + 40.0;
    }
};

// Decorador adicional para agregar régimen de 'All Inclusive'
class AllInclusiveDecorator : public AlojamientoDecorator {
public:
    AllInclusiveDecorator(shared_ptr<Alojamiento> alojamiento) : AlojamientoDecorator(alojamiento) {}

    string getDescripcion() const override {
        return alojamientoPrimitivo->getDescripcion() + " + All Inclusive (Comidas y bebidas ilimitadas)";
    }

    double getCosto() const override {
        return alojamientoPrimitivo->getCosto() + 30.0;
    }
};

// =========================================================================
// 5. Main
// =========================================================================
int main() {
    cout << "=== SIMULADOR DE PRESUPUESTO DE ALOJAMIENTOS (PATRÓN DECORATOR) ===" << endl << endl;

    // 1. Crear un hotel base simple
    shared_ptr<Alojamiento> miReserva = make_shared<HotelBase>();
    cout << "[Reserva 1]: " << miReserva->getDescripcion() << endl;
    cout << "Presupuesto Total: $" << miReserva->getCosto() << " USD\n" << endl;

    // 2. Extensibilidad: Transformar el hotel base en un Apartamento mediante un Decorator en tiempo de ejecución
    shared_ptr<Alojamiento> miReservaApartamento = make_shared<ApartamentoDecorator>(make_shared<HotelBase>());
    cout << "[Reserva 2]: " << miReservaApartamento->getDescripcion() << endl;
    cout << "Presupuesto Total: $" << miReservaApartamento->getCosto() << " USD\n" << endl;

    // 3. Extensibilidad avanzada: Combinar múltiples capas (Un Hostel con régimen All Inclusive)
    shared_ptr<Alojamiento> miReservaHostelCompleto = 
        make_shared<AllInclusiveDecorator>(
            make_shared<HostelDecorator>(
                make_shared<HotelBase>()
            )
        );
    
    cout << "[Reserva 3]: " << miReservaHostelCompleto->getDescripcion() << endl;
    cout << "Presupuesto Total: $" << miReservaHostelCompleto->getCosto() << " USD" << endl;

    return 0;
}