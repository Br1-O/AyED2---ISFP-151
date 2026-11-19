find_package(GTest QUIET)

if(NOT GTest_FOUND)
    include(FetchContent)

    FetchContent_Declare(googletest
        URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
    )

    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    set(INSTALL_GTEST OFF CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)
endif()

include(GoogleTest)

add_executable(domain_tests
    domain/DroneTest.cpp
)
target_link_libraries(domain_tests PRIVATE DomainLayer GTest::gtest_main)
enable_project_warnings(domain_tests)
gtest_discover_tests(domain_tests)

add_executable(application_tests
    application/DroneControlServiceTest.cpp
)
target_link_libraries(application_tests
    PRIVATE ApplicationLayer DomainLayer GTest::gtest_main
)
enable_project_warnings(application_tests)
gtest_discover_tests(application_tests)

add_executable(infrastructure_tests
    infrastructure/ConsoleDroneApiAdapterTest.cpp
    infrastructure/ConsoleDroneControllerTest.cpp
)
target_link_libraries(infrastructure_tests
    PRIVATE InfrastructureLayer ApplicationLayer DomainLayer GTest::gtest_main
)
enable_project_warnings(infrastructure_tests)
gtest_discover_tests(infrastructure_tests)
