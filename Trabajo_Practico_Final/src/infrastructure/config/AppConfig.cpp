#include "infrastructure/config/AppConfig.hpp"

#include <memory>

#include "application/services/DroneControlService.hpp"
#include "domain/entities/Drone.hpp"
#include "infrastructure/adapters/in/ConsoleDroneController.hpp"
#include "infrastructure/adapters/out/ConsoleDroneApiAdapter.hpp"

namespace ibag151 {

std::unique_ptr<ConsoleDroneController> AppConfig::createConsoleController(
    std::istream& input,
    std::ostream& output) {
    auto drone = std::make_shared<Drone>("IBag151");
    auto droneApi = std::make_shared<ConsoleDroneApiAdapter>(output);
    auto useCase = std::make_shared<DroneControlService>(drone, droneApi);

    return std::make_unique<ConsoleDroneController>(useCase, input, output);
}

int AppConfig::run(std::istream& input, std::ostream& output) {
    auto controller = createConsoleController(input, output);
    controller->run();
    return 0;
}

}  // namespace ibag151
