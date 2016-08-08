from collections import OrderedDict
from functools import partial

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
    
    def addTool(self, tool, callback):
        layout = self.layout()
        
        button = QtGui.QPushButton(tool.name)
        
        button.clicked.connect(callback)
        
        layout.insertWidget(layout.count()-1, button)


class PropertiesWidget(QtGui.QTabWidget):
    def __init__(self, *args, **kwargs):
        super(PropertiesWidget, self).__init__(*args, **kwargs)
        

class ToolBoxWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolBoxWidget, self).__init__(*args, **kwargs)
        self._setupUi()
        
        self.tools = {}

    def _setupUi(self):
        self._layoutMain = QtGui.QHBoxLayout()
        self.setLayout(self._layoutMain)
        
        self._widgetToolsList = ToolsListWidget()
        self._layoutMain.addWidget(self._widgetToolsList)    

        self._widgetProperties = PropertiesWidget()
        self._layoutMain.addWidget(self._widgetProperties)

    def addTool(self, tool):
        callback = partial(self.toolClicked, tool)
        
        self.toolsList.addTool(tool, callback)
        
        props = ToolPropertiesWidget()
        props.setHeading(tool.properties)
        
        self.tools[tool] = props
    
    def toolClicked(self, tool):
        props = self.tools[tool]
        self.properties.insertTab(0, props, tool.name)
        self.properties.setCurrentWidget(props)

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

tbw.addTool(tool1)
tbw.addTool(tool2)
tbw.addTool(tool3)
