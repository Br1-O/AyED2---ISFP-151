#include "infrastructure/adapters/in/ConsoleMenu.hpp"
#include <iostream>
#include <limits>
#include <string>

ConsoleMenu::ConsoleMenu(
    std::shared_ptr<SupplierService> supplierService,
    std::shared_ptr<ArticleService> articleService,
    std::shared_ptr<OrderService> orderService
) : supplierService(supplierService), articleService(articleService), orderService(orderService) {}

void ConsoleMenu::start() {
    int option = 0;
    do {
        std::cout << "\n========================================\n";
        std::cout << " PATITO DE GOMA APP MENU \n";
        std::cout << "========================================\n";
        std::cout << "1. Gestion de Proveedores (CRUD)\n";
        std::cout << "2. Gestion de Articulos (Crear / Consultar)\n";
        std::cout << "3. Gestion de Ordenes de Compra (Crear / Consultar)\n";
        std::cout << "0. Salir\n";
        std::cout << "Seleccione una opcion: ";
        
        if (!(std::cin >> option)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        switch (option) {
            case 1: handleSupplierCrud(); break;
            case 2: handleArticleOperations(); break;
            case 3: handleOrderOperations(); break;
            case 0: std::cout << "Saliendo del sistema...\n"; break;
            default: std::cout << "Opcion invalida.\n";
        }
    } while (option != 0);
}

void ConsoleMenu::handleSupplierCrud() {
    int opt = 0;
    do {
        std::cout << "\n--- CRUD DE PROVEEDORES ---\n";
        std::cout << "1. Crear Proveedor \n";
        std::cout << "2. Listar Proveedores\n";
        std::cout << "3. Buscar Proveedor por ID\n";
        std::cout << "4. Actualizar Proveedor (Enter para mantener valor actual)\n";
        std::cout << "5. Eliminar Proveedor\n";
        std::cout << "0. Volver\n";
        std::cout << "Opcion: ";
        std::cin >> opt;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 

        if (opt == 1) {
            std::string name, cuit, email;
            std::cout << "Nombre: "; std::getline(std::cin, name);
            std::cout << "CUIT: "; std::getline(std::cin, cuit);
            std::cout << "Email: "; std::getline(std::cin, email);
            
            auto created = supplierService->createSupplier(name, cuit, email);
            std::cout << "[Info] Proveedor creado con ID autogenerado: " << created.getId() << "\n";
        } else if (opt == 2) {
            auto list = supplierService->getAllSuppliers();
            std::cout << "\n--- LISTA DE PROVEEDORES ---\n";
            for (const auto& s : list) {
                std::cout << "ID: " << s.getId() << " | Name: " << s.getName() 
                          << " | CUIT: " << s.getCuit() << " | Email: " << s.getEmail() << "\n";
            }
        } else if (opt == 3) {
            int id; std::cout << "ID a buscar: "; std::cin >> id;
            auto optSupplier = supplierService->getSupplierById(id);
            if (optSupplier.has_value()) {
                std::cout << "Encontrado -> ID: " << optSupplier->getId() 
                          << " | Nombre: " << optSupplier->getName() 
                          << " | CUIT: " << optSupplier->getCuit() 
                          << " | Email: " << optSupplier->getEmail() << "\n";
            } else {
                std::cout << "[Error] Proveedor no encontrado.\n";
            }
        } else if (opt == 4) {
            int id; std::cout << "ID a actualizar: "; std::cin >> id;
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            auto optSupplier = supplierService->getSupplierById(id);
            if (!optSupplier.has_value()) {
                std::cout << "[Error] Proveedor no encontrado.\n";
                continue;
            }

            Supplier current = optSupplier.value();
            std::string input;

            std::cout << "Nuevo Nombre [" << current.getName() << "]: ";
            std::getline(std::cin, input);
            if (!input.empty()) current.setName(input);

            std::cout << "Nuevo CUIT [" << current.getCuit() << "]: ";
            std::getline(std::cin, input);
            if (!input.empty()) current.setCuit(input);

            std::cout << "Nuevo Email [" << current.getEmail() << "]: ";
            std::getline(std::cin, input);
            if (!input.empty()) current.setEmail(input);

            supplierService->updateSupplier(current);
            std::cout << "[Info] Proveedor actualizado con éxito.\n";
        } else if (opt == 5) {
            int id; std::cout << "ID a eliminar: "; std::cin >> id;
            supplierService->deleteSupplier(id);
            std::cout << "[Info] Proveedor eliminado.\n";
        }
    } while (opt != 0);
}

void ConsoleMenu::handleArticleOperations() {
    int opt = 0;
    do {
        std::cout << "\n--- ARTICULOS (CREAR Y CONSULTAR) ---\n";
        std::cout << "1. Registrar Articulo\n";
        std::cout << "2. Listar Articulos\n";
        std::cout << "3. Buscar Articulo por ID\n";
        std::cout << "0. Volver\n";
        std::cout << "Opcion: ";
        std::cin >> opt;

        if (opt == 1) {
            int id, stock; double price; std::string name;
            std::cout << "ID: "; std::cin >> id;
            std::cout << "Nombre: "; std::cin >> name;
            std::cout << "Precio: "; std::cin >> price;
            std::cout << "Stock: "; std::cin >> stock;
            articleService->registerArticle(id, name, price, stock);
            std::cout << "[Info] Articulo registrado.\n";
        } else if (opt == 2) {
            auto articles = articleService->getAllArticles();
            std::cout << "\n--- CATALOGO DE ARTICULOS ---\n";
            for (const auto& a : articles) {
                std::cout << "ID: " << a->getId() << " | " << a->getName() 
                          << " | $" << a->getUnitPrice() << " | Stock: " << a->getStock() << "\n";
            }
        } else if (opt == 3) {
            int id; std::cout << "ID: "; std::cin >> id;
            auto found = articleService->getArticleById(id);
            if (found.has_value()) {
                std::cout << "Encontrado -> " << (*found)->getName() 
                          << " | $" << (*found)->getUnitPrice() 
                          << " | Stock: " << (*found)->getStock() << "\n";
            } else {
                std::cout << "[Error] Articulo no encontrado.\n";
            }
        }
    } while (opt != 0);
}

void ConsoleMenu::handleOrderOperations() {
    int opt = 0;
    do {
        std::cout << "\n--- ORDENES DE COMPRA (CREAR Y CONSULTAR) ---\n";
        std::cout << "1. Crear Orden de Compra \n";
        std::cout << "2. Listar Ordenes de Compra\n";
        std::cout << "0. Volver\n";
        std::cout << "Opcion: ";
        std::cin >> opt;

        if (opt == 1) {
            int supplierId;
            std::cout << "ID del Proveedor: "; 
            std::cin >> supplierId;

            std::vector<std::pair<int, int>> items;
            char addMore = 's';

            do {
                int articleId, qty;
                std::cout << "  -> ID del Articulo: "; std::cin >> articleId;
                std::cout << "  -> Cantidad: "; std::cin >> qty;

                items.push_back({articleId, qty});

                std::cout << "  ¿Desea agregar otro articulo a esta orden? (s/n): ";
                std::cin >> addMore;
            } while (addMore == 's' || addMore == 'S');

            try {
                auto createdOrder = orderService->createOrder(supplierId, items);
                std::cout << "\n[Info] Orden #" << createdOrder.getId() << " creada con exito.\n";
            } catch (const std::exception& e) {
                std::cout << "\n[Error] " << e.what() << "\n";
            }
        } else if (opt == 2) {
            auto orders = orderService->getAllOrders();
            std::cout << "\n--- LISTADO DE ORDENES DE COMPRA ---\n";
            for (const auto& o : orders) {
                std::cout << "\n========================================\n";
                std::cout << "Orden ID: #" << o.getId() << " | Proveedor: " << o.getSupplier().getName() << "\n";
                std::cout << "Detalles:\n";
                double totalOrden = 0.0;
                for (const auto& d : o.getDetails()) {
                    double subtotal = d.calculateSubtotal();
                    totalOrden += subtotal;
                    std::cout << "  * [" << d.getArticle()->getId() << "] " 
                              << d.getArticle()->getName() 
                              << " | Cantidad: " << d.getQuantity() 
                              << " | Precio U.: $" << d.getArticle()->getUnitPrice()
                              << " | Subtotal: $" << subtotal << "\n";
                }
                std::cout << "TOTAL ORDEN: $" << totalOrden << "\n";
            }
        }
    } while (opt != 0);
}