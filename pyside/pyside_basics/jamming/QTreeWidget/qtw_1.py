# http://doc.qt.io/qt-4.8/qtreewidget.html
# http://doc.qt.io/qt-4.8/qtreewidgetitem.html

from odwgui import QtGui
from odwgui import QtCore

qtw = QtGui.QTreeWidget()

qtw.setColumnCount(4)

qtw.show()

for entity in entities:
    qtwi = QtGui.QTreeWidgetItem(qtw)
    qtwi.setText(0, entity.namespace)
    qtwi.setText(1, entity.task)
    qtwi.setText(2, entity.group)
    qtwi.setText(3, entity.__class__.__name__)

qtw.setSortingEnabled(True)
