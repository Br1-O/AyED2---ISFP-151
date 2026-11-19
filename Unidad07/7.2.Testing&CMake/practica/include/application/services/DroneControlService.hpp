#ifndef DRONE_CONTROL_SERVICE_HPP
#define DRONE_CONTROL_SERVICE_HPP

#include <memory>
#include <string>

#include "application/ports/in/IDroneControlUseCase.hpp"
#include "domain/entities/IDrone.hpp"
#include "domain/ports/out/IDroneApi.hpp"

namespace ibag151 {

class DroneControlService final : public IDroneControlUseCase {
public:
    DroneControlService(std::shared_ptr<IDrone> drone,
                        std::shared_ptr<IDroneApi> droneApi);

    std::string id() const override;
    void takeOff() override;
    void land() override;
    void elevate() override;
    void descend() override;
    void turnRight() override;
    void turnLeft() override;
    void unloadPackage() override;
    void takeReceptionPhoto() override;
    void notifyDelivery() override;
    void accelerate() override;
    void brake() override;

    DroneTelemetry telemetry() const override;

private:
    std::shared_ptr<IDrone> drone_;
    std::shared_ptr<IDroneApi> droneApi_;
};

}  // namespace ibag151

#endif
