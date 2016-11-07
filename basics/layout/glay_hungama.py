from PySide import QtGui, QtCore
    

class HeaderWidget(QtGui.QWidget):
    def __init__(self, label, parent=None):
        super(HeaderWidget, self).__init__(parent)
        self.label = label
        self._setupUI()
    
    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        self.label = QtGui.QLabel(self.label)
        layout.addWidget(self.label, 0, 0)

class FooterWidget(QtGui.QWidget):
    def __init__(self, label, parent=None):
        super(FooterWidget, self).__init__(parent)
        self.label = label
        self._setupUI()
    
    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        self.label = QtGui.QLabel(self.label)
        layout.addWidget(self.label, 0, 0)

class ScrollingWidget(QtGui.QScrollArea):
    def __init__(self, parent=None):
        super(ScrollingWidget, self).__init__(parent)
        self.setWidgetResizable(True)

class GroupWidget(QtGui.QWidget):
    def __init__(self, count, parent=None):
        super(GroupWidget, self).__init__(parent)
        self.count = count
        self._setupUI()
    
    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        
        for index in range(self.count):
            but = QtGui.QPushButton("Button {0}".format(index))
            layout.addWidget(but, index, 0)

class PropertiesStack(QtGui.QStackedWidget):
    def __init__(self, parent=None):
        super(PropertiesStack, self).__init__(parent)

class PropertiesWidget(QtGui.QWidget):
    def __init__(self, props, parent=None):
        super(PropertiesWidget, self).__init__(parent)
        self.props = props.split()
        self._setupUI()
    
    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        for index, prop in enumerate(self.props):
            label = QtGui.QLabel(prop)
            layout.addWidget(label, index, 0)

class GettingItAllTogether(QtGui.QWidget):
    def __init__(self, parent=None):
        super(GettingItAllTogether, self).__init__(parent)
        self._setupUI()
    
    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        
        header = HeaderWidget("Please use this widget")
        layout.addWidget(header, 0, 0)
        
        groupWgt = GroupWidget(15)
        self.area = ScrollingWidget()
        self.area.setFixedWidth(200)
        self.area.setWidget(groupWgt)
        layout.addWidget(self.area, 1, 0)
    
        self.propsStack = PropertiesStack()
        self.propsStack.setMinimumWidth(200)
        layout.addWidget(self.propsStack, 1, 1)
        
        defaultProps = PropertiesWidget('Click a tool to choose its properties')
        self.propsStack.addWidget(defaultProps)
        self.propsStack.setCurrentWidget(defaultProps)
    
        footer = FooterWidget("Thank you for using this widget")
        layout.addWidget(footer, 2, 0)

self = GettingItAllTogether()
self.show()

self.propsStack.setVisible(False); self.adjustSize()
self.propsStack.setVisible(True)
