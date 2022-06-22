#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_05_04_02.py
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
from math import pi,sqrt,fabs,sin

def main(args):
    L=float(input("Wprowadź długość rury L[m]: "))
    D=float(input("Wprowadź średnicę rury D[mm]: "))
    D/=1000
    e=float(input("Wprowadź chropowatość ścianki e[mm]: "))
    e/=1000
    rho=float(input("Wprowadź gęstość medium rho[kg/m^3]: "))
    my=float(input("Wprowadź lepkość medium my[Pa*s]: "))
    H=float(input("Wprowadź odległość powierzchni swobodnej cieczy od środka wylotu H[m]: "))
    alpha=float(input("Wprowadź kąt nachylenia prostoliniowego odcinka rury wylotowej alpha[deg]: "))
    alpha*=pi/180
    
    a=2*9.81*(H+L*sin(alpha))
    b=L/D
    
    f=0.01
    v=sqrt(a/(1+f*b))
    TOL=1e-7
    licznik=0
    compute=True
    while compute:
        f=getWspF(v*D*rho/my,e/D,TOL,f)
        vPrev=v
        v=sqrt(a/(1+f*b))
        if fabs(v-vPrev)<=TOL:
            compute=False
        licznik+=1
    print("(obliczono v=%s po %s iteracjach)" % (v,licznik))
        
    Q=v*pi*D**2/4
    print("Prędkość średnia medium: v=%s[m/s], wydatek objętościowy przepływu: Q=%s[m^3/s]." %(v,Q))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
