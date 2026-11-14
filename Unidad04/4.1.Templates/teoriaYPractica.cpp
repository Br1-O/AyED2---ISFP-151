#include <iostream>
#include <string>

using namespace std;

/* =========================================================================
   TEORIA
   =========================================================================
   - Plantillas de Funciones: Son funciones genéricas que permiten operar con 
     diferentes tipos de datos sin necesidad de reescribir la lógica para cada uno.
   - Plantillas de Clases: Permiten definir estructuras de clases parametrizadas 
     por tipos, facilitando la creación de contenedores y componentes reutilizables.
   - Especialización de Plantillas: Mecanismo que permite proveer una implementación 
     customizada y específica para un tipo de dato particular (por ejemplo, especializar 
     una clase genérica para el tipo 'char').
   ========================================================================= */


/* =========================================================================
   PRACTICA
   ========================================================================= */

// 1. Declarar una función que toma dos parámetros de plantilla distintos:
//    Uno es el tipo de retorno (T) y el otro es el argumento de entrada (U).
template <typename T, typename U>
T convertirYProcesar(U argumento) {
    return static_cast<T>(argumento);
}

// 2. Declarar una clase que toma un parámetro de plantilla, el cual es 
//    una variable miembro (atributo) de la misma.
template <typename T>
class ClaseConAtributoGenerico {
private:
    T atributoMiembro;
public:
    ClaseConAtributoGenerico(T val) : atributoMiembro(val) {}
    
    T getAtributo() const {
        return atributoMiembro;
    }
    
    void setAtributo(T val) {
        atributoMiembro = val;
    }
};

// 3. Declarar una clase que toma dos parámetros de plantilla:
//    Uno como argumento al constructor (T) y otro como tipo de retorno 
//    de una función miembro (método) sin argumentos (R).
template <typename T, typename R>
class ClaseDobleParametro {
private:
    T valorInicial;
public:
    ClaseDobleParametro(T val) : valorInicial(val) {}
    
    R obtenerResultadoConvertido() {
        return static_cast<R>(valorInicial);
    }
};


/* =========================================================================
   PRACTICA - FUNCIÓN MENOR Y COMPROBACIONES
   ========================================================================= */

// Versión A: Con un solo parámetro de plantilla (T)
template <typename T>
T menorUnParam(T a, T b) {
    return (a < b) ? a : b;
}

// Versión B: Con dos parámetros de plantilla (T y U) para manejar distintos tipos
template <typename T, typename U>
auto menorDosParam(T a, U b) {
    return (a < b) ? a : b;
}


/* =========================================================================
   MAIN
   ========================================================================= */
int main() {
    cout << "=== COMPROBACION PRACTICA - UNIDAD 4.1: PLANTILLAS ===" << endl << endl;

    // --- Comprobación de los ejercicios de declaración ---
    cout << "1. Funcion con tipo de retorno y argumento distintos:" << endl;
    double resultadoConv = convertirYProcesar<double, int>(25);
    cout << "   Convertir int 25 a double -> Resultado: " << resultadoConv << endl << endl;

    cout << "2. Clase con atributo parametrizado:" << endl;
    ClaseConAtributoGenerico<string> objetoStr("Hola desde ISFT N° 151");
    cout << "   Atributo almacenado: " << objetoStr.getAtributo() << endl << endl;

    cout << "3. Clase con dos parametros (constructor T, metodo R):" << endl;
    ClaseDobleParametro<int, double> procesador(150);
    cout << "   Constructor recibe int (150), metodo retorna double -> Resultado: " 
         << procesador.obtenerResultadoConvertido() << endl << endl;

    cout << "--- PRUEBAS DE LA FUNCION MENOR ---" << endl;

    // 1. Parejas de argumentos numéricos del mismo tipo (int, double, float)
    cout << "menor(2, 3) [int] == " << menorUnParam(2, 3) << endl;
    cout << "menor(6.0, 4.0) [double] == " << menorUnParam(6.0, 4.0) << endl;
    cout << "menor(5.5f, 2.1f) [float] == " << menorUnParam(5.5f, 2.1f) << endl << endl;

    // 2. Comprobación con argumentos de distinto tipo:
    cout << "--- Comprobacion con distintos tipos ---" << endl;
    
    // Con la versión de 1 parámetro (menorUnParam), si se mezclan tipos sin especificar 
    // explícitamente el template, el compilador genera un error de deducción. 
    // Para solucionarlo con 1 parámetro, se debe forzar el tipo:
    cout << "menorUnParam<double>(2, 4.5) [Forzando T=double] == " << menorUnParam<double>(2, 4.5) << endl;

    // Con la versión de 2 parámetros (menorDosParam), el compilador deduce automáticamente 
    // ambos tipos y resuelve la comparación y el tipo de retorno de forma segura (usando auto):
    cout << "menorDosParam(2, 4.5) [int y double] == " << menorDosParam(2, 4.5) << endl;
    cout << "menorDosParam(6.5, 3) [double e int] == " << menorDosParam(6.5, 3) << endl;

    return 0;
}