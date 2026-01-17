import numpy as Np
import matplotlib.pyplot as mat 
#Range of Temperatures: 2,500 Kelvin - 50,000 Kelvin
#Range of Luminosity: 10^-4 solar units - 10^6 solar units

solar_radius = 6.957 * (10**8) # meters
solar_kelvin = 5778 # Kelvin
solar_lum = 3.828 * (10**26) # watts

rand_temp = Np.random.rand(2500, 50001)
rand_lum = Np.random.uniform(10 ** -4, 10 ** 6)
rand_radius = Np.random.uniform(0.1 * solar_radius, 1000 * solar_radius)

σ = 5.67 * 10 ** -8 # W/m^2/K^4, Approximation of Stefan - Boltzmann Constant




# Luminosity = 4πr^2 * σT^4

#Lum_solar_units = 4*Np.pi()*σ*

rows = 1
amount = 800

temp_list = Np.random.normal(10000, 3000, amount)
temp_lsit = Np.clip(temp_list, 2500, 50001)

radius = (temp_list / solar_kelvin) ** 0.7
radius_list = radius * Np.random.normal( 1, 0.25, amount) * solar_radius
radius_list = Np.clip(radius_list, 0.08 * solar_radius, 30 * solar_radius)

lum_list = Np.ones(amount)
lum_list = (4 * Np.pi * radius_list**2 * σ * temp_list**4) * Np.random.normal(1.0, 0.35, amount)



log_lum_solar = Np.log10(lum_list / solar_lum)
log_temp_solar = Np.log10(temp_list / solar_kelvin)









#mat.plot(Np.log10(lum_list / solar_lum), Np.log10(temp_list / solar_kelvin), linestyle = '', color = 'r', alpha = 0.5)
mat.figure(figsize=(8, 8))
mat.title('H-R Diagram')
mat.xlabel('Temeperature (Kelvin)')
mat.ylabel('Luminosity (W/m^2/K^4)')
mat.xscale('log')
mat.yscale('log')
mat.scatter(Np.log10(lum_list / solar_lum), Np.log10(temp_list / solar_kelvin), c = temp_list, cmap='coolwarm_r')
mat.gca().invert_xaxis()
mat.grid(True)
mat.colorbar(label = 'Temperature (K)')
mat.show()


