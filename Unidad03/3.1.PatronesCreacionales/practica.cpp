#include <iostream>
#include <memory>
#include <string>

using namespace std;

// =========================================================================
// 1. Interfaces
// =========================================================================
class Chair {
public:
    virtual ~Chair() = default;
    virtual bool hasLegs() const = 0;
    virtual void sitOn() const = 0;
};

class Sofa {
public:
    virtual ~Sofa() = default;
    virtual void lieOn() const = 0;
};

class CoffeeTable {
public:
    virtual ~CoffeeTable() = default;
    virtual void putCoffee() const = 0;
};

// =========================================================================
// 2. PRODUCTOS CONCRETOS - FAMILIA VICTORIANA
// =========================================================================
class VictorianChair : public Chair {
public:
    bool hasLegs() const override { return true; }
    void sitOn() const override {
        cout << "Sentándose en una elegante silla victoriana." << endl;
    }
};

class VictorianSofa : public Sofa {
public:
    void lieOn() const override {
        cout << "Recostándose en un sofá victoriano acolchado." << endl;
    }
};

class VictorianCoffeeTable : public CoffeeTable {
public:
    void putCoffee() const override {
        cout << "Colocando café en una mesa ratonera victoriana de madera tallada." << endl;
    }
};

// =========================================================================
// 3. PRODUCTOS CONCRETOS - FAMILIA MODERNA
// =========================================================================
class ModernChair : public Chair {
public:
    bool hasLegs() const override { return false; }
    void sitOn() const override {
        cout << "Sentándose en una silla moderna de diseño minimalista." << endl;
    }
};

class ModernSofa : public Sofa {
public:
    void lieOn() const override {
        cout << "Recostándose en un sofá moderno modular." << endl;
    }
};

class ModernCoffeeTable : public CoffeeTable {
public:
    void putCoffee() const override {
        cout << "Colocando café en una mesa de centro moderna de vidrio y metal." << endl;
    }
};

// =========================================================================
// 4. INTERFAZ DE LA FÁBRICA ABSTRACTA
// =========================================================================
class FurnitureFactory {
public:
    virtual ~FurnitureFactory() = default;
    virtual unique_ptr<Chair> createChair() const = 0;
    virtual unique_ptr<Sofa> createSofa() const = 0;
    virtual unique_ptr<CoffeeTable> createCoffeeTable() const = 0;
};

// =========================================================================
// 5. FÁBRICAS CONCRETAS
// =========================================================================
class VictorianFurnitureFactory : public FurnitureFactory {
public:
    unique_ptr<Chair> createChair() const override {
        return make_unique<VictorianChair>();
    }
    unique_ptr<Sofa> createSofa() const override {
        return make_unique<VictorianSofa>();
    }
    unique_ptr<CoffeeTable> createCoffeeTable() const override {
        return make_unique<VictorianCoffeeTable>();
    }
};

class ModernFurnitureFactory : public FurnitureFactory {
public:
    unique_ptr<Chair> createChair() const override {
        return make_unique<ModernChair>();
    }
    unique_ptr<Sofa> createSofa() const override {
        return make_unique<ModernSofa>();
    }
    unique_ptr<CoffeeTable> createCoffeeTable() const override {
        return make_unique<ModernCoffeeTable>();
    }
};

// =========================================================================
// 6. Main
// =========================================================================
void simularTiendaMuebles(const FurnitureFactory& factory) {
    auto silla = factory.createChair();
    auto sofa = factory.createSofa();
    auto mesa = factory.createCoffeeTable();

    silla->sitOn();
    cout << "  - ¿La silla tiene patas?: " << (silla->hasLegs() ? "Sí" : "No") << endl;
    sofa->lieOn();
    mesa->putCoffee();
}

int main() {
    cout << "=== SIMULADOR DE TIENDA DE MUEBLES (ABSTRACT FACTORY) ===" << endl << endl;

    cout << "Catálogo de muebles estilo VICTORIANO:" << endl;
    VictorianFurnitureFactory victorianFactory;
    simularTiendaMuebles(victorianFactory);

    cout << "\n--------------------------------------------------" << endl;

    cout << "Catálogo a estilo MODERNO:" << endl;
    ModernFurnitureFactory modernFactory;
    simularTiendaMuebles(modernFactory);

    return 0;
}