class MyWebView(QWebView):
    def __init__(self, *args, **kwargs):
        super(MyWebView, self).__init__(*args, **kwargs)
    
    def mousePressEvent(self, evt):
        wframe = self.page().mainFrame()
        element = wframe.hitTestContent(evt.pos()).element()

        print evt.pos(), element.tagName()

        if element.parent().attribute('class') == 'node':
            if element.attribute('fill') == 'white':
                element.setAttribute('fill', 'gray')
            else:
                element.setAttribute('fill', 'white')

        super(MyWebView, self).mousePressEvent(evt)
