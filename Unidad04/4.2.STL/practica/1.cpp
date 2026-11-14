#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void imprimirVector(const vector<int>& v) {
    for (int val : v) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    // 1. Definir un vector de enteros e insertar elementos
    vector<int> vec = {10, 20, 30, 40, 50};

    // 2. Imprimir contenido inicial utilizando bucle basado en rangos
    cout << "Vector inicial: ";
    imprimirVector(vec);

    // 3. Borrar el segundo elemento del vector (índice 1)
    if (vec.size() > 1) {
        vec.erase(vec.begin() + 1);
    }
    cout << "Despues de borrar el segundo elemento: ";
    imprimirVector(vec);

    // 4. Borrar el rango de 3 elementos a partir del principio del vector
    if (vec.size() >= 3) {
        vec.erase(vec.begin(), vec.begin() + 3);
    }
    cout << "Despues de borrar el rango de 3 elementos desde el inicio: ";
    imprimirVector(vec);

    // Repoblar el vector para probar la búsqueda y eliminación con std::find
    vec = {5, 12, 25, 33, 50};
    cout << "\nVector para busqueda: ";
    imprimirVector(vec);

    // 5. Buscar un elemento vectorial utilizando la función std::find()
    int valorBuscar = 25;
    auto it = find(vec.begin(), vec.end(), valorBuscar);

    // 6. Si se ha encontrado el elemento, eliminarlo
    if (it != vec.end()) {
        cout << "Elemento " << valorBuscar << " encontrado. Eliminando..." << endl;
        vec.erase(it);
    } else {
        cout << "Elemento " << valorBuscar << " no encontrado." << endl;
    }

    // 7. Imprimir el contenido vectorial final
    cout << "Vector final: ";
    imprimirVector(vec);

    return 0;
}