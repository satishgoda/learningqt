"""
class Adapter(dict):
    __getattr__ = dict.__getitem__
    
    def __init__(self, name, *args, **kwargs):
        kwargs['id'] = name
        super(Adapter, self).__init__(*args, **kwargs)

sections = {
...
...
...
}
"""

def createIdItemRow(data, parent):
    item = QStandardItem(data.id)
    item.setData(data, Qt.UserRole)
    item.setEditable(False)
    parent.appendRow(item)
    return item

model = QStandardItemModel()

for sname, sattributes in sections.iteritems():
    section = Adapter(sname, sattributes)
    sitem = createIdItemRow(section, model)
    for ename, eattributes in section.elements.iteritems():
        element = Adapter(ename, eattributes)
        eitem = createIdItemRow(element, sitem)


columnView = QtGuiQColumnView()
columnView.setModel(model)
columnView.show()
