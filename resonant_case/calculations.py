#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0

if __name__ == "__main__":
    L1 = .5 # Henries
    L2 = .5

    # L_m is not super straightforward

    V0 = 10 # Volts
    R0 = 1 # ohm
    w = 1000 # in Hertz
    w = 10000 # in Hertz
    #w = 10 # in Hertz
    

    #Lm = .2  # 3819 wraps
    n = 3819
    d = .01
    l = .01524
    r = 0.0115
    Lm = (2 * np.pi**2 * r**4 * n**2) / ( (d+l)**2 + r**2)**(3/2) * (mu_0/(4*np.pi))
    print(Lm)

    I1 = []
    I2 = []
    COMPARE = []

    TIME_RANGE = 100
    TIME_SEGMENT = 10
    #TIME_SEGMENT = 100

    for j in range(0,TIME_RANGE):
        t = j/TIME_SEGMENT
        i1 = ((Lm/L1)*V0) / (R0**2 + (L2 + (Lm**2)/L1)**2 * w**2 ) * ( ( L2 + (Lm**2)/L1)*w*np.cos(w*t) + R0*np.sin(w*t))
        i2 = -V0 / (Lm * w ) * np.cos(w * t)
        #print(i)
        I1.append(i1/R0* 10)
        I2.append(i2/R0)
        COMPARE.append(i2/i1)

    plt.plot(range(0,TIME_RANGE), I1)
    plt.plot(range(0,TIME_RANGE), I2)
    #plt.plot(range(0,TIME_RANGE), COMPARE)
    #print(max(I))
    plt.show()
