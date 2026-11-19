#include "infrastructure/adapters/in/ConsoleDroneController.hpp"

#include <algorithm>
#include <cctype>
#include <exception>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace ibag151 {

ConsoleDroneController::ConsoleDroneController(
    std::shared_ptr<IDroneControlUseCase> useCase,
    std::istream& input,
    std::ostream& output)
    : useCase_(std::move(useCase)), input_(input), output_(output) {}

void ConsoleDroneController::run() {
    output_ << "=============================================\n";
    output_ << " Control del Drone IBag151\n";
    output_ << "=============================================\n";
    printHelp();

    std::string line;
    while (true) {
        output_ << "\n> " << std::flush;
        if (!std::getline(input_, line)) {
            break;
        }

        const ConsoleAction action = parseCommand(line);
        if (action == ConsoleAction::Quit) {
            output_ << "Saliendo del control del drone.\n";
            break;
        }

        try {
            execute(action);
        } catch (const std::exception& error) {
            output_ << "[Error] " << error.what() << '\n';
        }
    }
}

std::string ConsoleDroneController::normalize(std::string_view text) {
    std::string normalized = trim(text);
    std::transform(normalized.begin(),
                   normalized.end(),
                   normalized.begin(),
                   [](unsigned char character) {
                       return static_cast<char>(std::tolower(character));
                   });
    return normalized;
}

std::string ConsoleDroneController::trim(std::string_view text) {
    const auto first = text.find_first_not_of(" \t\r\n");
    if (first == std::string_view::npos) {
        return {};
    }

    const auto last = text.find_last_not_of(" \t\r\n");
    return std::string(text.substr(first, last - first + 1));
}

ConsoleDroneController::ConsoleAction ConsoleDroneController::parseCommand(
    std::string_view text) {
    static const std::unordered_map<std::string, ConsoleAction> actions{
        {"despegar", ConsoleAction::TakeOff},
        {"aterrizar", ConsoleAction::Land},
        {"elevar", ConsoleAction::Elevate},
        {"bajar", ConsoleAction::Descend},
        {"derecha", ConsoleAction::TurnRight},
        {"girar derecha", ConsoleAction::TurnRight},
        {"girar-derecha", ConsoleAction::TurnRight},
        {"izquierda", ConsoleAction::TurnLeft},
        {"girar izquierda", ConsoleAction::TurnLeft},
        {"girar-izquierda", ConsoleAction::TurnLeft},
        {"descargar", ConsoleAction::UnloadPackage},
        {"foto", ConsoleAction::TakeReceptionPhoto},
        {"notificar", ConsoleAction::NotifyDelivery},
        {"acelerar", ConsoleAction::Accelerate},
        {"frenar", ConsoleAction::Brake},
        {"estado", ConsoleAction::Status},
        {"ayuda", ConsoleAction::Help},
        {"salir", ConsoleAction::Quit},
    };

    const auto found = actions.find(normalize(text));
    return found == actions.end() ? ConsoleAction::Unknown : found->second;
}

void ConsoleDroneController::execute(ConsoleAction action) {
    switch (action) {
        case ConsoleAction::TakeOff:
            useCase_->takeOff();
            break;
        case ConsoleAction::Land:
            useCase_->land();
            break;
        case ConsoleAction::Elevate:
            useCase_->elevate();
            break;
        case ConsoleAction::Descend:
            useCase_->descend();
            break;
        case ConsoleAction::TurnRight:
            useCase_->turnRight();
            break;
        case ConsoleAction::TurnLeft:
            useCase_->turnLeft();
            break;
        case ConsoleAction::UnloadPackage:
            useCase_->unloadPackage();
            break;
        case ConsoleAction::TakeReceptionPhoto:
            useCase_->takeReceptionPhoto();
            break;
        case ConsoleAction::NotifyDelivery:
            useCase_->notifyDelivery();
            break;
        case ConsoleAction::Accelerate:
            useCase_->accelerate();
            break;
        case ConsoleAction::Brake:
            useCase_->brake();
            break;
        case ConsoleAction::Status:
            printStatus();
            break;
        case ConsoleAction::Help:
            printHelp();
            break;
        case ConsoleAction::Quit:
            break;
        case ConsoleAction::Unknown:
            output_ << "[Error] Comando desconocido. Escriba 'ayuda' para ver "
                       "los comandos disponibles.\n";
            break;
    }
}

void ConsoleDroneController::printHelp() const {
    const std::vector<std::pair<std::string, std::string>> commands{
        {"despegar", "iniciar el vuelo"},
        {"aterrizar", "descender y detener el drone"},
        {"elevar", "subir 10 metros"},
        {"bajar", "descender 10 metros"},
        {"derecha", "girar 90 grados a la derecha"},
        {"izquierda", "girar 90 grados a la izquierda"},
        {"descargar", "descargar el paquete"},
        {"foto", "tomar la foto de recepcion"},
        {"notificar", "notificar la entrega"},
        {"acelerar", "aumentar 10 km/h"},
        {"frenar", "reducir 10 km/h"},
        {"estado", "mostrar la telemetria"},
        {"ayuda", "mostrar esta ayuda"},
        {"salir", "cerrar la aplicacion"},
    };

    output_ << "\nComandos disponibles:\n";
    for (const auto& command : commands) {
        output_ << "  " << command.first << " - " << command.second << '\n';
    }
}

void ConsoleDroneController::printStatus() const {
    const DroneTelemetry telemetry = useCase_->telemetry();

    output_ << "--- Estado del drone " << useCase_->id() << " ---\n";
    output_ << "Estado: "
            << (telemetry.status == FlightStatus::Flying ? "En vuelo"
                                                         : "En tierra")
            << '\n';
    output_ << "Altitud: " << telemetry.altitudeMeters << " m\n";
    output_ << "Velocidad: " << telemetry.speedKph << " km/h\n";
    output_ << "Rumbo: " << telemetry.headingDegrees << " grados\n";
    output_ << "Paquete: "
            << (telemetry.packageLoaded ? "cargado" : "descargado") << '\n';
    output_ << "Foto de recepcion: "
            << (telemetry.receptionPhotoTaken ? "tomada" : "pendiente") << '\n';
    output_ << "Entrega: "
            << (telemetry.deliveryNotified ? "notificada" : "pendiente") << '\n';
}

}  // namespace ibag151
