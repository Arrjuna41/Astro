import numpy as Np
import matplotlib.pyplot as mat 
#Range of Temperatures: 2,500 Kelvin - 50,000 Kelvin
#Range of Luminosity: 10^-4 solar units - 10^6 solar units

solar_radius = 6.957 * (10**8) # meters
solar_kelvin = 5778 # Kelvin
solar_lum = 3.828 * (10**26) # watts
'''
rand_temp = Np.random.rand(2500, 50001)
rand_lum = Np.random.uniform(10 ** -4, 10 ** 6)
rand_radius = Np.random.uniform(0.1 * solar_radius, 1000 * solar_radius)
'''

σ = 5.67 * 10 ** -8 # W/m^2/K^4, Approximation of Stefan - Boltzmann Constant




# Luminosity = 4πr^2 * σT^4

#Lum_solar_units = 4*Np.pi()*σ*

rows = 1
amount = 200

temp_list = Np.random.normal(10000, 3000, amount)
temp_list = Np.clip(temp_list, 2500, 50001)

radius = (temp_list / solar_kelvin) ** 0.6
radius_list = radius * Np.random.normal( 1, 0.25, amount) * solar_radius
radius_list = Np.clip(radius_list, 0.08 * solar_radius, 30 * solar_radius)

lum_list = Np.ones(amount)
lum_list = (4 * Np.pi * radius_list**2 * σ * temp_list**4) * Np.random.normal(1.0, 0.35, amount)



log_temp_solar = Np.log10(temp_list / solar_kelvin)
log_lum_solar = Np.log10(lum_list / solar_lum)


slope , intercept = Np.polyfit(Np.log10(temp_list / solar_kelvin), Np.log10(lum_list / solar_lum), 1)
α = slope
log_α = intercept

smooth_temp = Np.logspace(Np.log10(temp_list.min()), Np.log10(temp_list.max()), 200 )
smooth_lumδ = log_α + α * smooth_temp # Power law
smooth_lum = 10 ** smooth_lumδ

x_list = Np.linspace(1, smooth_temp.size, smooth_temp.size)



mat.figure(figsize=(8, 8))
mat.title('H-R Diagram')
mat.xlabel('Temeperature (Kelvin)')
mat.ylabel('Luminosity (W/m^2/K^4)')
mat.plot(smooth_temp, smooth_lumδ, 'r--', color = 'r', alpha = 0.5)
mat.scatter(log_temp_solar, log_lum_solar, cmap = 'coolwarm')
mat.xscale('log')
mat.yscale('log')
mat.gca().invert_xaxis()
mat.grid(True)
mat.colorbar(label = 'Temperature (K)')
mat.show()


