###############

qw = QtGui.QWidget()

qw.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

qw.show()

###############

mainLayout = QtGui.QVBoxLayout()

qw.setLayout(mainLayout)

###############

label = QtGui.QLabel("Shot Manager")

mainLayout.addWidget(label)

###############

mainLayout.setAlignment(QtCore.Qt.AlignBottom)

mainLayout.update()

###############

mainLayout.setAlignment(QtCore.Qt.AlignTop)

mainLayout.update()
