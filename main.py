import os
import random

USEDIR = os.getcwd() + '/bibliomancy'
USEFILE=False

def biblioDir(directory):
    files = os.listdir(directory)
    targetBib = directory + '/' + random.choice(files)
    with open(targetBib) as f:
        splitup = (f.read().split("\n\n")) #double newline because proj gutenberg books use single newline for typographical purposes and double as a paragraph division. ideally id have better control over the input texts - maybe test for other evidence of PG formatting and exclude the license text and split by double newline with newline as default? idk
        poppable = []
        for sector in range(len(splitup)):
            if splitup[sector].strip == "":
                poppable.append(sector)
        i=len(poppable)-1
        while (i>=0):
            splitup.pop(i)
            i-1
        return random.choice(splitup)
                
    

if USEFILE:
    biblioFile(USEFILE)
else:
    print(biblioDir(USEDIR))

