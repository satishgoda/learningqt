# http://doc.qt.io/qt-4.8/modelview.html

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
        print role,' ',

        if role == 8:
            print '\n', '-'*35

        row = modelIndex.row() + 1
        column = modelIndex.column() + 1
        
        if role == QtCore.Qt.DisplayRole:
            return "Row{0}, Column{1}".format(row, column)
        return ""

tableView = QtGui.QTableView()
myModel = MyModel(None)
tableView.setModel(myModel)
tableView.show()

# http://doc.qt.io/qt-4.8/modelview.html#2-2-extending-the-read-only-example-with-roles

# Now we need to determine how using a separated model impacts the application's performance, 
# so let's trace how often the view calls the data() method. 
# Each time you hover the cursor over the field, data() will be called again — 7 times for each cell. 
# That's why it is important to make sure that your data is available when data() is invoked and expensive
# lookup operations are cached. 

"""
6   7   9   10   1   0   8   
-----------------------------------
6   7   9   10   1   0   8   
-----------------------------------
6   7   9   10   1   0   8   
-----------------------------------
6   7   9   10   1   0   8   
-----------------------------------
6   7   9   10   1   0   8   
-----------------------------------
6   7   9   10   1   0   8   
-----------------------------------
"""

# Interactive model index inspection using Interactive Editor for Python

selectedIndex = tableView.selectedIndexes()[0]

selectedIndex

selectedIndex.row()
selectedIndex.column()

selectedIndex.data()
selectedIndex.data(QtCore.Qt.ItemDataRole.BackgroundRole)
selectedIndex.data(QtCore.Qt.ItemDataRole.BackgroundColorRole)
selectedIndex.data(QtCore.Qt.ItemDataRole.ForegroundRole)
selectedIndex.data(QtCore.Qt.ItemDataRole.DisplayRole)
selectedIndex.data(QtCore.Qt.ItemDataRole.FontRole)
selectedIndex.data(QtCore.Qt.ItemDataRole.CheckStateRole)

QtCore.Qt.ItemDataRole.values
"""
{'AccessibleDescriptionRole': PySide.QtCore.Qt.ItemDataRole.AccessibleDescriptionRole,
 'AccessibleTextRole': PySide.QtCore.Qt.ItemDataRole.AccessibleTextRole,
 'BackgroundColorRole': PySide.QtCore.Qt.ItemDataRole.BackgroundColorRole,
 'BackgroundRole': PySide.QtCore.Qt.ItemDataRole.BackgroundRole,
 'CheckStateRole': PySide.QtCore.Qt.ItemDataRole.CheckStateRole,
 'DecorationPropertyRole': PySide.QtCore.Qt.ItemDataRole.DecorationPropertyRole,
 'DecorationRole': PySide.QtCore.Qt.ItemDataRole.DecorationRole,
 'DisplayPropertyRole': PySide.QtCore.Qt.ItemDataRole.DisplayPropertyRole,
 'DisplayRole': PySide.QtCore.Qt.ItemDataRole.DisplayRole,
 'EditRole': PySide.QtCore.Qt.ItemDataRole.EditRole,
 'FontRole': PySide.QtCore.Qt.ItemDataRole.FontRole,
 'ForegroundRole': PySide.QtCore.Qt.ItemDataRole.ForegroundRole,
 'InitialSortOrderRole': PySide.QtCore.Qt.ItemDataRole.InitialSortOrderRole,
 'SizeHintRole': PySide.QtCore.Qt.ItemDataRole.SizeHintRole,
 'StatusTipPropertyRole': PySide.QtCore.Qt.ItemDataRole.StatusTipPropertyRole,
 'StatusTipRole': PySide.QtCore.Qt.ItemDataRole.StatusTipRole,
 'TextAlignmentRole': PySide.QtCore.Qt.ItemDataRole.TextAlignmentRole,
 'TextColorRole': PySide.QtCore.Qt.ItemDataRole.TextColorRole,
 'ToolTipPropertyRole': PySide.QtCore.Qt.ItemDataRole.ToolTipPropertyRole,
 'ToolTipRole': PySide.QtCore.Qt.ItemDataRole.ToolTipRole,
 'UserRole': PySide.QtCore.Qt.ItemDataRole.UserRole,
 'WhatsThisPropertyRole': PySide.QtCore.Qt.ItemDataRole.WhatsThisPropertyRole,
 'WhatsThisRole': PySide.QtCore.Qt.ItemDataRole.WhatsThisRole}
"""
