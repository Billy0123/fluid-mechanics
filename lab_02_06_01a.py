#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_02_06_01.py
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

from math import pi

def twSteinera(Ic,d,A):
    return Ic+A*d**2
    
def twSteineraXY(Ic,xc,yc,A):
    return Ic+A*xc*yc

def main(args):
    przyklad=""
    while przyklad!="a" and przyklad!="b" and przyklad!="c" and przyklad!="d":
        przyklad = input("Wybierz przykład (a-d): ")
        if przyklad!="a" and przyklad!="b" and przyklad!="c" and przyklad!="d":
            print("Wartość %s jest błędna.\n" % przyklad)
    
    R=1
    H=2
    g=9.81
    
    if przyklad=="a":
        A=pi*R**2/2
        xc=H+4*R/3/pi
        yc=0
        Ix=pi*R**4/8
        Icy=pi*R**4/8-A*(4*R/3/pi)**2
        Iy=twSteinera(Icy,xc,A)
        Ixy=0 #moment odśrodkowy jest równy zeru, jeśli przynajmniej jedna oś jest osią symetrii tego przekroju
    elif przyklad=="b":
        A=pi*(2*R)**2-pi*R**2
        xc=H
        yc=0
        Ix=pi*(2*R)**4/4-pi*R**4/4
        Iy=twSteinera(pi*(2*R)**4/4-pi*R**4/4,xc,A)
        Ixy=0 #moment odśrodkowy jest równy zeru, jeśli przynajmniej jedna oś jest osią symetrii tego przekroju
    elif przyklad=="c":
        A=2*R*4*R+2*R*2*R+2*R*R/2
        xc=(((H+2*R)*2*R*4*R+(H+R)*2*R*2*R+(H+2*R/3)*2*R*R/2)/A)
        yc=(((-R)*2*R*4*R+(R)*2*R*2*R+(2*R+R/3)*2*R*R/2)/A)
        Ix1=4*R*(2*R)**3/3
        Ix2=2*R*(2*R)**3/3
        Ix3c=2*R*R**3/12-2*R*R/2*(R/3)**2
        Ix3=twSteinera(Ix3c,2*R+R/3,2*R*R/2)
        Ix=Ix1+Ix2+Ix3
        Iy1c=2*R*(4*R)**3/3-4*R*2*R*(2*R)**2
        Iy1=twSteinera(Iy1c,2*R+H,2*R*4*R)
        Iy2c=2*R*(2*R)**3/3-2*R*2*R*(R)**2
        Iy2=twSteinera(Iy2c,R+H,2*R*2*R)
        Iy3c=R*(2*R)**3/12-2*R*R/2*(2*R/3)**2
        Iy3=twSteinera(Iy3c,H+2*R/3,2*R*R/2)
        Iy=Iy1+Iy2+Iy3
        Ixy1=twSteineraXY(0,-(H+2*R),R,4*R*2*R) #moment odśrodkowy jest równy zeru, jeśli przynajmniej jedna oś jest osią symetrii tego przekroju
        Ixy2=twSteineraXY(0,-(H+R),-R,2*R*2*R)
        Ixy3c=(2*R)**2*R**2/24-2*R*R/2*(-2/3*R)*(-R/3)
        Ixy3=twSteineraXY(Ixy3c,-(H+2/3*R),-(2*R+R/3),2*R*R/2)
        Ixy=Ixy1+Ixy2+Ixy3
    elif przyklad=="d":
        A=3*R*2*R+pi*R**2
        xc=H+R
        yc=0
        Ix1=2*R*(3/2*R)**3/3
        Ix2c=pi*R**4/8-pi*R**2/2*(4*R/3/pi)**2
        Ix2=twSteinera(Ix2c,3/2*R+4*R/3/pi,pi*R**2/2)
        Ix=2*(Ix1+Ix2)
        Iy1c=3/2*R*(2*R)**3/3-3/2*R*2*R*(R)**2
        Iy1=twSteinera(Iy1c,H+R,3/2*R*2*R)
        Iy2=twSteinera(pi*R**4/8,H+R,pi*R**2/2)
        Iy=2*(Iy1+Iy2)
        Ixy=0 #moment odśrodkowy jest równy zeru, jeśli przynajmniej jedna oś jest osią symetrii tego przekroju
        
    F=g*1000*xc*A
    xs=Iy/xc/A
    ys=Ixy/xc/A
    
    print("Siła naporu: F=%s[N], współrzędne środka naporu: S=(%s,%s)[m]" % (F,xs,ys))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
