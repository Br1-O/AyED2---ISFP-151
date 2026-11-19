#include <gtest/gtest.h>

#include <memory>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include "application/ports/in/IDroneControlUseCase.hpp"
#include "application/services/DroneControlService.hpp"
#include "domain/entities/Drone.hpp"
#include "domain/valueObjects/DroneTelemetry.hpp"
#include "infrastructure/adapters/in/ConsoleDroneController.hpp"
#include "infrastructure/adapters/out/ConsoleDroneApiAdapter.hpp"

namespace {

using ibag151::ConsoleDroneApiAdapter;
using ibag151::ConsoleDroneController;
using ibag151::Drone;
using ibag151::DroneControlService;
using ibag151::DroneTelemetry;
using ibag151::FlightStatus;
using ibag151::IDroneControlUseCase;

class FakeDroneControlUseCase final : public IDroneControlUseCase {
public:
    std::string id() const override {
        return "IBag151";
    }

    void takeOff() override { record("takeOff"); }
    void land() override { record("land"); }
    void elevate() override { record("elevate"); }
    void descend() override { record("descend"); }
    void turnRight() override { record("turnRight"); }
    void turnLeft() override { record("turnLeft"); }
    void unloadPackage() override { record("unloadPackage"); }
    void takeReceptionPhoto() override { record("takeReceptionPhoto"); }
    void notifyDelivery() override { record("notifyDelivery"); }
    void accelerate() override { record("accelerate"); }
    void brake() override { record("brake"); }

    DroneTelemetry telemetry() const override {
        return telemetry_;
    }

    const std::vector<std::string>& calls() const {
        return calls_;
    }

    DroneTelemetry& mutableTelemetry() {
        return telemetry_;
    }

private:
    void record(const std::string& call) {
        calls_.push_back(call);
    }

    std::vector<std::string> calls_;
    DroneTelemetry telemetry_;
};

struct CommandCase {
    std::string input;
    std::string expectedCall;
};

void runController(const std::string& input,
                   const std::shared_ptr<FakeDroneControlUseCase>& useCase,
                   std::ostringstream& output) {
    std::istringstream inputStream(input);
    ConsoleDroneController controller(useCase, inputStream, output);
    controller.run();
}

}  // namespace

TEST(ConsoleDroneControllerTest, DispatchesEveryActivityToTheUseCase) {
    const std::vector<CommandCase> cases{
        {"despegar", "takeOff"},
        {"aterrizar", "land"},
        {"elevar", "elevate"},
        {"bajar", "descend"},
        {"derecha", "turnRight"},
        {"izquierda", "turnLeft"},
        {"descargar", "unloadPackage"},
        {"foto", "takeReceptionPhoto"},
        {"notificar", "notifyDelivery"},
        {"acelerar", "accelerate"},
        {"frenar", "brake"},
    };

    for (const auto& testCase : cases) {
        auto useCase = std::make_shared<FakeDroneControlUseCase>();
        std::ostringstream output;

        runController(testCase.input + "\nsalir\n", useCase, output);

        EXPECT_EQ(useCase->calls(), std::vector<std::string>{testCase.expectedCall});
    }
}

TEST(ConsoleDroneControllerTest, AcceptsUppercaseCommandsAndExtraWhitespace) {
    auto useCase = std::make_shared<FakeDroneControlUseCase>();
    std::ostringstream output;

    runController("   DESPEGAR   \nsalir\n", useCase, output);

    EXPECT_EQ(useCase->calls(), std::vector<std::string>{"takeOff"});
}

TEST(ConsoleDroneControllerTest, AcceptsSpokenAliasesForTurns) {
    auto useCase = std::make_shared<FakeDroneControlUseCase>();
    std::ostringstream output;

    runController("girar derecha\ngirar-izquierda\nsalir\n", useCase, output);

    EXPECT_EQ(useCase->calls(),
              (std::vector<std::string>{"turnRight", "turnLeft"}));
}

TEST(ConsoleDroneControllerTest, PrintsTheTelemetryOnStatusRequest) {
    auto useCase = std::make_shared<FakeDroneControlUseCase>();
    useCase->mutableTelemetry().status = FlightStatus::Flying;
    useCase->mutableTelemetry().altitudeMeters = 30;
    useCase->mutableTelemetry().speedKph = 20;
    useCase->mutableTelemetry().headingDegrees = 90;
    useCase->mutableTelemetry().packageLoaded = false;
    useCase->mutableTelemetry().receptionPhotoTaken = true;
    std::ostringstream output;

    runController("estado\nsalir\n", useCase, output);

    EXPECT_TRUE(useCase->calls().empty());
    EXPECT_NE(output.str().find("IBag151"), std::string::npos);
    EXPECT_NE(output.str().find("En vuelo"), std::string::npos);
    EXPECT_NE(output.str().find("30 m"), std::string::npos);
    EXPECT_NE(output.str().find("20 km/h"), std::string::npos);
    EXPECT_NE(output.str().find("90"), std::string::npos);
}

TEST(ConsoleDroneControllerTest, RejectsUnknownCommandsWithoutCallingTheUseCase) {
    auto useCase = std::make_shared<FakeDroneControlUseCase>();
    std::ostringstream output;

    runController("volar\nsalir\n", useCase, output);

    EXPECT_TRUE(useCase->calls().empty());
    EXPECT_NE(output.str().find("Comando desconocido"), std::string::npos);
}

TEST(ConsoleDroneControllerTest, PrintsHelpWithoutCallingTheUseCase) {
    auto useCase = std::make_shared<FakeDroneControlUseCase>();
    std::ostringstream output;

    runController("ayuda\nsalir\n", useCase, output);

    EXPECT_TRUE(useCase->calls().empty());
    EXPECT_NE(output.str().find("despegar"), std::string::npos);
    EXPECT_NE(output.str().find("notificar"), std::string::npos);
}

TEST(ConsoleDroneControllerTest, ReportsDomainErrorsAndKeepsRunning) {
    auto drone = std::make_shared<Drone>();
    std::ostringstream output;
    auto api = std::make_shared<ConsoleDroneApiAdapter>(output);
    auto service = std::make_shared<DroneControlService>(drone, api);
    std::istringstream input("aterrizar\nestado\nsalir\n");
    ConsoleDroneController controller(service, input, output);

    controller.run();

    EXPECT_NE(output.str().find("[Error] El drone ya esta en tierra."),
              std::string::npos);
    EXPECT_EQ(output.str().find("[API Drone]"), std::string::npos);
    EXPECT_NE(output.str().find("En tierra"), std::string::npos);
}
