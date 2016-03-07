from PySide.QtGui import QPushButton, QLabel
from PySide.QtCore import QStateMachine, QState

switch = QPushButton("Switch")
notification = QLabel("Flip the switch")

onState = QState()
offState = QState()

offState.addTransition(switch, "clicked()", onState)
onState.addTransition(switch, "clicked()", offState)

offState.assignProperty(notification, "text", "Off")
onState.assignProperty(notification, "text", "On")

machine = QStateMachine()

machine.addState(onState)
machine.addState(offState)

machine.setInitialState(offState)

machine.start()

switch.show()
notification.show()
