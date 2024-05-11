import numpy as np
class PlanetaExoplanetario(): #Entre los parentesis poner la clase Planeta
    def __init__(self, star_name, mass_pla, radius, a, i, e, omega, discovery, tatooine=False): # defino los atributos de la clase
        super().__init__(star_name, mass_pla, radius, a, i, e, omega) # heredo los atributos de la clase Planeta
        self.discovery_method = discovery # método de descubrimiento del planeta
        self.similar_tatooine = tatooine # si el planeta es similar a Tatooine
def determinar_metodo_descubrimiento(self):
    return f"Método de descubrimiento: {self.discovery_method}" # devuelvo el método de descubrimiento del planeta
def determinar_similar_tatooine(self):
    if self.similar_tatooine: # si el planeta es similar a Tatooine
        return "El planeta es similar a Tatooine." # devuelvo que el planeta es similar a Tatooine
    else:
        return "El planeta no es similar a Tatooine." # devuelvo que el planeta no es similar a Tatooine
def calcular_parametro_impacto(self):
    if self._eccentricity != 0 and self._ownmovement == "tránsito": # si la excentricidad es distinta de cero y el movimiento propio es tránsito
        b= (self._a * np.cos(self._inclination) * (1 - self._eccentricity**2)) / (self._starhostess.radius * (1 + self._eccentricity * np.sin(np.radians(self._periastron)))) # calculo el parámetro de impacto
        return b
    else:
        return None