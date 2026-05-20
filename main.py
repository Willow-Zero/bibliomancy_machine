import os
import random
import argparse
from pypdf import PdfReader,PdfWriter
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-d","--directory",help="specifies a directory. conflicts with -f/--file.")
parser.add_argument("-f","--file",help="specifies a directory. conflicts with -d/--directory.")
parser.add_argument("-k","--kitty",action='store_true',help="enables icat viewing of pdf files")

args = parser.parse_args()

USEDIR = os.getcwd() + '/bibliomancy'
USEFILE=False

if args.file:
    USEFILE = args.file
if args.directory:
    USEDIR = args.directory

def txtHandler(file):
    splitter = "\n"
    gutFlag = False
    with open(file) as f:
        fulltext = f.read()
        if "PROJECT GUTENBERG EBOOK" in fulltext:
            splitter = "\n\n"
            gutFlag = True
        splitup = (fulltext.split(splitter)) #double newline because proj gutenberg books use single newline for typographical purposes and double as a paragraph division. ideally id have better control over the input texts - maybe test for other evidence of PG formatting and exclude the license text and split by double newline with newline as default? idk
        poppable = []
        after = len(splitup)+50
        for sector in range(len(splitup)-1):
            if splitup[sector].strip == "":
                poppable.append(sector)
            if gutFlag and "END OF THE PROJECT GUTENBERG EBOOK" in splitup[sector]:
                after = sector
                poppable.append(sector)             # after end, its just license text, and i dont want to be bibliomancing license text
            if gutFlag and "The Project Gutenberg eBook of" in splitup[sector]:
                poppable.append(sector)
            if gutFlag and "This eBook is for the use of anyone anywhere in the United States" in splitup[sector]:
                poppable.append(sector)
            if gutFlag and "Title:" in splitup[sector]:
                poppable.append(sector)
            if gutFlag and "Release date:" in splitup[sector]:
                poppable.append(sector)                                         # these all strip elements of the project gutenberg pre-text from the randomness. 
            if gutFlag and "Language:" in splitup[sector]:                      # i plan to split this into a seperate function after allthe standard stripping of empty text, it would look prettier. but this works.
                poppable.append(sector)
            if gutFlag and "Other information and formats:" in splitup[sector]:
                poppable.append(sector)
            if gutFlag and "*** START OF THE PROJECT GUTENBERG EBOOK" in splitup[sector]:
                poppable.append(sector)
            if sector>after:
                poppable.append(sector)
        i=len(poppable)-1
        while (i>=0):
            try: splitup.pop(poppable[i])
            except: print("error encountered popping " + str(poppable[i]))
            i=i-1
        return random.choice(splitup)





def pdfHandler(file):
    reader = PdfReader(file)
    page = random.choice(reader.pages)
    text = page.extract_text(extraction_mode="layout")
    if args.kitty:
        newWriter = PdfWriter()
        newWriter.insert_page(page)
        newWriter.write("tempOutput.pdf")
        subprocess.run(["kitten","icat","--scale-up","--fit","height","--background","white","tempOutput.pdf"])
        return("USED ICAT")
    elif text:
        return text
    else: return "ERR"





def biblioFile(file,directory=False):
    if (os.path.isdir(file)):
        return biblioDir(file)
    elif (file.split(".")[-1].lower() in ["txt","md"]): 
        return txtHandler(file)
    elif (file.split(".")[-1].lower() in ["pdf"]): 
        return pdfHandler(file)







def biblioDir(directory):
    files = os.listdir(directory)
    targetBib = directory + '/' + random.choice(files)
    return biblioFile(targetBib,directory=directory)
                
    

if USEFILE:
    print(biblioFile(USEFILE))
else:
    print(biblioDir(USEDIR))

