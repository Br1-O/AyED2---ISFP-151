#include "application/services/DroneControlService.hpp"

#include <stdexcept>
#include <utility>

#include "domain/valueObjects/DroneAction.hpp"

namespace ibag151 {

DroneControlService::DroneControlService(std::shared_ptr<IDrone> drone,
                                         std::shared_ptr<IDroneApi> droneApi)
    : drone_(std::move(drone)), droneApi_(std::move(droneApi)) {
    if (!drone_ || !droneApi_) {
        throw std::invalid_argument(
            "El servicio requiere un drone y una API no nulos.");
    }
}

std::string DroneControlService::id() const {
    return drone_->id();
}

void DroneControlService::takeOff() {
    drone_->takeOff();
    droneApi_->execute(DroneAction::TakeOff);
}

void DroneControlService::land() {
    drone_->land();
    droneApi_->execute(DroneAction::Land);
}

void DroneControlService::elevate() {
    drone_->elevate();
    droneApi_->execute(DroneAction::Elevate);
}

void DroneControlService::descend() {
    drone_->descend();
    droneApi_->execute(DroneAction::Descend);
}

void DroneControlService::turnRight() {
    drone_->turnRight();
    droneApi_->execute(DroneAction::TurnRight);
}

void DroneControlService::turnLeft() {
    drone_->turnLeft();
    droneApi_->execute(DroneAction::TurnLeft);
}

void DroneControlService::unloadPackage() {
    drone_->unloadPackage();
    droneApi_->execute(DroneAction::UnloadPackage);
}

void DroneControlService::takeReceptionPhoto() {
    drone_->takeReceptionPhoto();
    droneApi_->execute(DroneAction::TakeReceptionPhoto);
}

void DroneControlService::notifyDelivery() {
    drone_->notifyDelivery();
    droneApi_->execute(DroneAction::NotifyDelivery);
}

void DroneControlService::accelerate() {
    drone_->accelerate();
    droneApi_->execute(DroneAction::Accelerate);
}

void DroneControlService::brake() {
    drone_->brake();
    droneApi_->execute(DroneAction::Brake);
}

DroneTelemetry DroneControlService::telemetry() const {
    return drone_->telemetry();
}

}  // namespace ibag151
