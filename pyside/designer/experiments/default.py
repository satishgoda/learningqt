# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default.ui'
#
# Created: Mon Oct 20 23:05:48 2014
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
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_load = QtGui.QPushButton(Form)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.pushButton_run = QtGui.QPushButton(Form)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        self.pushButton_view = QtGui.QPushButton(Form)
        self.pushButton_view.setObjectName("pushButton_view")
        self.verticalLayout.addWidget(self.pushButton_view)
        self.pushButton_unload = QtGui.QPushButton(Form)
        self.pushButton_unload.setObjectName("pushButton_unload")
        self.verticalLayout.addWidget(self.pushButton_unload)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtGui.QPushButton(Form)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.setToolTip(QtGui.QApplication.translate("Form", "I cannot be resized at all. Sorry!", None, QtGui.QApplication.UnicodeUTF8))
        Form.setWhatsThis(QtGui.QApplication.translate("Form", "I am a widget that cannot be resized", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_load.setText(QtGui.QApplication.translate("Form", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_run.setText(QtGui.QApplication.translate("Form", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view.setText(QtGui.QApplication.translate("Form", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_unload.setText(QtGui.QApplication.translate("Form", "Unload", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

