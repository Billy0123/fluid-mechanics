#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_05_03_04b.py
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
    
    Dp=(H1-H2)*rho*9.81
    '''poniżej, rozwiązania uk. równań (Mathematica): 
            FullSimplify[Solve[{
                v1 == Sqrt[2*\[CapitalDelta]p1*D1/\[Rho]/L1/f1],
                v2 == Sqrt[2*\[CapitalDelta]p2*D2/\[Rho]/L2/f2],
                \[CapitalDelta]p == \[CapitalDelta]p1 + \[CapitalDelta]p2,
                v2*A2 == v1*A1 /. {A1 -> Pi*D1^2/4, A2 -> Pi*D2^2/4}}, 
            {v1, v2, \[CapitalDelta]p1, \[CapitalDelta]p2}]]'''
    f1=0.01
    f2=0.01
    v1=sqrt(2*D1*D2**5*Dp/(D2**5*f1*L1*rho+D1**5*f2*L2*rho))
    v2=sqrt(2*D1**5*D2*Dp/(D2**5*f1*L1*rho+D1**5*f2*L2*rho))
    
    TOL=1e-7
    licznik=0
    compute=True
    while compute:
        f1=getWspF(v1*D1*rho/my,e/D1,TOL,f1)
        f2=getWspF(v2*D2*rho/my,e/D2,TOL,f2)
        v1Prev=v1
        v2Prev=v2
        v1=sqrt(2*D1*D2**5*Dp/(D2**5*f1*L1*rho+D1**5*f2*L2*rho))
        v2=sqrt(2*D1**5*D2*Dp/(D2**5*f1*L1*rho+D1**5*f2*L2*rho))
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
