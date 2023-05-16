"""
Controlador principal

Descripción:
    El controlador es el componente que actúa como intermediario entre la vista y el modelo maneja las acciones del usuario en la vista y actualiza el modelo en consecuencia.
    Luego, el controlador actualiza la vista con los datos actualizados del modelo.

    El controlador es responsable de:
        > Recibir la entrada del usuario y actualizar el modelo en consecuencia.
        > Actualizar la vista con los cambios del modelo.
        > Entre otras tareas.

    El directorio 'controllers' contiene:
        > Todos los módulos relacionados con los controladores.
"""

# libreria
from PySide2.QtCore import QObject

# libreria
from source.view import View
from source.model import Model


class Controller(QObject):
    """ controlador """

    def __init__(self, view: View, model: Model):
        super().__init__()

        # instancia de vista y modelo
        self.view = view
        self.model = model
