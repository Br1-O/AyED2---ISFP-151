#include "infrastructure/adapters/out/ConsoleDroneApiAdapter.hpp"

#include <string_view>

namespace ibag151 {

ConsoleDroneApiAdapter::ConsoleDroneApiAdapter(std::ostream& output)
    : output_(output) {}

void ConsoleDroneApiAdapter::execute(DroneAction action) {
    output_ << "[API Drone] " << commandText(action) << '\n';
}

std::string_view ConsoleDroneApiAdapter::commandText(DroneAction action) noexcept {
    switch (action) {
        case DroneAction::TakeOff:
            return "DESPEGAR";
        case DroneAction::Land:
            return "ATERRIZAR";
        case DroneAction::Elevate:
            return "ELEVAR";
        case DroneAction::Descend:
            return "BAJAR";
        case DroneAction::TurnRight:
            return "GIRAR DERECHA";
        case DroneAction::TurnLeft:
            return "GIRAR IZQUIERDA";
        case DroneAction::UnloadPackage:
            return "DESCARGAR PAQUETE";
        case DroneAction::TakeReceptionPhoto:
            return "SACAR FOTO DE RECEPCION";
        case DroneAction::NotifyDelivery:
            return "NOTIFICAR ENTREGA";
        case DroneAction::Accelerate:
            return "ACELERAR";
        case DroneAction::Brake:
            return "FRENAR";
    }

    return "ACCION DESCONOCIDA";
}

}  // namespace ibag151
