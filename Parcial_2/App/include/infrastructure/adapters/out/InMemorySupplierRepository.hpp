#ifndef IN_MEMORY_SUPPLIER_REPOSITORY_HPP
#define IN_MEMORY_SUPPLIER_REPOSITORY_HPP

#include <vector>
#include <optional>
#include "domain/ports/out/ISupplierRepository.hpp"

class InMemorySupplierRepository : public ISupplierRepository {
private:
    std::vector<Supplier> suppliers;
    int nextId;
    InMemorySupplierRepository();

public:
    static InMemorySupplierRepository& getInstance();

    Supplier save(Supplier supplier) override;
    std::optional<Supplier> findById(int id) const override;
    std::vector<Supplier> findAll() const override;
    void update(const Supplier& supplier) override;
    void remove(int id) override;
};

#endif