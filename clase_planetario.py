class SistemaPlanetario:
    def __init__(self, planets): # defino los atributos de la clase
        self.planets = planets # planetas del sistema

    def obtener_numero_planetas(self):
        return len(self.planets) # devuelvo la cantidad de planetas del sistema

    def orden_eje(self):
        return sorted(self.planets, key=lambda planet: planet._a) # ordeno los planetas por semieje mayor