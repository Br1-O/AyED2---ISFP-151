#ifndef ORDER_HPP
#define ORDER_HPP

#include <vector>
#include <memory>
#include "Supplier.hpp"
#include "OrderDetail.hpp"

class Order {
private:
    int id;
    Supplier supplier;
    std::vector<OrderDetail> details;
public:
    Order(int id, const Supplier& supplier);

    int getId() const;
    void setId(int id);
    const Supplier& getSupplier() const;
    const std::vector<OrderDetail>& getDetails() const;
    void addDetail(std::shared_ptr<Article> article, int quantity);
};

#endif