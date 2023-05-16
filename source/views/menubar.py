"""
Menu de barra principal

Descripción:
"""

# librerias
from PySide2.QtWidgets import QMenuBar,  QAction


class MainMenuBar(QMenuBar):
    """ ventana principal """

    def __init__(self, parent=None) -> None:
        """ constructor """
        super().__init__(parent)

        # atributos
        self.atributos()

        # init methods

        # widgets
        self.widgets()

    # atributos
    def atributos(self):
        """ atributos """

    # widgets
    def widgets(self):
        """ widgets """

        # definir menus
        self.set_archivo()
        self.set_editar()
        self.set_configurar()
        self.set_preferencias()
        self.set_complementos()
        self.set_ayuda()

    # items
    def set_archivo(self):
        """ establecer item archivo """

        # agregar menu
        self.archivo = self.addMenu("Archivo")

        # items del menu
        self.archivo_items = {"nuevo": QAction("Nuevo"),
                              "abrir": QAction("Abrir"),
                              "guardar": QAction("Guardar"),
                              "guardar_como": QAction("Guardar como"),
                              "recientes": QAction("Recientes")}

        # agregar items al menu
        i = 0
        for item in self.archivo_items.values():
            if i == 4:
                self.archivo.addSeparator()
            self.archivo.addAction(item)
            i += 1

    def set_editar(self):
        """ establecer item editar """

        # agregar menu
        self.editar = self.addMenu("Editar")

        # items del menu
        self.editar_items = {"copiar": QAction("Copiar"),
                             "deshacer": QAction("Deshacer"),
                             "pegar": QAction("Pegar")}

        # agregar items al menu
        for item in self.editar_items.values():
            self.editar.addAction(item)

    def set_configurar(self):
        """ establecer item configurar """

        # agregar menu
        self.configurar = self.addMenu("Configurar")

        # items del menu
        self.configurar_items = {"importar": QAction("Importar"),
                                 "estilos": QAction("Estilos"),
                                 "tema": QAction("Tema")}

        # agregar items al menu
        for item in self.configurar_items.values():
            self.configurar.addAction(item)

    def set_preferencias(self):
        """ establecer item preferencias """

        # agregar menu
        self.preferencias = self.addMenu("Preferencias")

        # items del menu
        self.preferencias_items = {"unidades": QAction("Unidades"),
                                   "impuestos": QAction("Impuestos"),
                                   "calendario": QAction("Calendario")}

        # agregar items al menu
        for item in self.preferencias_items.values():
            self.preferencias.addAction(item)

    def set_complementos(self):
        """ establecer item complementos """

        # agregar menu
        self.complementos = self.addMenu("Complementos")

        # items del menu
        self.complementos_items = {"plugins": QAction("Plugins"),
                                   "apps": QAction("Aplicaciones")}

        # agregar items al menu
        for item in self.complementos_items.values():
            self.complementos.addAction(item)

    def set_ayuda(self):
        """ establecer item ayuda """

        # agregar menu
        self.ayuda = self.addMenu("Ayuda")

        # items del menu
        self.ayuda_items = {"tutorial": QAction("Tutorial"),
                            "acerca_de": QAction("Acerca de"),
                            "licencia": QAction("Licencia")}

        # agregar items al menu
        for item in self.ayuda_items.values():
            self.ayuda.addAction(item)

    # utilidades
