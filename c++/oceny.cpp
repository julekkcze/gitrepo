/*
 * oceny.cpp
 */


#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
    
    float ocena, ilosc_ocen, suma, srednia;
    suma = 0;
    cout << "Podaj liczbę ocen:";
    cin >> ilosc_ocen;
    while (ilosc_ocen < 1) {
        cout << "Podaj liczbę ocen:";
        cin >> ilosc_ocen;
   
    }
    for(int i = 0; i < ilosc_ocen; i = i + 1) {
        cout << "Podaj ocenę:";
        cin >> ocena;
        while (ocena < 1 or ocena > 6) {
            cout << "Podaj poprawną ocenę:";
            cin >> ocena;
        }
        
        suma = suma + ocena;
   
    }
    srednia = suma / ilosc_ocen;
    cout << "Średnia:";
    cout << srednia;
    
    return 0;
}
