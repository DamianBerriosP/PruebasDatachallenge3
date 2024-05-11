import numpy as np
class Planet:
    def __init__(self, star_name, mass_pla, radius, a, i, e, omega): # defino los atributos de la clase
        self._starhostess = star_name # estrella anfitriona
        self._mass_pla = mass_pla # masa del planeta
        self._radius = radius # radio del planeta
        self._a = a # semieje mayor de la órbita del planeta
        self._inclination = i # inclinación de la órbita del planeta
        self._eccentricity = e # excentricidad de la órbita del planeta
        self._periastron = omega # argumento del periastron del planeta
def calcular_periodo_rotacion_kepleriana(self):
        G = 6.67430e-11 # constante de gravitación universal
        T = 2 * np.pi * np.sqrt(self._a**3 / (G * self._mass_pla)) # calculo el periodo de rotación kepleriano del planeta
        return T