import argparse

parser= argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("outfile")
args = parser.parse_args()
infile = args.infile
outfile = args.outfile

reserved={'if': 'om', 'for': 'för', 'int': 'hel', 'bool': 'bool', 'while': 'medans', 'float': 'flyt', 'false': 'falskt',
          'true': 'sant', 'return': 'returnera', 'try': 'försök', 'catch': 'fånga', 'throw': 'kasta', 'this': 'detta',
          'break': 'bryt', 'void': 'tom', 'unsigned': 'osignerad', 'char': 'karr', 'short':'kort'}

def parse(line):
    inString = False
    done = ""
    word = ""
    cand = ""
    for c in line:
        if inString and c == "\"":
            inString = False
        elif c == "\"":
            inString = True
        if inString:
            done += c
        elif not inString and c.isalpha():
            word+=c
            if(len(cand)>0):
                cand = ""
            try:
                cand = reserved[word]
            except:
                pass
        elif not inString and not c.isalpha():
            if(len(cand)>0):
                done += cand
                cand = ""
            else:
                done += word
            word = ""
            done += c 
        
    return done

lines = []
with open(infile, 'r') as file:
    for line in file:
        lines.append(parse(line))

with open(outfile, 'w') as file:
    for line in lines:
        file.write(line)



            
            
                



