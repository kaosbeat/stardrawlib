from __future__ import nested_scopes
import random
import math
import datetime
# from turtle import width

def line(x1,y1,x2,y2, char):
    #draws line from.(x1,y1) to (x2,y2)  both points included using char
    #if char == 'auto' selects /\|- according to orientation 
    #if char is 'random' pick a random char!
    buffer = ''

    if x2 < x1:
        xoff = x2
    else: 
        xoff = x1
    if y2 < y1:
        yoff = y2
    else: 
        yoff = y1
    buffer = yoff * '\n'
    if (x2-x1 == 0):
        #vertical div by zero
        # print("vertical!")
        rc = 1000000
    else:
        rc = (y2-y1)/(x2-x1)
        # print("rico = ", rc)

    if rc < 0:
        # xoff = xoff + min(x1,x2)
        # print ("x1= " ,x1) 
        # print ("x2= " ,x2) 
        xoff = xoff + abs(x2-x1)

    if char == 'auto':
        if -4 < rc <= -0.25:
            char = "/"
        if -0.25 < rc <= 0.25:
            char = '-'
        if 0.25 < rc <= 4:
            char = '\\'
        if abs(rc) > 4:
            char = '|'
    
    if char == 'random':
        chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
        char = chars[random.randint(len(chars))-1]

    if y2 > y1:
        for j in range(y2-y1+1):
            if rc == 0:
                x = x1
            else: 
                x = j/rc + xoff
            if x >= 0:
                line = int(x) * ' ' + char
            else:
                line = ''
            buffer = buffer + line + '\n'
    if y2 < y1:
        for j in range(y1-y2+1):
            if rc == 0:
                x = x1
            else:
                x = j/rc + xoff
            if x >= 0:
                line = int(x) * ' ' + char
            else:
                line = ''
            buffer = buffer + line + '\n'
    if y1 == y2:
        # print("horizontal!")
        if x1 < 1:
            x1 = 1
        if x2 < 1:
            x2 = 1
        line = ' ' * (xoff) + (abs(x2-x1)+1) * char
        buffer = buffer + line + '\n'

    # print("done")
    return buffer


# k = line(16,2, 10, 2, 'a')
# print(k)

def brokenline(x1,y1,x2,y2, char):
    #draws line from...to using char
    buffer = ''
    if (x2-x1 == 0):
        #vertical div by zero
        print("vertical!")
        rc = 0
        xoff = x1
    else:
        rc = (y2-y1)/(x2-x1)
        print("rico = ", rc)
    if x2 < x1 and rc < 0:
        xoff = x2
    if x2 < x1 and rc > 0: 
        xoff = x1
    if x2 > x1 and rc < 0:
        xoff = x1
    if x2 > x1 and rc > 0: 
        xoff = x2
    
    if y2 < y1:
        yoff = y2
    else: 
        yoff = y1
    buffer = yoff * '\n'


    if y2 > y1:
        for j in range(y2-y1):
            if rc == 0:
                x = x1
            else: 
                x = j/rc + xoff
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y2 < y1:
        for j in range(y1-y2):
            if rc == 0:
                x = x1
            else:
                x = j/rc + xoff
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y1 == y2:
        line = ' ' * xoff + abs(x2-x1) * char
        buffer = buffer + line + '\n'

    print("done")
    return buffer


def square(x1,y1,x2,y2,charh,charv):
    # returns a bufferlist of lines, print using
    a = line(x1,y1,x2,y1,charh)
    b = line(x1,y1,x1,y2,charv)
    c = line(x1,y2,x2,y2,charh)
    d = line(x2,y1,x2,y2,charv)
    return [a, b, c, d]

def square2(x1,y1,x2,y2,charh,charv):
    buffer = x1*" "+(x2-x1)*charh+"\n"
    for i in range(y2-y1-2):
        if (x2-x1-2) >= 0:
            buffer = buffer + x1*" "+ charv + (x2-x1-2)*" " + charv +"\n"
        else:
            buffer = buffer + x1*" "+ charv + "\n"
    if (x2-x1) > 0:
            buffer = buffer + x1*" "+(x2-x1)*charh
    return buffer


