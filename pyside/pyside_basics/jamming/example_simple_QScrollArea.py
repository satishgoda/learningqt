from PySide.QtGui import QMainWindow, QWidget, QScrollArea, QPushButton
from PySide.QtGui import QVBoxLayout, QHBoxLayout

mainWindow = QMainWindow()

mainWindow.show()

centralWidget = QWidget()

centralWidget.show()

centralWidgetLayout = QVBoxLayout()
centralWidget.setLayout(centralWidgetLayout)

mainWindow.setCentralWidget(centralWidget)

buttonsWidget = QWidget()
buttonsLayout = QHBoxLayout()
buttonsWidget.setLayout(buttonsLayout)

buttonsWidget.show()

for char in 'abracadabra':
    buttonsLayout.addWidget(QPushButton("Button '{0}'".format(char)))


scrolledButtonsWidget = QScrollArea()
scrolledButtonsWidget.setWidgetResizable(True)
"""
This property holds whether the scroll area should resize the view widget.

If this property is set to false (the default), the scroll area honors the size of its widget. Regardless of this property, you can programmatically resize the widget using widget()->resize(), and the scroll area will automatically adjust itself to the new size.

If this property is set to true, the scroll area will automatically resize the widget in order to avoid scroll bars where they can be avoided, or to take advantage of extra space.
"""

scrolledButtonsWidget.show()

scrolledButtonsWidget.setWidget(buttonsWidget)
"""
Sets the scroll area's widget.

The widget becomes a child of the scroll area, and will be destroyed when the scroll area is deleted or when a new widget is set.

The widget's autoFillBackground property will be set to true.

If the scroll area is visible when the widget is added, you must show() it explicitly.

Note that You must add the layout of widget before you call this function; if you add it later, the widget will not be visible - regardless of when you show() the scroll area. In this case, you can also not show() the widget later.
"""

scrolledButtonsWidget.adjustSize()

centralWidgetLayout.addWidget(scrolledButtonsWidget)

