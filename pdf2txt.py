import PyPDF2
import os
path = 'C:\\Users\\giorg\\Desktop\\Coronavirus\\Scaricati\\003 - 23 marzo 2020.pdf'
pdf = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
tot_Page = pdfReader.numPages
Pagine = range(0,tot_Page)
book = []
for num_Page in Pagine:
    book = [(pdfReader.getPage(num_Page).extractText())]
print(book[0])      #stampa la prima pagina
pdf.close

fld,fil=os.path.split(path)

print()
print('la variabile book rappresenta un array di pagine del file', fil)
print()
print('nel proseguo provo a creare un ciclo for che legga la cartella Scaricati e per ogni file esegua una funzione identica a quella definita sopra')
print()

import os
curDir = 'C:\\Users\\giorg\\Desktop\\Coronavirus\\Scaricati\\'
os.chdir(curDir)

##fold = os.listdir(curDir)
##for f in os.listdir(curDir):
##    if os.path.isfile(f):
##        print(os.path.join(curDir,f))
        
f = []
for (dirpath, dirnames, filenames) in os.walk(curDir):
    for file in filenames:
        print(dirpath,file)
        f.append(dirpath + file)
    break
print(f)
