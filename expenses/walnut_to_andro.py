import pandas as pd
import PyPDF2

pdfFileObject=open('sbi_oct_20_aug_21.pdf', 'rb')

sbi_pdf=PyPDF2.PdfFileReader(pdfFileObject)
# printing number of pages in pdf file
print(sbi_pdf.numPages)

# creating a page object
for page in range(sbi_pdf.numPages):
    pageObj = sbi_pdf.getPage(page)
    # extracting text from page

    print(pageObj.extractText(),end='')





