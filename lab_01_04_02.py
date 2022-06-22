#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_01_04_02.py
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

from math import pi,pow,sqrt

def main(args):
    #krok 1
    L = float(input("Wprowadź L[mm]: "))
    D = float(input("Wprowadź D[mm]: "))
    h = float(input("Wprowadź h[mm]: "))
    n = float(input("Wprowadź n[obr/min]: "))
    my = float(input("Wprowadź my[Pa*s]: "))
    epsilon = float(input("Wprowadź epsilon: "))
    
    #krok 1.2
    L/=1000
    D/=1000
    R=D/2
    h/=1000
    n/=60
    omega=2*pi*n 
    
    #krok 2
    F = 12*pi*my*pow(R,3)*L*omega*epsilon/(pow(h,2)*(2+pow(epsilon,2))*sqrt(1-pow(epsilon,2)))
    M = 2*pi*my*pow(R,3)*L*omega/h
    P = M*omega
    
    #krok 3
    print("\nWyniki: F=%s[N], M=%s[Nm], P=%s[W]." % (F,M,P))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
