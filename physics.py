#physics.py
import numpy as np
g = 9.81  # acceleration due to gravity (m/s^2)

def calculate_buoyancy(V, density_fluid):
    return (f"{V * g * density_fluid} Newtons")
    """Calculate buoyant force with volume, fluid density and earth's gravitational acceleration"""

def will_it_float(density_object, density_fluid):
    if density_object < density_fluid:
        return True
    if density_object > density_fluid:
        return False
    if density_object == density_fluid:
        return None  # Object is neutrally buoyant
    if density_object != density_fluid:
        return ValueError("Invalid density values")