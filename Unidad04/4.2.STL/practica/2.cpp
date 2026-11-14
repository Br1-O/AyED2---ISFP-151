#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Función para imprimir utilizando iteradores
void imprimirConIterador(const vector<int>& v) {
    for (auto it = v.begin(); it != v.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
}

int main() {
    vector<int> vec = {10, 20, 30, 40, 50};

    cout << "Vector inicial con iteradores: ";
    imprimirConIterador(vec);

    // Borrar el segundo elemento usando iterador aritmético
    if (vec.size() > 1) {
        vec.erase(vec.begin() + 1);
    }
    cout << "Despues de borrar el segundo elemento: ";
    imprimirConIterador(vec);

    // Borrar un rango de 3 elementos a partir del principio usando iteradores
    if (vec.size() >= 3) {
        vec.erase(vec.begin(), vec.begin() + 3);
    }
    cout << "Despues de borrar rango de 3 elementos desde el inicio: ";
    imprimirConIterador(vec);

    // Repoblar para búsqueda
    vec = {5, 12, 25, 33, 50};
    cout << "\nVector actual: ";
    imprimirConIterador(vec);

    int valorBuscar = 25;
    auto it = find(vec.begin(), vec.end(), valorBuscar);

    if (it != vec.end()) {
        cout << "Elemento " << valorBuscar << " encontrado. Eliminando con iterador..." << endl;
        vec.erase(it);
    }

    cout << "Vector final con iteradores: ";
    imprimirConIterador(vec);

    return 0;
}