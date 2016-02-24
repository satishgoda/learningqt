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

qte = QtGui.QTextEdit()

################

mainLayout.addWidget(qte)

################

qte.setMaximumHeight(70)

################

qte.setMaximumHeight(100)

################

qte.setMaximumHeight(30)

################

def updateStatus():
    selItem = qtw.selectedItems()[0]
    namespace = selItem.text(0)
    qte.append(namespace)

qtw.itemClicked.connect(updateStatus)

################

qte.setReadOnly(True)

################

qte.setHtml("<b>Nice</b>")
qte.append("<b>Better</b>")
qte.append("<i style='color:red'>Better</i>")
qte.append("<pre style='çolor:black'>Why the style changed?</pre>")

################
