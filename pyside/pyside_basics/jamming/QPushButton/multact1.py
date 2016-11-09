from functools import partial

pb = QtGui.QPushButton()

a1 = QtGui.QAction('Next', pb)
a2 = QtGui.QAction('Done', pb)

def a1CB(self, *args, **kwargs):
    print self.text()

def a2CB(self, *args, **kwargs):
    print self.text()

a1.triggered.connect(partial(a1CB, a1))
a2.triggered.connect(partial(a2CB, a2))

pb.show()

pb.addAction(a1)
pb.setText(a1.text())
pb.clicked.connect(pb.actions()[0].trigger)
pb.clicked.disconnect(pb.actions()[0].trigger)
pb.removeAction(a1)
pb.actions()


pb.addAction(a2)
pb.setText(a2.text())
pb.clicked.connect(pb.actions()[0].trigger)
pb.clicked.disconnect(pb.actions()[0].trigger)
pb.removeAction(a2)
pb.actions()
