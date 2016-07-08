##

dg = DiGraph()

dg.add_edge('a', 'b')
dg.add_edge('a', 'c')
dg.add_edge('c', 'd')

dg.add_edge('e', 'f')
dg.add_edge('f', 'a')

for key in dg.node:
    dg.node[key]['id'] = key

drawing.nx_pydot.write_dot(dg, "F:\webkit.dot")

pdg = graph_from_dot_file("F:\webkit.dot")

pdg.write_svg("F:\webkit.svg")

##

wview = QWebView()
wview.setWindowFlags(Qt.WindowStaysOnTopHint)
svgData = open("F:\webkit.svg").read()
wview.setHtml(svgData)
wview.setZoomFactor(2)
wview.show()

##

wpage = wview.page()
wframe = wpage.mainFrame()
wdocument = wframe.documentElement()

svg = wdocument.findFirst('svg')
svg.setAttribute('stroke-width', '2')

##

for element in svg.findAll('g'):
    ellipse = element.findFirst('ellipse')
    ellipse.setAttribute('fill', 'gray')
    ellipse.setAttribute('stroke-width', '1')

##

for element in svg.findAll('g'):
    ellipse = element.findFirst('ellipse')
    ellipse.removeAttribute('stroke-width')
    ellipse.setAttribute('fill', 'white')
  
##

nodes_in_path = shortest_path(dg, 'e', 'd')

for element in svg.findAll('g'):
    aclass = element.attribute('class')
    if aclass and aclass == 'node' and element.attribute('id') in nodes_in_path:
        ellipse = element.findFirst('ellipse')
        ellipse.setAttribute('fill', 'gray')

wview.setZoomFactor(0.9)
