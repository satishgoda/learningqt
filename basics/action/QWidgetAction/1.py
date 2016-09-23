class SelectionSetsView(QTableView):
    def _onContextMenu(self, widget, pos):
        menu = QtGui.QMenu()
        colorAction = menu.addAction("Edit Color")
        colorAction.triggered.connect(partial(self._editColor, widget, pos))
        colorWidgetAction = QtGui.QWidgetAction(menu)
        cbg = ColoredButtonGroup(6)
        cbg.currentColorChosen.connect(widget.colorize)
        colorWidgetAction.setDefaultWidget(cbg)
        menu.addAction(colorWidgetAction)
        widget.addActionsTo(menu)
        menu.exec_(widget.mapToGlobal(pos))