# def filledsquare(size, angle, char):
#     # 0 < angle < size/2 
#     buffer  = ""
#     for x in range(size+1):
#         if x < size/2:
#             line = " " * int(size/2-x) + char*int((x*4)/2+1)
#         elif x == size/2:
#             line = char*(size+1)
#         else:
#             line = " " * int(x-size/2) + char*int(((size-x)*4)/2+1)
#         buffer = buffer + line + "\n"
#     print(buffer)
#     return buffer

def building(w,h):
    vert = [["[", "]"], ["I"], ["|"],["!"],["(",")"], ["/","\\"],[":"]]
    wall=["#","o","H","U",".","O","="," ","±","+","-"]
    roof=["_", "=", "^","~"]
    buffer = []
    v = vert[random.randint(0,len(vert)-1)]
    wl = wall[random.randint(0,len(wall)-1)]
    r = roof[random.randint(0,len(roof)-1)]
    for i in range(h+1):
        line = ""
        for j in range(w+1):
            if i > 0:
                if (j == 0): 
                    v = v[0]
                    line = line + v
                elif (j == w):
                    if (len(v)==2):
                        v = v[1]
                    else:
                        v = v[0]
                    line = line + v
                else:
                    line = line + wl
            if i == 0:
                line = line + r                
        buffer.append(line)
    return buffer


    
def filledsquare(size, angle, char):
    # 0 < angle < size/2 
    buffer  = ""
    step = (size/2)/angle
    pre = (size/2) - angle
    for x in range(size+1):
        if x < size/2:
            x+1
            line = " " * int(pre - x*step) + char*int((x*4)/2+1)
        elif x == size/2:
            line = char*(size+1)
        else:
            line = " " * int(x-size/2 + angle * (x-size/2)/2 ) + char*int(((size-x)*4)/2+1)
        buffer = buffer + line + "\n"
    print(buffer)
    return buffer


# filledsquare(10,2,"d")

def parallelogram(height, width, dirchange, char):
    # parallelogram is (int(width/dirchange)+height high and width wide)
    buffer = ""
    h = height
    a = dirchange
    b = width
    c = char
    line =""
    if a == 0:
        r = h
        a = width
    else:
        r = int(b/a)+h+1
    for y in range(r):
        # print("y =", y)
        if (y > h):
            line = " "*a + line
        elif len(line) < b:
            line = line + a*c
        line = line[:b-1]
        if not line.isspace():
            buffer = buffer + line + "\n"
    return buffer

def parallelogram_charlist(height, width, dirchange, charlist):
    # parallelogram is (int(width/dirchange)+height high and width wide)
    buffer = ""
    h = height
    realheight = int(width/dirchange)+height
    a = dirchange
    b = width
    # if realheight*width > len(charlist):
    #     charlist = (realheight*width / len(charlist))*charlist
    line =""
    if a == 0:
        r = h
        a = width
    else:
        r = int(b/a)+h+1
    for y in range(r):
        # print("y =", y)
        if (y > h):
            line = " "*a + line
        elif len(line) < b:
            for c in range(a):
                line = line + charlist.pop()
        # line = line[:b-1]
        if not line.isspace():
            buffer = buffer + line + "\n"
        line = ""
    return buffer




