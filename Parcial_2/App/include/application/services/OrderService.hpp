#ifndef ORDER_SERVICE_HPP
#define ORDER_SERVICE_HPP

#include <memory>
#include <vector>
#include <utility>
#include "domain/entities/Order.hpp"
#include "domain/ports/out/IOrderRepository.hpp"
#include "domain/ports/out/ISupplierRepository.hpp"
#include "domain/ports/out/IArticleRepository.hpp"

class OrderService {
private:
    std::shared_ptr<IOrderRepository> orderRepo;
    std::shared_ptr<ISupplierRepository> supplierRepo;
    std::shared_ptr<IArticleRepository> articleRepo;
public:
    OrderService(
        std::shared_ptr<IOrderRepository> orderRepo,
        std::shared_ptr<ISupplierRepository> supplierRepo,
        std::shared_ptr<IArticleRepository> articleRepo
    );

    Order createOrder(int supplierId, const std::vector<std::pair<int, int>>& items);
    std::vector<Order> getAllOrders() const;
};

#endif