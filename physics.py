#physics.py
import numpy as np
def calculate_buoyancy(V, density_fluid, g):
    """
      Find the buoyant force as F(b) = V * ρ * g
      V: volume of the displaced fluid
      density_fluid: density of the fluid = ρ
      g: gravitational force = 9.81 m/s^2
      returns:
        float: product of V * density_fluid * g
    """
    g = 9.81

    return V * density_fluid * g

 