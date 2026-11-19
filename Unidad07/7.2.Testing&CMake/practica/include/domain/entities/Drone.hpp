#ifndef DRONE_HPP
#define DRONE_HPP

#include <string>
#include <string_view>

#include "domain/entities/IDrone.hpp"

namespace ibag151 {

class Drone final : public IDrone {
public:
    static constexpr int MaxAltitudeMeters = 120;
    static constexpr int ElevationStepMeters = 10;
    static constexpr int MaxSpeedKph = 100;
    static constexpr int SpeedStepKph = 10;
    static constexpr int TurnStepDegrees = 90;
    static constexpr int TakeOffAltitudeMeters = 10;

    explicit Drone(std::string id = "IBag151", bool packageLoaded = true);

    std::string id() const override;
    void takeOff() override;
    void land() override;
    void elevate() override;
    void descend() override;
    void turnRight() override;
    void turnLeft() override;
    void unloadPackage() override;
    void takeReceptionPhoto() override;
    void notifyDelivery() override;
    void accelerate() override;
    void brake() override;

    DroneTelemetry telemetry() const override;

private:
    void requireFlying(std::string_view action) const;

    std::string id_;
    FlightStatus status_{FlightStatus::OnGround};
    int altitudeMeters_{0};
    int speedKph_{0};
    int headingDegrees_{0};
    bool packageLoaded_{true};
    bool receptionPhotoTaken_{false};
    bool deliveryNotified_{false};
};

}  // namespace ibag151

#endif
