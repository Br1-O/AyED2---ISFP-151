#ifndef I_DRONE_API_HPP
#define I_DRONE_API_HPP

#include "domain/valueObjects/DroneAction.hpp"

namespace ibag151 {

class IDroneApi {
public:
    virtual ~IDroneApi() = default;

    virtual void execute(DroneAction action) = 0;
};

}  // namespace ibag151

#endif
