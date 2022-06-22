#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_06_03_02.py
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

from math import sqrt,fabs,pi

def C_D(Re):
    return 1+10/Re**0.67

def main(args):    
    g=9.81
    R=8.31446261815324 #[J/(mol*K)], w skrypcie podają R "dla powietrza", czyli R/M_powietrza=8.3144.../0.029=ok. 287 [J/(mol*K) / kg/mol = J/(kg*K)]
    M=0.029 #masa molowa powietrza: 29 [g/mol]
    
    H=float(input("Wprowadź H[m]: "))
    D=float(input("Wprowadź D[cm]: "))
    D/=100
    G=float(input("Wprowadź G[cm]: "))
    G/=100
    Jy=pi/64*(D**4-(D-2*G)**4)
    W=Jy/(D/2) #wskaźnik wytrzymałości na zginanie dla wydrążonego walca, W=Jy/(D/2)   (Jy/y_max_sigma)
    T=float(input("Wprowadź T[C deg.]: "))
    T+=273
    p=float(input("Wprowadź p[mm Hg]: "))
    p*=g*13534*0.001 #1 mm Hg = g*rho_Hg*H = g*rho_Hg[kg/m^3]*0.001[m]
    rho=p*M/R/T #pV=nRT -> n/V=p/RT -> (m/M)/V=p/RT -> rho=m/V=pM/RT
    my=float(input("Wprowadź my[Pa*s]: "))
    sigma_dop=float(input("Wprowadź sigma_dop[MPa]: "))
    sigma_dop*=1000000
    M_g_max=sigma_dop*W
    alpha=4*M_g_max/rho/H**2/D
    
    v=1
    TOL=1e-7
    licznik=0
    compute=True
    while compute:
        vPrev=v
        Re=rho*v*D/my
        v=sqrt(alpha/C_D(Re))
        if fabs(v-vPrev)<=TOL:
            compute=False
        licznik+=1
    print("(obliczono v=%s[m/s] po %s iteracjach)" % (v,licznik))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
