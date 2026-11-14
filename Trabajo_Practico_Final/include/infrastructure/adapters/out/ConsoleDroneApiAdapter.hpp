#ifndef CONSOLE_DRONE_API_ADAPTER_HPP
#define CONSOLE_DRONE_API_ADAPTER_HPP

#include <ostream>
#include <string_view>

#include "domain/ports/out/IDroneApi.hpp"

namespace ibag151 {

class ConsoleDroneApiAdapter final : public IDroneApi {
public:
    explicit ConsoleDroneApiAdapter(std::ostream& output);

    void execute(DroneAction action) override;

private:
    static std::string_view commandText(DroneAction action) noexcept;

    std::ostream& output_;
};

}  // namespace ibag151

#endif
