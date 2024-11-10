import bitarray
import bitarray.util
import random

charss = {
  ":": "11",
  "'": "10",
  ".": "01",
  ";": "00",

  " ": "0000000000000",

  "A": "1100011100010",
  "b": "0100001100011",
  "c": "0000001100001",
  "d": "0000011100011",
  "E": "1100001100001",
  "F": "1100001100000",
  "g": "1100000110101",
  "H": "0100011100010",
  "I": "0001000001000",
  "J": "0000010100011",
  "k": "0001100001100",
  "L": "0100000100001",
  "M": "0110110100010",
  "N": "0110010100110",
  "O": "1100010100011",
  "P": "1100011100000",
  "q": "1100011000100",
  "R": "1100011100100",
  "S": "1100001000011",
  "T": "1001000001000",
  "U": "0100010100011",
  "v": "0010100000000",
  "w": "0000000110110",
  "X": "0010100010100",
  "Y": "0010100010000",
  "Z": "1000100010001",
    
  "a": "1100011100010",
  "B": "0100001100011",
  "C": "0000001100001",
  "D": "0000011100011",
  "e": "1100001100001",
  "f": "1100001100000",
  "G": "1100000110101",
  "h": "0100011100010",
  "i": "0001000001000",
  "j": "0000010100011",
  "K": "0001100001100",
  "l": "0100000100001",
  "m": "0110110100010",
  "n": "0110010100110",
  "o": "1100010100011",
  "P": "1100011100000",
  "Q": "1100011000100",
  "r": "1100011100100",
  "s": "1100001000011",
  "t": "1001000001000",
  "u": "0100010100011",
  "v": "0010100000000",
  "W": "0000000110110",
  "x": "0010100010100",
  "y": "0010100010000",
  "z": "1000100010001",
  
  "^": "0000000010100",
  "[": "1100000100001",
  "]": "1000010000011",
  "(": "1100001000000",
  ")": "1000011000000",
  "<": "0000100000100",
  ">": "0010000010000",
  "~": "1000000000000",
  "-": "0000001000000",
  "_": "0000000000001",
  "=": "0000001000001", # draw a '=' on bottom rows
  "\"": "1000001000000", # draw a '=' on top rows
  "*": "0011101011100",
  "1": "0100000100000"

}



segment_dict13 = {
    0: ['     ', '_____'],
    1: [' ', '|'],
    2: [' ', '\\'],
    3: [' ', '|'],
    4: [' ', '/'],
    5: [' ', '|'],
    6: ['     ', '-----'],
    7: [' ', '|'],
    8: [' ', '/'],
    9: [' ', '|'],
    10: [' ', '\\'],
    11: [' ', '|'],
    12: ['     ', '-----'],
}
    
segment_dict2 = {
    0: [' ','x'],
    1: [' ','x'],
}




def displayText(text):
    line = 0
    lines = ["","","","",""]
    for c in text:
        while line < 5:
            l = charss[c]
            linestring = lines[line]
            if len(l) == 2:
                if line == 0 or line == 2 or line == 4 :
                    linestring += "  "
                if line == 1:
                    linestring +=  segment_dict2[0][int(l[0])]
                    linestring += " "
                if line == 3:
                    linestring +=  segment_dict2[1][int(l[1])]
                    linestring += " "
            if len(l) == 13:
                if line == 0:
                    linestring +=  segment_dict13[0][int(l[0])]
                    linestring += " "
                if line == 1: 
                    linestring +=  segment_dict13[1][int(l[1])]
                    linestring +=  segment_dict13[2][int(l[2])]
                    linestring +=  segment_dict13[3][int(l[3])]
                    linestring +=  segment_dict13[4][int(l[4])]
                    linestring +=  segment_dict13[5][int(l[5])]
                    linestring += " "
                if line == 2:
                    linestring +=  segment_dict13[6][int(l[6])]
                    linestring += " "
                if line == 3: 
                    linestring +=  segment_dict13[7][int(l[7])]
                    linestring +=  segment_dict13[8][int(l[8])]
                    linestring +=  segment_dict13[9][int(l[9])]
                    linestring +=  segment_dict13[10][int(l[10])]
                    linestring +=  segment_dict13[11][int(l[11])]
                    linestring += " "
                if line == 4:
                    linestring +=  segment_dict13[12][int(l[12])]
                    linestring += " "
            lines[line] = linestring
            line += 1
        line = 0
    lines = "\n".join(["{0}".format(pl) for i, pl in enumerate(lines)])
    return lines



