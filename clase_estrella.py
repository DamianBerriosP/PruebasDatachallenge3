import numpy as np
LSun = 3.828e26  # Luminosidad solar en vatios
MSun = 1.9884e30  # Masa solar en kg

class Star:
    def __init__(self, name, mass, radius, teff, d, own_movement): # defino los atributos de la clase
        self.name = name # nombre de la estrella
        self._mass = mass # masa de la estrella
        self._radius = radius # radio de la estrella
        self._temperature = teff # temperatura efectiva de la estrella
        self._distance = d # distancia de la estrella
        self._ownmovement= own_movement # movimiento propio de la estrella

    def calcular_luminosidad_total(self):
        return 4 * np.pi * self._radius**2 * self._temperature # calculo la luminosidad total de la estrella


    def calcular_luminosidad_secuencia_principal(self): # calculo la luminosidad de la secuencia principal
        return LSun * (self._mass / MSun)**3.5