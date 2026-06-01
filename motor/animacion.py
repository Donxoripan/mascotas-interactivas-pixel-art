from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QTransform


class Animacion:

    def __init__(
        self,
        ruta,
        ancho_fotograma,
        alto_fotograma,
        cantidad_fotogramas,
        fps=6
    ):
        self.mirando_derecha = True

        self.sprite_derecha = QPixmap(ruta)

        self.sprite_izquierda = self.sprite_derecha.transformed(
            QTransform().scale(-1, 1)
        )

        self.ancho_fotograma = ancho_fotograma
        self.alto_fotograma = alto_fotograma

        self.cantidad_fotogramas = cantidad_fotogramas

        self.fotograma_actual = 0

        self.timer = QTimer()

        self.timer.setInterval(
            int(1000 / fps)
        )

    def obtener_fotograma(
        self,
        mirando_derecha=True
    ):

        x = (
            self.fotograma_actual
            * self.ancho_fotograma
        )

        sprite = (
            self.sprite_derecha
            if mirando_derecha
            else self.sprite_izquierda
        )

        return sprite.copy(
            x,
            0,
            self.ancho_fotograma,
            self.alto_fotograma
        )

    def avanzar(self):

        self.fotograma_actual += 1

        if self.fotograma_actual >= self.cantidad_fotogramas:
            self.fotograma_actual = 0