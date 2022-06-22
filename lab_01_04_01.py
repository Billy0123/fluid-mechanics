#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_01_04_01.py
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

from math import pi,pow

def main(args):
    #krok 1
    typLepkosciomierza=0
    while typLepkosciomierza<=0 or typLepkosciomierza>3:
        typLepkosciomierza = int(input("Wybierz typ lepkościomierza (liczba od 1 do 3): "))
        if typLepkosciomierza<=0 or typLepkosciomierza>3:
            print("Wartość %s jest błędna.\n" % typLepkosciomierza)

    #krok 2
    print()
    if typLepkosciomierza==1:
        L = float(input("Wprowadź L[m]: "))
        d = float(input("Wprowadź d[mm]: "))
        Dp = float(input("Wprowadź Dp[Pa]: "))
        Q = float(input("Wprowadź Q[m^3/s]: "))
    elif typLepkosciomierza==2:
        d = float(input("Wprowadź d[mm]: "))
        rho_k = float(input("Wprowadź rho_k[kg/m^3]: "))
        rho_p = float(input("Wprowadź rho_p[kg/m^3]: "))
        t = float(input("Wprowadź t[s]: "))
        L = float(input("Wprowadź L[m]: "))
    elif typLepkosciomierza==3:
        R = float(input("Wprowadź R[mm]: "))
        M = float(input("Wprowadź M[Nm]: "))
        h = float(input("Wprowadź h[(mikro)m]: "))
        omega = float(input("Wprowadź omega[1/s]: "))
        L = float(input("Wprowadź L[m]: "))
    
    #krok 3
    if typLepkosciomierza==1:
        d/=1000
    elif typLepkosciomierza==2:
        d/=1000
    elif typLepkosciomierza==3:
        R/=1000
        h/=1000000
    
    #krok 4
    print()
    if typLepkosciomierza==1:
        my = pi*Dp*pow(d,4)/(128*L*Q)
    elif typLepkosciomierza==2:
        g=9.80665
        my = pow(d,2)*g*(rho_k-rho_p)*t/(18*L)
    elif typLepkosciomierza==3:
        my = M*h/(2*pi*pow(R,3)*L*omega)
        
    #krok 5
    print("Obliczona wartość współczynnika lepkości: my=%s[Pa*s]." % my)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
