#ifndef APP_CONFIG_HPP
#define APP_CONFIG_HPP

#include <iostream>
#include <memory>

#include "infrastructure/adapters/in/ConsoleDroneController.hpp"

namespace ibag151 {

class AppConfig {
public:
    static std::unique_ptr<ConsoleDroneController> createConsoleController(
        std::istream& input = std::cin,
        std::ostream& output = std::cout);

    static int run(std::istream& input = std::cin,
                   std::ostream& output = std::cout);
};

}  // namespace ibag151

#endif
