#include "infrastructure/config/AppConfig.hpp"

int main() {
    auto menu = AppConfig::createConsoleMenu();
    menu->start();
    return 0;
}