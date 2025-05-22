import PyPDF2

pdfFile = ["1.pdf","2.pdf","3.pdf"]

merger = PyPDF2.PDFmerger()

for filename in pdfFile:
    pdfFile = open(filename, rb)
    pdfReader = PyPDF.PdfFileReader(pdfFile)
    pdfMerger.append(pdfReader)
pdfFile.close()
pdfMerge.write('merged.pdf')


