# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testsDialog.ui'
#
# Created: Thu Oct 23 00:00:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 354)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.testsPlaceholder = QtGui.QWidget()
        self.testsPlaceholder.setGeometry(QtCore.QRect(0, 0, 479, 283))
        self.testsPlaceholder.setObjectName("testsPlaceholder")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.testsPlaceholder)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.testsPlaceholder)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("released()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.detailsLabel.setText(QtGui.QApplication.translate("Dialog", "Health Tests", None, QtGui.QApplication.UnicodeUTF8))
        self.detailsDescriptionLabel.setText(QtGui.QApplication.translate("Dialog", "Check your health regularly", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

