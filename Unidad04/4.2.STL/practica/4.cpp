#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

// Función auxiliar para limpiar signos de puntuación y pasar a minúsculas
string limpiarPalabra(const string& palabra) {
    string limpia = "";
    for (char c : palabra) {
        // Conservar caracteres alfanuméricos y letras con tilde / caracteres especiales
        if (isalnum(static_cast<unsigned char>(c)) || (c >= (char)128 && c <= (char)255)) {
            limpia += tolower(static_cast<unsigned char>(c));
        }
    }
    return limpia;
}

int main() {
    string frase = "Existen dos tipos de lenguajes de programacion: por un lado, aquellos de los que la gente se queja todo el rato; por otro, los que nadie utiliza. Bjarne Stroustrup";

    unordered_map<string, int> conteoPalabras;
    stringstream ss(frase);
    string palabra;

    // Leer cada palabra separada por espacios
    while (ss >> palabra) {
        string palabraLimpia = limpiarPalabra(palabra);
        if (!palabraLimpia.empty()) {
            conteoPalabras[palabraLimpia]++;
        }
    }

    // Imprimir las frecuencias almacenadas en el unordered_map
    cout << "--- Frecuencia de repeticion de palabras ---" << endl;
    for (const auto& par : conteoPalabras) {
        cout << "\"" << par.first << "\": " << par.second << " vez/veces" << endl;
    }

    return 0;
}