def circle(radius, basefontsize, linefeed, char):
    #density is current linefeed density >> n/72inch,
    buffer = ""
    proportion = 1.5
    #at linefeed = 8 > prop = 1
    
    radiusv = radius*linefeed

    #    print("proportion = " ,proportion)
    radiush = radius * basefontsize
    # radiusv = 
    
    for r in range(int(radius * 2 +1 )):
        v = (radius-r)
        if v == radius:
            v = radius - 0.1
        if v == -radius:
            v = -radius + 0.1
        if v == 1:
            v = 0 
        # print ("corrected:" , v)
        v = v*linefeed
        
        # factor = linefeed*(basefontsize + linefeed)/basefontsize / 2 # (ok for linespace 9)
        # factor = 7.03125 # ok for linespace 9  
        # factor = 8.125 # ok for linespace ??
        factor = 7.5 # ok for linespace 10, size 10 
        # factor = 7 # ok for linespace 14, size 14
        # factor = 6.5 # ok for linespace 16, size 16


        h = math.sqrt( abs(math.pow(radiusv ,2 ) -  math.pow(v,2) ))  / factor 


        # basefontsize*(basefontsize + linefeed)/linefeed
        
        buffer = buffer + int(h)*char + "\n"
    # print(buffer)
    buffer2 = ""
    xsize,ysize = dimensions(buffer)
    # print("xsize = ",xsize)

    for i,l in enumerate(buffer.splitlines()):
        # print("t"+l+"t")
        # print (len(l))

        pad = xsize - len(l)
        line = "\n" +" " * pad + 2*l + " " * pad
        # print("t"+line+"t")
        buffer2 = buffer2 + line
        # print(line)
    # print(basefontsize*(basefontsize + linefeed)/linefeed)
    # print(linefeed*(basefontsize + linefeed)/basefontsize)
    # print("factor = ",factor)
    # print(buffer2)
    return buffer2


def cube(w,h,d,c1,c2,c3):
    # if w < h:
    #     b = w
    #     w = h
    #     h = b
    if d > w:
        d = w
    if d > h:
        d = h
    buffer = '''
                                _
                               /__
                              //___
                             ///____
                            ////_____
                           /////______
                          ///// _______
                         ///// \ ______
                        ///// \ \ _____
                       ///// \ \ \ ____
                       //// \ \ \ \ ___
                       /// \ \ \ \ \ __
                       // \ \ \ \ \ \ _
                       / \ \ \ \ \ \ \\
                        \ \ \ \ \ \ \\
                         \ \ \ \ \ \\
                          \ \ \ \ \\
                           \ \ \ \\
                            \ \ \\
                             \ \\
                              \\
                        
    
    '''
    buffer = ""
    # w = 28
    # h = 28
    # d = 15
    # c1 = "+"
    # c2 = "."
    # c3 = "*"
    for y in range(h):
        line = ""
        for x in range(w):
            if x>=d:
                x = d
            line = line + (w-x)*" " + x*c1 + (x+1)*c2 + "\n"
    buffer = buffer + line
    for y in range(int(h)):
        line = ""
        for x in range(int(w)):
            if x<d:
                x1 = d
            else:
                x1 = w -x

            # line = line +
            # line = line + (w-x)*" " + x1*c1 + x*c3 + (x1+1)*c2 + "\n"
            line = line + (w-d)*" " + (d-x)*c1 + x*2*c3+c3 + (d-x)*c2 +"\n"
            if len(x*2*c3+c3) > w:
                break
    for y in range(d):
        line = ""
        for x in range(int(w)):
            # print("fix needed")
            if x>=d:
                x = d
            line = line + " "*((w-d) ) + (d-x)*c1 + ((2*x)+1)*c3 + (d-x)*c2 + "\n"
            # line = line + (w-x)*" " 
            # line = line + (w-x)*c3 +"\n"
            if (2*x)+1 >= 2 * d:
                break
    
    buffer = buffer + line

    for y in range(d):
        line = ""
        line = line + " "*((w-d) + y) + 2*(d-y)*c3 + "\n"
        buffer = buffer + line
    
    return buffer



def dimensions(buffer):
    if len(buffer) != 0:
        width = len(max(buffer.splitlines(), key = len))    
        height = len(buffer.splitlines())
        return width, height
    else: 
        return 0,0



