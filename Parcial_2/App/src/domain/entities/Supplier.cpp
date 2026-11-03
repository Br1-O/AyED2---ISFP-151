#include "domain/entities/Supplier.hpp"

Supplier::Supplier(int id, std::string name, std::string cuit, std::string email)
    : id(id), name(name), cuit(cuit), email(email) {}

int Supplier::getId() const { return id; }
std::string Supplier::getName() const { return name; }
std::string Supplier::getCuit() const { return cuit; }
std::string Supplier::getEmail() const { return email; }

void Supplier::setId(int id) { this->id = id; }
void Supplier::setName(const std::string& name) { this->name = name; }
void Supplier::setCuit(const std::string& cuit) { this->cuit = cuit; }
void Supplier::setEmail(const std::string& email) { this->email = email; }