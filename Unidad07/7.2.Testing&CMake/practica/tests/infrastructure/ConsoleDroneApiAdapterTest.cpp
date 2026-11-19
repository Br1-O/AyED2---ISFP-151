#include <gtest/gtest.h>

#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include "domain/valueObjects/DroneAction.hpp"
#include "infrastructure/adapters/out/ConsoleDroneApiAdapter.hpp"

namespace {

using ibag151::ConsoleDroneApiAdapter;
using ibag151::DroneAction;

struct CommandCase {
    DroneAction action;
    std::string expectedText;
};

}  // namespace

TEST(ConsoleDroneApiAdapterTest, TranslatesEveryActivityToApiText) {
    const std::vector<CommandCase> cases{
        {DroneAction::TakeOff, "DESPEGAR"},
        {DroneAction::Land, "ATERRIZAR"},
        {DroneAction::Elevate, "ELEVAR"},
        {DroneAction::Descend, "BAJAR"},
        {DroneAction::TurnRight, "GIRAR DERECHA"},
        {DroneAction::TurnLeft, "GIRAR IZQUIERDA"},
        {DroneAction::UnloadPackage, "DESCARGAR PAQUETE"},
        {DroneAction::TakeReceptionPhoto, "SACAR FOTO DE RECEPCION"},
        {DroneAction::NotifyDelivery, "NOTIFICAR ENTREGA"},
        {DroneAction::Accelerate, "ACELERAR"},
        {DroneAction::Brake, "FRENAR"},
    };

    for (const auto& testCase : cases) {
        std::ostringstream output;
        ConsoleDroneApiAdapter adapter(output);

        adapter.execute(testCase.action);

        EXPECT_EQ(output.str(), "[API Drone] " + testCase.expectedText + "\n");
    }
}

TEST(ConsoleDroneApiAdapterTest, AppendsCommandsToTheSameStream) {
    std::ostringstream output;
    ConsoleDroneApiAdapter adapter(output);

    adapter.execute(DroneAction::TakeOff);
    adapter.execute(DroneAction::Accelerate);

    EXPECT_EQ(output.str(),
              "[API Drone] DESPEGAR\n[API Drone] ACELERAR\n");
}
