from PySide.QtGui import QPushButton, QAction, QMenu, QWidget, QLabel, QLineEdit
from PySide.QtGui import QVBoxLayout, QHBoxLayout, QStackedWidget, QScrollArea
from PySide.QtGui import QSizePolicy


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

    def _setupUi(self):
        self._placeholderUi()
    
    def _placeholderUi(self):
        layout = self.layout()
        
        placeholderLayout = QHBoxLayout()
        
        self.placeholder = QLabel(self.description)
        
        placeholderLayout.addWidget(self.placeholder)
        
        layout.insertLayout(0, placeholderLayout)

        
class CreateWidget(Widget):
    description = "Create button will appear here"
    
    def __init__(self, parent=None):
        super(CreateWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        layout = QVBoxLayout()
        
        self.createLayout = QHBoxLayout()
        
        self.createLayout.addStretch()
        self.actionButton = QPushButton("Create")
        self.createLayout.addWidget(self.actionButton)
        
        self.setLayout(layout)
        layout.addLayout(self.createLayout)
        layout.addStretch()
        
        super(CreateWidget, self)._setupUi()
    
    def _setupSignals(self):
        pass

    
class CreatingWidget(Widget):
    description = "Widget to accept name of object and done/cancel buttons will appear here"
    
    def __init__(self, parent=None):
        super(CreatingWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()

    def _setupUi(self):
        layout = QVBoxLayout()
        
        self.creatingLayout = QHBoxLayout()
        
        self.userInput = QLineEdit()
        self.creatingLayout.addWidget(self.userInput)
        
        self.actionButton = QPushButton("Done")
        self.creatingLayout.addWidget(self.actionButton)
        
        self.setLayout(layout)
        layout.addLayout(self.creatingLayout)
        layout.addStretch()
        
        super(CreatingWidget, self)._setupUi()

    def _setupSignals(self):
        pass


class CreationWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(CreationWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        self.createWidget = CreateWidget()
        self.creatingWidget = CreatingWidget()
        
        self.addWidget(self.createWidget)
        self.addWidget(self.creatingWidget)
    
    def _setupSignals(self):
        pass


class CreatedWidget(Widget):
    def __init__(self, parent=None):
        super(CreatedWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        layout.addStretch()

    def add(self, name):
        created = QPushButton()
        created.setText("{0} @ {1}".format(name, hex(id(created))))
        layout = self.layout()
        
        layout.insertWidget(layout.count()-1, created)

    def _setupSignals(self):
        pass    

class CreateRemoveWidget(QWidget):
    def __init__(self, parent=None):
        super(CreateRemoveWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.creationWidget = CreationWidget()
        
        layout.addWidget(self.creationWidget)
        
        self.createdWidget = CreatedWidget()
        
        layout.addWidget(self.createdWidget)
        
        layout.addStretch()

    def _setupSignals(self):
        self.creationWidget.createWidget.actionButton.clicked.connect(self._aboutToCreate)
        self.creationWidget.creatingWidget.actionButton.clicked.connect(self._letsCreate)

    def _aboutToCreate(self):
        self.creationWidget.setCurrentIndex(1)
    
    def _letsCreate(self):
        name = self.creationWidget.creatingWidget.userInput.text()
        self.createdWidget.add(name)

        self.creationWidget.setCurrentIndex(0)


widget = CreateRemoveWidget()

widget.show()

#widget.deleteLater()




"""
createWidget = CreateWidget()
createWidget.show()

creatingWidget = CreatingWidget()
creatingWidget.show()

creationWidget = QStackedWidget()
creationWidget.addWidget(createWidget)
creationWidget.addWidget(creatingWidget)
creationWidget.children()
creationWidget.show()
creationWidget.deleteLater()

#creationWidget = CreationWidget()

#creationWidget.show()


"""