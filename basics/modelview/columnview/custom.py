class CustomColumnView(QtGui.QColumnView):
    def __init__(self, *args, **kwargs):
        super(CustomColumnView, self).__init__(*args, **kwargs)

    def setModel(self, *args, **kwargs):
        super(CustomColumnView, self).setModel(*args, **kwargs)
        width = self.columnWidths()[0]
        self.setMinimumWidth(width*3)

    def selectionChanged(self, selected, deselected):
        def path(index):
            return "{0}/{1}".format(index.parent().data(), index.data())

        curindex = selected.indexes()[0]

        try:
            previndex = deselected.indexes()[0]
            navigation_path = ' -> '.join(map(path, (previndex, curindex)))
        except IndexError:
            navigation_path = path(curindex)
        
        self.setWindowTitle(navigation_path)
