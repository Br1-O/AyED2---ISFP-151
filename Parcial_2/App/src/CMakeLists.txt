cmake_minimum_required(VERSION 3.14)

# 1. Capa de Dominio (Domain Layer)
add_library(DomainLayer 
    domain/entities/Article.cpp
    domain/entities/Supplier.cpp
    domain/entities/OrderDetail.cpp
    domain/entities/Order.cpp
)

# 2. Capa de Aplicación (Application Layer)
add_library(ApplicationLayer 
    application/services/SupplierService.cpp
    application/services/ArticleService.cpp
    application/services/OrderService.cpp
)

# 3. Capa de Infraestructura (Infrastructure Layer) - INCLUYE LOS REPOSITORIOS .CPP
add_library(InfrastructureLayer 
    infrastructure/adapters/in/ConsoleMenu.cpp
    infrastructure/adapters/out/InMemorySupplierRepository.cpp
    infrastructure/adapters/out/InMemoryArticleRepository.cpp
    infrastructure/adapters/out/InMemoryOrderRepository.cpp
)

# Configuración de directorios de inclusión (Headers)
target_include_directories(DomainLayer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)
target_include_directories(ApplicationLayer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)
target_include_directories(InfrastructureLayer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Regla de Dependencias Hexagonal: Infrastructure -> Application -> Domain
target_link_libraries(ApplicationLayer PUBLIC DomainLayer)
target_link_libraries(InfrastructureLayer PUBLIC ApplicationLayer DomainLayer)

# Executable Principal
add_executable(App main.cpp)
target_include_directories(App PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../include)
target_link_libraries(App PRIVATE InfrastructureLayer ApplicationLayer DomainLayer)