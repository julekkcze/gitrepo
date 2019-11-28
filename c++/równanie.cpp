/*
 * równanie.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    cout << "Witaj w C++";
	int a;
    int b;
    float x;
    cout << "Podaj liczbę a: ";
    cin >> a;
    cout << "Podaj liczbę b: ";
    cin >> b;
    if (a == 0) {
        if (b == 0) {
            cout << "Nieskończenie wiele";
        } else {
            cout<< "Równanie sprzecznee";
        }
    } else {
        x = -b / (float)a;
        cout << x;
    }
    return 0;
}