def padBuffer(buffer, xpad,ypad,Xpad, Ypad ):
    """
    pad multiline buffer
    print("padding buffer")
    """

    # widest bufferline?
    if len(buffer) != 0:
        maxlength = len(max(buffer.splitlines(), key = len))
    else:
        maxlength = 0
    # print(maxlength)
    buffer1 = ""
    for y in range(ypad):
        line = " "*(xpad+maxlength+Xpad)  +"\n"
        buffer1 = buffer1 + line
    for i,l in enumerate(buffer.splitlines()):
        l = l.ljust(maxlength, ' ')
        line = xpad*" " + l + Xpad*" " + "\n"
        buffer1 = buffer1 + line
    for y in range(Ypad):
        line = " "*(xpad+maxlength+Xpad) + "\n"
        buffer1 = buffer1 + line
    return buffer1

def trimbuffer(buffer, newsize, side):
    """trim sides of a multiline buffer
    newsize sets desired width or height
    l cuts from the left, r from the right
    t cuts from the top, b cuts from the bottom
    """

    buffer2 = ''''''
    if len(buffer) == 0:
        return buffer2
    buffer1 = padBuffer(buffer,0,0,0,0)
    width,height = dimensions(buffer1)
    

    if side == "r" or side == "l":
        for i,l in enumerate(buffer1.splitlines()):
            if side == "r":
                l = l[:newsize]
            if side == "l":
                l = l[-newsize:]
            buffer2 += l + "\n"
    if side == "t" or side == "b":
        for i,l in enumerate(buffer1.splitlines()):
            if side == "t":
                if i >= height-newsize:
                    buffer2 += l + "\n"
            if side == "b":
                if i < newsize:
                    buffer2 += l + "\n"
    return buffer2

def padMax(buffer,columns,height):
    # pad buffer to match columns/height
    x,y = dimensions(buffer)
    padx = columns - x
    pady = height - y
    if padx > 1:
        prex = random.randint(0,padx)
        postx = padx - prex
    elif padx == 1:
        prex = 1
        postx = 0
    else:
        prex = 0
        postx = 0
    if pady > 1:
        prey = random.randint(0,pady)
        posty = pady - prey
    elif pady == 1:
        prey = 1
        posty = 0
    else:
        prey = 0
        posty = 0
    paddedbuffer = padBuffer(buffer,prex,prey,postx,posty)
    return paddedbuffer

def padMidMax(buffer,columns,height):
    x,y = dimensions(buffer)
    padx = columns - x -2
    pady = height - y
    if padx > 1:
        prex = int(padx/2) -1
        postx = padx - prex
    elif padx == 1:
        prex = 1
        postx = 0
    else:
        prex = 0
        postx = 0
    if pady > 1:
        prey = int(pady/2)
        posty = pady - prey
    elif pady == 1:
        prey = 1
        posty = 0
    else:
        prey = 0
        posty = 0
    paddedbuffer = padBuffer(buffer,prex,prey,postx,posty)
    return paddedbuffer


def mergeBuffers(buffer1,buffer2,xpos):
    """
    merge 2 buffers leaving buffer1 in front until xpos
    pad until same height and width using padBuffer
    buffers should have equal width/height
    """
    
    # print(dimensions(buffer1))
    # print(dimensions(buffer2))
    
    buffer1 = buffer1.splitlines()
    buffer2 = buffer2.splitlines()
    buffer = ""
    for y in range(len(buffer1)):
        line = ""
        for x in range(len(buffer1[0])):
            if x < xpos:
                c = buffer1[y][x]
                if (c != " "):
                    c = buffer1[y][x]
                else:
                    c = buffer2[y][x]
            else:
                c = buffer2[y][x]
                if (c != " "):
                    c = buffer2[y][x]
                else:
                    c = buffer1[y][x]
            line = line + c
        # print (line)
        buffer = buffer + line + "\n"
    return buffer




def consoleBuffer(buffer):
    for l in buffer.splitlines():
        print(l)



def signstring(title):
    """p.printXY(signstring(title), p.columns - len(string), y)"""

    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string


# def sign(title, y):
#     s.setLineSpace(12)
#     p.setLineSpace(12)
#     string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
#     string = "kaotec []<> " + title + " " + string
#     s.printXY(string, s.columns - len(string), y) 
