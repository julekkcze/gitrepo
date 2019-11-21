#!/usr/bin/en
# -*- coding: utf-8 -*-



def main(args):
    n = int(input("Podaj liczbę : "))
    m = int(input("Podaj drugą liczbę: "))
    
    suma = n + m 
    
    if suma < 76:
        print(suma)
    
    if suma > 76:
        print(suma)
        print("suma przekracza wartość 75")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
