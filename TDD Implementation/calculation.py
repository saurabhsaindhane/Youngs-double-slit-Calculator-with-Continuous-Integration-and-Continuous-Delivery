def youngs_double_slit_formula(wavelength, slit_distance, screen_distance):
    diffraction_pattern = (wavelength * screen_distance) / (slit_distance * 10 ** -3)
    return diffraction_pattern

def coefficient_of_viscosity_formula(density, radius, velocity):
    viscosity_coefficient = (2 * density * radius ** 2 * velocity) / 9
    return viscosity_coefficient

def rocket_velocity_formula(thrust, mass, time):
    velocity = (thrust * time) / mass
    return velocity
