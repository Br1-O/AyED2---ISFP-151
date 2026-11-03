#include "application/services/OrderService.hpp"
#include <stdexcept>

OrderService::OrderService(
    std::shared_ptr<IOrderRepository> orderRepo,
    std::shared_ptr<ISupplierRepository> supplierRepo,
    std::shared_ptr<IArticleRepository> articleRepo
) : orderRepo(orderRepo), supplierRepo(supplierRepo), articleRepo(articleRepo) {}

Order OrderService::createOrder(int supplierId, const std::vector<std::pair<int, int>>& items) {
    auto supplierOpt = supplierRepo->findById(supplierId);
    if (!supplierOpt.has_value()) {
        throw std::runtime_error("Proveedor no encontrado");
    }

    if (items.empty()) {
        throw std::runtime_error("La orden debe contener al menos un articulo");
    }

    Order order(0, supplierOpt.value()); 

    for (const auto& item : items) {
        int articleId = item.first;
        int qty = item.second;

        auto articleOpt = articleRepo->findById(articleId);
        if (!articleOpt.has_value()) {
            throw std::runtime_error("Articulo ID " + std::to_string(articleId) + " no encontrado");
        }

        order.addDetail(articleOpt.value(), qty);
    }

    return orderRepo->save(order);
}

std::vector<Order> OrderService::getAllOrders() const {
    return orderRepo->findAll();
}