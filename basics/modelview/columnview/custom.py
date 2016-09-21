class CustomColumnView(QtGui.QColumnView):
    def __init__(self, *args, **kwargs):
        super(CustomColumnView, self).__init__(*args, **kwargs)
        self.activated.connect(self.onActivated)
    
    def keyPressEvent(self, event):
        super(CustomColumnView, self).keyPressEvent(event)
        index = self.selectedIndexes()[0]
        self.activated.emit(index)

    def onActivated(self, index):
        print index.data()
