#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    n = int(input("Podaj liczbę naturalną: "))
    m = int(input("Podaj drugą liczbę, większą od poprzedniej: "))
    c = list(range(n, m+1))
    
    if n < 0 or m < 0:
        print("Podane liczby nie są naturalne.")
        
    if n == 0 or n > 0 or m == 0 or m > 0:
        for i in range(n , m+1):
            print(i, " ", end = "")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
