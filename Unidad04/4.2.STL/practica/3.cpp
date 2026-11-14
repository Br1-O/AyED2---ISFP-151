#include <iostream>
#include <map>

using namespace std;

int main() {
    // 1. Contenedor de mapa vacío
    map<int, string> Map1;

    // 2. Insertar elementos en orden aleatorio
    Map1[5] = "Cinco";
    Map1[2] = "Dos";
    Map1[8] = "Ocho";
    Map1[1] = "Uno";
    Map1[3] = "Tres";
    Map1[4] = "Cuatro";
    Map1[6] = "Seis";

    // 3. Imprimiendo mapa Map1
    cout << "--- Contenido de Map1 ---" << endl;
    for (const auto& [clave, valor] : Map1) {
        cout << "Clave: " << clave << " -> Valor: " << valor << endl;
    }

    // 4. Asignando los elementos de Map1 a Map2
    map<int, string> Map2 = Map1;

    // 5. Imprimir todos los elementos del mapa Map2
    cout << "\n--- Contenido de Map2 (copia de Map1) ---" << endl;
    for (const auto& kv : Map2) {
        cout << "Clave: " << kv.first << " -> Valor: " << kv.second << endl;
    }

    // 6. Eliminar todos los elementos hasta el elemento con clave = 3 en Map2
    auto itClave3 = Map2.find(3);
    if (itClave3 != Map2.end()) {
        Map2.erase(Map2.begin(), itClave3);
    }
    cout << "\n--- Map2 despues de eliminar elementos hasta clave = 3 ---" << endl;
    for (const auto& kv : Map2) {
        cout << "Clave: " << kv.first << " -> Valor: " << kv.second << endl;
    }

    // 7. Eliminar todos los elementos con clave = 4
    Map2.erase(4);
    cout << "\n--- Map2 despues de eliminar clave = 4 ---" << endl;
    for (const auto& kv : Map2) {
        cout << "Clave: " << kv.first << " -> Valor: " << kv.second << endl;
    }

    // 8. Límite inferior y límite superior para el mapa Map1 con clave = 5
    cout << "\n--- Busqueda lower_bound y upper_bound en Map1 (clave = 5) ---" << endl;
    auto lb = Map1.lower_bound(5);
    auto ub = Map1.upper_bound(5);

    if (lb != Map1.end()) {
        cout << "lower_bound(5) -> Clave: " << lb->first << ", Valor: " << lb->second << endl;
    }
    if (ub != Map1.end()) {
        cout << "upper_bound(5) -> Clave: " << ub->first << ", Valor: " << ub->second << endl;
    } else {
        cout << "upper_bound(5) apunta al final del contenedor." << endl;
    }

    return 0;
}