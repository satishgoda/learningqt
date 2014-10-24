import pymel.core as pm
from PySide import QtGui, QtCore

def run():
    class pbCallback(object):
        def __init__(self, message, cb=None):
            self.message = message
            self.cb = cb

        def __call__(self, *args, **kwargs):
            pm.warning(self.message)
            if self.cb:
                self.cb()

    d = QtGui.QDialog()

    d.setWindowTitle("My custom Maya Dialog")
    d.setGeometry(100, 100, 400, 200)

    vbl = QtGui.QVBoxLayout()
    d.setLayout(vbl)

    pb = QtGui.QPushButton(d)
    pb.setText("Hello")
    pb.released.connect(pbCallback("Welcome"))
    vbl.addWidget(pb)

    vbl.addStretch()

    pb = QtGui.QPushButton(d)
    pb.setText("Close")
    pb.clicked.connect(pbCallback("Bye", d.close))
    vbl.addWidget(pb)

    d.exec_()

if __name__ == '__main__':
    import mayapyside
    reload(mayapyside)
    from mayapyside import hellomayapyside
    reload(hellomayapyside)
    hellomayapyside.run()
