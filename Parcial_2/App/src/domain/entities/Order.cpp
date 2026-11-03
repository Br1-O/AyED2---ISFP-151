#include "domain/entities/Order.hpp"

Order::Order(int id, const Supplier& supplier) : id(id), supplier(supplier) {}

int Order::getId() const { return id; }
void Order::setId(int id) { this->id = id; }
const Supplier& Order::getSupplier() const { return supplier; }
const std::vector<OrderDetail>& Order::getDetails() const { return details; }

void Order::addDetail(std::shared_ptr<Article> article, int quantity) {
    details.emplace_back(article, quantity);
}