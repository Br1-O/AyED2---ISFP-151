#include "infrastructure/adapters/out/InMemorySupplierRepository.hpp"
#include <algorithm>

InMemorySupplierRepository::InMemorySupplierRepository() : nextId(1) {}

InMemorySupplierRepository& InMemorySupplierRepository::getInstance() {
    static InMemorySupplierRepository instance;
    return instance;
}

Supplier InMemorySupplierRepository::save(Supplier supplier) {
    if (supplier.getId() <= 0) {
        supplier.setId(nextId++);
    } else if (supplier.getId() >= nextId) {
        nextId = supplier.getId() + 1;
    }
    suppliers.push_back(supplier);
    return supplier;
}

std::optional<Supplier> InMemorySupplierRepository::findById(int id) const {
    for (const auto& s : suppliers) {
        if (s.getId() == id) return s;
    }
    return std::nullopt;
}

std::vector<Supplier> InMemorySupplierRepository::findAll() const {
    return suppliers;
}

void InMemorySupplierRepository::update(const Supplier& supplier) {
    for (auto& s : suppliers) {
        if (s.getId() == supplier.getId()) {
            s = supplier;
            break;
        }
    }
}

void InMemorySupplierRepository::remove(int id) {
    suppliers.erase(
        std::remove_if(suppliers.begin(), suppliers.end(), [id](const Supplier& s) { return s.getId() == id; }),
        suppliers.end()
    );
}