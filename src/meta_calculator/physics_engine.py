def get_physical_energy(mass_kg):
    """Calculates E = MC^2 using the exact speed of light."""
    C = 299792458 
    return mass_kg * (C**2)

def keebler_equation(mass_kg, spiritual_h, efficiency_c=1.0):
    """Implements: E = c(MC^2 + H)"""
    mc2 = get_physical_energy(mass_kg)
    total_e = efficiency_c * (mc2 + spiritual_h)
    return total_e
