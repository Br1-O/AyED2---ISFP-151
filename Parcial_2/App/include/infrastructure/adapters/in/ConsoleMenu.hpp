#ifndef CONSOLE_MENU_HPP
#define CONSOLE_MENU_HPP

#include <memory>
#include "application/services/SupplierService.hpp"
#include "application/services/ArticleService.hpp"
#include "application/services/OrderService.hpp"

class ConsoleMenu {
private:
    std::shared_ptr<SupplierService> supplierService;
    std::shared_ptr<ArticleService> articleService;
    std::shared_ptr<OrderService> orderService;

    void handleSupplierCrud();
    void handleArticleOperations();
    void handleOrderOperations();

public:
    ConsoleMenu(
        std::shared_ptr<SupplierService> supplierService,
        std::shared_ptr<ArticleService> articleService,
        std::shared_ptr<OrderService> orderService
    );

    void start();
};

#endif