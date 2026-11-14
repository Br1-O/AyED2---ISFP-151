add_library(DomainLayer
    domain/entities/Drone.cpp
)

target_include_directories(DomainLayer PUBLIC ${PROJECT_SOURCE_DIR}/include)
enable_project_warnings(DomainLayer)

add_library(ApplicationLayer
    application/services/DroneControlService.cpp
)

target_include_directories(ApplicationLayer PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_link_libraries(ApplicationLayer PUBLIC DomainLayer)
enable_project_warnings(ApplicationLayer)

add_library(InfrastructureLayer
    infrastructure/adapters/in/ConsoleDroneController.cpp
    infrastructure/adapters/out/ConsoleDroneApiAdapter.cpp
    infrastructure/config/AppConfig.cpp
)

target_include_directories(InfrastructureLayer PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_link_libraries(InfrastructureLayer PUBLIC ApplicationLayer DomainLayer)
enable_project_warnings(InfrastructureLayer)

add_executable(DroneIBag151 main.cpp)
target_link_libraries(DroneIBag151 PRIVATE InfrastructureLayer)
enable_project_warnings(DroneIBag151)
