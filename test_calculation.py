import pytest
from calculation import youngs_double_slit_formula, coefficient_of_viscosity_formula, rocket_velocity_formula


def test_youngs_double_slit_formula():
    wavelength = 650
    slit_distance = 0.1
    screen_distance = 2

    result = youngs_double_slit_formula(wavelength, slit_distance, screen_distance)
    assert round(result, 2) == 13.0

def test_coefficient_of_viscosity_formula():
    density = 1000
    radius = 0.01
    velocity = 0.1

    result = coefficient_of_viscosity_formula(density, radius, velocity)
    assert round(result, 2) == 0.22

def test_rocket_velocity_formula():
    thrust = 1000
    mass = 50
    time = 10

    result = rocket_velocity_formula(thrust, mass, time)
    assert round(result, 2) == 200.0
