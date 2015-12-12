# http://doc.qt.io/qt-4.8/modelview.html
# http://doc.qt.io/qt-4.8/modelview.html#2-3-a-clock-inside-a-table-cell

from PySide import QtGui
from PySide import QtCore

Qt = QtCore.Qt


class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        super(MyModel, self).__init__(parent)
        self.topLeftCellIndex = self.createIndex(0, 0)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timerHit)
        self.timer.start()
    
    def timerHit(self):
        # emit a signal to make the view reread identified data
        # When the model is attached to the view, the dataChanged signal
        # is connected to a slot in the view!!
        self.dataChanged.emit(self.topLeftCellIndex, self.topLeftCellIndex)
    
    def rowCount(self, modelIndex):
        return 2
    
    def columnCount(self, modelIndex):
        return 3
    
    def data(self, modelIndex, role=Qt.ItemDataRole.DisplayRole):
        row = modelIndex.row()
        column = modelIndex.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            return QtCore.QTime.currentTime().toString()
        elif role == Qt.ItemDataRole.FontRole:
            if modelIndex == self.timerIndex:
                boldFont = QtGui.QFont()
                boldFont.setBold(True)
                return boldFont
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignVCenter
        return ""


tableView = QtGui.QTableView()

tableView.show()

myModel = MyModel(None)

tableView.setModel(myModel)

# Implicit signal/slot connections
# The model's dataChanged signal is connected to a slot in the view!
