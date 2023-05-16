"""
Modelo Item

Descripción:
    - En el contexto de un presupuesto, un ítem es un elemento individual.

    - Se identifica y se enumera en una lista detallada de los gastos o ingresos previstos para un determinado período.
      
    - Cada ítem puede representar un costo específico, como la compra de un equipo o la contratación de un servicio, o un ingreso específico, como la venta de un producto o la recepción de un pago por un servicio.
"""

# librerias


class Item():
    """ modelo item """

    def __init__(self):
        """ constructor """

        # atributos
        self.atributos()

    # atributos
    def atributos(self):
        """ atributos """

        # atributos
        self.nombre = ''
        self.precio_unitario = 0
        self.cantidad = 0

    # methods
    def definir_precio_unitario(self, precio_unitario: float = 0.0):
        """ precio unitario """
        self.precio_unitario = precio_unitario

    def definir_cantidad(self, cantidad: float = 0.0):
        """ definir cantidad """
        self.cantidad = cantidad

    # materiales
    def definir_material(self):
        """ definir/agregar material al item """

    def monto_total_materiales(self):
        """ monto total de materiales """

    # equipo
    def definir_equipo(self):
        """ definir/agregar equipo al item """

    def monto_total_equipo(self):
        """ monto total de equipo """

    # herramientas
    def definir_herramienta(self):
        """ definir/agregar herramienta al item """

    def monto_total_herramientas(self):
        """ monto total de herramientas """

    # maquinaria
    def definir_maquinaria(self):
        """ definir/agregar maquinaria al item """

    def monto_total_maquinaria(self):
        """ monto total de maquinaria """

    # impuestos
    def definir_impuesto_iva(self):
        """ definir/agregar impuesto impuesto al valor agregado """

    def definir_impuesto_it(self):
        """ definir/agregar impuesto a las transacciones """

    def definir_impuesto_personalizado(self):
        """ definir/agregar impuesto personalizado """

    def monto_total_impuestos(self):
        """ monto total de impuestos """
