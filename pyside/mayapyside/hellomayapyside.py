import pymel.core as pm
from PySide import QtGui, QtCore

def run():
    def hello():
        pm.warning(hello.message)

    def hellocallback(message):
        hello.message = message
        return hello

    def close():
        pm.warning("Closing dialog")
        close.exec_()

    def closecallback(w):
        close.exec_ = w.close
        return close

    d = QtGui.QDialog()

    d.setWindowTitle("My custom Maya Dialog")
    d.setGeometry(100, 100, 400, 200)

    vbl = QtGui.QVBoxLayout()
    d.setLayout(vbl)

    pb = QtGui.QPushButton(d)
    pb.setText("Hello")
    pb.released.connect(hellocallback("Hello World"))
    vbl.addWidget(pb)

    vbl.addStretch()

    pb = QtGui.QPushButton(d)
    pb.setText("Close")
    pb.clicked.connect(closecallback(d))
    vbl.addWidget(pb)

    d.exec_()

if __name__ == '__main__':
    import mayapyside
    reload(mayapyside)
    from mayapyside import hellomayapyside
    reload(hellomayapyside)
    hellomayapyside.run()
