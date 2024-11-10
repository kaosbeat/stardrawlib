import random
from perlin_noise import PerlinNoise
import lib.starLC20 as p
import lib.staremulator as s
import sqlite3

# showtime


con=sqlite3.connect('data/Belgium14.sqlite')
cur = con.cursor()
# cur.execute( 'SELECT * FROM db_sanitized14 WHERE relationshipstatus = "It\'s complicated"')
# cur.execute( 'SELECT relationshipstatus FROM db_sanitized14 WHERE relationshipstatus != ""' )
global relationshipstatusses
relationshipstatusses = ["\"In a relationship\"",  "\"It\'s complicated\"", "\"Divorced\"", "\"Engaged\"", "\"Widowed\"", "\"Single\"", "\"Married\"", "\"\""] 
global data
data = []


def getnewList(datatype):
    global data
    rs = relationshipstatusses[datatype]
    # statement = 'SELECT phone FROM db_sanitized14 WHERE relationshipstatus =' + rs + 'AND phone != ""'
    statement = 'SELECT firstname FROM db_sanitized14 WHERE relationshipstatus =' + rs + 'AND firstname != ""'

    print(statement)
    cur.execute(statement)
    data = list(cur)


# print(data[random.randint(0,len(data)-1)][0] + " is in"  + rs)
# get random person 

# return (data[random.randint(0,len(data)-1)][0], zone)

# r = cur.fetchone()

# print (data)


font5x7 = {
    " ":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],"a":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,1,1],
    [0,1,1,0,1]
    ], "b":[
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"c":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,0],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"d":[
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"e":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [0,1,1,1,1]
    ],"f":[
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [1,1,1,1,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0]
    ],"g":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"h":[
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,1,1,0],
    [1,1,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"i":[
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ],"j":[
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,1,1,0]
    ],"k":[
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,1,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [1,0,1,0,0],
    [1,0,0,1,0]
    ],"l":[
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ],"m":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,0,1,0],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1]
    ],"n":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,1,1,0],
    [1,1,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"o":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"p":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0]
    ],"q":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [0,0,0,0,1]
    ],"r":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,1,1,0],
    [1,1,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]
    ],"s":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [1,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,1],
    [1,1,1,1,0]
    ],"t":[
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ],"u":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"v":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ],"w":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [0,1,0,1,0]
    ],"x":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
    ],"y":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"z":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,1,1,1,1]
    ],"1":[
    [0,0,1,1,0],
    [0,1,0,1,0],
    [1,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0]
    ],"2":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,1,1,1,1]
    ],"3":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"4":[
    [0,0,0,1,0],
    [0,0,1,1,0],
    [0,1,0,1,0],
    [1,0,0,1,0],
    [1,1,1,1,1],
    [1,0,0,1,0],
    [0,0,0,1,0]
    ],"5":[
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"6":[
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"7":[
    [1,1,1,1,1],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,1,1,1],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,1]
    ],"8":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"9":[
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0]
    ],"0":[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"!":[
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,1,0,0]
    ] ,"A":[
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ] ,"B":[
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0]
    ] ,"C":[
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,1]
    ] ,"D":[
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0]
    ] 
    ,"E":[
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
    ] 
    ,"F":[
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]
    ] 
    ,"G":[
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [0,1,1,1,1]
    ] 
    ,"H":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ] ,"I":[
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ]  ,"J":[
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,0,1,0,0],
    [1,1,1,0,0]
    ],"K":[
    [1,0,0,0,1],
    [1,0,0,1,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [1,0,1,0,0],
    [1,0,0,1,0],
    [1,0,0,0,1]
    ],"L":[
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
    ],"M":[
    [1,0,0,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"N":[
    [1,0,0,0,1],
    [1,1,0,0,1],
    [1,0,1,0,1],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"O":[
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
    ],"P":[
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]
    ],"Q":[
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,1,1],
    [1,1,1,1,1]
    ],"R":[
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"S":[
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [1,1,1,1,0]
    ] ,"T":[
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    ],"U":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],"V":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
    ],"W":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,1,1,1,0]
    ],"X":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1]
    ],"Y":[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ],"Z":[
    [1,1,1,1,1],
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
    ],",":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,0,1,0,0]
    ],"_":[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1]
    ],"'":[
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]
    }

