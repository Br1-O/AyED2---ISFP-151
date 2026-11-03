#ifndef IN_MEMORY_ORDER_REPOSITORY_HPP
#define IN_MEMORY_ORDER_REPOSITORY_HPP

#include <vector>
#include "domain/ports/out/IOrderRepository.hpp"

class InMemoryOrderRepository : public IOrderRepository {
private:
    std::vector<Order> orders;
    int nextId;
    InMemoryOrderRepository();

public:
    static InMemoryOrderRepository& getInstance();

    Order save(Order order) override;
    std::vector<Order> findAll() const override;
};

#endif