import base64
import os


def split(word): #split string into list
    return [char for char in word]


def gen_str(instr): #generates the payload string
    while True:
        if len(instr) == 10000:
            break
        else:
            instr += b"#"

    return(instr)


def placeholder(): #generates the executable-placeholder string
    out = ""
    while True:
        out += "#"
        if len(out) == 10000:
            break
        else:
            pass
    return(out.encode())


def main():

    base = open("base.exe",'rb').read() #opens executable, source code is: https://github.com/9-s3c/pyloader/blob/main/base.c
    
    infile = base64.b64encode(open(input("infile: "),'rb').read()) #opens python input file
    
    dat = gen_str(infile) #creates new payload bytes
    
    sect1 = base.split(placeholder())[0] #gets first half of executable bytes

    sect2 = base.split(placeholder())[1] #gets second half of executable bytes

    out = sect1 + dat + sect2 # creates new executable with payload

    outfile = input("outfile: ") # gets file name of new executable

    open(outfile,'wb').write(out) #writes output to new executable

main()
