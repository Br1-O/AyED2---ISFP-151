#ifndef CONSOLE_DRONE_CONTROLLER_HPP
#define CONSOLE_DRONE_CONTROLLER_HPP

#include <istream>
#include <memory>
#include <ostream>
#include <string>
#include <string_view>

#include "application/ports/in/IDroneControlUseCase.hpp"

namespace ibag151 {

class ConsoleDroneController {
public:
    ConsoleDroneController(std::shared_ptr<IDroneControlUseCase> useCase,
                           std::istream& input,
                           std::ostream& output);

    void run();

private:
    enum class ConsoleAction {
        TakeOff,
        Land,
        Elevate,
        Descend,
        TurnRight,
        TurnLeft,
        UnloadPackage,
        TakeReceptionPhoto,
        NotifyDelivery,
        Accelerate,
        Brake,
        Status,
        Help,
        Quit,
        Unknown
    };

    static std::string normalize(std::string_view text);
    static std::string trim(std::string_view text);
    static ConsoleAction parseCommand(std::string_view text);

    void execute(ConsoleAction action);
    void printHelp() const;
    void printStatus() const;

    std::shared_ptr<IDroneControlUseCase> useCase_;
    std::istream& input_;
    std::ostream& output_;
};

}  // namespace ibag151

#endif
