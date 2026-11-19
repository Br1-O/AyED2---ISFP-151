#ifndef DRONE_TELEMETRY_HPP
#define DRONE_TELEMETRY_HPP

#include "domain/valueObjects/FlightStatus.hpp"

namespace ibag151 {

struct DroneTelemetry {
    FlightStatus status{FlightStatus::OnGround};
    int altitudeMeters{0};
    int speedKph{0};
    int headingDegrees{0};
    bool packageLoaded{true};
    bool receptionPhotoTaken{false};
    bool deliveryNotified{false};
};

inline bool operator==(const DroneTelemetry& lhs, const DroneTelemetry& rhs) noexcept {
    return lhs.status == rhs.status &&
           lhs.altitudeMeters == rhs.altitudeMeters &&
           lhs.speedKph == rhs.speedKph &&
           lhs.headingDegrees == rhs.headingDegrees &&
           lhs.packageLoaded == rhs.packageLoaded &&
           lhs.receptionPhotoTaken == rhs.receptionPhotoTaken &&
           lhs.deliveryNotified == rhs.deliveryNotified;
}

inline bool operator!=(const DroneTelemetry& lhs, const DroneTelemetry& rhs) noexcept {
    return !(lhs == rhs);
}

}  // namespace ibag151

#endif
