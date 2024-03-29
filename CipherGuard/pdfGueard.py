from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('Rest API.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Enter password: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)