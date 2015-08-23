class ContainerWidget(QWidget):
    """Display content"""
    def __init__(self, parent=None):
        super(ContainerWidget, self).__init__(parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.create = QPushButton("Create")
        layout.addWidget(self.create)
        
        layout.addStretch()
        
        self.create.clicked.connect(self.addContainee)
        
        self._count = 1
    
    @property
    def count(self):
        count = self._count
        self._count += 1
        return count
    
    def addContainee(self):
        layout = self.layout()
        
        button = QPushButton("Selection set #{0}".format(self.count))
        
        layout.insertWidget(layout.count()-1, button)

class ScrollableWidget(QScrollArea):
    """Constrain content to be displayed in a scrolalble area"""
    def __init__(self, widget, parent=None):
        super(ScrollableWidget, self).__init__(parent)
        self.setWidget(widget)
        self.setWidgetResizable(True)

class DemoWidget(QWidget):
    """Ïntegrate everything"""
    def __init__(self, widget, parent=None):
        super(DemoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(widget)
        self.setMinimumHeight(400)

containerWidget = ContainerWidget()
containerWidget.show()

scrollableWidget = ScrollableWidget(containerWidget)
scrollableWidget.show()

demoWidget = DemoWidget(scrollableWidget)
demoWidget.show()

"""
I started with the following snippet that did not yeild expected results.

sa = QScrollArea()

sa.setMaximumHeight(400)

sa.adjustSize()

layout = QVBoxLayout()
sa.setLayout(layout)

sa.setEnabled(True)

for c in "stringbringfringhringshring":
    layout.addWidget(QPushButton(c))

sa.setWidgetResizable(True)

sa.show()
"""