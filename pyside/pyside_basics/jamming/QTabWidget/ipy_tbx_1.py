from PySide import QtCore
from PySide import QtGui


class Tool(object):
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties


class ToolPropertiesWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolPropertiesWidget, self).__init__(*args, **kwargs)
        self._setupUi()
    
    def _setupUi(self):
        self._layoutMain = QtGui.QVBoxLayout()
        self.setLayout(self._layoutMain)
        
        self._heading = QtGui.QLabel()
        self._layoutMain.addWidget(self._heading)

        self._layoutMain.addStretch()

    def setHeading(self, heading):
        self._heading.setText(heading)


class ToolsListWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolsListWidget, self).__init__(*args, **kwargs)
        self._setupUi()

    def _setupUi(self):
        self._layoutMain = QtGui.QVBoxLayout()
        self.setLayout(self._layoutMain)
        
        self._layoutMain.addStretch()
    
    def addTool(self, tool):
        layout = self.layout()
        
        button = QtGui.QPushButton(tool.name)
        
        layout.insertWidget(layout.count()-1, button)


class PropertiesWidget(QtGui.QTabWidget):
    def __init__(self, *args, **kwargs):
        super(PropertiesWidget, self).__init__(*args, **kwargs)
        

class ToolBoxWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolBoxWidget, self).__init__(*args, **kwargs)
        self._setupUi()

    def _setupUi(self):
        self._layoutMain = QtGui.QHBoxLayout()
        self.setLayout(self._layoutMain)
        
        self._widgetToolsList = ToolsListWidget()
        self._layoutMain.addWidget(self._widgetToolsList)    

        self._widgetProperties = PropertiesWidget()
        self._layoutMain.addWidget(self._widgetProperties)

    @property
    def toolsList(self):
        return self._widgetToolsList
    
    @property
    def properties(self):
        return self._widgetProperties

##

tbw = ToolBoxWidget()
tbw.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
tbw.show()


tool1 = Tool('tool1', 'a b c')
tool2 = Tool('tool2', 'x y')
tool3 = Tool('tool3', 'm n o p')

tbw.toolsList.addTool(tool1)
tbw.toolsList.addTool(tool2)
tbw.toolsList.addTool(tool3)

props1 = ToolPropertiesWidget()
props1.setHeading(tool1.properties)
tbw.properties.addTab(props1, tool1.name)

props2 = ToolPropertiesWidget()
props2.setHeading(tool2.properties)
tbw.properties.addTab(props2, tool2.name)

props3 = ToolPropertiesWidget()
props3.setHeading(tool3.properties)
tbw.properties.addTab(props3, tool3.name)

##

tbw.adjustSize()

##

tbw.properties.hide()
tbw.adjustSize()

tbw.properties.show()

tbw.adjustSize()

##

tbw.properties.removeTab(1)
tbw.properties.insertTab(0, props2, tool2.name)
tbw.properties.setCurrentWidget(props2)

##

tbw.properties.removeTab(2)
tbw.properties.insertTab(0, props3, tool3.name)
tbw.properties.setCurrentWidget(props3)

##

tbw.properties.removeTab(2)
tbw.properties.insertTab(0, props1, tool1.name)
tbw.properties.setCurrentWidget(props1)
