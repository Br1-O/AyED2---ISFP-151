#ifndef I_SUPPLIER_REPOSITORY_HPP
#define I_SUPPLIER_REPOSITORY_HPP

#include <vector>
#include <optional>
#include "domain/entities/Supplier.hpp"

class ISupplierRepository {
public:
    virtual ~ISupplierRepository() = default;
    virtual Supplier save(Supplier supplier) = 0; 
    virtual std::optional<Supplier> findById(int id) const = 0;
    virtual std::vector<Supplier> findAll() const = 0;
    virtual void update(const Supplier& supplier) = 0;
    virtual void remove(int id) = 0;
};

#endif