"""
Costos Technologies

Descripción:
    Costos-Technologies es un proyecto de código abierto(open source) de desarrollo de software de análisis de costos y presupuestos, con el propósito de ser completo, implementando así las últimas tecnologías en tema análisis, visualización e interacción.

Proyecto creado e iniciado por:
    - Adhemar Mizushima Medina, Nabla-Tec.
        LinkedIn: https://www.linkedin.com/in/adhemar-mizushima-38b048121/
        E-mail: adhemizu.med@gmail.com

Colaboradores:
    -

Repositorio:
    - GitHub: https://github.com/Adhemizu/Costos-Technologies

Fecha de creación: 13/05/2023 01:13
"""

# Libreria
import sys

# Libreria PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QFont


# Librería Estilos temáticos
import qdarktheme

# Libreria gui, controllers, models
from source.view import View
from source.controller import Controller
from source.model import Model

if __name__ == "__main__":

    # Crear la aplicación
    app = QApplication(sys.argv)

    # Aplica tema oscuro
    qdarktheme.setup_theme(theme='dark',
                           custom_colors={"primary": "#00A8F3"},
                           corner_shape="rounded")

    # Establecer el tamaño de fuente predeterminado para toda la aplicación
    font = QFont()
    font.setPointSize(10)
    app.setFont(font)

    # Crear la ventana principal y el modelo
    view = View()
    model = Model(view)

    # Crear el controlador y vincular la vista y el modelo
    controller = Controller(view, model)

    # Mostrar la ventana principal
    view.show()

    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec_())
