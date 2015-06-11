import sys
from PySide.QtGui import QApplication, QMainWindow
from PySide.QtGui import QTextEdit
from PySide.QtGui import QLabel
from PySide.QtGui import QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.initTitle()
        self.initMainToolBar()
        self.initCentralWidget()

    def initTitle(self):
        pid = QApplication.instance().applicationPid()
        self.setWindowTitle("My Projects - ({0})".format(pid))

    def initMainToolBar(self):
        self.tb1 = self.addToolBar("ToolBar 1")
        self.tb1.addWidget(QLabel("ToolBar 1"))
        self.tb1.orientationChanged.connect(self.mainToolBarOrientationChanged)
        
        self.tb1.addSeparator()
        
        for index in range(5):
            pb = QPushButton("B {0}".format(index))
            self.tb1.addWidget(pb)

    def mainToolBarOrientationChanged(self, orientation):
        print "Orientation changed {0}".format(orientation)

    def initCentralWidget(self):
        self.intro = QTextEdit()
        self.setCentralWidget(self.intro)
        self.intro.setText("This application is still being designed")

class MyApplication(QApplication):
    def __init__(self, *args):
        super(MyApplication, self).__init__(*args)
        self.mainWindow = MyMainWindow()
        self.lastWindowClosed.connect(self.cleanup)
    
    def cleanup(self):
        print "Hope you had fun with this app"
    
    def run(self):
        self.mainWindow.show()
        return self.exec_()

if __name__ == '__main__':
    app = MyApplication(sys.argv)
    exit_code = app.run()
    print exit_code

