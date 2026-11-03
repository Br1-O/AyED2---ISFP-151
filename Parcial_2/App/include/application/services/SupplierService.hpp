#ifndef SUPPLIER_SERVICE_HPP
#define SUPPLIER_SERVICE_HPP

#include <memory>
#include <vector>
#include <optional>
#include "domain/entities/Supplier.hpp"
#include "domain/ports/out/ISupplierRepository.hpp"

class SupplierService {
private:
    std::shared_ptr<ISupplierRepository> supplierRepo;
public:
    explicit SupplierService(std::shared_ptr<ISupplierRepository> supplierRepo);

    Supplier createSupplier(const std::string& name, const std::string& cuit, const std::string& email);
    std::vector<Supplier> getAllSuppliers() const;
    std::optional<Supplier> getSupplierById(int id) const;
    void updateSupplier(const Supplier& supplier);
    void deleteSupplier(int id);
};

#endif