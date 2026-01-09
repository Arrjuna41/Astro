import numpy as Np
import pandas as pan
import matplotlib.pyplot as mat

#Range of Temperatures: 2,500 Kelvin - 50,000 Kelvin
#Range of Luminosity: 10^-4 solar units - 10^6 solar units

solar_radius = 6.957 * 10**8 # meters
solar_kelvin = 5778 # Kelvin
solar_lum = 3.828 * 10**26 # watts

rand_temp = Np.random.rand(2500, 50001)
rand_lum = Np.random.rand(10 ** -4, 10 ** 6)
rand_radius = Np.random.rand(0.01 * solar_kelvin, 3000 * solar_kelvin)



σ = 5.67 * 10 ** -8 # W/m^2/K^4, Approximation of Stefan - Boltzmann Constant



def fill_array(rows, cols, small, large):
    r=0
    c=0
    arr = Np.empty((rows,cols))
    for r in range (rows):
        for c in range (cols):
            arr[r][c] = Np.random.uniform(small, large + 1)

    return (arr)    
# Luminosity = 4πr^2 * σT^4

#Lum_solar_units = 4*Np.pi()*σ*

lum_list = fill_array(40, 40, 2500, 50000)
temp_list = fill_array(40, 40, 10**-4, 10**6)       


        
        