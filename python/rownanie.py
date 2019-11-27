#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    if a == 0 and b == 0:
        print("Nieskończenie wiele rzowiązań.")
        if b != 0:
            print("Równanie sprzeczne.")
    
    else:
        x = -b / a
        print(x)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
