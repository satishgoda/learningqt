from PySide.QtGui import QPushButton, QAction, QMenu, QWidget, QLabel, QLineEdit
from PySide.QtGui import QVBoxLayout, QHBoxLayout, QStackedWidget, QScrollArea

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
        self.setLayout(layout)
        self.actionButton = QPushButton("Create")
        layout.addWidget(self.actionButton)
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
        self.setLayout(layout)
        self.actionButton = QPushButton("Done")
        layout.addWidget(self.actionButton)
        layout.addStretch()
        super(CreatingWidget, self)._setupUi()

    def _setupSignals(self):
        pass
    
createWidget = CreateWidget()
createWidget.show()

creatingWidget = CreatingWidget()
creatingWidget.show()

creationWidget = QStackedWidget()
creationWidget.addWidget(createWidget)
creationWidget.addWidget(creatingWidget)
creationWidget.children()
creationWidget.show()

createWidget.actionButton.clicked.connect(lambda index=1: creationWidget.setCurrentIndex(index))
creatingWidget.actionButton.clicked.connect(lambda index=0: creationWidget.setCurrentIndex(index))


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
        self.createWidget.actionButton.clicked.connect(lambda index=1: self.setCurrentIndex(index))
        self.creatingWidget.actionButton.clicked.connect(lambda index=0: self.setCurrentIndex(index))


class CreatedWidget(Widget):
    def __init__(self, parent=None):
        super(CreatedWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        pass

    def _setupSignals(self):
        pass

class RemoveWidgetExampleWidget(QWidget):
    def __init__(self, parent=None):
        super(RemoveWidgetExampleWidget, self).__init__(parent)
        self._setupUi()
        self._setupSignals()
    
    def _setupUi(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.creationWidget = CreationWidget()
        
        layout.addWidget(self.creationWidget)
        
        layout.addStretch()

    def _setupSignals(self):
        pass    