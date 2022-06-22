#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_05_03_06.py
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

from math import sqrt

def main(args):
    L=100 #jest błąd w skrypcie, dla L=1000 wychodzi inny wynik, ale dla L=100 idealnie taki sam
    D=0.25
    rho=1000
    my=0.001
    Dp=(200-100)*rho*9.81
    f=0.02
    v=sqrt(2*Dp*D/rho/L/f)
    Re=v*D*rho/my
    print(Re)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
