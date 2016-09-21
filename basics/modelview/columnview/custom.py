class CustomColumnView(QtGui.QColumnView):
    def __init__(self, *args, **kwargs):
        super(CustomColumnView, self).__init__(*args, **kwargs)

    def selectionChanged(self, selected, deselected):
        curindex = selected.indexes()[0]
        print 'current: ', curindex.data()
        try:
            previndex = deselected.indexes()[0]
            print 'previous: ',previndex.data()
        except IndexError:
            pass
