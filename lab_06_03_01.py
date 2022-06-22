#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_06_03_01.py
#  
#  Copyright 2021 MBilly <MBilly@DESKTOP-PSHUP1C>
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

from math import sqrt,fabs

def C_D(Re):
    return 24/Re+6/(1+sqrt(Re))+0.4

def main(args):
    rho_k=float(input("Wprowadź rho_k[kg/m^3]: "))
    rho_p=float(input("Wprowadź rho_p[kg/m^3]: "))
    D=float(input("Wprowadź D[mm]: "))
    D/=1000
    my=float(input("Wprowadź my[Pa*s]: "))
    g=9.81
    alpha=4*D*g*(rho_k-rho_p)/3/rho_p
    
    v=1
    TOL=1e-7
    licznik=0
    compute=True
    while compute:
        vPrev=v
        Re=rho_p*v*D/my
        v=sqrt(alpha/C_D(Re))
        if fabs(v-vPrev)<=TOL:
            compute=False
        licznik+=1
    print("(obliczono v=%s[m/s] po %s iteracjach)" % (v,licznik))
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
