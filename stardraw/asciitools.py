def strip2ascii(str):
    if str.isascii() == False:
        asciistring = ""
        for c in str:
            if ord(c) < 128:
                asciistring+=c
            else:
                asciistring+="X"
    else:
        asciistring = str 
    return asciistring   
