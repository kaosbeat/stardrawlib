import svgwrite

warnings = True  ## enable to see emulation problems at stdout

basefontsize = 16 # 4.233 mm 
linefeed = 16 # setLineSpace(12)  12 matches default 16
fontproportion = 0.6 #calculated from rules measurements
# font = 'Wonky Pins'
font = 'Courier New'
lineCursorY = 0 # pixel position of the cursor, because of changing linefeed this is not simply "linefeed * cursorY"
cursorY = 0   #integer line index
cursorYoffset = 0 # used for extending pages longer than 1 page setTopAtCurrent
svgfile = "page 0"
currentdwg = ""
pagecounter = 0
debug = False

def openfile(filename):
    global svgfile
    global currentdwg
    svgfile = filename
    currentdwg = svgwrite.Drawing(filename, size=("210mm","297mm"), profile='full', class_='svgpage')
    currentdwg.defs.add(currentdwg.style('svg {background-color: white;'))
    currentdwg.defs.add(currentdwg.style('.txt {white-space: pre; }'))
    currentdwg.add(currentdwg.rect(("0mm", "0mm"), ("210mm","297mm"), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='white')
)
    # return dwg


def openmultipagefile(filename, pages):
    global svgfile
    global currentdwg
    svgfile = filename
    length = str(297*pages)
    currentdwg = svgwrite.Drawing(filename, size=("210mm",length+"mm"), profile='full', class_='svgpage multi')
    currentdwg.defs.add(currentdwg.style('svg {background-color: white;'))
    currentdwg.defs.add(currentdwg.style('.txt {white-space: pre; }'))
    currentdwg.add(currentdwg.rect(("0mm", "0mm"), ("210mm",length+"mm"), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='white')
)
    # return dwg

def lf():
    #linefeed
    global cursorY
    global lineCursorY
    cursorY = cursorY + 1
    lineCursorY = lineCursorY + linefeed
    # print (cursorY)

def rlf():
    #linefeed
    global cursorY
    global lineCursorY
    cursorY = cursorY - 1
    lineCursorY = lineCursorY - linefeed
    # print (cursorY)

def closefile():
    global currentdwg
    currentdwg.save()


def printXY(string,x,y):
    global cursorY
    if (len(string) + x > 80):
        if warnings:
            if debug: print("WARNING LINE WILL WRAP ON PRINTER!!!!")
            if debug: print("CUTTING LINE TO PREVENT WRAP")
            if debug: print("Line =" , str(len(string) + x) )
        string = string[0:80-x]
    if (y > cursorY):
        # print ("emu advancing ", y - cursorY) 
        for i in range(y-cursorY):
            lf()
    if (y < cursorY):
        # print ("emu reversing ", cursorY - y) 
        for i in range(cursorY-y):
            rlf()
    if (y == cursorY):
        # print ("emu not advancing")
        pass
    svg = currentdwg.add(currentdwg.g(id="txt", class_="txt", style="font-size:"+str(basefontsize)+";font-family:"+font+";"))
    svg.add(currentdwg.text(string, insert=(fontproportion*basefontsize*x,lineCursorY)))  #  n * 7.5 >>> from linefeed units to px
    lf()

###for printing to specific group
def printXYtoGroup(string,x,y, svggroup):
    global cursorY
    if (len(string) + x > 80):
        if warnings:
            if debug: print("WARNING LINE WILL WRAP ON PRINTER!!!!")
            if debug: print("CUTTING LINE TO PREVENT WRAP")
            if debug: print("Line =" , str(len(string) + x) )
        string = string[0:80-x]
    if (y > cursorY):
        # print ("emu advancing ", y - cursorY) 
        for i in range(y-cursorY):
            lf()
    if (y < cursorY):
        # print ("emu reversing ", cursorY - y) 
        for i in range(cursorY-y):
            rlf()
    if (y == cursorY):
        # print ("emu not advancing")
        pass
    
    svg = svggroup.add(currentdwg.g(id="txt", class_="txt", style="font-size:"+str(basefontsize)+";font-family:"+font+";"))
    svg.add(currentdwg.text(string, insert=(fontproportion*basefontsize*x,lineCursorY)))  #  n * 7.5 >>> from linefeed units to px
    lf()

def setLineSpace(n):
    # sets the distance the paper advances or reverses in subsequent linefeeds to n/72 inch, where n is between O and 255..  ## 0.35 * 12
    global linefeed
    linefeed = n/3*4   ### n = 12 should return 16 >> which corresponds with pixel size in svg
    return linefeed

def currentTop():
    # feeds paper to top of current page
    # we probably don't need this, as we use absolute printing coordinates and use rlf/lf accordingly
    global cursorY
    global lineCursorY
    global cursorYoffset 
    if debug: print( cursorY, lineCursorY, cursorYoffset)
    # for i in range(cursorY):
    #     rlf()
    cursorY = 0
    lineCursorY = 0

def setTopAtCurrent():
    global cursorY
    global cursorYoffset 
    cursorYoffset = cursorY
    cursorY = 0

def nextTop():
    #needs to init newsvg
    global pagecounter
    pagecounter = pagecounter + 1
    openfile("page" + pagecounter + ".svg")

def printBuffer(buffer,x,y,maxheight):
    # print a multiline buffer  
    for i,l in enumerate(buffer.splitlines()):
        if (i<=maxheight-1-y):
            if (l != ""): # don't print empty lines, it's time consuming
                printXY(l, x, i+y)

### for printing to specific SVGgroup
def printBufferToGroup(buffer,x,y,maxheight,svggroup):
    # print a multiline buffer  
    for i,l in enumerate(buffer.splitlines()):
        if (i<=maxheight-1-y):
            if (l != ""): # don't print empty lines, it's time consuming
                printXYtoGroup(l, x, i+y, svggroup)

def debugCircle(x,y,r):
    global currentdwg
    # 16 # 4.233 mm 
    # currentdwg.add(currentdwg.rect(("0mm", "0mm"), ("210mm","297mm"), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='white')
    currentdwg.add(currentdwg.circle((str(x)+"mm", str(y)+"mm"), str(r)+"mm", stroke=svgwrite.rgb(10, 10, 160, '%'), fill='white'))

def setNewDensityAndGotoTop(newdensity, pageheight, linefeed):
    printBuffer(" ",int(1),0,pageheight*12/linefeed)
    setLineSpace(newdensity)

def unitTest():
    global currentdwg
    printXY(currentdwg,"line1", 0, 1)
    printXY(currentdwg,"line2", 0, 2)
    printXY(currentdwg,"line3", 0, 3)
    printXY(currentdwg,"line4", 0, 4)

    setTopAtCurrent()
    printXY(currentdwg,"lineA", 10, 0)
    printXY(currentdwg,"lineB", 10, 2)
    printXY(currentdwg,"lineC", 10, 3)
    printXY(currentdwg,"lineD", 10, 4)

    printXY(currentdwg,"line1", 20, 0)
    printXY(currentdwg,"line2", 20, -2)
    printXY(currentdwg,"line3", 20, 3)
    printXY(currentdwg,"line4", 20, 4)