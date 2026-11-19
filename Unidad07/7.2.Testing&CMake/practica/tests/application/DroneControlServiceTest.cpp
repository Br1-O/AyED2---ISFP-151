#include <gtest/gtest.h>

#include <memory>
#include <stdexcept>
#include <vector>

#include "application/services/DroneControlService.hpp"
#include "domain/entities/Drone.hpp"
#include "domain/ports/out/IDroneApi.hpp"
#include "domain/valueObjects/DroneAction.hpp"

namespace {

using ibag151::Drone;
using ibag151::DroneAction;
using ibag151::DroneControlService;
using ibag151::FlightStatus;
using ibag151::IDroneApi;

class FakeDroneApi final : public IDroneApi {
public:
    void execute(DroneAction action) override {
        actions_.push_back(action);
    }

    const std::vector<DroneAction>& actions() const {
        return actions_;
    }

private:
    std::vector<DroneAction> actions_;
};

struct DroneSystem {
    std::shared_ptr<Drone> drone{std::make_shared<Drone>()};
    std::shared_ptr<FakeDroneApi> api{std::make_shared<FakeDroneApi>()};
    std::shared_ptr<DroneControlService> service{
        std::make_shared<DroneControlService>(drone, api)};
};

}  // namespace

TEST(DroneControlServiceTest, ExposesTheDroneIdentityAndTelemetry) {
    DroneSystem system;

    EXPECT_EQ(system.service->id(), "IBag151");
    EXPECT_EQ(system.service->telemetry().status, FlightStatus::OnGround);
}

TEST(DroneControlServiceTest, TakeOffUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;

    system.service->takeOff();

    EXPECT_EQ(system.drone->telemetry().status, FlightStatus::Flying);
    ASSERT_EQ(system.api->actions().size(), 1U);
    EXPECT_EQ(system.api->actions().back(), DroneAction::TakeOff);
}

TEST(DroneControlServiceTest, LandUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();

    system.service->land();

    EXPECT_EQ(system.drone->telemetry().status, FlightStatus::OnGround);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::Land);
}

TEST(DroneControlServiceTest, ElevateUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();

    system.service->elevate();

    EXPECT_EQ(system.drone->telemetry().altitudeMeters,
              Drone::TakeOffAltitudeMeters + Drone::ElevationStepMeters);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::Elevate);
}

TEST(DroneControlServiceTest, DescendUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();
    system.service->elevate();

    system.service->descend();

    EXPECT_EQ(system.drone->telemetry().altitudeMeters,
              Drone::TakeOffAltitudeMeters);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::Descend);
}

TEST(DroneControlServiceTest, TurnRightUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();

    system.service->turnRight();

    EXPECT_EQ(system.drone->telemetry().headingDegrees, 90);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::TurnRight);
}

TEST(DroneControlServiceTest, TurnLeftUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();

    system.service->turnLeft();

    EXPECT_EQ(system.drone->telemetry().headingDegrees, 270);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::TurnLeft);
}

TEST(DroneControlServiceTest, UnloadPackageUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;

    system.service->unloadPackage();

    EXPECT_FALSE(system.drone->telemetry().packageLoaded);
    ASSERT_EQ(system.api->actions().size(), 1U);
    EXPECT_EQ(system.api->actions().back(), DroneAction::UnloadPackage);
}

TEST(DroneControlServiceTest, TakeReceptionPhotoUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->unloadPackage();

    system.service->takeReceptionPhoto();

    EXPECT_TRUE(system.drone->telemetry().receptionPhotoTaken);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::TakeReceptionPhoto);
}

TEST(DroneControlServiceTest, NotifyDeliveryUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->unloadPackage();
    system.service->takeReceptionPhoto();

    system.service->notifyDelivery();

    EXPECT_TRUE(system.drone->telemetry().deliveryNotified);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::NotifyDelivery);
}

TEST(DroneControlServiceTest, AccelerateUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();

    system.service->accelerate();

    EXPECT_EQ(system.drone->telemetry().speedKph, Drone::SpeedStepKph);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::Accelerate);
}

TEST(DroneControlServiceTest, BrakeUpdatesTheDroneAndSendsTheApiAction) {
    DroneSystem system;
    system.service->takeOff();
    system.service->accelerate();

    system.service->brake();

    EXPECT_EQ(system.drone->telemetry().speedKph, 0);
    ASSERT_FALSE(system.api->actions().empty());
    EXPECT_EQ(system.api->actions().back(), DroneAction::Brake);
}

TEST(DroneControlServiceTest, DoesNotSendAnApiActionWhenTheDomainRejectsIt) {
    DroneSystem system;
    system.service->takeOff();

    EXPECT_THROW(system.service->takeOff(), std::domain_error);

    ASSERT_EQ(system.api->actions().size(), 1U);
    EXPECT_EQ(system.api->actions().front(), DroneAction::TakeOff);
}
