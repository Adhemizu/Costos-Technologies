"""
Vista principal

Descripción:
    Vista es encargada de la representación visual de los datos y la interacción con el usuario.

    Presenta las siguientes características:
        > Presentación: La Vista se encarga de mostrar los datos del modelo de una manera comprensible y significativa para el usuario. Puede representar los datos en forma de texto, tablas, gráficos, formularios, interfaces gráficas de usuario, entre otros.

        > Interfaz de usuario: La Vista es responsable de la interacción con el usuario. Recibe las acciones del usuario, como clics, pulsaciones de teclas o gestos, y las envía al Controlador para su procesamiento.

        > Independencia del modelo: La Vista, en principio, no tiene conocimiento directo del modelo de datos subyacente. En lugar de eso, se comunica con el Controlador para obtener los datos que necesita y mostrarlos al usuario.

        > Actualización de la interfaz: La Vista puede necesitar actualizarse cuando los datos del modelo cambian. En ese caso, tanto el modelo como el controlador pueden realizar la tarea de actualizar la Vista para reflejar los cambios en la interfaz de usuario, pero se recomienda que sea el controlador quien lo realize.

    Cabe resaltar que, si bien la Vista se encarga de la representación visual y la interacción con el usuario, ésta no debe tener lógica compleja, ya que dicha lógica compleja debe residir principalmente en el modelo y, en algunos casos, también puede implementarse en el controlador.

    El directorio 'views' contiene:
        > Todos los módulos relacionados con la vista(interfaz gráfica de usuario) de la aplicación.        
"""

# librerias
from PySide2.QtWidgets import QMainWindow, QWidget, QLabel
from PySide2.QtWidgets import QTabWidget, QStatusBar
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon


# librerias
from source.views.menubar import MainMenuBar
from source.views.toolbar import MainToolBar
from source.views.presupuesto.presupuesto import WidgetPresupuesto

# libreria path
from source.functions.path import resource_path


class View(QMainWindow):
    """ ventana principal """

    def __init__(self) -> None:
        """ constructor """
        super().__init__()

        # atributos
        self.atributos()

        # initial methods
        self.setWindowIcon(QIcon(resource_path("icon/logo.png")))

        # widgets
        self.widgets()

        # finish methods
        self.setWindowTitle(self.titulo)
        self.showMaximized()

    # atributos
    def atributos(self):
        """ atributos """

        # titulo
        self.titulo = "Costos Technologies"

    # widgets
    def widgets(self):
        """ widgets """

        # menu de barras
        self.set_menubar()

        # barra de herramientas
        self.set_toolbar()

        # construir tabwidget
        self.set_tabwidget()

        # barra de estado
        self.set_status_bar()

    # menu de barras
    def set_menubar(self):
        """ construir menu de barras """

        # crear widget
        self.item_menu_bar = MainMenuBar(self)

        # establecer menu de barras
        self.setMenuBar(self.item_menu_bar)

    # barra de herramientas
    def set_toolbar(self):
        """ crear barra de herramientas """

        # crear widget
        self.item_toolbar = MainToolBar(self)

        # establecer barra de herramientas
        self.addToolBar(self.item_toolbar)

    # pestañas de tabulacion
    def set_tabwidget(self):
        """ establecer tabwidget """

        # tabwidget
        self.item_tabwidget = QTabWidget()
        # self.item_tabwidget.setTabPosition(QTabWidget.South)
        self.item_tabwidget.setTabShape(QTabWidget.Rounded)

        # crear widgets del tabwidget
        self.widget_presupuesto()
        self.widget_apu()

        # establecer tabwidget como widget central
        self.setCentralWidget(self.item_tabwidget)

    def widget_presupuesto(self):
        """ construir widget presupuesto """

        # crear widget
        self.presupuesto = WidgetPresupuesto(self)

        # agregar widgets al tabwidget
        self.item_tabwidget.addTab(self.presupuesto, 'Presupuesto')
        self.item_tabwidget

    def widget_apu(self):
        """ construir widget de analisis de precios unitarios """

        # crear widget
        self.apu = QWidget()

        # agregar widgets al tabwidget
        self.item_tabwidget.addTab(self.apu, 'Analisis de Precios Unitarios')

    # barra de estado
    def set_status_bar(self):
        """ construir barra de estado """

        # Crear la barra de información y agregarla a la ventana
        self.item_status_bar = QStatusBar(self)

        # establecer barra de estado
        self.setStatusBar(self.item_status_bar)

        # agregar cuadro permanente
        etiqueta = QLabel("Costos Technologies")
        etiqueta.setAlignment(Qt.AlignRight)
        self.item_status_bar.addPermanentWidget(etiqueta)

        # Mostrar un mensaje en la barra de información
        self.item_status_bar.showMessage("Bienvenido", 5000)
