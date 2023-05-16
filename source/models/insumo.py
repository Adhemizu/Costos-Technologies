"""
Modelo Insumo

Descripción:
    - En el contexto de un presupuesto, un insumo se refiere a los materiales, suministros, mano de obra y otros recursos necesarios para producir un bien o prestar un servicio.

    - En términos más generales, un insumo es un elemento básico que se utiliza en la producción de un bien o servicio.
      
    - Los insumos se incluyen como parte de los costos directos o indirectos asociados con la producción o prestación de un bien o servicio.
"""

# librerias


class Insumo():
    """ modelo insumo """

    def __init__(self):
        """ constructor """

        # atributos
        self.atributos()

    # atributos
    def atributos(self):
        """ atributos """

        # atributos
        self.nombre = ""
        self.precio_unitario = 0
        self.cantidad = 0

    # methods
    def definir_precio_unitario(self, precio_unitario: float = 0.0):
        """ precio unitario """

        # definir precio unitario
        self.precio_unitario = precio_unitario

    def definir_cantidad(self, cantidad: float = 0.0):
        """ definir cantidad """

        # definir cantidad
        self.cantidad = cantidad
