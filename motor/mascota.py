class Mascota:

    def __init__(self):

        self.animaciones = {}

        self.estado = "quieto"

        self.x = 500
        self.y = 500

        self.velocidad = 2

        self.destino_x = 500

        self.mirando_derecha = True

    def agregar_animacion(
        self,
        nombre,
        animacion
    ):

        self.animaciones[nombre] = animacion

    def cambiar_estado(
        self,
        nombre
    ):

        if nombre in self.animaciones:

            self.estado = nombre

    def obtener_animacion_actual(self):

        return self.animaciones[
            self.estado
        ]