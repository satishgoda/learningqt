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

"""
In [11]: (executing lines 1 to 58 of "modelview.py")
Updating time
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time
Updating time

In [12]: timer = tableView.model().timer
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time

In [13]: timer.isActive()
Out[13]: True
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time

In [14]: timer.stop()

In [15]: timer.start()
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time
Timer timed out
Inform the view that it needs to update the specified modelIndex
Updating time

In [16]: timer.stop()
"""