def displayBits(bits):
    # print(bits)
    # needs array of 13,13,2,13,13,2,13,13 bitarrays
    line = 0
    lines = ["","","","",""]
    for bit in bits:
        while line < 5:
            l = bit
            linestring = lines[line]
            if len(l) == 2:
                if line == 0 or line == 2 or line == 4 :
                    linestring += "  "
                if line == 1:
                    linestring +=  segment_dict2[0][int(l[0])]
                    linestring += " "
                if line == 3:
                    linestring +=  segment_dict2[1][int(l[1])]
                    linestring += " "
            if len(l) == 13:
                if line == 0:
                    linestring +=  segment_dict13[0][int(l[0])]
                    linestring += " "
                if line == 1: 
                    linestring +=  segment_dict13[1][int(l[1])]
                    linestring +=  segment_dict13[2][int(l[2])]
                    linestring +=  segment_dict13[3][int(l[3])]
                    linestring +=  segment_dict13[4][int(l[4])]
                    linestring +=  segment_dict13[5][int(l[5])]
                    linestring += " "
                if line == 2:
                    linestring +=  segment_dict13[6][int(l[6])]
                    linestring += " "
                if line == 3: 
                    linestring +=  segment_dict13[7][int(l[7])]
                    linestring +=  segment_dict13[8][int(l[8])]
                    linestring +=  segment_dict13[9][int(l[9])]
                    linestring +=  segment_dict13[10][int(l[10])]
                    linestring +=  segment_dict13[11][int(l[11])]
                    linestring += " "
                if line == 4:
                    linestring +=  segment_dict13[12][int(l[12])]
                    linestring += " "
            lines[line] = linestring
            line += 1
        line = 0
    lines = "\n".join(["{0}".format(pl) for i, pl in enumerate(lines)])
    return lines



def genOneBits(bittype=None):
    big1 = bitarray.bitarray("0100000100000")
    big2 = bitarray.bitarray("0001000001000")
    big3 = bitarray.bitarray("0000010000010")
    bigs = [big1,big2,big3]
    small1 = bitarray.bitarray("0100000000000")
    small2 = bitarray.bitarray("0001000000000")
    small3 = bitarray.bitarray("0000010000000")
    small4 = bitarray.bitarray("0000000100000")
    small5 = bitarray.bitarray("0000000001000")
    small6 = bitarray.bitarray("0000000000010")
    smalls = [small1,small2,small3,small4,small5,small6]

    bits = "77777777"
    if bittype==None:
        bittype = random.choice(["random1s","maxbig","midbig","twobig","somebig","topsmall", "bottomsmall","somesmall" ])
        # print(bittype)

    if bittype == "random1s":
        ba = bitarray.util.urandom(13)
        ba &= bitarray.bitarray('0101010101010')
        # print(ba.to01())
        bits = ba.to01()
    if bittype == "maxbig":
        bits = "0101010101010"
    if bittype == "midbig":
        bits = "0001000001000"
    if bittype == "twobig":
        bits = "0100010100010"
    if bittype == "somebig":
        i = 0
        big = bitarray.bitarray(13)
        while i < 3:
            big |= random.choice(bigs)
            i +=1
        bits = big.to01()
    if bittype == "topsmall":
        bits = "0101010000000"
    if bittype == "bottomsmall":
        bits = "0000000101010"  
    if bittype == "somesmall":
        i = 0
        small = bitarray.bitarray(13)
        while i < 6:
            small |= random.choice(smalls)
            i +=1
        bits = small.to01()

    return bits

