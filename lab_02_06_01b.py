#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_02_06_01b.py
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

from math import pi,sin

class kolo:
    def __init__(self, sign, x, y, R): #wsp. środka okręgu i jego promień
        A = pi*R**2*sign
        self.Sy = x*A
        self.Iy = sign*pi*R**4/4 + A*x**2
        self.Ixy = 0 + A*x*y
        
class polkole:
    def __init__(self, sign, x, y, R, orientacja): #wsp. środka okręgu (którego jest połowa) i jego promień oraz orientacja         
        if orientacja==0:
            xc=x
            yc=y+4*R/3/pi
        elif orientacja==90:
            yc=y
            xc=x-4*R/3/pi
        elif orientacja==180:
            xc=x
            yc=y-4*R/3/pi
        else:
            yc=y
            xc=x+4*R/3/pi
        A = pi*R**2/2*sign
        self.Sy = xc*A
        self.Iy = sign*pi*R**4/8-A*(x-xc)**2+A*xc**2
        self.Ixy = 0 + A*xc*yc
        
class wielokat:
    def __init__(self, sign, coords):         
        self.Sy=0
        self.Iy=0
        self.Ixy=0
        for i in range(len(coords)-1): #lepiej stworzyć lokalnie xi, xi1, yi, yi1
            self.Sy+=(coords[i][1]-coords[i+1][1])*(coords[i][0]**2+coords[i][0]*coords[i+1][0]+coords[i+1][0]**2)
            self.Iy+=(coords[i][1]-coords[i+1][1])*(coords[i][0]**3+coords[i][0]**2*coords[i+1][0]+coords[i][0]*coords[i+1][0]**2+coords[i+1][0]**3)
            self.Ixy+=(coords[i+1][0]-coords[i][0])*(coords[i][0]*(3*coords[i][1]**2+2*coords[i][1]*coords[i+1][1]+coords[i+1][1]**2)+coords[i+1][0]*(3*coords[i+1][1]**2+2*coords[i][1]*coords[i+1][1]+coords[i][1]**2))
        self.Sy+=(coords[len(coords)-1][1]-coords[0][1])*(coords[len(coords)-1][0]**2+coords[len(coords)-1][0]*coords[0][0]+coords[0][0]**2)
        self.Iy+=(coords[len(coords)-1][1]-coords[0][1])*(coords[len(coords)-1][0]**3+coords[len(coords)-1][0]**2*coords[0][0]+coords[len(coords)-1][0]*coords[0][0]**2+coords[0][0]**3)
        self.Ixy+=(coords[0][0]-coords[len(coords)-1][0])*(coords[len(coords)-1][0]*(3*coords[len(coords)-1][1]**2+2*coords[len(coords)-1][1]*coords[0][1]+coords[0][1]**2)+coords[0][0]*(3*coords[0][1]**2+2*coords[len(coords)-1][1]*coords[0][1]+coords[len(coords)-1][1]**2))
        self.Sy/=6*sign
        self.Iy/=12*sign
        self.Ixy/=24*sign
        
        

def main(args):
    rho = float(input("Wprowadź gęstość cieczy rho[kg/m^3]: "))
    gamma=9.81*rho
    
    phi = float(input("Wprowadź kąt nachylenia ściany z klapą phi[deg]: "))
    phiRad=phi*pi/180
    
    figures = ()
    odp="t"
    while odp=="t":
        typFigury=input("Wprowadź nazwę figury (obsługiwane: kolo, polkole, wielokat): ")
        if typFigury=="kolo":
            sign=int(input("Figura jest dodatnia czy ujemna? (1/-1): "))
            x=float(input("Wprowadź wsp. x[m] środka: "))
            y=float(input("Wprowadź wsp. y[m] środka: "))
            R=float(input("Wprowadź promień R[m]: "))
            figure=kolo(sign,x,y,R)
        elif typFigury=="polkole":
            sign=int(input("Figura jest dodatnia czy ujemna? (1/-1): "))
            x=float(input("Wprowadź wsp. x[m] środka (koła, którego to połowa): "))
            y=float(input("Wprowadź wsp. y[m] środka (koła, którego to połowa): "))
            R=float(input("Wprowadź promień R[m]: "))
            orientacja=int(input("Wprowadź orientację półokręgu (obsługiwane: 0, 90, 180, 270): "))
            figure=polkole(sign,x,y,R,orientacja)
        elif typFigury=="wielokat":
            sign=int(input("Figura jest dodatnia czy ujemna? (1/-1): "))
            odpW="t"
            coords=[]
            while odpW=="t":
                print("Wierzchołek: %s" % (len(coords)+1))
                x=float(input("Wprowadź wsp. x[m] (zgodnie z ruchem wskazówek zegara): "))
                y=float(input("Wprowadź wsp. y[m] (zgodnie z ruchem wskazówek zegara): "))
                coords.append([x,y])
                if len(coords)>=3:
                    odpW=input("Czy wielokąt posiada kolejny wierzchołek? (t/n) ")
            figure=wielokat(sign,coords)
        figures+=(figure,) #appendowanie do 'tupli' (ona nie ma funkcji append, jak zwykła [tj. single-type] lista)
        odp=input("Dodać kolejną figurę? (t/n) ")
    
    Sy=0
    Iy=0
    Ixy=0
    for figure in figures:
        Sy+=figure.Sy
        Iy+=figure.Iy
        Ixy+=figure.Ixy

    F=gamma*sin(phiRad)*Sy
    xs=Iy/Sy
    ys=Ixy/Sy
    
    print("\nSiła naporu: F=%s[N], współrzędne środka naporu: S=(%s,%s)[m]" % (F,xs,ys))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
