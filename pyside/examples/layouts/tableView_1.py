from PySide import QtGui
from PySide import QtCore

class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        super(MyModel, self).__init__(parent)
    
    def rowCount(self, modelIndex):
        return 2
    
    def columnCount(self, modelIndex):
        return 3
    
    def data(self, modelIndex, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return "Row{0}, Column{1}".format(modelIndex.row()+1, modelIndex.column()+1)
        return ""

tableView = QtGui.QTableView()

tableView.show()

myModel = MyModel(None)

tableView.setModel(myModel)
