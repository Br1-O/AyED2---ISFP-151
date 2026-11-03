#ifndef I_ORDER_REPOSITORY_HPP
#define I_ORDER_REPOSITORY_HPP

#include <vector>
#include "domain/entities/Order.hpp"

class IOrderRepository {
public:
    virtual ~IOrderRepository() = default;
    virtual Order save(Order order) = 0;
    virtual std::vector<Order> findAll() const = 0;
};

#endif