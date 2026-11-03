#include "infrastructure/adapters/out/InMemoryOrderRepository.hpp"

InMemoryOrderRepository::InMemoryOrderRepository() : nextId(1000) {}

InMemoryOrderRepository& InMemoryOrderRepository::getInstance() {
    static InMemoryOrderRepository instance;
    return instance;
}

Order InMemoryOrderRepository::save(Order order) {
    if (order.getId() <= 0) {
        order.setId(nextId++);
    } else if (order.getId() >= nextId) {
        nextId = order.getId() + 1;
    }
    orders.push_back(order);
    return order;
}

std::vector<Order> InMemoryOrderRepository::findAll() const {
    return orders;
}