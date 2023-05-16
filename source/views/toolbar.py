"""
Barra de herramientas principal

Descripción:
"""

# librerias
from PySide2.QtWidgets import QToolBar


class MainToolBar(QToolBar):
    """ barra de herramientas """

    def __init__(self, parent=None) -> None:
        """ constructor """
        super().__init__(parent)

        # atributos
        self.atributos()

        # widgets
        self.widgets()

    # atributos
    def atributos(self):
        """ atributos """

    # widgets
    def widgets(self):
        """ widgets """
