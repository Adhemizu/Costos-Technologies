"""
Tabla Presuesto

Descripción:
"""

# librerias
from PySide2.QtWidgets import QTableWidget


class TablaPresupuesto(QTableWidget):
    """ tabla de presupuesto """

    def __init__(self, rows: int, columns: int, parent=None):
        """ constructor """
        super().__init__(rows, columns, parent)

        # atributos
        self.atributos()

        # initial functions
        self.inicializar()

    # atributos
    def atributos(self):
        """ atributos """

    # inicializar
    def inicializar(self):
        """ inicializar """
