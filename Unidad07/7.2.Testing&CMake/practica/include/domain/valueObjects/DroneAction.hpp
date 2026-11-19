#ifndef DRONE_ACTION_HPP
#define DRONE_ACTION_HPP

namespace ibag151 {

enum class DroneAction {
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
    Brake
};

}  // namespace ibag151

#endif
