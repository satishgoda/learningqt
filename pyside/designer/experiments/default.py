# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default.ui'
#
# Created: Mon Oct 20 22:47:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setMaximumSize(QtCore.QSize(400, 400))
        Form.setStyleSheet("background-color: rgb(153, 153, 153);\n"
"")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.setToolTip(QtGui.QApplication.translate("Form", "I cannot be resized at all. Sorry!", None, QtGui.QApplication.UnicodeUTF8))
        Form.setWhatsThis(QtGui.QApplication.translate("Form", "I am a widget that cannot be resized", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