def genZeroBits(bittype=None):
    bits = "77777777"
    if bittype==None:
        bittype = random.choice(["topzero","bottomzero","bigzero"])
    if bittype == "topzero":
        bits = "1100011000000"
    if bittype == "bottomzero":
        bits = "0000001100011"
    if bittype == "bigzero":
        bits = "1100010100011"
    if bittype == "leftzero":
        bits = "1100000100001"
    if bittype == "midzero":
        bits = "1000000000001"
    if bittype == "rightzero":
        bits = "1000010000011"
    if bittype == "topleftzero":
        bits = "1100001000000"
    if bittype == "topmidzero":
        bits = "1000001000000"
    if bittype == "toprightzero":
        bits = "1000011000000"
    if bittype == "bottomleftzero":
        bits = "0000001100001"
    if bittype == "bottommidzero":
        bits = "0000001000001"
    if bittype == "bottomrightzero":
        bits = "0000001000011"
    if bittype == "leftzero45":
        bits = "0000100000100"
    if bittype == "rightzero45":
        bits = "0010000010000"

    return bits




#######################################
########### displayfunctions ##########
#######################################

def indexupdate(index, bitsarr):
    index+=1
    if index == 2 or index == 4:
        bitsarr.append("11")
    return index

def randomOneBits():
    bitsarr = []
    bitsarr.append(genOneBits())
    bitsarr.append(genOneBits())
    bitsarr.append("00")
    bitsarr.append(genOneBits())
    bitsarr.append(genOneBits())
    bitsarr.append("00")
    bitsarr.append(genOneBits())
    bitsarr.append(genOneBits())
    return bitsarr



def randomZeroBits():
    bitsarr = []
    weightsspace = [50,40,20,15,10,5]
    spaceleft=6
    index = 0
    while spaceleft > 0:
        i=0
        space = []
        weights = ()
        while i < spaceleft:
            i+=1
            space.append(i)
            weights+=(weightsspace[i-1],)
        fill = random.choices(space, weights=weights)
        # print(fill[0], space, weights, spaceleft)
        fill = fill[0]
        if fill == 1:
            bitsarr.append(genZeroBits())
            index = indexupdate(index, bitsarr)
            spaceleft-=1
        if fill == 2:        
            zerotype = random.choice([["leftzero","rightzero"], ["topleftzero", "toprightzero"], ["bottomleftzero","bottomrightzero"], ["leftzero45", "rightzero45"]])
            bitsarr.append(genZeroBits(zerotype[0]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[1]))     
            index = indexupdate(index, bitsarr)
            spaceleft-=2    
        if fill == 3:
            zerotype = random.choice([["leftzero","midzero","rightzero"], ["topleftzero","topmidzero", "toprightzero"], ["bottomleftzero","bottommidzero","bottomrightzero"]])
            bitsarr.append(genZeroBits(zerotype[0]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[1]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[2]))
            index = indexupdate(index, bitsarr)
            spaceleft-=3
        if fill == 4:
            zerotype = random.choice([["leftzero","midzero","midzero","rightzero"], 
                                      ["topleftzero","topmidzero","topmidzero", "toprightzero"], 
                                      ["bottomleftzero","bottommidzero","bottommidzero","bottomrightzero"]])
            bitsarr.append(genZeroBits(zerotype[0]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[1]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[2]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[3]))
            index = indexupdate(index, bitsarr)
            spaceleft-=4  
        if fill == 5:
            zerotype = random.choice([["leftzero","midzero","midzero","midzero","rightzero"], 
                                      ["topleftzero","topmidzero","topmidzero","topmidzero","toprightzero"], 
                                      ["bottomleftzero","bottommidzero","bottommidzero","bottommidzero","bottomrightzero"]])
            bitsarr.append(genZeroBits(zerotype[0]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[1]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[2]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[3]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[4]))
            index = indexupdate(index, bitsarr)
            spaceleft-=5
        if fill == 6:        
            zerotype = random.choice([["leftzero","midzero","midzero","midzero","midzero","rightzero"], 
                                      ["topleftzero","topmidzero","topmidzero","topmidzero","topmidzero","toprightzero"], 
                                      ["bottomleftzero","bottommidzero","bottommidzero","bottommidzero","bottommidzero","bottomrightzero"]])
            bitsarr.append(genZeroBits(zerotype[0]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[1]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[2]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[3]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[4]))
            index = indexupdate(index, bitsarr)
            bitsarr.append(genZeroBits(zerotype[5]))
            index = indexupdate(index, bitsarr)
            spaceleft-=6
        # print(bitsarr)
        

    return bitsarr