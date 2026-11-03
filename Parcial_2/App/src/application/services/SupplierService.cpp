#include "application/services/SupplierService.hpp"

SupplierService::SupplierService(std::shared_ptr<ISupplierRepository> supplierRepo) 
    : supplierRepo(supplierRepo) {}

Supplier SupplierService::createSupplier(const std::string& name, const std::string& cuit, const std::string& email) {
    return supplierRepo->save(Supplier(0, name, cuit, email));
}

std::vector<Supplier> SupplierService::getAllSuppliers() const {
    return supplierRepo->findAll();
}

std::optional<Supplier> SupplierService::getSupplierById(int id) const {
    return supplierRepo->findById(id);
}

void SupplierService::updateSupplier(const Supplier& supplier) {
    supplierRepo->update(supplier);
}

void SupplierService::deleteSupplier(int id) {
    supplierRepo->remove(id);
}