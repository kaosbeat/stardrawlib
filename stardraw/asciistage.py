import os
import sys
import time
import lib.stardraw.starDraw as sd
from pyfiglet import Figlet
import random


time.sleep(2)
columns, lines = os.get_terminal_size() 
line = 0 # 0 is bottom line
col = 0 # 0 is left
global screenit
screenit = True




def gotoline(y):
    global screenit
    if screenit:
        ## value to print to go back a line: \033[F
        global line
        if y > lines: y = lines
        if y < 0: y = 0
        if (y > line):
            for i in range(y-line):
                print(f"\033[F", end='\r', flush=True)
        elif (y < line):
            for i in range(line-y):
                print(f"", flush=True)
        else:
            print('\r',end='',flush=True)
        line = y

def clearstage(c=" "):
    global colums,lines
    for i in range(lines):
        print(c*columns)


def initstage(scrolltype="scroll"):
    global columns, lines
    # print("creating stage")
    if scrolltype == "clear":
        gotoline(lines)
        # "clear" seems to be buggy!
    if scrolltype == "scroll":
        gotoline(0)
    print("#"*columns)
    sleeptime = 0.1
    for i in range(lines-2):
        print("#" + " "*(columns-2) + "#")
        time.sleep(sleeptime*0.5)
    print("#"*columns, end='',flush=False)
    print(f"\b",end='', flush=True)

def quickinit():
    global columns, lines
    gotoline(1)
    print("\n"+"#"*columns)
    for i in range(lines-2):
        print("#" + " "*(columns-2) + "#")
    print("#"*columns, end='',flush=False)
    print(f"\r",end='', flush=True)

def quickclear():
    global columns, lines
    gotoline(1)
    for i in range(lines):      
        print(" "*columns, end='',flush=False)
    print(f"\r",end='', flush=True)

def printonstage(text, x, y):
    global screenit
    global line,col
    if screenit:
        gotoline(y)
        s = f"\033[{x}G" + text
        S = s[:columns] 
        print(S, end='',  flush=True)
        # col = 0
        

def printMultilineonstage(multilinebuffer, x, y, lineForLine=False, overdrop=True, center=False ):
    global screenit
    global line,col
    width, height = sd.dimensions(multilinebuffer)
    if center:
        x = int((columns-width)/2)
        y = lines - int((lines-height)/2)
    if screenit: 
        for i,l in enumerate(multilinebuffer.splitlines()):
            printonstage(l, x, y)
            if lineForLine: 
                time.sleep(lineForLine)
            y -= 1
            # line = y
        # print(f"\b", flush=True)
        gotoline(1)

def figProps(text, font):
    """returns the string, width and height of rendered figlet"""
    global columns
    f = Figlet(font=font, width=2000)
    figtext = f.renderText(text)
    width, height = sd.dimensions(figtext)
    return width, height, figtext

def printFiglet(text, font="big", x=1, y=1, trim=True):
    """print a figlet from 'text' in 'font' at x, y 
       output is trimmed by default if it's wider/heigher 
       than available terminal space.
       width of the figlet should be columns-2
    """

    global columns
    global screenit
    if screenit:
        f = Figlet(font=font, width=2000)
        figtext = f.renderText(text)
        if len(figtext) > 0:
            # figtext = str(sd.padBuffer(figtext,1, 1, 1, 1))
            width, height = sd.dimensions(figtext)
            if x <= -width:
                figtext = ""
            elif 0 <= x + width <= columns:
                figtext = sd.trimbuffer(figtext, width+x, "l")
            elif width >= x + width >= columns:
                figtext = sd.trimbuffer(figtext, width+x, "l")
                figtext = sd.trimbuffer(figtext, columns, "r")
            elif 0 < x < columns:
                figtext = sd.trimbuffer(figtext, columns-x, "r")


            if y >= lines:
                figtext = sd.trimbuffer(figtext, height-y+lines, "t")
            if height > y: #cut of the bottom
                figtext = sd.trimbuffer(figtext, y, "b")
    
            for i,l in enumerate(figtext.splitlines()):
                printonstage(l, x, y)
                y -= 1
            return width,height,figtext

def printFigletAtRandomLoc(text, font="big"):
    global lines, columns
    global screenit
    if screenit:
        if font == "none":
             font="big"
        f = Figlet(font=font, width=columns)
        figtext = f.renderText(text)
        if len(figtext) > 0:
            # figtext = str(sd.padBuffer(figtext,1, 1, 1, 1))
            width, height = sd.dimensions(figtext)
            maxx = columns - width - 2
            maxy = lines - height - 2 
            x = random.randint(2,max(maxx,3))
            y = random.randint(1,max(maxy, 2))
            for i,l in enumerate(figtext.splitlines()):
                printonstage(l, x, height+y)
                y -= 1

