#physics.py
import numpy as np
g = 9.81  # acceleration due to gravity (m/s^2)

def calculate_buoyancy(V, density_fluid, g = 9.81):
    if isinstance(V, (int, float)) and isinstance(density_fluid, (int, float)):
        return (f"{V * g * density_fluid} Newtons")    
    else:
        return ValueError("Insert valid values for volume and fluid density")



def will_it_float(density_object, density_fluid):
    if density_object < density_fluid:
        return True
    if density_object > density_fluid:
        return False
    if density_object == density_fluid:
        return None  # Object is neutrally buoyant
    if density_object != density_fluid:
        return ValueError("Invalid density values")

def calculate_pressure(depth, density_fluid):
    density_fluid = 1000
    if isinstance(depth, (float, int)):
        return (f"{depth * density_fluid * g} Pascals")
    else:
        return ValueError("Insert valid values for depth and fluid density")

def calculate_acceleration(F, m):
    """F = Force applied in newtons, m: the mass of the object in kilograms."""
    if isinstance(F, (float, int)) and isinstance(m, (float, int)):
        return (f"{F / m} m/s^2")
    else:
        return ValueError("Insert valid values for mass and force") 

def calculate_angular_acceleration(tau, I):
    if isinstance(tau, (float, int)) and isinstance(I, (float, int)):
        return (f"{tau / I} rad/s^2")
    else:
        return ValueError("Insert valid values for torque and moment of inertia")

def calculate_torque(F_magnitude, F_direction, r):
    """F_magnitude: the magnitude of force applied to the object in Newtons,
    F_direction: the direction of the force applied to the object in degrees,
    r: the distance from the axis of rotation to the point where the force is applied in meters."""
    if isinstance(F_direction, (float, int)) and isinstance(F_magnitude, (float, int)) and isinstance(r, (float, int)):
        return (f"{F_magnitude * r * np.sin(np.radians(F_direction))} N⋅m")
    else:
        return ValueError("Insert valid values for force magnitude, direction, and radius")

def calculate_moment_of_inertia(m,r):
    if isinstance(m, (float, int)) and isinstance(r, (float, int)):
        return (f"{m * r**2} kg⋅m^2")
    else:
        return ValueError("Insert valid values for mass and radius")
    
def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance):

