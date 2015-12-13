# http://doc.qt.io/qt-4.8/modelview.html
# http://doc.qt.io/qt-4.8/modelview.html#2-3-a-clock-inside-a-table-cell
# http://doc.qt.io/qt-4.8/modelview.html#2-4-setting-up-headers-for-columns-and-rows

from PySide import QtGui
from PySide import QtCore

Qt = QtCore.Qt


class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        super(MyModel, self).__init__(parent)
        self.topLeftCellIndex = self.createIndex(0, 0)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.timerHit)
        self.timer.start()
    
    def timerHit(self):
        # emit a signal to make the view reread identified data
        # When the model is attached to the view, the dataChanged signal
        # is connected to a slot in the view!!
        print "Timer timed out"
        self.dataChanged.emit(self.topLeftCellIndex, self.topLeftCellIndex)
        print "Inform the view that it needs to update the specified modelIndex"
    
    def rowCount(self, modelIndex):
        return 2
    
    def columnCount(self, modelIndex):
        return 3
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                headers = ("first", "second", "third")
            else:
                headers = ("Bugs Bunny", "Daffy Duck")
            return dict(enumerate(headers))[section]
    
    def data(self, modelIndex, role=Qt.ItemDataRole.DisplayRole):
        row = modelIndex.row()
        column = modelIndex.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            if modelIndex == self.topLeftCellIndex:
                if self.timer.isActive():
                    print "Updating time"
            return QtCore.QTime.currentTime().toString()
        elif role == Qt.ItemDataRole.FontRole:
            if modelIndex == self.topLeftCellIndex:
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


tableView.verticalHeader().hide()
tableView.verticalHeader().show()

tableView.horizontalHeader().hide()
tableView.horizontalHeader().show()
