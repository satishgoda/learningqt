
from PySide import QtCore, QtGui

from testDetailsDialog import Ui_Dialog


class TestDetailsDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, tester):
        super(TestDetailsDialog, self).__init__()
        self.setupUi(self)
        self._tester = tester
        self.updateUi()

    def layout(self, *args, **kwargs):
        return self.detailsPlaceholder.layout()

    def updateUi(self):
        self._tester.drawUi(self)


class BaseTest(object):
    def __init__(self):
        pass


class ZeroAreaTest(BaseTest):
    description = "Zero area faces were found for the following"

    def __init__(self):
        super(BaseTest, self).__init__()

    def drawUi(self, parent):
        layout = parent.layout()
        parent.detailsDescriptionLabel.setText(self.description)
        for i in range(0, 50):
            pb = QtGui.QPushButton(parent)
            layout.addWidget(pb)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    zat = ZeroAreaTest()
    tdd = TestDetailsDialog(zat)
    tdd.show()

    sys.exit(app.exec_())