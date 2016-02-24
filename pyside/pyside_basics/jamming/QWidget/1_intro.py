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

################

qtw = QtGui.QTreeWidget()
mainLayout.addWidget(qtw)

################

qtw.setColumnCount(2)

################

qtwhi = QtGui.QTreeWidgetItem()
qtwhi.setText(0, "Namespace")
qtwhi.setText(1, "Representation")
qtw.setHeaderItem(qtwhi)

################

qtw.setColumnWidth(0, 150)

################

for rig in pm.ls(regex="*:*_rig"):
    qtwtli = QtGui.QTreeWidgetItem()
    qtwtli.setText(0, rig.namespace())
    qtwtli.setText(1, rig.attr('representations').get())
    qtw.addTopLevelItem(qtwtli)

################


################


################
