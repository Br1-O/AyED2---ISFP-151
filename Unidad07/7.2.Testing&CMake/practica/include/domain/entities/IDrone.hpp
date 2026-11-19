#ifndef I_DRONE_HPP
#define I_DRONE_HPP

#include <string>

#include "domain/valueObjects/DroneTelemetry.hpp"

namespace ibag151 {

class IDrone {
public:
    virtual ~IDrone() = default;

    virtual std::string id() const = 0;
    virtual void takeOff() = 0;
    virtual void land() = 0;
    virtual void elevate() = 0;
    virtual void descend() = 0;
    virtual void turnRight() = 0;
    virtual void turnLeft() = 0;
    virtual void unloadPackage() = 0;
    virtual void takeReceptionPhoto() = 0;
    virtual void notifyDelivery() = 0;
    virtual void accelerate() = 0;
    virtual void brake() = 0;

    virtual DroneTelemetry telemetry() const = 0;
};

}  // namespace ibag151

#endif
