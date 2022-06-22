#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_03_04_01.py
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

from math import sqrt,log10,fabs

def getWspF(Re, eDd, TOL, f0):
    if Re==-1:
        Re = float(input("Wprowadź liczbę Reynoldsa (Re, może być w formie np. 2e6): "))
    if eDd==-1:
        eDd = float(input("Wprowadź chropowatość względną (e/D): "))
    if TOL==-1:
        TOL = float(input("Wprowadź tolerancję obliczeń (TOL, może być w formie np. 1e-5): "))
    if f0==-1:
        f0 = float(input("Wprowadź wartość wejściową iteracji (f0): "))
    
    compute=True
    licznik=0
    fNext=f0
    while compute:
        fPrev=fNext
        fNext=1/(1.14-2*log10(eDd+9.35/Re/sqrt(fPrev)))**2
        if fabs(fNext-fPrev)<=TOL:
            compute=False
        licznik+=1
    print("(obliczono f=%s po %s iteracjach)" % (fNext,licznik))

    return fNext
    

def main(args):   
    print("Wartość współczynnika strat tarcia: f=%s" % getWspF(-1,-1,-1,-1))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
