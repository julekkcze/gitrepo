/*
 * wieksza.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)


{   int a, b;
    cout << "Podaj liczbę: ";
    cin >> a;
    cout << "Podaj liczbę: ";
	cin >> b;
    
    if (a > b){
        cout << a;
    }
    else if (a < b){
        cout << b;
    }
    else{
        cout << "Podane liczby są równe.";
    }
    
	return 0;
}

