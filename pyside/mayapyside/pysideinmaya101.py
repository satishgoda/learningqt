import pymel.core as pm
from PySide import QtGui, QtCore

w = QtGui.QDialog()

w.setWindowTitle("My custom Maya Dialog")
w.setGeometry(100, 100, 400, 200)

l = QtGui.QVBoxLayout()
w.setLayout(l)

pb = QtGui.QPushButton(w)
pb.setText("Hello")
pb.clicked.connect(lambda: pm.warning("Hello World"))
l.addWidget(pb)

l.addStretch()

pb = QtGui.QPushButton(w)
pb.setText("Close")
pb.clicked.connect(w.close)
l.addWidget(pb)

w.exec_()
