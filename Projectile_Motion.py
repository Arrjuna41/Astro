import matplotlib.pyplot as mat
import pandas as pan
import numpy as Np

#Constants

g = 9.81 # m/s^2


def vx(V, theta):
    return V * Np.rad2deg(Np.cos(Np.deg2rad(theta)))

def vy(V, theta):
    return V * Np.sin(theta)

def T (V, Height, theta):
    t1 = 2 * V*Np.sin(theta) / g
    t2 = ( vy(V, theta) - Np.sqrt( (vy(V, theta )**2) + (2 * g * Height ) )) / -g
    return t1 + t2

def ProjMotPLot(V0 , theta , Height):
    figs = mat.figure()
    a,b = mat.subplots(1 , 2)
    
    arr_t = [0]
    arr_h = [Height]
    
    y = 0.05 # Time interevals 

    # Creating the arrays for a height vs time graph
    while (y <= T(V0, Height, theta)):
        arr_h.append(Height + (vy(V0, theta)*y) - (0.5 * g * y**2))
        arr_t.append(y)
        y += 0.05
    
    
    arr_h.append(0)
    arr_t.append(T(V0, Height, theta))
    #return (arr_t)

    b[0].set_title('Height vs Time')
    b[0].set_xlabel('Time')
    b[0].set_ylabel('Height')

    b[1].set_title('Part 2')
    
    return b[0].plot(arr_t, arr_h) , b[1].plot(Np.linspace(0, vx(V0, theta) * y, len(arr_h)), arr_h)

    
(ProjMotPLot(5, 15, 1))
mat.show()

