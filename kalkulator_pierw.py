#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    print("WITAJ W KALKULATORZE PIERWIASTKÓW")
    print("")
    
    liczba_pierw = int(input ("Podaj liczbę pierwiastkowaną: "))
    print("")
    stop_pierw = int(input ("Podaj stopień pierwiastka: "))
    print("")
    pierw = liczba_pierw ** (1 / stop_pierw)
    print("")
    print(pierw)
    
    if liczba_pierw == 0
        print("Nie można obliczyć pierwiastka z takiej liczby")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
