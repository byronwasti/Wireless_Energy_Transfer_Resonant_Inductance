#!/usr/bin/python3
from scipy.constants import mu_0
import numpy as np


def resonant():
    C = 50 * 10**(-9)
    L = .5 # 500mH for inductors
    f_res = 1000 # 1kH

    f_res = 1/( 2* np.pi * np.sqrt(L * C) )

    C = 1/( (f_res * 2 * np.pi)**2 * L )

    print("C is {}".format(C))
    print("F_res is {}".format(f_res))

def non_resonant():
    Vs = 5
    L = .5 # 500mH
    f = 1000 # 1kH
    
    R = (f * 2 * np.pi)*L  # omega = 2pi*f

    # Coupling coefficient for inductors
    # assuming they are inductive balls
    d = .1
    r1 = .008
    r2 = r1

    k = 1 / ( 2 * (d / np.sqrt(r1*r2))**3)

    R_STUFF = ( R / L ) / ( R / L )


    # All the power calculations
    P_0 = Vs**2 / (4*R) * (k**2 / 2) * 1/ ( 1 + R_STUFF)

    print(P_0)

    P_i = Vs**2 / R
    print(P_i)

    print( P_0 / P_i )

if __name__ == "__main__":
    non_resonant()
