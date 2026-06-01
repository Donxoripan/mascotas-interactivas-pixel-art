from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class VentanaMascota(QLabel):

    def __init__(self):

        super().__init__()

        self.arrastrando = False
        self.posicion_inicial = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

    def mousePressEvent(self, evento):

        if evento.button() == Qt.LeftButton:

            self.arrastrando = True

            self.posicion_inicial = (
                evento.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, evento):

        if self.arrastrando:

            self.move(
                evento.globalPosition().toPoint()
                - self.posicion_inicial
            )

    def mouseReleaseEvent(self, evento):

        self.arrastrando = False