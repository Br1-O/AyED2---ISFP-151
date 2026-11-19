#include <gtest/gtest.h>

#include <memory>
#include <stdexcept>

#include "domain/entities/Drone.hpp"

namespace {

using ibag151::Drone;
using ibag151::FlightStatus;

std::shared_ptr<Drone> makeFlyingDrone() {
    auto drone = std::make_shared<Drone>();
    drone->takeOff();
    return drone;
}

}  // namespace

TEST(DroneInitialStateTest, StartsOnGroundWithPackageAndNoDeliveryActivity) {
    const Drone drone;

    EXPECT_EQ(drone.id(), "IBag151");
    EXPECT_EQ(drone.telemetry().status, FlightStatus::OnGround);
    EXPECT_EQ(drone.telemetry().altitudeMeters, 0);
    EXPECT_EQ(drone.telemetry().speedKph, 0);
    EXPECT_EQ(drone.telemetry().headingDegrees, 0);
    EXPECT_TRUE(drone.telemetry().packageLoaded);
    EXPECT_FALSE(drone.telemetry().receptionPhotoTaken);
    EXPECT_FALSE(drone.telemetry().deliveryNotified);
}

TEST(DroneInitialStateTest, RejectsAnEmptyIdentifier) {
    EXPECT_THROW(Drone(""), std::invalid_argument);
}

TEST(DroneTakeOffTest, TakesOffFromTheGround) {
    Drone drone;

    drone.takeOff();

    EXPECT_EQ(drone.telemetry().status, FlightStatus::Flying);
    EXPECT_EQ(drone.telemetry().altitudeMeters, Drone::TakeOffAltitudeMeters);
}

TEST(DroneTakeOffTest, CannotTakeOffTwice) {
    Drone drone;
    drone.takeOff();

    EXPECT_THROW(drone.takeOff(), std::domain_error);

    EXPECT_EQ(drone.telemetry().status, FlightStatus::Flying);
    EXPECT_EQ(drone.telemetry().altitudeMeters, Drone::TakeOffAltitudeMeters);
}

TEST(DroneLandTest, LandsAndStopsTheDrone) {
    auto drone = makeFlyingDrone();
    drone->accelerate();

    drone->land();

    EXPECT_EQ(drone->telemetry().status, FlightStatus::OnGround);
    EXPECT_EQ(drone->telemetry().altitudeMeters, 0);
    EXPECT_EQ(drone->telemetry().speedKph, 0);
}

TEST(DroneLandTest, CannotLandWhenAlreadyOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.land(), std::domain_error);

    EXPECT_EQ(drone.telemetry().status, FlightStatus::OnGround);
}

TEST(DroneElevateTest, ElevatesInStepsWhileFlying) {
    auto drone = makeFlyingDrone();

    drone->elevate();

    EXPECT_EQ(drone->telemetry().altitudeMeters,
              Drone::TakeOffAltitudeMeters + Drone::ElevationStepMeters);
}

TEST(DroneElevateTest, StopsAtTheMaximumAltitude) {
    auto drone = makeFlyingDrone();
    while (drone->telemetry().altitudeMeters < Drone::MaxAltitudeMeters) {
        drone->elevate();
    }

    EXPECT_THROW(drone->elevate(), std::domain_error);

    EXPECT_EQ(drone->telemetry().altitudeMeters, Drone::MaxAltitudeMeters);
}

TEST(DroneElevateTest, CannotElevateOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.elevate(), std::domain_error);

    EXPECT_EQ(drone.telemetry().altitudeMeters, 0);
}

TEST(DroneDescendTest, DescendsInStepsWhileFlying) {
    auto drone = makeFlyingDrone();
    drone->elevate();

    drone->descend();

    EXPECT_EQ(drone->telemetry().altitudeMeters, Drone::TakeOffAltitudeMeters);
}

TEST(DroneDescendTest, CannotDescendBelowTheMinimumFlightAltitude) {
    auto drone = makeFlyingDrone();

    EXPECT_THROW(drone->descend(), std::domain_error);

    EXPECT_EQ(drone->telemetry().altitudeMeters, Drone::TakeOffAltitudeMeters);
}

TEST(DroneDescendTest, CannotDescendOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.descend(), std::domain_error);
}

TEST(DroneTurnRightTest, TurnsNinetyDegreesToTheRight) {
    auto drone = makeFlyingDrone();

    drone->turnRight();

    EXPECT_EQ(drone->telemetry().headingDegrees, 90);
}

