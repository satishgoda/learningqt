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

qte.setTextColor(QtCore.Qt.red)

################

qte.setTextColor(QtCore.Qt.black)

################

qte.setTextColor(QtCore.Qt.green)

################

qte.clear()

################

qgb = QtGui.QGroupBox("Modes")
mainLayout.addWidget(qgb)

################

qgbHlayout = QtGui.QHBoxLayout()
qgb.setLayout(qgbHlayout)

redMode = QtGui.QRadioButton("Red")
greenMode = QtGui.QRadioButton("Green")

qgbHlayout.addWidget(redMode)

################

qgbHlayout.addWidget(greenMode)

################

redMode.setChecked(True)

################

print qgb.children()

################


qgb.setCheckable(True)

################


def setCurrentMode():
    print ("Red" if redMode.isChecked() else "Green")

qgb.toggled.connect(setCurrentMode)

################

def updateMode():
    color = QtCore.Qt.red if redMode.isChecked() else QtCore.Qt.green
    qte.setTextColor(color)
    
redMode.toggled.connect(updateMode)
