"""
Model principal

Descripción:
    El modelo se encarga de gestionar y manipular los datos, así como de aplicar las reglas y operaciones relacionadas con la lógica de la aplicación.

    El modelo es responsable de:
        > Recuperar y almacenar los datos en la base de datos.
        > Procesar los datos.
        > Realizar cálculos y validaciones.
        > Preparar los datos para su presentación en la vista.
        > Entre otras tareas.

    El directorio 'models' contiene:
        > Todos los módulos relacionados con el modelo.
"""

# libreria
from PySide2.QtCore import QObject

# libreria
from source.view import View


class Model(QObject):
    """ modelo """

    def __init__(self, view: View):
        super().__init__()

        # instancia de vista
        self.view = view
