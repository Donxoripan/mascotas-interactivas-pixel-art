import sys
import random

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication

from motor.mascota import Mascota
from motor.animacion import Animacion
from motor.ventana_principal import VentanaMascota


app = QApplication(sys.argv)

# -------------------------
# VENTANA
# -------------------------

ventana = VentanaMascota()

# -------------------------
# MASCOTA
# -------------------------

pantalla = QGuiApplication.primaryScreen()

geometria = pantalla.availableGeometry()

ANCHO_PANTALLA = geometria.width()
ALTO_PANTALLA = geometria.height()

cuervo = Mascota()

cuervo.agregar_animacion(
    "quieto",
    Animacion(
        "mascotas/cuervo/animaciones/quieto.png",
        32,
        32,
        4,
        fps=4
    )
)

cuervo.agregar_animacion(
    "caminar",
    Animacion(
        "mascotas/cuervo/animaciones/caminar.png",
        32,
        32,
        6,
        fps=8
    )
)

# Posición inicial

cuervo.x = 500
cuervo.y = 500

# Movimiento

cuervo.velocidad = 2

# Destino inicial

cuervo.destino_x = cuervo.x

ventana.move(
    cuervo.x,
    cuervo.y
)

# -------------------------
# ANIMACIÓN
# -------------------------

contador = 0


def actualizar_animacion():

    animacion = cuervo.obtener_animacion_actual()

    ventana.setPixmap(
        animacion.obtener_fotograma(
            cuervo.mirando_derecha
        )
    )

    animacion.avanzar()


# -------------------------
# COMPORTAMIENTO
# -------------------------

def actualizar_comportamiento():

    global contador

    contador += 1

    if cuervo.estado == "quieto":

        if contador >= 30:

            contador = 0

            cuervo.destino_x = random.randint(
                0,
                ANCHO_PANTALLA - 32
            )

            cuervo.cambiar_estado(
                "caminar"
            )   

    elif cuervo.estado == "caminar":

        if cuervo.x < cuervo.destino_x:

            cuervo.mirando_derecha = True

            cuervo.x += cuervo.velocidad

        elif cuervo.x > cuervo.destino_x:

            cuervo.mirando_derecha = False

            cuervo.x -= cuervo.velocidad

        ventana.move(
            cuervo.x,
            cuervo.y
        )

        if abs(
            cuervo.x - cuervo.destino_x
        ) <= cuervo.velocidad:

            cuervo.cambiar_estado(
                "quieto"
            )

            contador = 0


# -------------------------
# TEMPORIZADOR ANIMACIÓN
# -------------------------

temporizador_animacion = QTimer()

temporizador_animacion.timeout.connect(
    actualizar_animacion
)

temporizador_animacion.start(120)

# -------------------------
# TEMPORIZADOR IA
# -------------------------

temporizador_comportamiento = QTimer()

temporizador_comportamiento.timeout.connect(
    actualizar_comportamiento
)

temporizador_comportamiento.start(100)

# -------------------------
# INICIO
# -------------------------

ventana.resize(32, 32)

actualizar_animacion()

ventana.show()

sys.exit(app.exec())