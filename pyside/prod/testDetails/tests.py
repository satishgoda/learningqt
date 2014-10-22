from PySide import QtCore, QtGui

import testsDialog
from testDetails import TestDetailsDialog


class BaseTest(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return self.nice_name


class InsanityTest(BaseTest):
    description = "Insane subjects were found as following"
    __nice_name = "Insanity Test"

    def __init__(self):
        super(BaseTest, self).__init__()

    @property
    def nice_name(self):
        return self.__nice_name

    def drawUi(self, parent):
        layout = parent.layout()
        parent.detailsDescriptionLabel.setText(self.description)
        for index in range(0, 2):
            hl = QtGui.QHBoxLayout()
            layout.addLayout(hl)
            lbl = QtGui.QLabel(parent)
            lbl.setText(str(index+1))
            pb1 = QtGui.QPushButton(parent)
            pb1.setText("Select")
            pb2 = QtGui.QPushButton(parent)
            pb2.setText("Fix")
            hl.addWidget(lbl)
            hl.addWidget(pb1)
            hl.addWidget(pb2)


class LactoseIntolerantTest(BaseTest):
    description = "Lactose Intolerance was found for the following subjects"
    __nice_name = "Lactose Intolerant Test"

    def __init__(self):
        super(BaseTest, self).__init__()

    @property
    def nice_name(self):
        return self.__nice_name

    def drawUi(self, parent):
        layout = parent.layout()
        parent.detailsDescriptionLabel.setText(self.description)
        for index in range(0, 25):
            hl = QtGui.QHBoxLayout()
            layout.addLayout(hl)
            lbl = QtGui.QLabel(parent)
            lbl.setText(str(index+1))
            pb = QtGui.QPushButton(parent)
            pb.setText("Select")
            hl.addWidget(lbl)
            hl.addWidget(pb)


class TestsDialog(QtGui.QDialog, testsDialog.Ui_Dialog):
    def __init__(self, parent=None, tests=None):
        super(TestsDialog, self).__init__(parent)
        self._tests = tests
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        layout = self.testsPlaceholder.layout()

        def callback(test):
            return lambda: TestDetailsDialog(test).exec_()

        if not self._tests:
            label = QtGui.QLabel(self)
            label.setText("No tests have been taken")
            layout.addWidget(label)
        else:
            for test in self._tests:
                hl = QtGui.QHBoxLayout()
                layout.addLayout(hl)
                pb = QtGui.QPushButton(self)
                pb.setText(test.name)
                pb.clicked.connect(callback(test))
                hl.addWidget(pb)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    it = InsanityTest()
    lit = LactoseIntolerantTest()

    td = TestsDialog(tests=[it, lit])

    td.show()

    sys.exit(app.exec_())
