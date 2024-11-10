#!/usr/bin/python3
# coding: utf-8


import os
import time

warnings = False  ## enable to see emulation problems at stdout
debug = False
# allowLineWrap = True
dropOverPrint = True ## if trying to print beyond column 80 drop it so lines don't wrap
# lp0 = os.open("/dev/usb/lp0", os.O_RDWR)
dummy = os.open("/dev/null", os.O_RDWR)
# dev = lp0 
dev = dummy
columns = 80
# lines = 120



basefontsize = 16 # 4.233 mm or 1.666 inch  or 120/7.5
linefeed = 16 # setLineSpace(120/7.5)  120 matches default 16
fontproportion = 0.6 #calculated from rules measurements
pageheight = 69 # pageheight at linefeed 16  # 68 works IF pagetop is at printhead

cursorX = 0
cursorY = 0



	


def lf(): #line feed
    #prints the current line and performs a line feed
    global cursorY
    data = "0A"
    os.write(dev,bytes.fromhex(data))
    cursorY = cursorY + 1

def rlf(): # reverse line feed
    global cursorY
    data = "1B5D"
    os.write(dev,bytes.fromhex(data))
    cursorY = cursorY - 1

def cr(): # carriage return
    global cursorX
    data = "0D"
    os.write(dev,bytes.fromhex(data))
    cursorX = 0

def noMargins(): #cancel both left and right margins
    #should check what font is currently in use!!!
    #hardcoded for PICA
    data = "1B580080"
    os.write(dev,bytes.fromhex(data))

def setFont(font):
    #columns of chars per page
    # Pica 80
    # Elite 96
    # CondensedPica 137
    # CondensedElite 160
    if (font == "pica"):
        data = "12"
        os.write(dev,bytes.fromhex(data))    
    if (font == "cPica"):
        data = "121B0F"
        os.write(dev,bytes.fromhex(data))     
    if (font == "elite"):
        data = "121B3A"
        os.write(dev,bytes.fromhex(data))    
    if (font == "cElite"):
        data = "1B3A1B0F"
        os.write(dev,bytes.fromhex(data))    

def setLineSpace(n):
    global linefeed
    # sets the distance the paper advances or reverses in subsequent linefeeds to n/72inch, where n is between O and 255..
    # If n=0,the linespacing is set to O
    # n = 10 => 0.35cm
    data = "1B41"+"{:02x}".format(n,'x')
    # if debug: print(data)
    os.write(dev,bytes.fromhex(data))
    # commit the new line spacing value
    data = "1B32"
    os.write(dev,bytes.fromhex(data))
    linefeed = n


def nextTop():
    # feeds paper to top of next page
    data = "0C"
    os.write(dev,bytes.fromhex(data))

def currentTop():
    # feeds paper to top of current page
    data = "1B0C"
    os.write(dev,bytes.fromhex(data))
    lf() 

def setTopAtCurrent():
    # sets current position as top of page
    global cursorY
    data = "1B34"
    os.write(dev,bytes.fromhex(data))
    cursorY = 0

def setOnLine():
    data = "11"
    os.write(dev,bytes.fromhex(data))


def beep():
    data = "07"
    os.write(dev,bytes.fromhex(data))


def reset():
    data = "1B40"
    os.write(dev,bytes.fromhex(data))

def printXY(string,x,y):
    # print string at x,y dropping chars that go past the last right column
    global cursorX
    global cursorY
    whitespace = ' ' * x
    if (x + len(string)> columns):
        if warnings:
            if debug: print("WARNING LINE WILL WRAP ON PRINTER!!!!")
            if debug: print("CUTTING LINE TO PREVENT WRAP")
        if dropOverPrint:
            string = string[0:columns - x]
    if (y > cursorY):
        # print ("advancing ", y - cursorY) 
        for i in range(y-cursorY):
            lf()
    if (y < cursorY):
        # print ("reversing ", cursorY - y) 
        for i in range(cursorY-y):
            rlf()
    if (y == cursorY):
        # print ("not advancing")
        cr()
    # for i in range(x):
        # string = ' ' + string
    if (string != ""):
        string = whitespace + string
        printstuff(string)
    lf()



def printstuff(stuff):
    global cursorX
    global cursorY
    os.write(dev,bytes(stuff, 'utf-8'))
    cursorX = cursorX + len(stuff)
    if (cursorX > columns):
        cursorY = cursorY + int(cursorX/columns)
        cursorX = cursorX%columns



def printBuffer(buffer,x,y,maxheight):
    # print a multiline buffer  
    for i,l in enumerate(buffer.splitlines()):
        if (i<=maxheight-y):
            if (l != ""): # don't print empty lines, it's time consuming
                printXY(l, x, i+y)


def setNewDensityAndGotoTop(newdensity, pageheight, linefeed):
    printBuffer(" ",int(1),0,pageheight*12/linefeed)
    setLineSpace(newdensity)




# setLineSpace(100)

# nextTop()
# rlf()

# currentTop()
# lf()

# os.lseek(dev,0,os.SEEK_SET)
# print os.read(dev,16)