def spacesquare(w,h):
    """
    generate w*h spaces in multiline buffer
    """

    buffer = """"""
    l = w*" " + "\n"
    for x in range(h):
        buffer = buffer + l
    return buffer


def blinkFiglet(x1 ,y1 ,text1, font1, x2 ,y2, text2=None, font2=None, interval=0.1, loop=4):
    single = False
    if font2==None: font2=font1
    w1,h1,figtext1 = printFiglet(text1, font1, x1, y1)
    blanktext1 = spacesquare(w1,h1)
    if text2!=None: 
        w2,h2,figtext2 = printFiglet(text2, font2, x2, y2)
        blanktext2 = spacesquare(w2,h2)
    else: 
        single = True
    
    for x in range(loop):
        if not single:
            printMultilineonstage(blanktext2,x2,y2)
        printMultilineonstage(figtext1,x1,y1)

        time.sleep(interval)
        printMultilineonstage(blanktext1,x1,y1)
        if not single:
            printMultilineonstage(figtext2,x2,y2)
            # printMultilineonstage(blanktext1,x1,y1)
            time.sleep(interval)
            # printMultilineonstage(blanktext2,x2,y2)
        else: 
            time.sleep(interval)
    
    
    




def scrollFiglet(text, font, y, speed, loop):
    """scroll text in font at height y at speed, loop it loop times """

    global screenit
    global columns, lines
    if screenit:
        x=0
        looping = True
        # 
        # for i in range(loop):
        while looping:
            x = x+1
            w,h,figtext = figProps(text, font)
            w = w+2
            h = h+2
            printFiglet(text, font, -w+x%(columns+w), y)
            if (-w+x%(columns+w) == 0):
                loop -= 1
            if loop <= 0:
                looping = False 
            time.sleep(speed)

def mergeFiglets (text1,text2,x1,y1,x2,y2):
    """
    pass in figlets as "w,h,text1 = figProps(text, font)"
    or pass you own multilinebuffer to
    merge two figlets or multilinebuffers and 
    draw to screen at x1,x2,y1,y2, space = empty 
    also returns the merged buffer for printing
    currently only support text1 top left of text2
    


     +-pl-+--------s1x-------+--p1r---+
     pt                      !        !
     +----┌──────────────────┐--------+
     !  x1,y1                │        !
     !    │                  │       p2t
    s1y   │                  │        !
     !    │     ┌────────────┼────────┐--+
     !    │   x2,y2          │        │  !
     !    │     │            │        │  !
     +----└─────┼────────────┘        │  s2y
     !    !     │                     │  !
    p1b   !     │                     │  !
     !    !     │                     │  !
     +----+-p2l-└─────────────────────┘--+
                !                     !
                +----------s2x--------+
    

    
    """

    buffer = """"""
    # calculate paddings
    s1x, s1y = sd.dimensions(text1)
    s2x, s2y = sd.dimensions(text2)
    p2l = x2 - x1
    p1r = s2x + p2l - s1x
    p2t = y2 - y1
    p1b = s2y + p2t - s1y

    # first pad buffers to make them the same size
    buffer1 = ""
    buffer2 = ""
    buffer1 = sd.padBuffer(text1, 0, 0, p1r, p1b)
    buffer2 = sd.padBuffer(text2, p2l, p2t, 0, 0)
    # print("buffer1length = " , str(len(buffer1)))
    buffer1 = buffer1.splitlines()
    buffer2 = buffer2.splitlines()

    for y in range(len(buffer1)):
        line = ""
        for x in range(len(buffer1[0])):
            try:
                c = buffer1[y][x]
            except:
                c =" "
            if (c != " "):
                c = buffer1[y][x]
            else:
                try: 
                    c = buffer2[y][x]
                except:
                    c=""
            line = line + c
        # print (line)
        buffer = buffer + line + "\n"
    # print(buffer)
    return buffer


def doNoise(x, X, y, Y, speed, iterations):
    global screenit
    count = 0
    if screenit:
        while count < iterations:
            chars = ["@", "!", "%"]
            i = random.randint(x,X)
            j = random.randint(y,Y)
            c = random.choice(chars)
            printonstage(c,i,j)
            time.sleep(speed)
            count += 1
