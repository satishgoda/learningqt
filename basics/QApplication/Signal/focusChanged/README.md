
```python
def trackFocusChange(old, new):
    print old
    print new
    print

appInstance.focusChanged.connect(trackFocusChange)
appInstance.focusChanged.disconnect(trackFocusChange)
```
