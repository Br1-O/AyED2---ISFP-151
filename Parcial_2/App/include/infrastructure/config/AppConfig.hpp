#ifndef APP_CONFIG_HPP
#define APP_CONFIG_HPP

#include <memory>
#include <vector>
#include <utility>
#include "infrastructure/adapters/out/InMemorySupplierRepository.hpp"
#include "infrastructure/adapters/out/InMemoryArticleRepository.hpp"
#include "infrastructure/adapters/out/InMemoryOrderRepository.hpp"
#include "application/services/SupplierService.hpp"
#include "application/services/ArticleService.hpp"
#include "application/services/OrderService.hpp"
#include "infrastructure/adapters/in/ConsoleMenu.hpp"

class AppConfig {
public:
    static std::shared_ptr<ConsoleMenu> createConsoleMenu() {
        auto supplierRepo = std::shared_ptr<ISupplierRepository>(&InMemorySupplierRepository::getInstance(), [](ISupplierRepository*){});
        auto articleRepo = std::shared_ptr<IArticleRepository>(&InMemoryArticleRepository::getInstance(), [](IArticleRepository*){});
        auto orderRepo = std::shared_ptr<IOrderRepository>(&InMemoryOrderRepository::getInstance(), [](IOrderRepository*){});

        auto supplierService = std::make_shared<SupplierService>(supplierRepo);
        auto articleService = std::make_shared<ArticleService>(articleRepo);
        auto orderService = std::make_shared<OrderService>(orderRepo, supplierRepo, articleRepo);

        // Carga de Datos Iniciales
        supplierService->createSupplier("Caucho Sur S.A.", "30-71123456-8", "contacto@cauchosur.com");
        supplierService->createSupplier("Polimeros Industriales", "30-68987654-3", "ventas@polimeros.com");

        articleService->registerArticle(101, "Manguera Alta Presion 1/2", 1500.50, 50);
        articleService->registerArticle(102, "Junta O-Ring 25mm", 120.00, 200);
        articleService->registerArticle(103, "Plancha de Goma Neopreno 5mm", 4500.00, 15);

        try {
            std::vector<std::pair<int, int>> initialItems = {
                {101, 5}, 
                {102, 20} 
            };
            orderService->createOrder(1, initialItems); 
        } catch (...) {}

        return std::make_shared<ConsoleMenu>(supplierService, articleService, orderService);
    }
};

#endif