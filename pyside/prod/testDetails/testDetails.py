
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


if __name__ == '__main__':
    import sys
    from tests import InsanityTest

    app = QtGui.QApplication(sys.argv)

    it = InsanityTest()
    tdd = TestDetailsDialog(it)
    tdd.show()

    sys.exit(app.exec_())