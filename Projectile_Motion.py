import matplotlib.pyplot as mat
import pandas as pan
import numpy as Np

#Constants

g = 9.81 # m/s^2


def vx(V, theta):
    return V * Np.rad2deg(Np.cos(Np.deg2rad(theta)))

def vy(V, theta):
    return V * Np.rad2deg(Np.sin(Np.deg2rad(theta)))

def T (V, Height, theta):
    t1 = 2 * V / g
    t2 = ( vy(V, theta) - Np.sqrt( (vy(V, theta ) ** 2) + (2 * g * Height ) )) / -g
    return t1 + t2

def ProjMotPLot(V0 , theta , Height):
    figs = mat.figure()
    a,b = figs.subplots(1 , 2)
    
    arr_t = [0]
    arr_h = [Height]
    
    y = 0.25 # Time interevals 

    # Creating the arrays for a height vs time graph
    while (y <= T(V0, Height, theta)):
        arr_h.append(Height + (vy(V0, theta)*y) - (0.5 * g * y**2))
        arr_t.append(y)
        y += 0.25
    
    if (y != T(V0, Height, theta)):
        arr_h.append(0)
        arr_t.append(T(V0, Height, theta))
    
    return b[0].plot(arr_t, arr_h) , b[1].plot(Np.linspace(0, vx(V0, theta) * y, len(arr_h)), arr_h)

    
ProjMotPLot(5, 15, 50)
mat.show()