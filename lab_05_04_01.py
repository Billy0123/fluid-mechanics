#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lab_05_04_01.py
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
from math import pi,sqrt,fabs

'''
UWAGA: program nie nadaje się do używania do przypadków gdzie np. po lewej mamy zbiornik 'otwarty', 
w którym słup cieczy o wysokości H powoduje przepływ (jak w programie 05_04_02), ze względu na to,
że różnica ciśnień NIE jest po prostu równa dp=p_hydrostat=H*rho*g. Gdyby wypływ (poziomej rury) 
był zatkany, to na wysokości wlotu rzeczywiście panowałoby takie ciśnienie STATYCZNE (H*rho*g). Jednak,
w momencie otwarcia wylotu, ciecz zaczyna się ruszać. W RÓŻNICZKOWYM otoczeniu wlotu, mamy cząstki, które
prawie się nie ruszają (tam działa ciśnienie statyczne H*rho*g), jednak już obok, tj. 'w rurze' już się 
ruszają, z prędkością v_wlot=v_wylot. Zatem tam, część ciśnienia statatycznego (w myśl r. Bernoullego) 
zamienia się w ciśnienie DYNAMICZNE. W równaniu v^2/(2g)+p/gamma+z=const. ciśnienie DYNAMICZNE (v^2/(2g)*gamma)
rośnie kosztem ciśnienia STATYCZNEGO. H*rho*g jest SUMĄ obu tych ciśnień. W momencie otwarcia wlotu
nie jest tak, że nagle oprócz H*rho*g 'pojawia się znikąd' ciśnienie dynamiczne równe v^2/(2g)*gamma,
tylko pojawia się ono kosztem ciśnienia statycznego, tak by r. Bernoullego było spełnione.
Mamy zatem p_statyczne = H*rho*g-v^2/(2g)*gamma. Jako, że program te 'v' dopiero ma obliczyć
to nie możemy 'p_statycznego' (stanowiącego w tym wypadku Dp) podać na jego wejściu. Jeżeli zaś 
uwzględnimy to w równaniu i wyprowadzimy sobie (przy założeniu jeszcze v1*A1=v2*A2 itd.) nowe równanie,
to okaże się, że w wyniku uzyskamy po prostu równanie używane w programie 05_04_02.
'''

def main(args):
    L=float(input("Wprowadź długość rury L[m]: "))
    D=float(input("Wprowadź średnicę rury D[mm]: "))
    D/=1000
    e=float(input("Wprowadź chropowatość ścianki e[mm]: "))
    e/=1000
    rho=float(input("Wprowadź gęstość medium rho[kg/m^3]: "))
    my=float(input("Wprowadź lepkość medium my[Pa*s]: "))
    Dp=float(input("Wprowadź różnicę ciśnień na końcach rury Dp[Pa]: "))
    
    v=Dp*D**2/32/my/L
    Re=v*D*rho/my
    if Re>=2300:
        c=2*Dp*D/rho/L
        f=64/Re #można skorzystać z przypadku laminarnego
        TOL=1e-7
        licznik=0
        compute=True
        while compute:
            f=getWspF(Re,e/D,TOL,f)
            vPrev=v
            v=sqrt(c/f)
            Re=v*D*rho/my
            if fabs(v-vPrev)<=TOL:
                compute=False
            licznik+=1
        print("(obliczono v=%s po %s iteracjach)" % (v,licznik))
        
    Q=v*pi*D**2/4
    print("Prędkość średnia medium: v=%s[m/s], wydatek objętościowy przepływu: Q=%s[m^3/s]." %(v,Q))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