TEST(DroneTurnRightTest, WrapsHeadingAroundNorth) {
    auto drone = makeFlyingDrone();
    drone->turnRight();
    drone->turnRight();
    drone->turnRight();

    drone->turnRight();

    EXPECT_EQ(drone->telemetry().headingDegrees, 0);
}

TEST(DroneTurnRightTest, CannotTurnOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.turnRight(), std::domain_error);
}

TEST(DroneTurnLeftTest, TurnsNinetyDegreesToTheLeft) {
    auto drone = makeFlyingDrone();

    drone->turnLeft();

    EXPECT_EQ(drone->telemetry().headingDegrees, 270);
}

TEST(DroneTurnLeftTest, WrapsHeadingAroundNorth) {
    auto drone = makeFlyingDrone();
    drone->turnRight();

    drone->turnLeft();

    EXPECT_EQ(drone->telemetry().headingDegrees, 0);
}

TEST(DroneTurnLeftTest, CannotTurnOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.turnLeft(), std::domain_error);
}

TEST(DroneUnloadPackageTest, UnloadsThePackageOnlyOnce) {
    Drone drone;

    drone.unloadPackage();

    EXPECT_FALSE(drone.telemetry().packageLoaded);
    EXPECT_THROW(drone.unloadPackage(), std::domain_error);
    EXPECT_FALSE(drone.telemetry().packageLoaded);
}

TEST(DroneReceptionPhotoTest, TakesThePhotoAfterUnloadingThePackage) {
    Drone drone;
    drone.unloadPackage();

    drone.takeReceptionPhoto();

    EXPECT_TRUE(drone.telemetry().receptionPhotoTaken);
}

TEST(DroneReceptionPhotoTest, RequiresThePackageToBeUnloadedFirst) {
    Drone drone;

    EXPECT_THROW(drone.takeReceptionPhoto(), std::domain_error);

    EXPECT_FALSE(drone.telemetry().receptionPhotoTaken);
}

TEST(DroneReceptionPhotoTest, CannotTakeThePhotoTwice) {
    Drone drone;
    drone.unloadPackage();
    drone.takeReceptionPhoto();

    EXPECT_THROW(drone.takeReceptionPhoto(), std::domain_error);
}

TEST(DroneNotifyDeliveryTest, NotifiesTheDeliveryAfterTakingThePhoto) {
    Drone drone;
    drone.unloadPackage();
    drone.takeReceptionPhoto();

    drone.notifyDelivery();

    EXPECT_TRUE(drone.telemetry().deliveryNotified);
}

TEST(DroneNotifyDeliveryTest, RequiresTheReceptionPhotoFirst) {
    Drone drone;
    drone.unloadPackage();

    EXPECT_THROW(drone.notifyDelivery(), std::domain_error);

    EXPECT_FALSE(drone.telemetry().deliveryNotified);
}

TEST(DroneNotifyDeliveryTest, CannotNotifyTheDeliveryTwice) {
    Drone drone;
    drone.unloadPackage();
    drone.takeReceptionPhoto();
    drone.notifyDelivery();

    EXPECT_THROW(drone.notifyDelivery(), std::domain_error);
}

TEST(DroneAccelerateTest, AcceleratesInStepsWhileFlying) {
    auto drone = makeFlyingDrone();

    drone->accelerate();

    EXPECT_EQ(drone->telemetry().speedKph, Drone::SpeedStepKph);
}

TEST(DroneAccelerateTest, StopsAtTheMaximumSpeed) {
    auto drone = makeFlyingDrone();
    while (drone->telemetry().speedKph < Drone::MaxSpeedKph) {
        drone->accelerate();
    }

    EXPECT_THROW(drone->accelerate(), std::domain_error);

    EXPECT_EQ(drone->telemetry().speedKph, Drone::MaxSpeedKph);
}

TEST(DroneAccelerateTest, CannotAccelerateOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.accelerate(), std::domain_error);

    EXPECT_EQ(drone.telemetry().speedKph, 0);
}

TEST(DroneBrakeTest, BrakesInStepsWhileFlying) {
    auto drone = makeFlyingDrone();
    drone->accelerate();
    drone->accelerate();

    drone->brake();

    EXPECT_EQ(drone->telemetry().speedKph, Drone::SpeedStepKph);
}

TEST(DroneBrakeTest, CannotBrakeBelowZero) {
    auto drone = makeFlyingDrone();
    drone->accelerate();

    drone->brake();
    drone->brake();

    EXPECT_EQ(drone->telemetry().speedKph, 0);
}

TEST(DroneBrakeTest, CannotBrakeOnTheGround) {
    Drone drone;

    EXPECT_THROW(drone.brake(), std::domain_error);
}
