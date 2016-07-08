class MyWebView(QWebView):
    def __init__(self, *args, **kwargs):
        super(MyWebView, self).__init__(*args, **kwargs)
    
    def mousePressEvent(self, evt):
        wpage = self.page()
        wframe = wpage.mainFrame()
        hte = wframe.hitTestContent(evt.pos())
        element = hte.element()
        print evt.pos(), element.tagName()
        if element.attribute('fill') == 'white':
            element.setAttribute('fill', 'gray')
        else:
            element.setAttribute('fill', 'white')
        super(MyWebView, self).mousePressEvent(evt)

##

wview = MyWebView()
wview.setWindowFlags(WindowStaysOnTopHint)
svgData = open("F:\webkit.svg").read()
wview.setHtml(svgData)
wview.setZoomFactor(0.9)
wview.show()
wpage = wview.page()
wframe = wpage.mainFrame()
wdocument = wframe.documentElement()
svg = wdocument.findFirst('svg')

for element in svg.findAll('g'):
    ellipse = element.findFirst('ellipse')
    ellipse.setAttribute('fill', 'white')
    ellipse.setAttribute('stroke-width', '1')
