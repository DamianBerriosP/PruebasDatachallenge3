class SistemaJerarquico:
    def __init__(self, stars): # defino los atributos de la clase
        self.stars = stars # estrellas del sistema

    def ordenar_por_masa_estelar(self):
        return sorted(self.stars, key=lambda estrella: estrella.mass) # ordeno las estrellas por masa

    def imprimir_nombres_ordenados(self):
        estrellas_ordenadas = self.ordenar_por_masa_estelar()
        nombres_ordenados = [f"{estrella.name}{chr(65 + i)}" for i, estrella in enumerate(estrellas_ordenadas)] # imprimo los nombres de las estrellas ordenadas
        return ", ".join(nombres_ordenados) # devuelvo los nombres de las estrellas ordenadas