"""
Modelo Presupuesto

Descripción:
"""

# librerias


class Presupuesto():
    """ modelo presupuesto """

    def __init__(self):
        """ constructor """

        # atributos
        self.atributos()

    # atributos
    def atributos(self):
        ''' atributos '''

        # presupuesto
        self.nombre = ''
        self.monto_presupuesto = 0

        # cliente
        self.cliente = ''

        # lista de items
        self.items = {}

    # methods

    # items
    def agregar_item(self):
        """ agregar item """

    def eliminar_item(self):
        """ eliminar item """

    def instanciar_item(self, nombre_item: str):
        """ instanciar item """

    # presupuesto
    def actualizar_presupuesto(self):
        """ actualizar presupuesto """

    def presupuesto_literal(self):
        """ obtener el presupuesto general en literal """
