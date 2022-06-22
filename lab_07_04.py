#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_07_04.py
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

from math import sqrt,fabs,pi,tan,cos,sin

def F(Y,typKanalu,args):
    if typKanalu==1:
        return Y**(5/3)/(2*Y+args[3])**(2/3)-args[0]*args[1]/args[3]**(5/3)/sqrt(args[2])
    elif typKanalu==3:
        return (Y-sin(Y))**(5/3)/Y**(2/3)-2**(5/3)*args[0]*args[1]/args[3]**(8/3)/sqrt(args[2])
    else:
        return ((args[4]+Y*tan(args[3]))*Y)**(5/3)/(args[4]+2*Y*sqrt(1+tan(args[3])**2))**(2/3)-args[0]*args[1]/sqrt(args[2])
       
def dFdY(Y,typKanalu,args):
    if typKanalu==1:
        return (5/3*Y**(2/3)*(args[3]+2*Y)**(2/3)-4/3*Y**(5/3)*(args[3]+2*Y)**(-1/3))/(2*Y+args[3])**(4/3)
    elif typKanalu==3:
        return -1/3*(Y-sin(Y))**(2/3)*(5*Y*cos(Y)-3*Y-2*sin(Y))/Y**(5/3)
    else:
        return 1/3*((args[4]+Y*tan(args[3]))*Y)**(2/3)*(10*Y*tan(args[3])*args[4]+16*Y**2*tan(args[3])*sqrt(1+tan(args[3])**2)+5*args[4]**2+6*args[4]*Y*sqrt(1+tan(args[3])**2))/(args[4]+2*Y*sqrt(1+tan(args[3])**2))**(5/3)

def main(args):
    s=float(input("Wprowadź nachylenie s (tg(alpha)): "))
    n=float(input("Wprowadź współczynnik Manninga n[s/m^(1/3)]: "))
    Q=float(input("Wprowadź obj. nat. przepływu Q[m^3/s]: "))
    
    typKanalu=0
    while typKanalu<1 or typKanalu>4:
        typKanalu=int(input("Wprowadź typ kanału (1-prostokątny, 2-trójkątny, 3-cylindryczny, 4-trapezowy): "))
        
    if typKanalu==1:
        B=float(input("Wprowadź szerokość kanału B[m]: "))
        args2=[n,Q,s,B]
    elif typKanalu==2:
        gamma=float(input("Wprowadź kąt rozwarcia kanału gamma[deg.]: "))
        gamma*=pi/180/2 #wzory ze skryptu są dla połowy kąta rozwiarcia (jest błąd, ale w dodatku B są poprawne wzory, oparte na gamma/2 oraz pojawia się Z^5/8 w mianowniku pierwszego wyrazu, zamiast 3/8)
    elif typKanalu==3:
        R=float(input("Wprowadź promień kanału cylindrycznego R[cm]: "))
        R/=100
        args2=[n,Q,s,R]
    else:
        beta=float(input("Wprowadź kąt odchylenia ściany bocznej od pionu beta[deg.]: "))
        beta*=pi/180
        B=float(input("Wprowadź szerokość dna B[m]: "))
        args2=[n,Q,s,beta,B]
    
    licznik=0
    if typKanalu!=2:
        Y=1
        TOL=1e-7
        compute=True
        while compute:
            licznik+=1
            YPrev=Y
            Y=Y-F(Y,typKanalu,args2)/dFdY(Y,typKanalu,args2)
            if fabs(Y-YPrev)<=TOL:
                compute=False
        if typKanalu==3:
            Y=R-R*cos(Y/2)
    else: #
        Y=(n*Q)**(3/8)/tan(gamma)**(5/8)*(2*sqrt(tan(gamma)**2+1))**(1/4)/s**(3/16)
    print("(obliczono Y=%s[m] po %s iteracjach)" % (Y,licznik))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
