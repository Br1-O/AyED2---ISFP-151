#include "domain/entities/Drone.hpp"

#include <algorithm>
#include <stdexcept>
#include <string>
#include <utility>

namespace ibag151 {

Drone::Drone(std::string id, bool packageLoaded)
    : id_(std::move(id)), packageLoaded_(packageLoaded) {
    if (id_.empty()) {
        throw std::invalid_argument("El identificador del drone no puede estar vacio.");
    }
}

std::string Drone::id() const {
    return id_;
}

void Drone::takeOff() {
    if (status_ == FlightStatus::Flying) {
        throw std::domain_error("El drone ya esta en vuelo.");
    }

    status_ = FlightStatus::Flying;
    altitudeMeters_ = TakeOffAltitudeMeters;
}

void Drone::land() {
    if (status_ == FlightStatus::OnGround) {
        throw std::domain_error("El drone ya esta en tierra.");
    }

    status_ = FlightStatus::OnGround;
    altitudeMeters_ = 0;
    speedKph_ = 0;
}

void Drone::elevate() {
    requireFlying("elevar");

    if (altitudeMeters_ >= MaxAltitudeMeters) {
        throw std::domain_error("El drone alcanzo la altitud maxima de " +
                                std::to_string(MaxAltitudeMeters) + " m.");
    }

    altitudeMeters_ = std::min(altitudeMeters_ + ElevationStepMeters,
                               MaxAltitudeMeters);
}

void Drone::descend() {
    requireFlying("bajar");

    if (altitudeMeters_ - ElevationStepMeters < TakeOffAltitudeMeters) {
        throw std::domain_error(
            "El drone alcanzo la altitud minima de vuelo; use aterrizar.");
    }

    altitudeMeters_ -= ElevationStepMeters;
}

void Drone::turnRight() {
    requireFlying("girar a la derecha");
    headingDegrees_ = (headingDegrees_ + TurnStepDegrees) % 360;
}

void Drone::turnLeft() {
    requireFlying("girar a la izquierda");
    headingDegrees_ = (headingDegrees_ + 360 - TurnStepDegrees) % 360;
}

void Drone::unloadPackage() {
    if (!packageLoaded_) {
        throw std::domain_error("No hay paquete para descargar.");
    }

    packageLoaded_ = false;
}

void Drone::takeReceptionPhoto() {
    if (packageLoaded_) {
        throw std::domain_error(
            "Debe descargar el paquete antes de tomar la foto de recepcion.");
    }
    if (receptionPhotoTaken_) {
        throw std::domain_error("La foto de recepcion ya fue tomada.");
    }

    receptionPhotoTaken_ = true;
}

void Drone::notifyDelivery() {
    if (!receptionPhotoTaken_) {
        throw std::domain_error(
            "Debe tomar la foto de recepcion antes de notificar la entrega.");
    }
    if (deliveryNotified_) {
        throw std::domain_error("La entrega ya fue notificada.");
    }

    deliveryNotified_ = true;
}

void Drone::accelerate() {
    requireFlying("acelerar");

    if (speedKph_ >= MaxSpeedKph) {
        throw std::domain_error("El drone alcanzo la velocidad maxima de " +
                                std::to_string(MaxSpeedKph) + " km/h.");
    }

    speedKph_ = std::min(speedKph_ + SpeedStepKph, MaxSpeedKph);
}

void Drone::brake() {
    requireFlying("frenar");
    speedKph_ = std::max(0, speedKph_ - SpeedStepKph);
}

DroneTelemetry Drone::telemetry() const {
    return DroneTelemetry{
        status_,
        altitudeMeters_,
        speedKph_,
        headingDegrees_,
        packageLoaded_,
        receptionPhotoTaken_,
        deliveryNotified_,
    };
}

void Drone::requireFlying(std::string_view action) const {
    if (status_ != FlightStatus::Flying) {
        throw std::domain_error(
            "El drone debe estar en vuelo para " + std::string(action) + ".");
    }
}

}  // namespace ibag151
