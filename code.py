'''file = open('data.txt','r')
data = file.readlines()
for r in data:
    print(r)
file = open('data.txt','a')
file.write('\n search Google...')
file.close
file = open('data.txt','r')
data = file.readlines()
for r in data:
    print(r)
file.close
with open('data3.txt','a')as file:
    file.write('\n Search Google...')'''
    
import PyPDF2

pdfFileObj = open('data05.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
pageObj = pdfReader.pages[1]
print(pageObj.extract_text())
pdfFileObj.close()
