from PySide import QtGui
from PySide import QtCore


self = QtGui.QMainWindow()
self.setWindowTitle("Qt MainWindow")

self.show()

menuBar = self.menuBar()

fileMenu = menuBar.addMenu('File')
exitAction = fileMenu.addAction("Exit")

exitAction.triggered.connect(self.close)

dockWidgetWidget = QtGui.QWidget(parent=self)
dockWidgetWidget.setLayout(QtGui.QVBoxLayout())
dockWidgetWidget.layout().addWidget(QtGui.QPushButton("Dock Widget 1"))

dockWidget = QtGui.QDockWidget('Dock Widget 1', self)

dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)

dockWidget.setWidget(dockWidgetWidget)

self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockWidget)


centralWidget = QtGui.QWidget(parent=self)
centralWidget.setLayout(QtGui.QVBoxLayout())
centralWidget.layout().addWidget(QtGui.QTextEdit())

self.setCentralWidget(centralWidget)

toolbar1 = self.addToolBar("toolbar1")
toolbar1.setToolTip("File tools")
toolbar1.addAction(exitAction)

"""
In [10]: self.actions()
Out[10]: []

In [11]: menuBar.actions()
Out[11]: [<PySide.QtGui.QAction at 0x4565a80>]

In [12]: exitAction
Out[12]: <PySide.QtGui.QAction at 0x4551b70>

In [13]: fileMenu.actions()
Out[13]: [<PySide.QtGui.QAction at 0x4551b70>]
"""
