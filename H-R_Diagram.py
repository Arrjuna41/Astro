import numpy as Np
import pandas as pan
import matplotlib.pyplot as mat

#Range of Temperatures: 2,500 Kelvin - 50,000 Kelvin
#Range of Luminosity: 10^-4 solar units - 10^6 solar units

rand_temp = Np.random.rand(2,500, 50001)
rand_lum = Np.random.rand(10 ** -4, 10 ** 6)

σ = 5.67 * 10 ** -8 # W/m^2/K^4, Approximation of Stefan - Boltzmann Constant

lum_list = Np.arange(40, 40)

temp_list = None


def fill_array(rows, cols, small, large):
    r=0
    c=0
    arr = Np.empty((rows,cols))
    for r in range (rows):
        for c in range (cols):
            arr[r][c] = Np.random.uniform(small, large + 1)

    return (arr)    

    
           
        
        