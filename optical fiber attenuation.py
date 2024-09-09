import numpy as np
import matplotlib.pyplot as plt

# Define parameters for optical fiber types
fiber_types = {
    "SMF-28": {'attenuation_coefficient': 0.2, 'dispersion_coefficient': 17},  # Values are arbitrary for demonstration
    "G.652": {'attenuation_coefficient': 0.18, 'dispersion_coefficient': 16},
    # Add more fiber types with their attenuation coefficients and dispersion coefficients
}

# Define wavelengths range (in nanometers)
wavelengths = np.linspace(800, 1600, 100)  # Example wavelengths range from 800 nm to 1600 nm

# Calculate attenuation for each fiber type
plt.figure(figsize=(10, 6))
for fiber_type, params in fiber_types.items():
    attenuation = params['attenuation_coefficient'] * wavelengths / 1000  # Attenuation in dB/km
    plt.plot(wavelengths, attenuation, label=fiber_type)

# Plotting settings
plt.title('Optical Fiber Attenuation Characteristics')
plt.xlabel('wavelength (nm)')
plt.ylabel('Attenuation (dB/km)')
plt.grid(True)
plt.legend()
plt.show()