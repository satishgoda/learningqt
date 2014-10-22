# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testDetailsDialog.ui'
#
# Created: Wed Oct 22 22:13:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 409)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.detailsLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailsLabel.sizePolicy().hasHeightForWidth())
        self.detailsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.detailsLabel.setFont(font)
        self.detailsLabel.setObjectName("detailsLabel")
        self.gridLayout.addWidget(self.detailsLabel, 0, 0, 1, 1)
        self.detailsDescriptionLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailsDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.detailsDescriptionLabel.setSizePolicy(sizePolicy)
        self.detailsDescriptionLabel.setObjectName("detailsDescriptionLabel")
        self.gridLayout.addWidget(self.detailsDescriptionLabel, 3, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.detailsPlaceholderLayout = QtGui.QVBoxLayout()
        self.detailsPlaceholderLayout.setObjectName("detailsPlaceholderLayout")
        self.detailsScrollArea = QtGui.QScrollArea(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailsScrollArea.sizePolicy().hasHeightForWidth())
        self.detailsScrollArea.setSizePolicy(sizePolicy)
        self.detailsScrollArea.setWidgetResizable(True)
        self.detailsScrollArea.setObjectName("detailsScrollArea")
        self.detailsPlaceholder = QtGui.QWidget()
        self.detailsPlaceholder.setGeometry(QtCore.QRect(0, 0, 625, 336))
        self.detailsPlaceholder.setObjectName("detailsPlaceholder")
        self.verticalLayout = QtGui.QVBoxLayout(self.detailsPlaceholder)
        self.verticalLayout.setObjectName("verticalLayout")
        self.detailsScrollArea.setWidget(self.detailsPlaceholder)
        self.detailsPlaceholderLayout.addWidget(self.detailsScrollArea)
        self.verticalLayout_3.addLayout(self.detailsPlaceholderLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("released()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.detailsLabel.setText(QtGui.QApplication.translate("Dialog", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.detailsDescriptionLabel.setText(QtGui.QApplication.translate("Dialog", "dgdfgdfgdgdfgdgdfgdfgdfg", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

