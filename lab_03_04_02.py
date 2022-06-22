#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_03_04_02.py
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
from math import pi

def main(args):
    L=float(input("Wprowadź długość rury L[m]: "))
    D=float(input("Wprowadź średnicę rury D[mm]: "))
    D/=1000
    e=float(input("Wprowadź chropowatość ścianki e[mm]: "))
    e/=1000
    rho=float(input("Wprowadź gęstość medium rho[kg/m^3]: "))
    my=float(input("Wprowadź lepkość medium my[Pa*s]: "))
    vOrQ=input("Znasz prędkość medium v[m/s], czy wydatek objętościowy przepływu Q[m^3/s]? (v/Q): ")
    if vOrQ=="v":
        v=float(input("Wprowadź prędkość medium v[m/s]: "))
    else:
        Q=float(input("Wprowadź wydatek objętościowy przepływu Q[m^3/s]: "))
        v=4*Q/pi/D**2
    
    Re=v*D*rho/my
    print("Liczba Reynoldsa: Re=%s" % Re)
    if Re<2300:
        print("(przepływ laminarny)")
        f=64/Re
    elif Re<4000:
        print("(przepływ przejściowy)")
        f=(2.82e-7)*Re**1.5
    else:
        print("(przepływ turbulentny)")
        f=getWspF(Re,e/D,-1,-1)
    
    Dp=0.5*f*L/D*rho*v**2
    hf=Dp/rho/9.81
    print("Różnica ciśnień wynosi: Dp=%s[Pa], wysokość strat tarcia: hf=%s[m]." % (Dp,hf))    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
