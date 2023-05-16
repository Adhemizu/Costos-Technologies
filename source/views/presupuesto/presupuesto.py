"""
Widget Presuesto

Descripción:
"""

# librerias
from PySide2.QtWidgets import QWidget, QVBoxLayout

# libreria
from source.views.presupuesto.tabla_presupuesto import TablaPresupuesto


class WidgetPresupuesto(QWidget):
    """ widget presupuesto """

    def __init__(self, parent=None):
        """ constructor """
        super().__init__(parent)

        # atributos
        self.atributos()

        # initial functions
        self.inicializar()

        # widgets
        self.widgets()

    # atributos
    def atributos(self):
        """ atributos """

    # inicializar
    def inicializar(self):
        """ inicializar """

    # widgets
    def widgets(self):
        """ widgets """

        # layout principal
        main_layout = QVBoxLayout()

        # widgets
        self.set_tabla_presupuesto(main_layout)

        # establecer layout
        self.setLayout(main_layout)

    def set_tabla_presupuesto(self, main_layout: QVBoxLayout):
        """ crear tabla de presupuesto """

        # crear tabla presupuesto
        self.tabla_presupuesto = TablaPresupuesto(0, 10, self)

        # agregar widget al tabwidget
        main_layout.addWidget(self.tabla_presupuesto)
