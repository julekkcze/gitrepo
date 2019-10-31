#!/usr/bin/env python
# -*- coding: utf-8 -*-
#



def main(args):
    #a = 10
    a = input ("Podaj liczbę:")
    #b = 5
    b = input ("Podaj liczbę:")
    suma = a + b
    print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
