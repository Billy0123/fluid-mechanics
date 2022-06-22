#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_05_03_04.py
#  
#  Copyright 2021 MBilly <MBilly@DESKTOP-TS5FEF9>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from lab_03_04_01 import getWspF
from math import pi,sqrt,fabs

def main(args):
    rho=1000
    my=0.001
    H1=33 #chyba błąd w skrypcie - dla H1=30 wynik błędny dwiema metodami (z r. Bernoulliego i r. Darcy'ego-Weisbacha) - POTWIERDZONE, w obliczeniach (LAB 3 ZAD 11 i 12 od RS) przy H=30 wynik jest inny i zgodny z obliczeniami tego programu
    H2=10
    L1=100
    L2=200
    D1=0.4
    D2=0.2
    e=1e-4
    
    #r. Bernoullego z postaci: v1^2/(2g)+p1/gamma+z1=v2^2/(2g)+p2/gamma+z2+Sum(hf)+Sum(hl) redukuje się do (v1=v2, p1=p2, hl=0): z1=z2+Sum(hf) 
    a=2*(H1-H2)
    b1=L1/D1/9.81
    b2=L2*D1**4/D2**5/9.81  
    f1=0.1
    f2=0.1
    v1=sqrt(a/(f1*b1+f2*b2))
    v2=v1*D1**2/D2**2 #v1*A1=v2*A2
    
    TOL=1e-7
    licznik=0
    compute=True
    while compute:
        f1=getWspF(v1*D1*rho/my,e/D1,TOL,f1)
        f2=getWspF(v2*D2*rho/my,e/D2,TOL,f2)
        v1Prev=v1
        v2Prev=v2
        v1=sqrt(a/(f1*b1+f2*b2))
        v2=v1*D1**2/D2**2
        if fabs(v1-v1Prev)<=TOL and fabs(v2-v2Prev)<=TOL:
            compute=False
        licznik+=1
    print("(obliczono v1=%s i v2=%s po %s iteracjach)" % (v1,v2,licznik))
        
    Q=v1*pi*D1**2/4
    print("Prędkość średnia medium: v1=%s[m/s], v2=%s[m/s], wydatek objętościowy przepływu: Q=%s[m^3/s]." %(v1,v2,Q))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
