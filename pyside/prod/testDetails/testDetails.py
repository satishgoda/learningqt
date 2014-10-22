
from PySide import QtCore, QtGui

import testDetailsDialog


class TestDetailsDialog(QtGui.QDialog, testDetailsDialog.Ui_Dialog):
    def __init__(self, tester):
        super(TestDetailsDialog, self).__init__()
        self.setupUi(self)
        self._tester = tester
        self.updateUi()
        self.setWindowTitle("Validation Test Details")
        self.detailsLabel.setText(self._tester.__class__.__name__)

    def layout(self, *args, **kwargs):
        return self.detailsPlaceholder.layout()

    def updateUi(self):
        self._tester.drawUi(self)


class BaseTest(object):
    def __init__(self):
        pass


class InsanityTest(BaseTest):
    description = "Insane subjects were found as following"

    def __init__(self):
        super(BaseTest, self).__init__()

    def drawUi(self, parent):
        layout = parent.layout()
        parent.detailsDescriptionLabel.setText(self.description)
        for index in range(0, 25):
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


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    it = InsanityTest()
    tdd = TestDetailsDialog(it)
    tdd.show()

    sys.exit(app.exec_())