charlist = ["_"," ", ",", "!", "'","0","1","2","3","4","5","6","7","8","9",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def getNextname():
    global data
    return data[random.randint(0,len(data)-1)][0]

from data.discordusers import dusers 
namelist = dusers


def getNextDiscordname():
    global namelist
    name = namelist[random.randint(0,len(namelist)-1)]
    print (name)
    # return namelist[random.randint(0,len(namelist)-1)][0]
    return name


def letter2page(letter, dim, margin, flipV):
    # returns str as a multiline buffer, ready to plot to a page (pw*ph)  # font5x7["a"
    name = iter(getNextname())
    # print(name)
    chars = ["*","X", "#","+", "=", "-", "<", ">" ,".", "*","X", "#","+", "=", "-", "<", ">" ,"."]
    # chars = ["1","2", "3","4", "5", "6", "7", "8" ,"9", "0","a", "b","c", "d", "e", "f", "g" ,"h"]
    count=0 
    buffer = ""
    noise = PerlinNoise()
    y = dim[1]
    size = int(p.columns/(dim[0]+1))
    margin = int((p.columns - (dim[0]*size)) / dim[0])
    for l in range(y):
        # size = 30
        anomalyx = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        anomalyy = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        # size = int(columns/(x+1))
        for i in range(size):
            line=""
            for k in range(dim[0]):
                if letter not in charlist:
                    letter = "X"
                print (letter, l, k)
                if font5x7[letter][l][k] == 1:
                    curchar = "#"
                else:
                    curchar = "."
                xstep = 1 / (anomalyy[k]+0.1)
                noisebuf = int(anomalyx[k] * noise(xstep*i))
                namebuf = ""
                if (curchar == "#"):
                    for x in range(size-noisebuf):
                        try:
                            char = next(name)
                            # print(curchar)
                        except StopIteration:
                            name = iter(getNextname())
                            char = " "
                        namebuf = namebuf + char
                else:
                    namebuf = (size-noisebuf)*curchar
                linebuf = noisebuf*chars[k+l] + namebuf
                if anomalyx[k] < size:
                    anomalyx[k] = anomalyx[k] + 1
                line = line + linebuf + " "*int(margin) 
            buffer = buffer + line + "\n"
        for i in range(margin):
            line =""
            buffer = buffer + line + "\n"
    return buffer


def letter2page4versum(letter, dim, margin, flipV,nameiter):
    # returns str as a multiline buffer, ready to plot to a page (pw*ph)  # font5x7["a"
    # nameiter = iter(getNextDiscordname())
    name = nameiter()
    # print(name)
    chars = ["*","X", "#","+", "=", "-", "<", ">" ,".", "*","X", "#","+", "=", "-", "<", ">" ,"."]
    # chars = ["1","2", "3","4", "5", "6", "7", "8" ,"9", "0","a", "b","c", "d", "e", "f", "g" ,"h"]
    count=0 
    buffer = ""
    noise = PerlinNoise()
    y = dim[1]
    size = int(p.columns/(dim[0]+1))
    margin = int((p.columns - (dim[0]*size)) / dim[0])
    for l in range(y):
        # size = 30
        anomalyx = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        anomalyy = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        # size = int(columns/(x+1))
        for i in range(size):
            line=""
            for k in range(dim[0]):
                if letter not in charlist:
                    letter = "X"
                print (letter, l, k)
                if font5x7[letter][l][k] == 1:
                    curchar = "#"
                else:
                    curchar = "."
                xstep = 1 / (anomalyy[k]+0.1)
                noisebuf = int(anomalyx[k] * noise(xstep*i))
                namebuf = ""
                if (curchar == "#"):
                    for x in range(size-noisebuf):
                        try:
                            char = next(name)
                            # print(curchar)
                        except StopIteration:
                            name = nameiter()
                            char = " "
                        namebuf = namebuf + char
                else:
                    namebuf = (size-noisebuf)*curchar
                linebuf = noisebuf*chars[k+l] + namebuf
                if anomalyx[k] < size:
                    anomalyx[k] = anomalyx[k] + 1
                line = line + linebuf + " "*int(margin) 
            buffer = buffer + line + "\n"
        for i in range(margin):
            line =""
            buffer = buffer + line + "\n"
    return buffer